"""Valuation building blocks: CAPM/WACC, DCF, terminal value, sensitivity, reverse DCF, multiples.

All rates are decimals (0.1219 = 12.19%). Cash flows are in whatever unit you pass (the course uses
₹ crore). Functions are deliberately small and composable so a lesson can show each step:

    ke   = capm(0.065, 1.05, 0.06)                   # 12.80%
    w    = wacc(ke, 0.089, 0.2517, 0.10)            # 12.19%
    tv   = terminal_value(nopat_next, w, 0.055, ronic=0.18)
    dcf  = dcf_fcff(fcffs, w, tv, mid_year=True)
    eq   = equity_bridge(dcf["ev"], net_debt=140.5, leases=18.2)

``dcf_from_drivers`` strings these together for a driver-based (revenue growth x margin x
reinvestment) FCFF model, and ``kaveri_reference()`` reproduces the course's house valuation of
Kaveri Pumps (₹320/share) by calling ``tools/running_example/valuation.py`` directly.
"""
from __future__ import annotations

import math
from collections.abc import Callable, Mapping, Sequence
from typing import Any

import pandas as pd

__all__ = [
    "capm",
    "wacc",
    "gordon_value",
    "terminal_value",
    "dcf_fcff",
    "equity_bridge",
    "sensitivity",
    "reverse_dcf",
    "justified_pe",
    "justified_pb",
    "dcf_from_drivers",
    "kaveri_base_drivers",
    "kaveri_reference",
]


def capm(rf: float, beta: float, erp: float) -> float:
    """Cost of equity by CAPM: $k_e = r_f + \\beta \\times ERP$.

    >>> round(capm(0.065, 1.05, 0.06), 4)   # Kaveri reference
    0.128
    """
    return rf + beta * erp


def wacc(ke: float, kd_pre_tax: float, tax_rate: float, debt_weight: float) -> float:
    """Weighted average cost of capital with *target* weights.

    $WACC = (1 - w_d) k_e + w_d k_d (1 - t)$ where $w_d$ = D / (D + E) at target (market) values.

    >>> round(wacc(0.128, 0.089, 0.2517, 0.10), 4)   # Kaveri: 12.19%
    0.1219
    """
    if not 0 <= debt_weight <= 1:
        raise ValueError("debt_weight must be between 0 and 1")
    return (1 - debt_weight) * ke + debt_weight * kd_pre_tax * (1 - tax_rate)


def gordon_value(cf_next: float, r: float, g: float) -> float:
    """Growing perpetuity value today of a cash flow ``cf_next`` received one period from now.

    $V_0 = CF_1 / (r - g)$. Raises ``ValueError`` if $g \\ge r$ (the sum diverges).
    """
    if g >= r:
        raise ValueError(f"growth g={g:.4f} must be below the discount rate r={r:.4f}")
    return cf_next / (r - g)


def terminal_value(nopat_next: float, r: float, g: float, ronic: float | None = None,
                   fcff_next: float | None = None) -> float:
    """Terminal value at the end of the explicit forecast.

    * With ``ronic`` (return on *new* invested capital) - the value-driver formula
      $TV = NOPAT_{T+1} (1 - g / RONIC) / (WACC - g)$. Reinvestment rate $g/RONIC$ is the
      capex + working capital needed to *earn* the growth; ``ronic == r`` makes growth worth nothing.
    * With ``fcff_next`` - plain Gordon growth on the given next-year FCFF.

    Exactly one of ``ronic`` / ``fcff_next`` must be supplied (growth without reinvestment is the
    classic DCF error, so there is deliberately no default).
    """
    if (ronic is None) == (fcff_next is None):
        raise ValueError("pass exactly one of ronic= (value-driver formula) or fcff_next= (Gordon)")
    if ronic is not None:
        if ronic <= 0:
            raise ValueError("ronic must be positive")
        cf = nopat_next * (1 - g / ronic)
    else:
        cf = float(fcff_next)
    return gordon_value(cf, r, g)


def dcf_fcff(fcffs: Sequence[float], r: float, tv: float, mid_year: bool = True) -> dict[str, Any]:
    """Discount explicit FCFFs and a terminal value to an enterprise value.

    Year *t* (1-based) cash flow is discounted by $(1+r)^{t-0.5}$ under the mid-year convention
    (cash arrives on average mid-year) or $(1+r)^t$ otherwise. The terminal value sits at the
    **end** of year *N* and is always discounted by $(1+r)^N$.

    Returns ``pv_explicit``, ``pv_tv``, ``ev``, ``discount_factors`` (list), ``pv_fcff`` (list),
    ``tv_share`` (PV of TV / EV).
    """
    fcffs = [float(x) for x in fcffs]
    n = len(fcffs)
    shift = 0.5 if mid_year else 0.0
    dfs = [1 / (1 + r) ** (t + 1 - shift) for t in range(n)]
    pvs = [cf * d for cf, d in zip(fcffs, dfs)]
    pv_explicit = sum(pvs)
    pv_tv = tv / (1 + r) ** n
    ev = pv_explicit + pv_tv
    return {"pv_explicit": pv_explicit, "pv_tv": pv_tv, "ev": ev, "discount_factors": dfs, "pv_fcff": pvs,
            "tv_share": pv_tv / ev if ev else math.nan}


