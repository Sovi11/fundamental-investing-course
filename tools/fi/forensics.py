"""Forensic scoring models: Beneish M-score, Altman Z / Z' / Z'', Piotroski F-score, accruals.

These are *screens*, not verdicts. Each was estimated on US data decades ago; sector mix, Indian
accounting (Ind AS, P&L by nature), and business model all move the scores. Use them to decide
where to dig in the notes to accounts, never to conclude fraud or distress on their own. Lenders
(banks, NBFCs, insurers) are excluded by design from all three models.

Sources for the formulas (paraphrased; see Module 09.6 for the full discussion):

* Beneish, M. D. (1999), "The Detection of Earnings Manipulation", *Financial Analysts Journal*
  55(5): 24-36. 8-variable probit model; threshold -1.78.
* Altman, E. I. (1968), "Financial Ratios, Discriminant Analysis and the Prediction of Corporate
  Bankruptcy", *Journal of Finance* 23(4): 589-609 (original Z). Z' (private firms) and Z''
  (non-manufacturers / emerging markets) from Altman's later work, e.g. Altman, Iwanicz-Drozdowska,
  Laitinen & Suvas (2017), *Journal of International Financial Management & Accounting* 28(2).
* Piotroski, J. D. (2000), "Value Investing: The Use of Historical Financial Statement Information
  to Separate Winners from Losers", *Journal of Accounting Research* 38 (Supplement): 1-41.
* Sloan, R. G. (1996), "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows about
  Future Earnings?", *The Accounting Review* 71(3): 289-315.

Input dicts use these keys (all in the same currency unit)::

    sales, cogs, sga, receivables, current_assets, ppe, securities, total_assets, depreciation,
    current_liabilities, long_term_debt, net_income, cfo,                      # Beneish
    total_assets_begin, avg_total_assets, share_capital | shares_outstanding | equity_issued  # Piotroski

``forensic_inputs(df, year)`` builds them from a Kaveri-layout annual frame (mapping documented there).
"""
from __future__ import annotations

import math
from collections.abc import Mapping
from typing import Any

import pandas as pd

__all__ = [
    "BENEISH_COEFFS",
    "BENEISH_THRESHOLD",
    "beneish_m",
    "altman_z",
    "altman_zone",
    "piotroski_f",
    "accruals_ratio",
    "balance_sheet_accruals",
    "cash_yield_check",
    "forensic_inputs",
    "forensic_summary",
]

#: Beneish (1999) 8-variable model: intercept and coefficients.
BENEISH_COEFFS: dict[str, float] = {
    "intercept": -4.84,
    "DSRI": 0.920,
    "GMI": 0.528,
    "AQI": 0.404,
    "SGI": 0.892,
    "DEPI": 0.115,
    "SGAI": -0.172,
    "TATA": 4.679,
    "LVGI": -0.327,
}
#: M-score above this flags a *likely manipulator* (8-variable model, Beneish 1999). Some sources
#: quote -2.22 instead; always check which model and sample a cut-off was estimated on.
BENEISH_THRESHOLD = -1.78


