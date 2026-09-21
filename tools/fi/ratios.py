"""Financial ratio calculations and the Kaveri-style ratio dashboard.

Every function takes plain numbers (floats or anything numpy can divide) so you can use them on
annual-report figures typed by hand, on the course CSVs, or on vendor data.

Conventions (same as ``docs/appendix/running-example/kaveri-pumps.md`` §6):

* **Averages** use opening and closing balance sheets: ``avg = (open + close) / 2``.
* **Capital employed** = equity + all borrowings + lease liabilities.
* **Invested capital** = net block + CWIP + right-of-use + intangibles + (inventories +
  receivables + other current assets - payables - other current liabilities).
* **NOPAT** = EBIT x (1 - tax rate), with EBIT *excluding* other income.
* **ROCE** numerator = EBIT + other income (the numerator must match the capital base: capital
  employed includes the cash that earns the other income).
* Working-capital days use **closing** balances; inventory and payable days are on cost of
  materials, receivable days on revenue.

``ratio_dashboard(load_kaveri())`` reproduces the course ratio table to one decimal.
"""
from __future__ import annotations

import math
from collections.abc import Mapping
from typing import Any

import pandas as pd

__all__ = [
    "margins",
    "roe",
    "roce",
    "roic",
    "dupont_3",
    "dupont_5",
    "working_capital_days",
    "capital_employed",
    "invested_capital",
    "net_debt",
    "ratio_dashboard",
    "format_dashboard",
    "RATIO_LABELS",
    "RATIO_KINDS",
]


def _avg(a: float, b: float) -> float:
    return (a + b) / 2


def margins(rev: float, **lines: float) -> dict[str, float]:
    """Each named line as a fraction of revenue.

    >>> m = margins(1318.0, ebitda=181.9, pat=90.5)
    >>> round(m["ebitda"], 3), round(m["pat"], 4)
    (0.138, 0.0687)
    """
    if rev == 0:
        raise ZeroDivisionError("revenue is zero")
    return {name: value / rev for name, value in lines.items()}


def roe(pat: float, equity_open: float, equity_close: float) -> float:
    """Return on equity = PAT / average equity.  Kaveri FY26: 90.5 / ((637.2 + 706.1)/2) = 13.5%."""
    return pat / _avg(equity_open, equity_close)


def roce(ebit: float, other_income: float, ce_open: float, ce_close: float) -> float:
    """Return on capital employed = (EBIT + other income) / average capital employed.

    Capital employed = equity + borrowings + lease liabilities (see ``capital_employed``).
    """
    return (ebit + other_income) / _avg(ce_open, ce_close)


def roic(ebit: float, tax_rate: float, ic_open: float, ic_close: float) -> float:
    """Return on invested capital = EBIT x (1 - t) / average invested capital (operating assets only)."""
    return ebit * (1 - tax_rate) / _avg(ic_open, ic_close)


def dupont_3(pat: float, revenue: float, avg_assets: float, avg_equity: float) -> dict[str, float]:
    """Three-step DuPont: ROE = net margin x asset turnover x equity multiplier.

    $$ROE = \\frac{PAT}{Rev} \\cdot \\frac{Rev}{\\overline{TA}} \\cdot \\frac{\\overline{TA}}{\\overline{E}}$$

    Returns ``margin``, ``turnover``, ``leverage`` and their product ``roe``.
    """
    margin = pat / revenue
    turnover = revenue / avg_assets
    leverage = avg_assets / avg_equity
    return {"margin": margin, "turnover": turnover, "leverage": leverage, "roe": margin * turnover * leverage}


