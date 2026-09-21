"""Kaveri Pumps (fictional) - three-statement model -> FCFF -> DCF, plus a receivables stress case.

The Module 10.5 build-along in one script. Offline.
    python "tools/examples/build_kaveri_model.py"
"""
from __future__ import annotations

import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # make tools/ importable

import pandas as pd  # noqa: E402

from fi.data import load_kaveri  # noqa: E402
from fi.model import Assumptions, fcff_from_projection, project  # noqa: E402
from fi.valuation import capm, dcf_fcff, equity_bridge, terminal_value, wacc  # noqa: E402

pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 20)

NET_DEBT, LEASES, DILUTED_SHARES = 140.5, 18.2, 6.07  # FY26, ₹ Cr / crore shares
G, RONIC = 0.055, 0.18


def value_per_share(proj: dict, w: float) -> tuple[float, dict]:
    fcff = fcff_from_projection(proj)
    nopat_next = proj["income"].loc["nopat"].iloc[-1] * (1 + G)
    tv = terminal_value(nopat_next, w, G, ronic=RONIC)
    dcf = dcf_fcff(fcff.tolist(), w, tv, mid_year=True)
    equity = equity_bridge(dcf["ev"], net_debt=NET_DEBT, leases=LEASES)
    return equity / DILUTED_SHARES, dcf


def main() -> None:
    hist = load_kaveri()
    w = wacc(capm(0.065, 1.05, 0.06), 0.089, 0.2517, 0.10)

    base = project(hist, Assumptions.kaveri_base())
    print("Projected income statement (₹ Cr)")
    print(base["income"].round(1).to_string())
    print("\nProjected balance sheet (₹ Cr; first column = FY26 actual)")
    print(base["balance"].round(1).to_string())
    print("\nProjected cash-flow statement (₹ Cr)")
    print(base["cash"].round(1).to_string())
    print("\nChecks (balance_diff and cash_recon_diff should be ~0)")
    print(base["checks"].loc[["balance_diff", "cash_recon_diff", "balances", "cash_negative"]].round(6).add(0.0).to_string())

    ps, dcf = value_per_share(base, w)
    print("\nFCFF (₹ Cr):", ", ".join(f"{v:.1f}" for v in fcff_from_projection(base)))
    print(f"EV ₹{dcf['ev']:,.1f} Cr  ->  value per share ₹{ps:,.0f} (reference: ₹320)")

    # Stress: solar receivables do not normalise - NWC stays at the FY26 level of 27.7% of revenue
    stress = project(hist, Assumptions.kaveri_base(nwc_pct=0.277))
    ps_s, _ = value_per_share(stress, w)
    print(f"\nReceivables stress (NWC stays 27.7% of revenue): value per share ₹{ps_s:,.0f} "
          f"({ps_s / ps - 1:+.0%} vs base)")

    # Days-driven variant: receivable days stuck at 96, inventory 80, payables 61 (FY26 actuals)
    days = project(hist, Assumptions.kaveri_base(nwc_pct=None, inventory_days=80, receivable_days=96,
                                                 payable_days=61))
    ps_d, _ = value_per_share(days, w)
    print(f"Days-driven variant (80/96/61 days): value per share ₹{ps_d:,.0f}; "
          f"balances every year: {bool(days['checks'].loc['balances'].all())}")


if __name__ == "__main__":
    main()