def beneish_m(cur: Mapping[str, float], prev: Mapping[str, float]) -> dict[str, Any]:
    """Beneish (1999) 8-variable M-score for year *t* (``cur``) versus *t-1* (``prev``).

    Indices (each equals 1.0 when nothing changed):

    * DSRI = (REC_t / Sales_t) / (REC_t-1 / Sales_t-1)             - receivables outrunning sales
    * GMI  = GM_t-1 / GM_t, GM = (Sales - COGS) / Sales            - margin deterioration (> 1)
    * AQI  = [1 - (CA_t + PPE_t + Sec_t)/TA_t] / [same at t-1]    - growth in "soft" assets
    * SGI  = Sales_t / Sales_t-1                                   - growth pressure
    * DEPI = [Dep_t-1/(Dep_t-1 + PPE_t-1)] / [Dep_t/(Dep_t + PPE_t)] - slowing depreciation (> 1)
    * SGAI = (SGA_t / Sales_t) / (SGA_t-1 / Sales_t-1)
    * LVGI = [(CL_t + LTD_t)/TA_t] / [(CL_t-1 + LTD_t-1)/TA_t-1]
    * TATA = (Net income from continuing operations_t - CFO_t) / TA_t   (cash-flow accruals version)

    $$M = -4.84 + 0.920\\,DSRI + 0.528\\,GMI + 0.404\\,AQI + 0.892\\,SGI + 0.115\\,DEPI
         - 0.172\\,SGAI + 4.679\\,TATA - 0.327\\,LVGI$$

    Returns the eight indices, ``m_score``, ``threshold`` (-1.78) and ``likely_manipulator``
    (M > threshold). A company with every index at 1 and zero accruals scores -2.48.

    Beneish's original TATA used balance-sheet accruals (change in working capital excl. cash,
    current maturities of LTD and income tax payable, minus depreciation); the (NI - CFO)/TA form
    is the common modern implementation.
    """
    def ratio(a: float, b: float) -> float:
        return a / b if b else math.nan

    gm_t = ratio(cur["sales"] - cur["cogs"], cur["sales"])
    gm_p = ratio(prev["sales"] - prev["cogs"], prev["sales"])
    soft_t = 1 - (cur["current_assets"] + cur["ppe"] + cur.get("securities", 0.0)) / cur["total_assets"]
    soft_p = 1 - (prev["current_assets"] + prev["ppe"] + prev.get("securities", 0.0)) / prev["total_assets"]
    dep_rate_t = ratio(cur["depreciation"], cur["depreciation"] + cur["ppe"])
    dep_rate_p = ratio(prev["depreciation"], prev["depreciation"] + prev["ppe"])
    idx = {
        "DSRI": ratio(cur["receivables"] / cur["sales"], prev["receivables"] / prev["sales"]),
        "GMI": ratio(gm_p, gm_t),
        "AQI": ratio(soft_t, soft_p),
        "SGI": ratio(cur["sales"], prev["sales"]),
        "DEPI": ratio(dep_rate_p, dep_rate_t),
        "SGAI": ratio(cur["sga"] / cur["sales"], prev["sga"] / prev["sales"]),
        "LVGI": ratio((cur["current_liabilities"] + cur["long_term_debt"]) / cur["total_assets"],
                      (prev["current_liabilities"] + prev["long_term_debt"]) / prev["total_assets"]),
        "TATA": (cur["net_income"] - cur["cfo"]) / cur["total_assets"],
    }
    m = BENEISH_COEFFS["intercept"] + sum(BENEISH_COEFFS[k] * v for k, v in idx.items())
    return {**idx, "m_score": m, "threshold": BENEISH_THRESHOLD, "likely_manipulator": bool(m > BENEISH_THRESHOLD)}


_ALTMAN = {
    # variant: (weights for X1..X5, (distress_below, safe_above), constant)
    "original": ((1.2, 1.4, 3.3, 0.6, 1.0), (1.81, 2.99), 0.0),
    "z_prime": ((0.717, 0.847, 3.107, 0.420, 0.998), (1.23, 2.90), 0.0),
    "z_double_prime": ((6.56, 3.26, 6.72, 1.05, 0.0), (1.10, 2.60), 0.0),
    "z_double_prime_em": ((6.56, 3.26, 6.72, 1.05, 0.0), (4.35, 5.85), 3.25),
}


def altman_z(wc: float, re: float, ebit: float, mve: float, sales: float, ta: float, tl: float,
             variant: str = "original") -> float:
    """Altman Z-score family.

    X1 = working capital / TA; X2 = retained earnings / TA; X3 = EBIT / TA;
    X4 = equity / total liabilities; X5 = sales / TA.

    * ``"original"`` (1968, listed manufacturers): Z = 1.2 X1 + 1.4 X2 + 3.3 X3 + 0.6 X4 + 1.0 X5,
      X4 uses the **market value** of equity. Zones: < 1.81 distress, 1.81-2.99 grey, > 2.99 safe.
    * ``"z_prime"`` (private firms): 0.717, 0.847, 3.107, 0.420 (X4 on **book** equity), 0.998.
      Zones: < 1.23 / > 2.90.
    * ``"z_double_prime"`` (non-manufacturers & emerging markets; drops X5 because asset turnover
      is so industry-specific): Z'' = 6.56 X1 + 3.26 X2 + 6.72 X3 + 1.05 X4, X4 on **book** equity.
      Zones: < 1.10 distress, 1.10-2.60 grey, > 2.60 safe.
    * ``"z_double_prime_em"``: Z'' + 3.25 (the emerging-market constant, which lets the score be
      mapped to bond-rating equivalents). ``altman_zone`` applies the Z'' cut-offs shifted by the
      same constant (< 4.35 / > 5.85); Altman's own EM usage maps the score to rating equivalents instead.

    For the book-equity variants pass book equity as ``mve`` (one signature for all variants).
    """
    if variant not in _ALTMAN:
        raise ValueError(f"variant must be one of {sorted(_ALTMAN)}")
    w, _, const = _ALTMAN[variant]
    x = (wc / ta, re / ta, ebit / ta, mve / tl, sales / ta)
    return const + sum(wi * xi for wi, xi in zip(w, x))


