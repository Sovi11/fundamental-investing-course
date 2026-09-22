# 10.2 · Building the historicals

> **Why this matters:** every forecast is an extrapolation from history, so a model is only as good as the
> historical block it starts from. Getting five to ten years of clean, consistently classified, tied-out statements
> is unglamorous and takes half the modelling time — and it is where you learn what the company actually does.
> This lesson covers where the data comes from, how to standardise it, what to reclassify, and how to prove the
> historicals tie before you forecast anything.

**Learning objectives** — after this lesson you can:

- Get financial data for an Indian company from the primary source (annual reports), from Screener.in and from
  `yfinance`/OpenBB via `tools/fi/data.py`, and know each source's limits.
- Map reported lines to a standard model layout and make consistent reclassification decisions (other income,
  exceptional items, leases, interest classification).
- Normalise history for one-offs and policy changes.
- Prove that the historicals tie: balance sheet balances, cash flow reconciles, retained earnings roll forward.
- Recognise data-vendor pitfalls: restatements, standalone/consolidated mix-ups, unit errors, missing rows.

**Prerequisites:** [02.6 Linking the three statements](../02-accounting/06-linking-the-three-statements.md),
[03.2 Anatomy of an annual report](../03-reading-filings/02-anatomy-of-an-annual-report.md)  ·  **Time:** ~75 min (plus a day the first time you do it on a real company)

---

## 1. Sources, in order of authority

| Source | What you get | Cost | Limits |
|:--|:--|:--|:--|
| **Annual reports** (company website; BSE/NSE) | Audited consolidated and standalone statements with every note; 2 years per report, so 5 reports for 10 years | Free | Manual extraction; restatements mean last year's comparatives may differ from last year's report — use the *latest* figure for each year |
| **Quarterly results** (exchange filings, Reg 33) | Quarterly P&L, half-yearly balance sheet, segment results | Free | Less detail; no cash-flow statement quarterly |
| **Screener.in** (free tier; Excel export) | 10+ years of standardised P&L, BS, CFS, ratios, quarterly; consolidated by default | Free | Its standardisation merges lines (e.g., "other income" includes some items you may want separate); "operating profit" is EBITDA ex other income; check units (₹ Cr) and consolidated vs standalone toggle |
| **Yahoo Finance via `yfinance` / OpenBB** | 4–5 years annual, limited quarterly, in INR; standardised US-style labels | Free | Coverage of Indian companies is patchy (quarterly cash flow often missing; some lines mislabelled); some VPNs block Yahoo; row names vary — always print them |
| **Paid terminals / databases** (Capitaline, Ace Equity, Prowess, Bloomberg, Refinitiv, Tikr) | Long histories, standardised, restated | ₹ thousands to lakhs a year | Standardisation choices are theirs |

The course convention: **build from annual reports for the company you are seriously studying; use Screener or
`fi.data` for screening and first looks; never mix sources within one model without reconciling.**

## 2. Fetching with the course tools

```python
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")   # ₹ on Windows
from fi.data import fetch_statements, fetch_price_info, revenue_row

stm = fetch_statements("ASIANPAINT.NS", period="annual", in_crore=True)   # disable VPN first
inc, bs, cf = stm["income"], stm["balance"], stm["cash"]
print(inc.index.tolist())          # ALWAYS inspect the row names before using them
print(revenue_row(inc))            # handles 'total_revenue' vs 'operating_revenue'
info = fetch_price_info("ASIANPAINT.NS")
print(info["price"], info["market_cap"], info["shares_outstanding"], info.get("beta"))
```