def dupont_5(pat: float, pbt: float, ebit: float, revenue: float, avg_assets: float,
             avg_equity: float) -> dict[str, float]:
    """Five-step DuPont: ROE = tax burden x interest burden x EBIT margin x turnover x leverage.

    tax burden = PAT/PBT; interest burden = PBT/EBIT; EBIT margin = EBIT/revenue;
    turnover = revenue/avg assets; leverage = avg assets/avg equity.

    Note: if you pass EBIT *excluding* other income (Kaveri's ``ebit``) the "interest burden" also
    absorbs other income and exceptional items and can exceed 1 for a cash-rich company. Passing
    ``ebit + other_income`` gives the textbook reading. The product equals PAT / avg equity either way.
    """
    tax_burden = pat / pbt
    interest_burden = pbt / ebit
    ebit_margin = ebit / revenue
    turnover = revenue / avg_assets
    leverage = avg_assets / avg_equity
    return {
        "tax_burden": tax_burden,
        "interest_burden": interest_burden,
        "ebit_margin": ebit_margin,
        "turnover": turnover,
        "leverage": leverage,
        "roe": tax_burden * interest_burden * ebit_margin * turnover * leverage,
    }


def working_capital_days(revenue: float, cogs: float, inventory: float, receivables: float,
                         payables: float, days: float = 365.0) -> dict[str, float]:
    """Inventory, receivable and payable days and the cash conversion cycle.

    DIO = inventory/COGS x 365; DSO = receivables/revenue x 365; DPO = payables/COGS x 365;
    CCC = DIO + DSO - DPO. Kaveri uses cost of materials as COGS and closing balances.
    """
    dio = inventory / cogs * days
    dso = receivables / revenue * days
    dpo = payables / cogs * days
    return {"dio": dio, "dso": dso, "dpo": dpo, "ccc": dio + dso - dpo}


def capital_employed(bs: Mapping[str, float]) -> float:
    """Equity + non-current borrowings + current borrowings + lease liabilities (Kaveri keys)."""
    return bs["equity"] + bs["lt_debt"] + bs["st_debt"] + bs["lease_liab"]


def invested_capital(bs: Mapping[str, float]) -> float:
    """Net block + CWIP + ROU + intangibles + (inventory + receivables + OCA - payables - OCL)."""
    fixed = bs["net_block"] + bs["cwip"] + bs["rou"] + bs["intangibles"]
    nwc = bs["inventory"] + bs["receivables"] + bs["oca"] - bs["payables"] - bs["ocl"]
    return fixed + nwc


def net_debt(bs: Mapping[str, float]) -> float:
    """Borrowings - cash - current (liquid) investments. Lease liabilities excluded (shown separately)."""
    return bs["lt_debt"] + bs["st_debt"] - bs["cash"] - bs["cur_inv"]


#: Row order and labels of the course ratio table (kaveri-pumps.md §6).
RATIO_LABELS: dict[str, str] = {
    "rev_growth": "Revenue growth",
    "gross_margin": "Gross margin",
    "ebitda_margin": "EBITDA margin",
    "ebit_margin": "EBIT margin",
    "pat_margin": "PAT margin",
    "roe": "ROE (PAT / avg equity)",
    "roce": "ROCE ((EBIT + other income) / avg capital employed)",
    "roic": "ROIC (NOPAT / avg invested capital)",
    "inv_days": "Inventory days (on material cost)",
    "rec_days": "Receivable days (on revenue)",
    "pay_days": "Payable days (on material cost)",
    "ccc": "Cash conversion cycle (days)",
    "cfo_to_ebitda": "CFO / EBITDA",
    "cfo_to_pat": "CFO / PAT",
    "fcf": "Free cash flow (CFO – capex), ₹ Cr",
    "net_debt": "Net debt (debt – cash – liquid inv.), ₹ Cr",
    "nd_to_ebitda": "Net debt / EBITDA",
    "int_cover": "Interest cover (EBIT / finance costs)",
    "de": "Debt / equity",
    "asset_turnover": "Asset turnover (revenue / total assets)",
    "eps": "EPS (basic), ₹",
    "adj_eps": "Adjusted EPS (ex-exceptional, post-tax), ₹",
    "bvps": "Book value per share, ₹",
    "dps_paid": "Dividend per share paid in year, ₹",
    "price": "Share price at 31-March, ₹",
    "pe": "P/E (trailing, on reported EPS)",
    "pb": "P/B",
    "ev_ebitda": "EV/EBITDA (EV incl. lease liabilities)",
}