def altman_zone(z: float, variant: str = "original") -> str:
    """Classify a Z-score as ``"distress"``, ``"grey"`` or ``"safe"`` using the variant's cut-offs."""
    lo, hi = _ALTMAN[variant][1]
    if z < lo:
        return "distress"
    if z > hi:
        return "safe"
    return "grey"


def _equity_issued(cur: Mapping[str, Any], prev: Mapping[str, Any]) -> bool:
    if "equity_issued" in cur:
        return bool(cur["equity_issued"])
    for key in ("shares_outstanding", "share_capital"):
        if key in cur and key in prev:
            return cur[key] > prev[key] + 1e-9
    raise KeyError("piotroski_f needs 'equity_issued', or 'shares_outstanding'/'share_capital' in both years")


def piotroski_f(cur: Mapping[str, Any], prev: Mapping[str, Any]) -> dict[str, Any]:
    """Piotroski (2000) F-score: nine binary signals, 1 = good news.

    Profitability
      1. ``f_roa``      ROA_t > 0, ROA = net income / **beginning-of-year** total assets
      2. ``f_cfo``      CFO_t > 0
      3. ``f_droa``     ROA_t > ROA_t-1
      4. ``f_accrual``  CFO_t / TA_begin > ROA_t (cash earnings exceed accounting earnings)
    Leverage, liquidity, source of funds
      5. ``f_dlever``   long-term debt / **average** total assets fell (1 also if zero in both years)
      6. ``f_dliquid``  current ratio rose
      7. ``f_eq_offer`` no common equity issued in the year
    Operating efficiency
      8. ``f_dmargin``  gross margin rose
      9. ``f_dturn``    asset turnover (sales / beginning-of-year TA) rose

    Each dict needs: ``net_income, cfo, total_assets_begin, long_term_debt, current_assets,
    current_liabilities, sales, cogs`` and ``avg_total_assets`` (defaults to the mean of
    ``total_assets_begin`` and ``total_assets``), plus ``equity_issued`` or ``shares_outstanding`` /
    ``share_capital`` for signal 7. Returns the nine signals, ``score`` (0-9) and ``values``.
    """
    def avg_ta(d: Mapping[str, Any]) -> float:
        if "avg_total_assets" in d:
            return d["avg_total_assets"]
        return (d["total_assets_begin"] + d["total_assets"]) / 2

    v = {}
    for tag, d in (("cur", cur), ("prev", prev)):
        v[f"roa_{tag}"] = d["net_income"] / d["total_assets_begin"]
        v[f"cfo_ta_{tag}"] = d["cfo"] / d["total_assets_begin"]
        v[f"lever_{tag}"] = d["long_term_debt"] / avg_ta(d)
        v[f"current_ratio_{tag}"] = d["current_assets"] / d["current_liabilities"]
        v[f"gross_margin_{tag}"] = (d["sales"] - d["cogs"]) / d["sales"]
        v[f"turnover_{tag}"] = d["sales"] / d["total_assets_begin"]
    lever_ok = v["lever_cur"] < v["lever_prev"] or (cur["long_term_debt"] == 0 and prev["long_term_debt"] == 0)
    signals = {
        "f_roa": int(v["roa_cur"] > 0),
        "f_cfo": int(cur["cfo"] > 0),
        "f_droa": int(v["roa_cur"] > v["roa_prev"]),
        "f_accrual": int(v["cfo_ta_cur"] > v["roa_cur"]),
        "f_dlever": int(lever_ok),
        "f_dliquid": int(v["current_ratio_cur"] > v["current_ratio_prev"]),
        "f_eq_offer": int(not _equity_issued(cur, prev)),
        "f_dmargin": int(v["gross_margin_cur"] > v["gross_margin_prev"]),
        "f_dturn": int(v["turnover_cur"] > v["turnover_prev"]),
    }
    return {**signals, "score": sum(signals.values()), "values": v}


def accruals_ratio(pat: float, cfo: float, avg_total_assets: float) -> float:
    """Cash-flow accruals ratio = (PAT - CFO) / average total assets.

    Persistent positive values mean profits are running ahead of cash (Sloan 1996 found high-accrual
    firms subsequently under-perform). Kaveri FY26: (90.5 - 65.1) / 1,089.7 = 2.3%.
    """
    return (pat - cfo) / avg_total_assets


