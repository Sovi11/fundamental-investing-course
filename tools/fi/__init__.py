"""``fi`` - Python helpers for the *Fundamental Investing - From Zero* course.

Modules
-------
data       load the fictional running examples (Kaveri Pumps, Nirmal Finance); fetch real Indian
           company statements via OpenBB / yfinance
ratios     margins, ROE/ROCE/ROIC, DuPont, working-capital days, the Kaveri ratio dashboard
valuation  CAPM/WACC, DCF, terminal value, sensitivity grids, reverse DCF, justified multiples,
           and the Kaveri reference valuation (₹320/share)
forensics  Beneish M-score, Altman Z/Z'/Z'', Piotroski F-score, accruals, cash-yield check
model      three-statement projection engine (cash as the plug, no circularity)

Make ``tools/`` importable first, e.g. from the repository root::

    import sys; sys.path.insert(0, "tools")
    from fi import load_kaveri, ratio_dashboard

Only ``fi.data.fetch_statements`` / ``fetch_price_info`` need the network (and no VPN).
Educational code: nothing here is a recommendation to buy or sell any security.
"""
from __future__ import annotations

from . import data, forensics, model, ratios, valuation
from .data import fetch_price_info, fetch_statements, load_kaveri, load_nirmal
from .forensics import altman_z, beneish_m, forensic_inputs, forensic_summary, piotroski_f
from .model import Assumptions, fcff_from_projection, project
from .ratios import format_dashboard, ratio_dashboard
from .valuation import (
    capm,
    dcf_fcff,
    dcf_from_drivers,
    equity_bridge,
    kaveri_reference,
    reverse_dcf,
    sensitivity,
    terminal_value,
    wacc,
)

__version__ = "1.0.0"

__all__ = [
    "data", "ratios", "valuation", "forensics", "model",
    "load_kaveri", "load_nirmal", "fetch_statements", "fetch_price_info",
    "ratio_dashboard", "format_dashboard",
    "capm", "wacc", "terminal_value", "dcf_fcff", "equity_bridge", "sensitivity", "reverse_dcf",
    "dcf_from_drivers", "kaveri_reference",
    "beneish_m", "altman_z", "piotroski_f", "forensic_inputs", "forensic_summary",
    "Assumptions", "project", "fcff_from_projection",
]