#: Display format of each ratio: pct (1 dp %), x (1 dp multiple), days (0 dp), cr (₹ Cr, brackets
#: for negatives), rs (₹ 1 dp), int (0 dp).
RATIO_KINDS: dict[str, str] = {
    "rev_growth": "pct", "gross_margin": "pct", "ebitda_margin": "pct", "ebit_margin": "pct",
    "pat_margin": "pct", "roe": "pct", "roce": "pct", "roic": "pct", "inv_days": "days",
    "rec_days": "days", "pay_days": "days", "ccc": "days", "cfo_to_ebitda": "pct", "cfo_to_pat": "pct",
    "fcf": "cr", "net_debt": "cr", "nd_to_ebitda": "x", "int_cover": "x", "de": "x",
    "asset_turnover": "x", "eps": "rs", "adj_eps": "rs", "bvps": "rs", "dps_paid": "rs", "price": "int",
    "pe": "x", "pb": "x", "ev_ebitda": "x",
}

_BS_KEYS = ("equity", "lt_debt", "st_debt", "lease_liab", "net_block", "cwip", "rou", "intangibles",
            "inventory", "receivables", "oca", "payables", "ocl", "cash", "cur_inv")


def _per_year(value: Any, year: str) -> float:
    if value is None:
        return math.nan
    if isinstance(value, Mapping):
        return float(value.get(year, math.nan))
    if isinstance(value, pd.Series):
        return float(value.get(year, math.nan))
    return float(value)


