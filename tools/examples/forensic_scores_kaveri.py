"""Kaveri Pumps (fictional) - Beneish M, Piotroski F, Altman Z/Z'', accruals and the cash-yield check.

Used in lesson 09.6. Offline.
    python "tools/examples/forensic_scores_kaveri.py"
The input mapping from an Ind AS (by-nature) P&L to the US-style model inputs is documented in
fi.forensics.forensic_inputs - read it before quoting any of these scores.
"""
from __future__ import annotations

import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # make tools/ importable

import pandas as pd  # noqa: E402

from fi.data import load_kaveri  # noqa: E402
from fi.forensics import BENEISH_THRESHOLD, forensic_summary  # noqa: E402

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def main() -> None:
    df = load_kaveri()
    years = ["FY22", "FY23", "FY24", "FY25", "FY26"]
    summaries = {y: forensic_summary(df, y) for y in years}

    beneish = pd.DataFrame({y: {k: s["beneish"][k] for k in
                                ("DSRI", "GMI", "AQI", "SGI", "DEPI", "SGAI", "LVGI", "TATA", "m_score")}
                            for y, s in summaries.items()})
    print(f"Beneish M-score (8-variable; flag if M > {BENEISH_THRESHOLD})")
    print(beneish.round(3).to_string())

    pio = pd.DataFrame({y: {k: v for k, v in s["piotroski"].items() if k.startswith("f_") or k == "score"}
                        for y, s in summaries.items()})
    print("\nPiotroski F-score signals (1 = good news)")
    print(pio.to_string())

    other = pd.DataFrame({y: {
        "Altman Z (original, market cap at 31-Mar)": round(s["altman_original"], 2),
        "zone": s["altman_original_zone"],
        "Altman Z'' (book equity)": round(s["altman_z_double_prime"], 2),
        "zone''": s["altman_z_double_prime_zone"],
        "Accruals (PAT-CFO)/avg TA": f"{s['accruals_ratio']:.1%}",
        "Sloan balance-sheet accruals": f"{s['balance_sheet_accruals']:.1%}",
        "Implied yield on cash + liquid funds": f"{s['cash_yield']:.1%}",
    } for y, s in summaries.items()})
    print("\nAltman, accruals and cash-yield check")
    print(other.to_string())

    fy26 = summaries["FY26"]
    print(f"\nFY26 read-out: M = {fy26['beneish']['m_score']:.2f} (below {BENEISH_THRESHOLD}, so not flagged, "
          f"but DSRI {fy26['beneish']['DSRI']:.2f} and positive TATA point at receivables); "
          f"F = {fy26['piotroski']['score']}/9 (peak {max(s['piotroski']['score'] for s in summaries.values())} "
          f"in FY22-FY26); Altman comfortably 'safe'."
          " Scores are screens: the receivables note (overdue > 6 months ₹62.4 Cr) is where to dig.")


if __name__ == "__main__":
    main()
