"""Three-statement projection engine (used by the Module 10 build-along).

``project(history, assumptions, years)`` rolls the last historical balance sheet forward and
returns an income statement, balance sheet, cash-flow statement and a ``checks`` frame. Design
choices (each is a standard modelling convention - see Module 10.3):

* **Cash is the plug.** Every other balance-sheet line is driven by an assumption; cash is
  whatever the cash-flow statement leaves behind. If the model is internally consistent the
  balance sheet then balances automatically - the ``checks`` frame proves it every year.
* **No circularity.** Interest expense is charged on *opening* borrowings and treasury income is
  earned on *opening* cash + liquid investments, so no iteration is needed.
* **Working capital** is driven either by a single % of revenue (``nwc_pct``) or by days
  (inventory and payable days on cost of materials, receivable days on revenue).
* **Fixed assets** are one line, net fixed assets (net block + CWIP + right-of-use + intangibles):
  closing = opening + capex - D&A. Lease liabilities are held flat; new right-of-use additions are
  assumed to be covered by the capex % (so the cash lease payment modelled is the lease interest).
* **Tax**: a flat rate on PBT, all paid in cash (DTL held flat). **Dividends** in year *t* =
  payout x PAT of year *t-1* (Indian final dividends are paid after the AGM, in the next FY).
* **Debt**: scheduled drawdowns/repayments per year; optional revolver (``min_cash``) draws
  current borrowings when cash would fall below the floor.

The FCFF from ``fcff_from_projection`` (NOPAT + D&A - capex - ΔNWC, NOPAT = EBIT x (1 - t)) matches
the course's reference DCF exactly when ``Assumptions.kaveri_base()`` is used - so the ₹320/share
house valuation can be rebuilt from a full three-statement model.
"""
from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass, field, replace

import pandas as pd

__all__ = ["Assumptions", "project", "fcff_from_projection"]

Driver = float | Sequence[float] | None


@dataclass
class Assumptions:
    """Forecast drivers. List drivers are per forecast year; a scalar applies to every year and a
    short list is extended with its last value.

    Attributes
    ----------
    growth : revenue growth per year (its length is the default horizon).
    ebitda_margin : EBITDA / revenue.
    da_pct, capex_pct : D&A and capex as % of revenue.
    nwc_pct : net working capital (inventory + receivables + OCA - payables - OCL) as % of revenue.
    inventory_days, receivable_days, payable_days : alternative to ``nwc_pct`` (all three needed).
        Inventory and payable days are on cost of materials = revenue x (1 - gross_margin).
    gross_margin, oca_pct, ocl_pct : used only in days mode; default to the last historical year.
    tax_rate : on PBT (Kaveri: 25.17%, Sec. 115BAA).
    dividend_payout : of the previous year's PAT.
    interest_rate : pre-tax rate on opening borrowings.
    lease_rate : rate on opening lease liabilities.
    treasury_yield : yield on opening cash + current investments (other income).
    lt_debt_change, st_debt_change : drawdown (+) / repayment (-) per year, ₹ Cr.
    min_cash : if set, a revolver draws current borrowings so closing cash never falls below it.
    """

    growth: Sequence[float]
    ebitda_margin: float | Sequence[float]
    da_pct: float | Sequence[float] = 0.034
    capex_pct: float | Sequence[float] = 0.035
    nwc_pct: Driver = None
    inventory_days: Driver = None
    receivable_days: Driver = None
    payable_days: Driver = None
    gross_margin: Driver = None
    oca_pct: Driver = None
    ocl_pct: Driver = None
    tax_rate: float = 0.2517
    dividend_payout: float = 0.25
    interest_rate: float = 0.089
    lease_rate: float = 0.085
    treasury_yield: float = 0.068
    lt_debt_change: float | Sequence[float] = 0.0
    st_debt_change: float | Sequence[float] = 0.0
    min_cash: float | None = None
    notes: str = field(default="", repr=False)

    @classmethod
    def kaveri_base(cls, **overrides) -> "Assumptions":
        """The Kaveri reference-valuation drivers (``kaveri-valuation.md``) plus financing defaults.

        Operating drivers come from ``tools/running_example/valuation.py``: growth 10%, 14%, 14%, 13%,
        12%, 11%, 10%, 9%, 8%, 7%; EBITDA margin 13.3% rising to 15.5%; D&A 3.4% and capex 3.5% of
        revenue; NWC 25%, 23%, then 22% of revenue; tax 25.17%. Financing (not needed for the FCFF):
        8.9% pre-tax cost of debt, 25% payout, term loans repaid ₹20 Cr a year for 4 years
        (₹92 Cr -> ₹12 Cr), working-capital loans flat. Pass keyword overrides to change any field.
        """
        from .data import _load_running_example

        a = _load_running_example("valuation").A
        base = cls(
            growth=list(a["growth"]),
            ebitda_margin=list(a["ebitda_margin"]),
            da_pct=a["da_pct"],
            capex_pct=list(a["capex_pct"]),
            nwc_pct=list(a["nwc_pct"]),
            tax_rate=a["tax"],
            dividend_payout=0.25,
            interest_rate=a["kd_pre"],
            lease_rate=0.085,
            treasury_yield=0.068,
            lt_debt_change=[-20.0, -20.0, -20.0, -20.0, 0.0],
            st_debt_change=0.0,
            notes="Kaveri reference valuation base case",
        )
        return replace(base, **overrides) if overrides else base


