"""Fetch a real Indian company's statements (OpenBB -> yfinance fallback) and compute a few ratios.

NEEDS NETWORK. Disable any VPN first - Yahoo Finance endpoints are commonly blocked by VPNs.
    python "tools/examples/fetch_indian_company.py" ASIANPAINT.NS
    python "tools/examples/fetch_indian_company.py" TCS.NS --quarter

Vendor data are Yahoo's standardisation, not the company's own presentation: tie revenue, PAT,
total assets and CFO to the annual report before using them (lesson 10.2). Educational only -
nothing printed here is a recommendation.
"""
from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # make tools/ importable

import pandas as pd  # noqa: E402

from fi.data import fetch_price_info, fetch_statements, revenue_row  # noqa: E402

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("ticker", nargs="?", default="ASIANPAINT.NS", help="Yahoo symbol, e.g. ASIANPAINT.NS")
    p.add_argument("--quarter", action="store_true", help="quarterly instead of annual")
    p.add_argument("--no-openbb", action="store_true", help="skip OpenBB and use yfinance directly")
    args = p.parse_args()

    st = fetch_statements(args.ticker, period="quarter" if args.quarter else "annual",
                          use_openbb=False if args.no_openbb else None, in_crore=True)
    inc, bal, cf = st["income"], st["balance"], st["cash"]
    print(f"{args.ticker}: source = {inc.attrs.get('source')}, units = {inc.attrs.get('units')}")
    if inc.empty:
        print("No data returned - check the ticker and that no VPN is blocking Yahoo Finance.")
        return

    rev = revenue_row(inc)
    view = pd.DataFrame({"Revenue": rev})
    for label, key, frame in [("EBITDA", "ebitda", inc), ("PAT", "net_income", inc),
                              ("Total assets", "total_assets", bal), ("Equity", "total_equity", bal),
                              ("Total debt", "total_debt", bal), ("CFO", "cfo", cf), ("Capex", "capex", cf)]:
        if key in frame.index:
            view[label] = frame.loc[key]
    view = view.T
    print("\nKey lines (₹ crore)")
    print(view.round(1).to_string())

    ratios = pd.DataFrame(index=view.columns)
    q = " (quarterly, not annualised)" if args.quarter else ""
    ratios["Revenue growth" + (" (QoQ)" if args.quarter else "")] = rev.pct_change()
    if "EBITDA" in view.index:
        ratios["EBITDA margin"] = view.loc["EBITDA"] / rev
    if "PAT" in view.index:
        ratios["PAT margin"] = view.loc["PAT"] / rev
    if {"PAT", "Equity"} <= set(view.index):
        ratios["ROE (on closing equity)" + q] = view.loc["PAT"] / view.loc["Equity"]
    if {"CFO", "PAT"} <= set(view.index):
        ratios["CFO / PAT"] = view.loc["CFO"] / view.loc["PAT"]
    print("\nRatios")
    print(ratios.T.map(lambda v: "–" if pd.isna(v) else f"{v:.1%}").to_string())

    info = fetch_price_info(args.ticker)
    print("\nMarket snapshot (Yahoo; verify before use)")
    for k in ("name", "price", "market_cap", "shares_outstanding", "trailing_pe", "price_to_book", "beta",
              "target_mean", "n_analysts"):
        print(f"  {k:20s} {info.get(k)}")


if __name__ == "__main__":
    main()
