"""Kaveri Pumps (fictional) - DCF from first principles, sensitivity grid and reverse DCF.

Rebuilds the course house valuation (₹320/share base case) with fi.valuation building blocks,
then asks the reverse question: what uniform growth does the ₹390 market price imply?
Used in lessons 06.2-06.6. Offline.
    python "tools/examples/kaveri_dcf_and_reverse_dcf.py"
"""
from __future__ import annotations

import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # make tools/ importable

import pandas as pd  # noqa: E402

from fi.valuation import (  # noqa: E402
    capm,
    dcf_from_drivers,
    justified_pb,
    justified_pe,
    kaveri_base_drivers,
    kaveri_reference,
    reverse_dcf,
    sensitivity,
    wacc,
)

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def main() -> None:
    # 1. Cost of capital
    ke = capm(rf=0.065, beta=1.05, erp=0.06)
    w = wacc(ke, kd_pre_tax=0.089, tax_rate=0.2517, debt_weight=0.10)
    print(f"Cost of equity (CAPM): {ke:.2%}   WACC: {w:.2%}")

    # 2. Base-case DCF with the reference drivers
    drivers = kaveri_base_drivers()
    base = dcf_from_drivers(**drivers)
    print("\nBase-case projection (₹ Cr)")
    print(base["projection"].loc[["rev", "ebitda", "nopat", "capex", "d_nwc", "fcff", "discount_factor",
                                  "pv_fcff"]].round(4).to_string())
    print(f"\nPV of explicit FCFF : ₹{base['pv_explicit']:,.1f} Cr")
    print(f"Terminal value      : ₹{base['tv']:,.1f} Cr (PV ₹{base['pv_tv']:,.1f} Cr, {base['tv_share']:.0%} of EV)")
    print(f"Enterprise value    : ₹{base['ev']:,.1f} Cr")
    print(f"Equity value        : ₹{base['equity']:,.1f} Cr")
    print(f"Value per share     : ₹{base['per_share']:,.0f}")

    # 3. Sensitivity: WACC x terminal growth
    def per_share(wacc: float, g: float) -> float:
        return dcf_from_drivers(**{**drivers, "wacc": wacc, "g": g})["per_share"]

    grid = sensitivity(per_share, {"wacc": [w - 0.01, w - 0.005, w, w + 0.005, w + 0.01]},
                       {"g": [0.04, 0.045, 0.05, 0.055, 0.06]})
    grid.index = [f"{x:.1%}" for x in grid.index]
    grid.columns = [f"{x:.1%}" for x in grid.columns]
    print("\nValue per share (₹), WACC down the side, terminal growth across")
    print(grid.round(0).astype(int).to_string())

    # 4. Reverse DCF: uniform growth that justifies ₹390
    cmp = 390.0
    implied = reverse_dcf(cmp, lambda g: dcf_from_drivers(**{**drivers, "growth": [g] * 10})["per_share"])
    print(f"\nReverse DCF: ₹{cmp:,.0f} implies uniform revenue growth of {implied:.1%} a year for FY27-FY36")
    print("(base case 10-year CAGR 10.8%; FY23-FY26 historical CAGR 14.7%)")

    # 5. Cross-check against the reference module and show the scenario ladder
    ref = kaveri_reference()
    print(f"\nReference valuation module: ₹{ref['per_share']:,.0f} base; "
          f"bull ₹{ref['scenarios']['Bull']:,.0f} / bear ₹{ref['scenarios']['Bear']:,.0f}; "
          f"probability-weighted ₹{ref['probability_weighted']:,.0f}")

    # 6. Justified multiples (Gordon-model consistency checks)
    print(f"\nJustified forward P/E at ROE 18%, ke 12.8%, g 5.5%: {justified_pe(0.18, 0.128, 0.055):.1f}x")
    print(f"Justified P/B at ROE 18%, ke 12.8%, g 5.5%       : {justified_pb(0.18, 0.128, 0.055):.2f}x")


if __name__ == "__main__":
    main()