def equity_bridge(ev: float, net_debt: float, leases: float = 0, nci: float = 0, investments: float = 0) -> float:
    """Enterprise value -> equity value.

    Equity = EV - net debt - lease liabilities - non-controlling interests + non-operating
    investments (only those whose income was *excluded* from the FCFF). Other claims you may need
    to subtract yourself: ESOP dilution (use diluted shares), probable contingent liabilities,
    unfunded pensions.

    Kaveri: 2,100.0 - 140.5 - 18.2 = 1,941.3.
    """
    return ev - net_debt - leases - nci + investments


def sensitivity(fn: Callable[..., float], rows: Mapping[str, Sequence[Any]],
                cols: Mapping[str, Sequence[Any]]) -> pd.DataFrame:
    """Generic two-way sensitivity table.

    ``rows`` and ``cols`` are single-key dicts ``{param_name: values}``; the table cell is
    ``fn(**{row_param: rv, col_param: cv})``.

    >>> t = sensitivity(lambda r, g: 100 / (r - g), {"r": [0.10, 0.12]}, {"g": [0.03, 0.05]})
    >>> round(float(t.loc[0.10, 0.05]), 1)
    2000.0
    """
    if len(rows) != 1 or len(cols) != 1:
        raise ValueError("rows and cols must each be a single-key dict {param: values}")
    (rk, rvals), = rows.items()
    (ck, cvals), = cols.items()
    data = [[fn(**{rk: rv, ck: cv}) for cv in cvals] for rv in rvals]
    out = pd.DataFrame(data, index=pd.Index(list(rvals), name=rk), columns=pd.Index(list(cvals), name=ck))
    return out


def reverse_dcf(price: float, value_fn: Callable[[float], float], lo: float = -0.05, hi: float = 0.5,
                tol: float = 1e-6, max_iter: int = 200) -> float:
    """Solve ``value_fn(x) == price`` for a scalar input *x* by bisection.

    Typical use: *x* is a uniform revenue growth rate and ``value_fn`` returns value per share.
    Works for increasing or decreasing ``value_fn`` as long as ``[lo, hi]`` brackets the price.
    This is implied volatility for fundamentals: the price is the input, the expectation the output.

    Raises ``ValueError`` if the price is not bracketed.
    """
    f_lo = value_fn(lo) - price
    f_hi = value_fn(hi) - price
    if f_lo == 0:
        return lo
    if f_hi == 0:
        return hi
    if f_lo * f_hi > 0:
        raise ValueError(f"price {price} not bracketed: value({lo})={f_lo + price:.4g}, "
                         f"value({hi})={f_hi + price:.4g}; widen lo/hi")
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        f_mid = value_fn(mid) - price
        if f_mid == 0 or (hi - lo) / 2 < tol:
            return mid
        if (f_lo < 0) == (f_mid < 0):
            lo, f_lo = mid, f_mid
        else:
            hi = mid
    return (lo + hi) / 2


def justified_pe(payout_or_roe: float, r: float, g: float | None, *, roe: float | None = None,
                 trailing: bool = False) -> float:
    """Justified (forward) P/E from the Gordon model.

    Two ways to call it:

    * ``justified_pe(roe, r, g)`` - payout implied by sustainable growth, $b = 1 - g/ROE$:
      $P/E_{fwd} = (1 - g/ROE) / (r - g)$.
    * ``justified_pe(payout, r, g, roe=roe)`` - explicit payout ratio: $P/E_{fwd} = payout/(r - g)$.
      If ``g`` is ``None`` it is set to the sustainable growth $g = ROE \\times (1 - payout)$.

    ``trailing=True`` returns the trailing multiple $P/E_{fwd} \\times (1 + g)$.

    >>> round(justified_pe(0.18, 0.128, 0.055), 2)   # ROE 18%, ke 12.8%, g 5.5%
    9.51
    """
    if roe is None:
        if g is None:
            raise ValueError("g is required when roe= is not given")
        if payout_or_roe == 0:
            raise ZeroDivisionError("ROE is zero")
        payout = 1 - g / payout_or_roe
    else:
        payout = payout_or_roe
        if g is None:
            g = roe * (1 - payout)
    if g >= r:
        raise ValueError(f"g={g:.4f} must be below r={r:.4f}")
    pe = payout / (r - g)
    return pe * (1 + g) if trailing else pe


