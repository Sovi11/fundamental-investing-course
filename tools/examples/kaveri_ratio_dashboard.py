"""Kaveri Pumps (fictional) - the six-year ratio dashboard, DuPont and working-capital days.

Used in lesson 04.6. Offline. Run from anywhere:
    python "tools/examples/kaveri_ratio_dashboard.py"
"""
from __future__ import annotations

import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # make tools/ importable

import pandas as pd  # noqa: E402

from fi.data import load_kaveri  # noqa: E402
from fi.ratios import dupont_3, dupont_5, format_dashboard, ratio_dashboard, working_capital_days  # noqa: E402

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)
pd.set_option("display.max_colwidth", 48)


def main() -> None:
    df = load_kaveri("annual")
    dash = ratio_dashboard(df)
    print("Kaveri Pumps & Motors (fictional) - ratio dashboard\n")
    print(format_dashboard(dash).to_string())

    # --- DuPont for FY26: why did ROE fall from 16.3% to 13.5%?
    print("\nDuPont decomposition (averages of opening and closing balances)")
    rows = {}
    for prev, cur in (("FY24", "FY25"), ("FY25", "FY26")):
        avg_ta = (df.at["total_assets", prev] + df.at["total_assets", cur]) / 2
        avg_eq = (df.at["equity", prev] + df.at["equity", cur]) / 2
        d3 = dupont_3(df.at["pat", cur], df.at["rev", cur], avg_ta, avg_eq)
        ebit_incl_oi = df.at["ebit", cur] + df.at["other_income", cur]
        d5 = dupont_5(df.at["pat", cur], df.at["pbt", cur], ebit_incl_oi, df.at["rev", cur], avg_ta, avg_eq)
        rows[cur] = {"net margin": d3["margin"], "asset turnover": d3["turnover"], "equity multiplier": d3["leverage"],
                     "tax burden": d5["tax_burden"], "interest burden": d5["interest_burden"],
                     "EBIT margin (incl. OI)": d5["ebit_margin"], "ROE": d3["roe"]}
    print(pd.DataFrame(rows).round(3).to_string())

    # --- Working-capital days: the solar receivables story
    print("\nWorking-capital days (closing balances; inventory & payables on material cost)")
    wc = {y: working_capital_days(df.at["rev", y], df.at["mat", y], df.at["inventory", y],
                                  df.at["receivables", y], df.at["payables", y]) for y in df.columns}
    print(pd.DataFrame(wc).round(0).astype(int).to_string())
    print("\nReading it: receivable days rose from 57 (FY22) to 96 (FY26) while CFO/PAT fell to 72%:"
          " profit is being booked faster than it is collected.")


if __name__ == "__main__":
    main()