`fetch_statements(ticker, period="annual"|"quarter", provider="yfinance", limit=5, use_openbb=None, in_crore=False)`
uses OpenBB's `obb.equity.fundamental.income/balance/cash` when OpenBB is installed and falls back to raw
`yfinance`; `in_crore=True` divides rupee values by 10⁷. Quarterly uses `period="quarter"` (OpenBB's spelling).
The [tools appendix](../appendix/tools.md) lists the known quirks (missing quarterly cash flows for some
companies; label differences). For the running example, `load_kaveri()` and `load_nirmal()` return the
course's clean frames.

## 3. The standard layout

Map every reported line to a fixed set of model rows. The Kaveri layout (`tools/data/kaveri_pumps_annual.csv`)
is the course standard for a non-financial company:

| Block | Model rows |
|:--|:--|
| P&L | `rev, mat, emp, sbc, oth, ebitda, dep_ppe, rou_amort, int_amort, da, ebit, other_income, debt_int, lease_int, fin_cost, exceptional, pbt, current_tax, deferred_tax, tax, pat` |
| Balance sheet | `gross_block, acc_dep, net_block, cwip, rou, intangibles, inventory, receivables, oca, cash, cur_inv, total_assets, share_capital, other_equity, equity, lt_debt, st_debt, lease_liab, payables, ocl, dtl, total_le` |
| Cash flow | `op_before_wc, d_inv, d_rec, d_oca, d_pay, d_ocl, wc_change, cfo, capex_ppe, capex_int, d_cur_inv, asset_sale, cfi, d_lt, d_st, lease_payment, dividends, cff, net_cash` |

Mapping decisions you must make — and record on a Notes sheet:

| Reported item | Model treatment | Reason |
|:--|:--|:--|
| Other income | Separate row below EBIT; **exclude from EBITDA/EBIT** | Treasury income is valued via cash in the bridge, not capitalised at an operating multiple |
| Exceptional items | Separate row; excluded from "adjusted" metrics with tax effect | One-offs distort trends ([02.3](../02-accounting/03-the-income-statement.md)) |
| Purchases of stock-in-trade and change in inventories | Fold into `mat` (cost of goods) | Gross margin needs all three |
| Share-based payment | Inside `emp`, shown as memo `sbc` | Real cost; non-cash add-back in CFS |
| Leases (Ind AS 116) | `rou` asset, `lease_liab`, `rou_amort` in D&A, `lease_int` in finance costs, payments in CFF | Consistent with treating leases as debt; restate pre-FY20 years if comparing |
| Interest paid / received | Paid in CFF, received in CFI (Kaveri's policy) — or restate all to CFO | Pick one and apply to every company you compare |
| Current maturities of long-term debt | Inside `st_debt` (Schedule III) — or reclassify to `lt_debt` for maturity analysis | Note which |
| Provisions (current) | Inside `ocl` | |
| Deferred tax | `dtl` net (or DTA separately if material) | Quasi-equity for capital employed |
| Non-controlling interests | Separate equity row; subtract in the bridge | |
| Investments in associates | Non-operating; add in the bridge at value | |
| Discontinued operations | Exclude from continuing lines; note separately | |

## 4. Normalising history

Before you compute ratios or trends, adjust for:

- **One-offs**: exceptional items (with tax); large provision reversals; asset sales in other income; COVID
  quarters.
- **Policy changes**: Ind AS 116 (FY20) — restate earlier EBITDA or later; revenue recognition changes (Ind AS 115,
  FY19, especially real estate); tax-regime switch (Sec. 115BAA from FY20 — effective rates jump).
- **Corporate actions**: mergers/demergers (pro-forma history if available in the scheme documents); bonus and
  splits (per-share history restated); changes in year-end.
- **Consolidation scope**: a subsidiary acquired mid-year contributes a partial year; disclosed in the
  business-combination note.

Keep both the *reported* and the *normalised* series; forecast from the normalised, reconcile to the reported.

## 5. Tie-outs — prove it before you forecast

Three identities must hold in every historical year, to the rounding of the source:

| Check | Formula | Kaveri FY26 |
|:--|:--|--:|
| Balance sheet | total_assets − total_le = 0 | 1,143.6 − 1,143.6 = 0 |
| Cash reconciliation | opening cash + net_cash − closing cash = 0 | 28.0 + 4.5 − 32.5 = 0 |
| Retained-earnings roll | other_equity₍ₜ₋₁₎ + PAT − dividends + SBC (± OCI, issuance) − other_equity₍ₜ₎ = 0 | 607.2 + 90.5 − 24.0 + 2.4 − 676.1 = 0 |
| Fixed-asset roll | gross_block₍ₜ₋₁₎ + capex + transfers from CWIP − disposals − gross_block₍ₜ₎ = 0 | 780.0 + 36.0 + 14.0 − 0 − 830.0 = 0 |
| Working-capital tie | Δ(inventory + receivables + oca − payables − ocl) on BS = −wc_change on CFS | ✓ by construction |

```python
from fi.data import load_kaveri
k = load_kaveri()
for c in k.columns:
    assert abs(k.loc["total_assets", c] - k.loc["total_le", c]) < 0.05
prev_cash = 34.0    # 31-Mar-2020 opening
for c in k.columns:
    assert abs(prev_cash + k.loc["net_cash", c] - k.loc["cash", c]) < 0.05
    prev_cash = k.loc["cash", c]
print("historicals tie")
```

If a tie fails on real data, the usual causes: OCI items or share issuance missing from the equity roll; a
reclassification between current and non-current between years; disposals or impairments not captured in the
fixed-asset roll; FX translation in a group with overseas subsidiaries; or a vendor's standardised line that
double-counts. Find it before forecasting — the forecast inherits every error.

## 6. Vendor and extraction pitfalls

| Pitfall | Symptom | Fix |
|:--|:--|:--|
| Standalone vs consolidated mix | Revenue jumps or falls 30% in one year with no event | Check the toggle/source; use consolidated throughout |
| Restatements | Last year's number differs between two annual reports | Take each year from the *latest* report that shows it; note the restatement reason |
| Units | Numbers 10x or 100x off; ₹ lakh vs crore; ₹ million | Read the header; `in_crore=True` for yfinance |
| Missing rows | "ebitda" absent in Yahoo; D&A inside operating expenses | Build from components; print `index.tolist()` |
| Sign conventions | Vendor shows expenses negative | Standardise on entry |
| Fiscal-year labels | Yahoo labels FY by calendar date (2026-03-31) | Map to FY26 |
| Merged line items | Screener's "other income" mixing treasury and operating items | Go to the report for the split when it matters |
| Quarterly patchiness (Indian companies on Yahoo) | Missing quarterly cash flow; four vs five quarters | Use exchange filings for quarterly detail |

!!! tip "Trader's lens"
    Historicals are your market data feed. A pricing model on a corrupted feed produces confident nonsense; so does
    a DCF on unreconciled statements. The tie-outs are the equivalent of checking that bid ≤ ask and that the
    close matches the exchange print — cheap, boring, and the only thing standing between you and a model that is
    precisely wrong.

!!! info "India notes"
    - Consolidated statements are the model base; standalone is read for governance and dividends
      ([02.8](../02-accounting/08-deeper-cuts-group-accounts-and-other.md)).
    - The Schedule III format is stable enough that a mapping template built for one manufacturer works for most;
      lenders, insurers and holdcos need their own layouts ([Module 07](../07-special-valuation/index.md)).
    - Pre-FY17 numbers are under old Indian GAAP for most companies; Ind AS transition-year reports give restated
      comparatives for one year only — treat older data as a different regime.

!!! warning "Common mistakes"
    - Forecasting from Screener's standardised lines without checking what they contain.
    - Mixing sources across years.
    - Skipping the tie-outs because "the vendor's numbers must balance".
    - Forgetting Ind AS 116 when comparing FY19 with FY20+ margins.
    - Treating restated comparatives as errors in your model rather than in the source.

## Key terms

| Term | Meaning |
|:--|:--|
| **Historicals** | The block of actual financial statements a model is built on |
| **Standard layout / mapping** | The fixed set of model rows and the rules for placing reported lines in them |
| **Reclassification** | Moving an item between categories (e.g., other income out of EBITDA) for analytical consistency |
| **Normalisation** | Adjusting history for one-offs and policy changes |
| **Tie-out** | A check that related figures agree (BS balances; CFS reconciles; rolls close) |
| **Restatement** | Revision of previously reported figures |
| **Roll-forward** | Opening + additions − reductions = closing, for equity, fixed assets, provisions |
| **Consolidated / standalone** | Group vs parent-only statements |

## Check your understanding

1. Screener shows "operating profit" of ₹186 Cr for Kaveri FY26 and your model shows EBITDA of ₹181.9 Cr. Why?
<details><summary>Answer</summary>Screener's operating profit typically includes other income (3.9) in some
layouts, or treats an item (e.g., a component of other expenses) differently; 181.9 + 3.9 = 185.8 ≈ 186. Confirm the
definition; use your own consistently.</details>

2. A company adopted Ind AS 116 in FY20; its EBITDA margin rose from 9% to 13% with no operational change. How
   do you make FY19 and FY21 comparable?
<details><summary>Answer</summary>Either add FY21's lease payments (from the CFS) back into opex to get a pre-116
EBITDA, or subtract FY19's rent from opex and treat it as D&A + interest. State the convention; compare EBIT if in
doubt.</details>

3. Your retained-earnings roll shows a ₹12 Cr unexplained gap. List three candidate causes.
<details><summary>Answer</summary>OCI items (actuarial remeasurements, FVOCI gains) taken directly to equity; share
issuance/ESOP exercise credited to securities premium; a transfer to/from a reserve, dividend distribution tax
(pre-2020), or a prior-period adjustment/restatement.</details>

4. Why does the course exclude other income from EBITDA and EBIT?
<details><summary>Answer</summary>Because treasury income is generated by cash and investments that are added
separately in the equity bridge; including it in EBIT would capitalise it at an operating multiple and count the
cash twice. It also makes margins comparable across companies with different cash piles.</details>

5. `fetch_statements("XYZ.NS")` returns an income frame with no `ebitda` row. What do you do?
<details><summary>Answer</summary>Print the index, find `operating_income`/`ebit` and `depreciation_and_amortization`
(or reconstruct from revenue and expense rows), build EBITDA yourself, and check it against the company's own
presentation for one year before using it.</details>

## Go deeper

- `tools/fi/data.py` and `tools/examples/fetch_indian_company.py` — read the code; run it on two companies and
  compare the row names.
- Screener.in's "Export to Excel" (free with an account) — the fastest way to a 10-year standardised history;
  then reconcile one year to the annual report to learn its mapping.
- Any company's last five annual reports — build the 10-year P&L by hand once; you will never again trust a
  vendor line without checking.

---
[← Previous: 10.1 Model architecture](01-model-architecture.md) · [Module index](index.md) · [Next: 10.3 Forecasting drivers →](03-forecasting-drivers.md)