def justified_pb(roe: float, r: float, g: float) -> float:
    """Justified P/B = (ROE - g) / (r - g). Above 1 only when ROE > cost of equity.

    >>> round(justified_pb(0.15, 0.14, 0.08), 3)
    1.167
    """
    if g >= r:
        raise ValueError(f"g={g:.4f} must be below r={r:.4f}")
    return (roe - g) / (r - g)


def _as_list(x: float | Sequence[float], n: int) -> list[float]:
    if isinstance(x, (int, float)):
        return [float(x)] * n
    xs = [float(v) for v in x]
    if len(xs) < n:
        xs += [xs[-1]] * (n - len(xs))
    return xs[:n]


def dcf_from_drivers(
    *,
    base_revenue: float,
    base_nwc: float,
    growth: Sequence[float],
    ebitda_margin: float | Sequence[float],
    da_pct: float | Sequence[float],
    capex_pct: float | Sequence[float],
    nwc_pct: float | Sequence[float],
    tax_rate: float,
    wacc: float,
    g: float,
    ronic: float | None = None,
    net_debt: float = 0.0,
    leases: float = 0.0,
    shares: float = 1.0,
    mid_year: bool = True,
    labels: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Driver-based FCFF DCF (the structure of the Kaveri reference valuation).

    For each forecast year: revenue = previous x (1 + growth); EBITDA = revenue x margin;
    D&A = revenue x da_pct; EBIT = EBITDA - D&A; NOPAT = EBIT x (1 - t); capex = revenue x capex_pct;
    NWC = revenue x nwc_pct; FCFF = NOPAT + D&A - capex - change in NWC.

    Terminal value: with ``ronic``, next-year NOPAT = last NOPAT x (1 + g) and
    FCFF = NOPAT x (1 - g/RONIC) (``terminal_value(..., ronic=)``); without it, the last FCFF is
    grown at ``g`` (Gordon). The horizon length is ``len(growth)``; scalar drivers are broadcast.

    Returns a dict with ``projection`` (DataFrame), ``fcff`` (list), ``tv``, ``pv_explicit``,
    ``pv_tv``, ``ev``, ``equity``, ``per_share``, ``tv_share``, ``fcff_next``, ``discount_factors``.
    """
    n = len(growth)
    gr = _as_list(growth, n)
    mg, da_p, cx_p, nwc_p = (_as_list(v, n) for v in (ebitda_margin, da_pct, capex_pct, nwc_pct))
    labels = list(labels) if labels is not None else [f"Y{t + 1}" for t in range(n)]
    rev, nwc_prev = float(base_revenue), float(base_nwc)
    rows = []
    for t in range(n):
        rev = rev * (1 + gr[t])
        ebitda = rev * mg[t]
        da = rev * da_p[t]
        ebit = ebitda - da
        nopat = ebit * (1 - tax_rate)
        capex = rev * cx_p[t]
        nwc = rev * nwc_p[t]
        d_nwc = nwc - nwc_prev
        nwc_prev = nwc
        rows.append({"rev": rev, "growth": gr[t], "ebitda": ebitda, "ebitda_margin": mg[t], "da": da,
                     "ebit": ebit, "nopat": nopat, "capex": capex, "nwc": nwc, "d_nwc": d_nwc,
                     "fcff": nopat + da - capex - d_nwc})
    last = rows[-1]
    if ronic is not None:
        nopat_next = last["nopat"] * (1 + g)
        fcff_next = nopat_next * (1 - g / ronic)
        tv = terminal_value(nopat_next, wacc, g, ronic=ronic)
    else:
        fcff_next = last["fcff"] * (1 + g)
        tv = terminal_value(math.nan, wacc, g, fcff_next=fcff_next)
    fcffs = [r["fcff"] for r in rows]
    d = dcf_fcff(fcffs, wacc, tv, mid_year=mid_year)
    for r, df_, pv in zip(rows, d["discount_factors"], d["pv_fcff"]):
        r["discount_factor"], r["pv_fcff"] = df_, pv
    equity = equity_bridge(d["ev"], net_debt=net_debt, leases=leases)
    proj = pd.DataFrame(rows, index=labels).T
    return {"projection": proj, "fcff": fcffs, "tv": tv, "pv_explicit": d["pv_explicit"], "pv_tv": d["pv_tv"],
            "ev": d["ev"], "equity": equity, "per_share": equity / shares, "tv_share": d["tv_share"],
            "fcff_next": fcff_next, "discount_factors": d["discount_factors"]}


def _reference_module():
    from .data import _load_running_example

    return _load_running_example("valuation")


def kaveri_base_drivers() -> dict[str, Any]:
    """Keyword arguments for ``dcf_from_drivers`` that reproduce the Kaveri reference base case.

    Built from ``tools/running_example/valuation.py`` (assumption dict ``A``) and FY26 actuals:
    base revenue ₹1,318.0 Cr, base NWC = inventory + receivables + OCA - payables - OCL = ₹365.0 Cr,
    WACC from ``capm``/``wacc`` (12.19%), g 5.5%, RONIC 18%, net debt ₹140.5 Cr, leases ₹18.2 Cr,
    6.07 Cr diluted shares.
    """
    ref = _reference_module()
    a = ref.A
    fy = ref.load_fy26()
    ke = capm(a["rf"], a["beta"], a["erp"])
    return dict(
        base_revenue=fy["rev"],
        base_nwc=fy["inventory"] + fy["receivables"] + fy["oca"] - fy["payables"] - fy["ocl"],
        growth=list(a["growth"]),
        ebitda_margin=list(a["ebitda_margin"]),
        da_pct=a["da_pct"],
        capex_pct=list(a["capex_pct"]),
        nwc_pct=list(a["nwc_pct"]),
        tax_rate=a["tax"],
        wacc=wacc(ke, a["kd_pre"], a["tax"], a["target_debt_weight"]),
        g=a["g_terminal"],
        ronic=a["ronic"],
        net_debt=a["net_debt"],
        leases=a["lease_liab"],
        shares=a["diluted_shares"],
        mid_year=True,
        labels=list(a["years"]),
    )


def kaveri_reference() -> dict[str, Any]:
    """Reproduce the course's Kaveri Pumps house valuation (``kaveri-valuation.md``).

    Calls ``run()`` and ``reverse_dcf()`` in ``tools/running_example/valuation.py`` (the single
    source of truth) and returns:

    ``per_share`` (≈ ₹320.0), ``ev`` (≈ 2,100.0), ``equity`` (≈ 1,941.3), ``wacc`` (12.19%), ``ke``,
    ``kd`` (post-tax), ``g``, ``ronic``, ``tv``, ``pv_tv``, ``pv_explicit``, ``tv_share`` (≈ 55%),
    ``fcff_next``, ``projection`` (DataFrame FY27-FY36), ``sensitivity`` (WACC x g DataFrame of
    value/share), ``scenarios`` ({"Bull", "Base", "Bear"} -> value/share), ``probabilities``,
    ``probability_weighted`` (≈ ₹306), ``implied_growth`` (≈ 14.1% at ₹390), ``cmp`` (₹390),
    ``roll_forward_per_share`` (≈ ₹338), ``assumptions`` (dict), and ``cross_check_per_share`` - the
    same valuation recomputed independently with this module's ``dcf_from_drivers``.
    """
    ref = _reference_module()
    a = ref.A
    base = ref.run()
    w = base["wacc"]
    waccs = [w - 0.01, w - 0.005, w, w + 0.005, w + 0.01]
    gs = [0.04, 0.045, 0.05, 0.055, 0.06]
    sens = pd.DataFrame(
        [[ref.run(wacc_override=ww, g_override=gg)["per_share"] for gg in gs] for ww in waccs],
        index=pd.Index([round(x, 6) for x in waccs], name="wacc"), columns=pd.Index(gs, name="g"))
    scen = {k: ref.run(growth=v["growth"], margin=v["ebitda_margin"], nwc=v["nwc_pct"])["per_share"]
            for k, v in ref.SCENARIOS.items()}
    scenarios = {"Bull": scen["Bull"], "Base": base["per_share"], "Bear": scen["Bear"]}
    pw = sum(ref.PROBS[k] * v for k, v in scenarios.items())
    proj = pd.DataFrame(base["rows"]).set_index("year").T
    check = dcf_from_drivers(**kaveri_base_drivers())
    return {
        "per_share": base["per_share"],
        "ev": base["ev"],
        "equity": base["equity"],
        "wacc": base["wacc"],
        "ke": base["ke"],
        "kd": base["kd"],
        "g": base["g"],
        "ronic": base["ronic"],
        "tv": base["tv"],
        "pv_tv": base["pv_tv"],
        "pv_explicit": base["pv_sum"],
        "tv_share": base["tv_share"],
        "fcff_next": base["fcff_next"],
        "projection": proj,
        "sensitivity": sens,
        "scenarios": scenarios,
        "probabilities": dict(ref.PROBS),
        "probability_weighted": pw,
        "implied_growth": ref.reverse_dcf(a["cmp"]),
        "cmp": a["cmp"],
        "roll_forward_per_share": base["per_share"] * (1 + base["ke"]) ** (171 / 365),
        "assumptions": dict(a),
        "cross_check_per_share": check["per_share"],
    }
