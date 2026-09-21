# `tools/` specification

Python helpers used by the lessons. Lessons reference these exact module paths and function names.
Python ≥ 3.11, pandas, numpy; network functions use `yfinance` and (optionally) OpenBB.

```
tools/
  fi/
    __init__.py
    data.py         # loading course data + fetching real Indian company data
    ratios.py       # ratio calculations and the ratio dashboard
    valuation.py    # CAPM/WACC, DCF, terminal value, sensitivity, reverse DCF, justified multiples
    forensics.py    # Beneish M, Altman Z / Z'', Piotroski F, accruals
    model.py        # three-statement projection engine (used by the M10 build-along)
  running_example/  # generators for the fictional companies (already built)
  data/             # CSVs produced by the generators
  examples/         # runnable scripts used in lessons
  tests/            # pytest suite
  requirements.txt
```

## `fi/data.py`
- `load_kaveri(kind="annual") -> pandas.DataFrame` — `kind` in {"annual","ratios","quarterly"}; index = line item, columns = periods.
- `load_nirmal() -> pandas.DataFrame`
- `fetch_statements(ticker: str, period: str = "annual", provider: str = "yfinance") -> dict[str, DataFrame]` —
  keys "income", "balance", "cash"; `ticker` like "ASIANPAINT.NS". Uses OpenBB `obb.equity.fundamental.income/balance/cash`
  if OpenBB is installed, else raw `yfinance`. Must handle the `total_revenue` vs `operating_revenue` column difference.
  Quarterly uses `period="quarter"` in OpenBB.
- `fetch_price_info(ticker) -> dict` — price, market cap, shares, beta, analyst target fields from `yf.Ticker(t).info`.
- Scripts that print ₹ on Windows must wrap stdout: `sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")`.
  yfinance calls fail behind some VPNs — document this.

## `fi/ratios.py`
- `margins(rev, **lines) -> dict`
- `roe(pat, equity_open, equity_close)`, `roce(ebit, other_income, ce_open, ce_close)`, `roic(ebit, tax_rate, ic_open, ic_close)`
- `dupont_3(pat, revenue, avg_assets, avg_equity) -> dict` (margin, turnover, leverage, roe)
- `dupont_5(pat, pbt, ebit, revenue, avg_assets, avg_equity) -> dict` (tax burden, interest burden, EBIT margin, turnover, leverage)
- `working_capital_days(revenue, cogs, inventory, receivables, payables) -> dict` (dio, dso, dpo, ccc)
- `ratio_dashboard(df: DataFrame) -> DataFrame` — takes the Kaveri annual frame layout and returns the ratio table
  (must reproduce `docs/appendix/running-example/kaveri-pumps.md` §6 to 1 decimal).

## `fi/valuation.py`
- `capm(rf, beta, erp) -> float`
- `wacc(ke, kd_pre_tax, tax_rate, debt_weight) -> float`
- `gordon_value(cf_next, r, g) -> float` (raise if g >= r)
- `terminal_value(nopat_next, r, g, ronic=None, fcff_next=None) -> float` — value-driver formula when ronic given
- `dcf_fcff(fcffs: list[float], r: float, tv: float, mid_year: bool = True) -> dict` (pv_explicit, pv_tv, ev, discount factors)
- `equity_bridge(ev, net_debt, leases=0, nci=0, investments=0) -> float`
- `sensitivity(fn, rows: dict, cols: dict) -> DataFrame` — generic 2-D sensitivity grid
- `reverse_dcf(price, value_fn, lo=-0.05, hi=0.5, tol=1e-6) -> float` — bisection on a scalar input (e.g., growth)
- `justified_pe(payout_or_roe, r, g, *, roe=None) -> float` — P/E = (1 − g/ROE)/(r − g) (forward)
- `justified_pb(roe, r, g) -> float` — (ROE − g)/(r − g)
- `kaveri_reference() -> dict` — reproduces `kaveri-valuation.md` (₹320 base) by calling `running_example/valuation.py`

## `fi/forensics.py`
- `beneish_m(cur: dict, prev: dict) -> dict` — 8 indices (DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA) + M-score; threshold −1.78 (8-var)
- `altman_z(wc, re, ebit, mve, sales, ta, tl, variant="original"|"z_double_prime") -> float`
- `piotroski_f(cur: dict, prev: dict) -> dict` — 9 binary signals + score
- `accruals_ratio(pat, cfo, avg_total_assets) -> float` and `balance_sheet_accruals(...)`
- `cash_yield_check(cash_and_investments_avg, other_income) -> float` — implied yield on cash (Satyam test)

## `fi/model.py`
- `@dataclass Assumptions` (growth list, ebitda margin list, da_pct, capex_pct, nwc days or % of sales, tax, dividend payout, debt schedule)
- `project(history: DataFrame, a: Assumptions, years: int) -> dict[str, DataFrame]` — returns projected income, balance, cash-flow
  frames that balance (cash as plug, interest on opening debt to avoid circularity) plus a `checks` frame.
- `fcff_from_projection(proj) -> Series`

## Tests
`pytest tools/tests` must pass offline (no network). Network functions are tested only for signature/import.