def ratio_dashboard(
    df: pd.DataFrame,
    opening: Mapping[str, float] | pd.Series | None = None,
    *,
    tax_rate: float | None = None,
    shares: float | Mapping[str, float] | None = None,
    prices: Mapping[str, float] | pd.Series | None = None,
    dps: Mapping[str, float] | pd.Series | None = None,
) -> pd.DataFrame:
    """Compute the full ratio table from a Kaveri-layout annual frame.

    Parameters
    ----------
    df : DataFrame
        Line item x period, with the Kaveri line-item keys (``rev``, ``mat``, ``ebitda``, ``ebit``,
        ``other_income``, ``fin_cost``, ``exceptional``, ``pat``, ``cfo``, ``capex_ppe``,
        ``capex_int``, balance-sheet keys ...). ``load_kaveri()`` returns exactly this.
    opening : mapping, optional
        Balance sheet *before* the first column (needed for first-year averages). Defaults to
        ``df.attrs["opening"]`` when ``df.attrs["opening_for"]`` equals the first column; otherwise
        first-year ROE/ROCE/ROIC are NaN.
    tax_rate : float, optional
        For NOPAT and adjusted EPS. Defaults to ``df.attrs["tax_rate"]``, else each year's
        effective rate (tax / PBT).
    shares, prices, dps : optional
        Share count (crore; scalar or per-year mapping), 31-March share price (₹) and dividend per
        share paid (₹) by period. Default to ``df.attrs``. Missing -> the per-share/valuation rows are NaN.

    Returns
    -------
    DataFrame with the rows of ``RATIO_LABELS`` (keys as in ``tools/data/kaveri_pumps_ratios.csv``),
    one column per period, values as decimals / multiples / days / ₹. Use ``format_dashboard`` to
    print it the way the course tables show it.
    """
    attrs = getattr(df, "attrs", {}) or {}
    years = [str(c) for c in df.columns]
    if opening is None and attrs.get("opening") is not None and attrs.get("opening_for") == years[0]:
        opening = attrs["opening"]
    if tax_rate is None:
        tax_rate = attrs.get("tax_rate")
    if shares is None:
        shares = attrs.get("shares")
    if prices is None:
        prices = attrs.get("price")
    if dps is None:
        dps = attrs.get("dps_paid")

    def col(year: str) -> dict[str, float]:
        return {k: float(v) for k, v in df[year].items()}

    rows: dict[str, dict[str, float]] = {k: {} for k in RATIO_LABELS}
    prev: dict[str, float] | None = dict(opening) if opening is not None else None
    if prev is not None and "equity" not in prev:
        prev["equity"] = prev["share_capital"] + prev["other_equity"]
    if prev is not None and "net_block" not in prev:
        prev["net_block"] = prev["gross_block"] - prev["acc_dep"]
    prev_rev: float | None = None

    for year in years:
        y = col(year)
        rev = y["rev"]
        t = tax_rate if tax_rate is not None else (y["tax"] / y["pbt"] if y.get("pbt") else math.nan)
        r = {k: math.nan for k in RATIO_LABELS}
        r["rev_growth"] = rev / prev_rev - 1 if prev_rev else math.nan
        m = margins(rev, gross=rev - y["mat"], ebitda=y["ebitda"], ebit=y["ebit"], pat=y["pat"])
        r["gross_margin"], r["ebitda_margin"], r["ebit_margin"], r["pat_margin"] = (
            m["gross"], m["ebitda"], m["ebit"], m["pat"])
        if prev is not None:
            r["roe"] = roe(y["pat"], prev["equity"], y["equity"])
            r["roce"] = roce(y["ebit"], y["other_income"], capital_employed(prev), capital_employed(y))
            r["roic"] = roic(y["ebit"], t, invested_capital(prev), invested_capital(y))
        wc = working_capital_days(rev, y["mat"], y["inventory"], y["receivables"], y["payables"])
        r["inv_days"], r["rec_days"], r["pay_days"], r["ccc"] = wc["dio"], wc["dso"], wc["dpo"], wc["ccc"]
        r["cfo_to_ebitda"] = y["cfo"] / y["ebitda"]
        r["cfo_to_pat"] = y["cfo"] / y["pat"]
        r["fcf"] = y["cfo"] - y["capex_ppe"] - y.get("capex_int", 0.0)
        nd = net_debt(y)
        r["net_debt"] = nd
        r["nd_to_ebitda"] = nd / y["ebitda"]
        r["int_cover"] = y["ebit"] / y["fin_cost"]
        r["de"] = (y["lt_debt"] + y["st_debt"]) / y["equity"]
        r["asset_turnover"] = rev / y["total_assets"]
        n = _per_year(shares, year)
        price = _per_year(prices, year)
        r["eps"] = y["pat"] / n
        r["adj_eps"] = (y["pat"] - y.get("exceptional", 0.0) * (1 - t)) / n
        r["bvps"] = y["equity"] / n
        r["dps_paid"] = _per_year(dps, year)
        r["price"] = price
        r["pe"] = price / r["eps"]
        r["pb"] = price / r["bvps"]
        r["ev_ebitda"] = (price * n + nd + y["lease_liab"]) / y["ebitda"]
        for k, v in r.items():
            rows[k][year] = v
        prev = {k: y[k] for k in _BS_KEYS}
        prev_rev = rev

    out = pd.DataFrame.from_dict(rows, orient="index")[years]
    out.index.name = "ratio"
    out.columns.name = "period"
    return out


def _fmt(v: float, kind: str) -> str:
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "–"
    if kind == "pct":
        return f"{v * 100:.1f}%"
    if kind == "x":
        return f"{v:.1f}x"
    if kind == "days":
        return f"{v:.0f}"
    if kind == "rs":
        return f"{v:,.1f}"
    if kind == "int":
        return f"{v:,.0f}"
    # ₹ crore: brackets for negatives, as in the course's financial statements
    if abs(v) < 0.05:
        return "0.0"
    if v < 0:
        return f"({-v:,.1f})"
    return f"{v:,.1f}"


def format_dashboard(dash: pd.DataFrame, labels: bool = True) -> pd.DataFrame:
    """Format a ``ratio_dashboard`` result as strings exactly like the course tables.

    Percentages to one decimal, multiples as ``7.8x``, days as integers, ₹ Cr with brackets for
    negatives. ``labels=True`` replaces the keys with the table's row labels.
    """
    out = pd.DataFrame(
        {c: [_fmt(dash.at[k, c], RATIO_KINDS.get(k, "cr")) for k in dash.index] for c in dash.columns},
        index=dash.index,
    )
    if labels:
        out.index = [RATIO_LABELS.get(k, k) for k in out.index]
        out.index.name = "Ratio"
    return out