def balance_sheet_accruals(d_current_assets: float, d_cash: float, d_current_liabilities: float,
                           d_short_term_debt: float, depreciation: float, avg_total_assets: float,
                           d_taxes_payable: float = 0.0) -> float:
    """Sloan (1996) balance-sheet accruals scaled by average total assets.

    $$Accruals = \\frac{(\\Delta CA - \\Delta Cash) - (\\Delta CL - \\Delta STD - \\Delta TP) - Dep}{\\overline{TA}}$$

    ΔCA/ΔCL: change in current assets/liabilities; ΔCash: change in cash and short-term (liquid)
    investments; ΔSTD: change in debt inside current liabilities; ΔTP: change in income tax payable;
    Dep: depreciation & amortisation. Financing items are excluded because they are not accruals.
    """
    accruals = (d_current_assets - d_cash) - (d_current_liabilities - d_short_term_debt - d_taxes_payable) - depreciation
    return accruals / avg_total_assets


def cash_yield_check(cash_and_investments_avg: float, other_income: float) -> float:
    """Implied yield on cash = treasury/other income / average (cash + liquid investments).

    The "Satyam test": a company reporting large cash balances should earn roughly deposit or
    liquid-fund rates on them. An implied yield far below those rates (Satyam Computer Services,
    whose cash turned out to be largely fictitious when the fraud was confessed in January 2009, is
    the classic case) says the cash may not exist or is encumbered. Far *above* them says other
    income contains non-treasury items. Compare with the prevailing liquid-fund / FD yield of the year.

    Kaveri FY26: 3.9 / ((28.0 + 30.0 + 32.5 + 15.0)/2) = 7.4%.
    """
    if cash_and_investments_avg <= 0:
        raise ValueError("average cash & investments must be positive")
    return other_income / cash_and_investments_avg


# ---------------------------------------------------------------------------
# Building inputs from a Kaveri-layout annual frame
# ---------------------------------------------------------------------------
def forensic_inputs(df: pd.DataFrame, year: str, *, opening: Mapping[str, float] | None = None,
                    price: float | None = None, shares: float | None = None) -> dict[str, float]:
    """Build the input dict for ``beneish_m`` / ``piotroski_f`` / ``altman_z`` from a Kaveri-layout frame.

    Mapping assumptions (Indian P&Ls are classified *by nature*, not by function, so some US
    line items have to be proxied - state these whenever you quote a score):

    * ``sales`` = revenue from operations (``rev``); ``cogs`` = cost of materials consumed incl.
      change in inventories (``mat``), so gross margin matches the course ratio table.
    * ``sga`` = employee benefits + other expenses (``emp + oth``). Factory wages sit in employee
      cost, so this overstates true SG&A, but it is consistent year to year, which is all SGAI needs.
    * ``current_assets`` = inventories + trade receivables + other current assets + current
      investments + cash. ``securities`` = 0 (Kaveri's liquid funds are already current assets and
      it has no long-term investments).
    * ``ppe`` = net block + CWIP + right-of-use assets; ``depreciation`` = PP&E depreciation +
      ROU amortisation (matching ``ppe``). So Beneish's "soft assets" are just intangibles.
    * ``current_liabilities`` = current borrowings + trade payables + other current liabilities;
      ``long_term_debt`` = non-current borrowings + lease liabilities.
    * ``net_income`` = PAT (no discontinued operations; exceptional items are included, as reported).
    * ``total_assets_begin`` = prior column's total assets (or ``opening`` / ``df.attrs["opening"]``
      for the first year); ``avg_total_assets`` = mean of opening and closing.
    * Altman: ``working_capital`` = current assets - current liabilities; ``retained_earnings`` =
      other equity (reserves & surplus - a proxy, it also contains any securities premium);
      ``ebit`` = EBIT + other income (= PBT + finance costs - exceptional items);
      ``book_equity`` = total equity; ``total_liabilities`` = total assets - equity;
      ``market_cap`` = 31-March price x shares (from ``df.attrs`` unless given), else absent.
    """
    years = [str(c) for c in df.columns]
    if year not in years:
        raise KeyError(f"{year} not in {years}")
    i = years.index(year)
    y = {k: float(v) for k, v in df[year].items()}
    attrs = getattr(df, "attrs", {}) or {}
    if i > 0:
        ta_begin = float(df.at["total_assets", years[i - 1]])
    else:
        op = opening
        if op is None and attrs.get("opening_for") == year:
            op = attrs.get("opening")
        ta_begin = float(op["total_assets"]) if op is not None and "total_assets" in op else math.nan
    ca = y["inventory"] + y["receivables"] + y["oca"] + y["cur_inv"] + y["cash"]
    cl = y["st_debt"] + y["payables"] + y["ocl"]
    out = {
        "year": year,
        "sales": y["rev"],
        "cogs": y["mat"],
        "sga": y["emp"] + y["oth"],
        "receivables": y["receivables"],
        "current_assets": ca,
        "ppe": y["net_block"] + y["cwip"] + y["rou"],
        "securities": 0.0,
        "total_assets": y["total_assets"],
        "depreciation": y["dep_ppe"] + y["rou_amort"],
        "current_liabilities": cl,
        "long_term_debt": y["lt_debt"] + y["lease_liab"],
        "net_income": y["pat"],
        "cfo": y["cfo"],
        "cash": y["cash"],
        "cash_and_investments": y["cash"] + y["cur_inv"],
        "other_income": y["other_income"],
        "total_assets_begin": ta_begin,
        "avg_total_assets": (ta_begin + y["total_assets"]) / 2,
        "share_capital": y["share_capital"],
        "working_capital": ca - cl,
        "retained_earnings": y["other_equity"],
        "ebit": y["ebit"] + y["other_income"],
        "book_equity": y["equity"],
        "total_liabilities": y["total_assets"] - y["equity"],
    }
    if price is None and isinstance(attrs.get("price"), Mapping):
        price = attrs["price"].get(year)
    if shares is None:
        shares = attrs.get("shares")
    if price is not None and shares is not None:
        out["market_cap"] = float(price) * float(shares)
    return out