def _series(x: Driver, n: int, name: str) -> list[float]:
    if x is None:
        raise ValueError(f"assumption {name!r} is required")
    if isinstance(x, (int, float)):
        return [float(x)] * n
    xs = [float(v) for v in x]
    if not xs:
        raise ValueError(f"assumption {name!r} is empty")
    return (xs + [xs[-1]] * n)[:n]


def _labels(last: str, n: int) -> list[str]:
    m = re.fullmatch(r"FY(\d{2})", str(last))
    if m:
        y = int(m.group(1))
        return [f"FY{(y + k) % 100:02d}" for k in range(1, n + 1)]
    m = re.match(r"(\d{4})", str(last))
    if m:
        y = int(m.group(1))
        return [str(y + k) for k in range(1, n + 1)]
    return [f"Y+{k}" for k in range(1, n + 1)]


_REQUIRED = ("rev", "mat", "pat", "net_block", "cwip", "rou", "intangibles", "inventory", "receivables", "oca",
             "cur_inv", "cash", "share_capital", "other_equity", "lt_debt", "st_debt", "lease_liab", "payables",
             "ocl", "dtl")


def project(history: pd.DataFrame, a: Assumptions, years: int | None = None) -> dict[str, pd.DataFrame]:
    """Project income statement, balance sheet and cash flow from the last historical column.

    Parameters
    ----------
    history : DataFrame
        Kaveri-layout frame (line item x period); only the **last** column is used as the base year.
        Required rows: ``rev, mat, pat, net_block, cwip, rou, intangibles, inventory, receivables,
        oca, cur_inv, cash, share_capital, other_equity, lt_debt, st_debt, lease_liab, payables,
        ocl, dtl``.
    a : Assumptions
    years : int, optional
        Forecast horizon (default ``len(a.growth)``).

    Returns
    -------
    dict with DataFrames ``income``, ``balance`` (includes the base-year column), ``cash``,
    ``checks`` and the ``assumptions`` object. ``checks`` rows: ``balance_diff`` (assets - equity &
    liabilities), ``cash_recon_diff`` (net cash flow - change in balance-sheet cash), ``balances``
    (1 if both are ~0), ``cash_negative`` (1 if closing cash < 0 - add debt or set ``min_cash``).
    """
    missing = [k for k in _REQUIRED if k not in history.index]
    if missing:
        raise KeyError(f"history is missing rows: {missing}")
    n = years if years is not None else len(a.growth)
    base_label = str(history.columns[-1])
    b = {k: float(v) for k, v in history[history.columns[-1]].items()}
    labels = _labels(base_label, n)

    growth = _series(a.growth, n, "growth")
    margin = _series(a.ebitda_margin, n, "ebitda_margin")
    da_pct = _series(a.da_pct, n, "da_pct")
    capex_pct = _series(a.capex_pct, n, "capex_pct")
    d_lt = _series(a.lt_debt_change, n, "lt_debt_change")
    d_st = _series(a.st_debt_change, n, "st_debt_change")

    days_mode = a.nwc_pct is None and None not in (a.inventory_days, a.receivable_days, a.payable_days)
    base_nwc = b["inventory"] + b["receivables"] + b["oca"] - b["payables"] - b["ocl"]
    if days_mode:
        inv_d = _series(a.inventory_days, n, "inventory_days")
        rec_d = _series(a.receivable_days, n, "receivable_days")
        pay_d = _series(a.payable_days, n, "payable_days")
        gm = _series(a.gross_margin if a.gross_margin is not None else 1 - b["mat"] / b["rev"], n, "gross_margin")
        oca_p = _series(a.oca_pct if a.oca_pct is not None else b["oca"] / b["rev"], n, "oca_pct")
        ocl_p = _series(a.ocl_pct if a.ocl_pct is not None else b["ocl"] / b["rev"], n, "ocl_pct")
    else:
        nwc_p = _series(a.nwc_pct if a.nwc_pct is not None else base_nwc / b["rev"], n, "nwc_pct")
        # liabilities held at base % of revenue; asset components share the rest in base-year mix
        pay_share, ocl_share = b["payables"] / b["rev"], b["ocl"] / b["rev"]
        wc_assets_base = b["inventory"] + b["receivables"] + b["oca"]
        mix = {k: b[k] / wc_assets_base for k in ("inventory", "receivables", "oca")}

    prev = {
        "rev": b["rev"], "pat": b["pat"],
        "nfa": b["net_block"] + b["cwip"] + b["rou"] + b["intangibles"],
        "inventory": b["inventory"], "receivables": b["receivables"], "oca": b["oca"],
        "cur_inv": b["cur_inv"], "cash": b["cash"], "share_capital": b["share_capital"],
        "other_equity": b["other_equity"], "lt_debt": b["lt_debt"], "st_debt": b["st_debt"],
        "lease_liab": b["lease_liab"], "payables": b["payables"], "ocl": b["ocl"], "dtl": b["dtl"],
    }

    def bs_row(d: dict) -> dict:
        nwc = d["inventory"] + d["receivables"] + d["oca"] - d["payables"] - d["ocl"]
        ta = d["nfa"] + d["inventory"] + d["receivables"] + d["oca"] + d["cur_inv"] + d["cash"]
        eq = d["share_capital"] + d["other_equity"]
        tle = eq + d["lt_debt"] + d["st_debt"] + d["lease_liab"] + d["payables"] + d["ocl"] + d["dtl"]
        return {"net_fixed_assets": d["nfa"], "inventory": d["inventory"], "receivables": d["receivables"],
                "oca": d["oca"], "cur_inv": d["cur_inv"], "cash": d["cash"], "total_assets": ta,
                "share_capital": d["share_capital"], "other_equity": d["other_equity"], "equity": eq,
                "lt_debt": d["lt_debt"], "st_debt": d["st_debt"], "lease_liab": d["lease_liab"],
                "payables": d["payables"], "ocl": d["ocl"], "dtl": d["dtl"], "total_le": tle, "nwc": nwc}

    base_bs = bs_row(prev)
    if abs(base_bs["total_assets"] - base_bs["total_le"]) > 0.05:
        raise ValueError(f"base-year balance sheet does not balance: {base_bs['total_assets']:.1f} vs "
                         f"{base_bs['total_le']:.1f} (check the history rows)")

    inc_rows, bs_rows, cf_rows, chk_rows = {}, {base_label: base_bs}, {}, {}
    for t, lab in enumerate(labels):
        rev = prev["rev"] * (1 + growth[t])
        ebitda = rev * margin[t]
        da = rev * da_pct[t]
        ebit = ebitda - da
        other_income = a.treasury_yield * max(prev["cash"] + prev["cur_inv"], 0.0)
        int_debt = a.interest_rate * (prev["lt_debt"] + prev["st_debt"])
        int_lease = a.lease_rate * prev["lease_liab"]
        fin_cost = int_debt + int_lease
        pbt = ebit + other_income - fin_cost
        tax = pbt * a.tax_rate
        pat = pbt - tax
        dividends = max(a.dividend_payout * prev["pat"], 0.0)

        # working capital
        if days_mode:
            cogs = rev * (1 - gm[t])
            inventory = cogs * inv_d[t] / 365
            receivables = rev * rec_d[t] / 365
            payables = cogs * pay_d[t] / 365
            oca = rev * oca_p[t]
            ocl = rev * ocl_p[t]
        else:
            payables, ocl = rev * pay_share, rev * ocl_share
            wc_assets = rev * nwc_p[t] + payables + ocl
            inventory, receivables, oca = (wc_assets * mix[k] for k in ("inventory", "receivables", "oca"))
        d_nwc = (inventory + receivables + oca - payables - ocl) - (
            prev["inventory"] + prev["receivables"] + prev["oca"] - prev["payables"] - prev["ocl"])

        capex = rev * capex_pct[t]
        lt_change = max(d_lt[t], -prev["lt_debt"])  # cannot repay more than is outstanding
        st_change = max(d_st[t], -prev["st_debt"])

        op_before_wc = pbt + da + fin_cost - other_income
        cfo = op_before_wc - d_nwc - tax
        cfi = -capex + other_income  # current investments held flat
        cff = lt_change + st_change - int_debt - int_lease - dividends
        net_cash = cfo + cfi + cff
        cash = prev["cash"] + net_cash
        revolver = 0.0
        if a.min_cash is not None and cash < a.min_cash:
            revolver = a.min_cash - cash
            cash = a.min_cash
            cff += revolver
            net_cash += revolver
            st_change += revolver

        cur = {
            "rev": rev, "pat": pat, "nfa": prev["nfa"] + capex - da,
            "inventory": inventory, "receivables": receivables, "oca": oca, "cur_inv": prev["cur_inv"],
            "cash": cash, "share_capital": prev["share_capital"],
            "other_equity": prev["other_equity"] + pat - dividends,
            "lt_debt": prev["lt_debt"] + lt_change, "st_debt": prev["st_debt"] + st_change,
            "lease_liab": prev["lease_liab"], "payables": payables, "ocl": ocl, "dtl": prev["dtl"],
        }
        bs = bs_row(cur)
        inc_rows[lab] = {"rev": rev, "growth": growth[t], "ebitda": ebitda, "ebitda_margin": margin[t], "da": da,
                         "ebit": ebit, "other_income": other_income, "debt_int": int_debt, "lease_int": int_lease,
                         "fin_cost": fin_cost, "pbt": pbt, "tax": tax, "pat": pat, "dividends": dividends,
                         "nopat": ebit * (1 - a.tax_rate)}
        cf_rows[lab] = {"pbt": pbt, "da": da, "fin_cost": fin_cost, "less_other_income": -other_income,
                        "op_before_wc": op_before_wc, "wc_change": -d_nwc, "taxes_paid": -tax, "cfo": cfo,
                        "capex": -capex, "interest_received": other_income, "cfi": cfi,
                        "d_lt": lt_change, "d_st": st_change, "revolver_draw": revolver,
                        "interest_paid": -int_debt, "lease_payment": -int_lease, "dividends": -dividends,
                        "cff": cff, "net_cash": net_cash, "opening_cash": prev["cash"], "closing_cash": cash}
        bal_diff = bs["total_assets"] - bs["total_le"]
        cash_diff = net_cash - (cash - prev["cash"])
        chk_rows[lab] = {"balance_diff": bal_diff, "cash_recon_diff": cash_diff,
                         "balances": int(abs(bal_diff) < 1e-6 and abs(cash_diff) < 1e-6),
                         "cash_negative": int(cash < 0), "nwc_pct_of_rev": bs["nwc"] / rev}
        bs_rows[lab] = bs
        prev = cur

    def frame(rows: dict) -> pd.DataFrame:
        f = pd.DataFrame(rows)
        f.columns.name = "period"
        return f

    return {"income": frame(inc_rows), "balance": frame(bs_rows), "cash": frame(cf_rows),
            "checks": frame(chk_rows), "assumptions": a}


def fcff_from_projection(proj: dict[str, pd.DataFrame]) -> pd.Series:
    """Free cash flow to the firm by forecast year from a ``project`` result.

    FCFF = NOPAT + D&A - capex - ΔNWC, with NOPAT = EBIT x (1 - tax rate) and EBIT excluding
    other income (treasury income belongs to the cash that is subtracted in the equity bridge).
    """
    inc, bal = proj["income"], proj["balance"]
    tax_rate = proj["assumptions"].tax_rate
    nwc = bal.loc["nwc"]
    d_nwc = nwc.diff().iloc[1:]
    capex = -proj["cash"].loc["capex"]
    fcff = inc.loc["ebit"] * (1 - tax_rate) + inc.loc["da"] - capex - d_nwc[inc.columns]
    fcff.name = "fcff"
    return fcff