def forensic_summary(df: pd.DataFrame, year: str, *, mve: float | None = None) -> dict[str, Any]:
    """Run every score on ``year`` versus the prior column of a Kaveri-layout frame.

    Returns ``beneish`` (dict), ``piotroski`` (dict), ``altman_original`` (market-cap based;
    NaN if no market value), ``altman_z_double_prime`` (book equity), ``accruals_ratio``,
    ``balance_sheet_accruals``, ``cash_yield`` and the two input dicts (``inputs_cur``, ``inputs_prev``).
    """
    years = [str(c) for c in df.columns]
    i = years.index(year)
    if i == 0:
        raise ValueError("need a prior year column for year-on-year scores")
    cur = forensic_inputs(df, year)
    prev = forensic_inputs(df, years[i - 1])
    mcap = mve if mve is not None else cur.get("market_cap", math.nan)
    alt_args = dict(wc=cur["working_capital"], re=cur["retained_earnings"], ebit=cur["ebit"],
                    sales=cur["sales"], ta=cur["total_assets"], tl=cur["total_liabilities"])
    z_orig = altman_z(mve=mcap, variant="original", **alt_args)
    z_dp = altman_z(mve=cur["book_equity"], variant="z_double_prime", **alt_args)
    d = lambda k: float(df.at[k, year]) - float(df.at[k, years[i - 1]])  # noqa: E731
    bs_acc = balance_sheet_accruals(
        d_current_assets=cur["current_assets"] - prev["current_assets"],
        d_cash=cur["cash_and_investments"] - prev["cash_and_investments"],
        d_current_liabilities=cur["current_liabilities"] - prev["current_liabilities"],
        d_short_term_debt=d("st_debt"),
        depreciation=float(df.at["da", year]),
        avg_total_assets=cur["avg_total_assets"],
    )
    return {
        "year": year,
        "beneish": beneish_m(cur, prev),
        "piotroski": piotroski_f(cur, prev),
        "altman_original": z_orig,
        "altman_original_zone": altman_zone(z_orig, "original") if not math.isnan(z_orig) else None,
        "altman_z_double_prime": z_dp,
        "altman_z_double_prime_zone": altman_zone(z_dp, "z_double_prime"),
        "accruals_ratio": accruals_ratio(cur["net_income"], cur["cfo"], cur["avg_total_assets"]),
        "balance_sheet_accruals": bs_acc,
        "cash_yield": cash_yield_check((cur["cash_and_investments"] + prev["cash_and_investments"]) / 2,
                                       cur["other_income"]),
        "inputs_cur": cur,
        "inputs_prev": prev,
    }
