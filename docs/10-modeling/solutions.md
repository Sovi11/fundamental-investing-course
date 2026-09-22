# Module 10 · Solutions

## Warm-up

**E10.01** Inputs → calculation schedules → statements → valuation → outputs, with checks reading from the
statements. The exception: interest on average debt, which is circular and must be broken (opening balances) or
controlled (iteration with a switch).

**E10.02** Inputs in one place (hidden assumptions); colour coding (hard-codes inside formulas); one sign
convention (sign errors at boundaries); one row one formula (column-specific edits); units in headers (lakh/crore
and share-count errors); a checks block (unknown errors); versioning (lost work and untraceable changes).

**E10.03** Cash is the residual of all sources and uses by the accounting identity, so letting it absorb the
difference is not a fudge; a revolver is modelled short-term debt that draws when cash would fall below a
minimum and repays when cash is surplus, keeping the balance sheet balanced without negative cash.

**E10.04** Balance sheet balances (a reclassification between current/non-current or a missing line); cash
reconciles (an item moved on the balance sheet with no cash-flow counterpart); retained earnings roll (OCI, share
issuance, reserve transfers, restatements).

**E10.05** Other income below EBIT and excluded from EBITDA/EBIT; exceptional items separate with tax effect; leases
as ROU/lease liability with amortisation in D&A and interest in finance costs; interest paid in CFF and received in
CFI (Kaveri's policy), restated consistently across comparisons.

**E10.06** Growth [10, 14, 14, 13, 12, 11, 10, 9, 8, 7]%; EBITDA margin 13.3% → 15.5%; D&A 3.4%; capex 3.5%; NWC 25%,
23%, 22%…; tax 25.17%; payout 25% of prior-year PAT; 8.9% on opening borrowings, 8.5% on leases, 6.8% treasury yield;
term-loan repayments of ₹20 Cr in FY27–FY30.

## Core

**E10.07**
```python
from fi.data import load_kaveri
k = load_kaveri(); prev = 34.0
for c in k.columns:
    assert abs(k.loc["total_assets", c] - k.loc["total_le", c]) < 0.05
    assert abs(prev + k.loc["net_cash", c] - k.loc["cash", c]) < 0.05; prev = k.loc["cash", c]
```
Passes for all six years.

**E10.08** Other equity: 607.2 + 90.5 − 24.0 + 2.4 = 676.1 ✓. Gross block: 780.0 + 36.0 + 14.0 = 830.0 ✓ (net block
830.0 − 334.7 = 495.3 ✓).

**E10.09** Checks all zero. FY27/28/29: revenue 1,449.8 / 1,652.8 / 1,884.2; EBITDA 192.8 / 234.7 / 278.9; PAT 96.1 /
126.4 / 158.1; cash 87.1 / 150.2 / 220.4; equity 779.6 / 882.0 / 1,008.5. FCFF 108.5, 114.2, 124.5, … ✓ (matches
`kaveri_reference()`).

**E10.10** Agri 645.6 / 687.6 / 732.3; industrial 387.9 / 434.5 / 486.6; solar 420.0 / 533.3 / 666.7; totals **1,453.5 /
1,655.4 / 1,885.6** vs reference 1,449.8 / 1,652.8 / 1,884.2 — within 0.3%; the segment build reproduces the path and
shows solar's share rising toward 35%.

**E10.11** Inventory 80/365 × 0.65 = 14.2% of revenue; payables 61/365 × 0.65 = 10.9%; OCA − OCL = −2%; receivables =
22 − 14.2 + 10.9 + 2 = 20.7% → **≈ 76 days**.

**E10.12** FY27: 188 × 8.9% + 18.2 × 8.5% = 16.7 + 1.5 = **₹18.3 Cr**. FY28: opening borrowings 168 → 15.0 + 1.5 =
**₹16.5 Cr**.

**E10.13** Receivables stress: **₹297** (FY27 cash ₹48.0 Cr); margin-down: **₹277** (FY27 cash ₹87.1 Cr — FY27 margin
unchanged in that case).

**E10.14** Rubric: with NWC at 30% the revolver draws in the early years (`cf.loc["revolver_draw"]` non-zero) and
FY28 finance costs rise by 8.9% of the FY27 draw; the exact amounts come from running the code.

**E10.15** ₹168 / ₹320 / ₹416 (within a rupee; the reference values are 168.4 / 319.8 / 415.9).

**E10.16** Growth 278–369 (swing 91); margin 287–352 (65); WACC 296–348 (52); capex 297–342 (45); NWC 309–331 (22).
Rank: growth > margin > WACC > capex > NWC.

**E10.17** Rubric: a 4 × 5 grid; cells ≥ ₹390 appear only at growth scale ≥ 1.2 with margin shift ≥ +1 pp, or
scale 1.4 with shift ≥ 0.

**E10.18** Rubric: satisfies checks 1–3, 5–7, 9 (no circularity), 11, 12, 15, 16; n/a Excel-specific items;
additions: a valuation-date/roll-forward note, a scenario-switch dict, an explicit dilution schedule.

**E10.19** Value per share unchanged (₹320): FCFF is pre-financing and the bridge uses FY26 net debt. FY29 cash
falls (higher dividends) — the balance sheet changes; the DCF value does not, by construction.

**E10.20** Rubric: inputs sheet with days (blue); schedule rows for COGS, inventory = days/365 × COGS, receivables =
days/365 × revenue, payables; ΔNWC row feeding the CFS; identical formulas across forecast columns; a check that
BS working capital equals the schedule; historical columns showing actual days computed from the statements.

## Stretch

**E10.21–23** Rubric: lease schedule with ROU additions, straight-line amortisation, interest on opening liability
and payments; interest on average debt converging within three iterations and differing from the opening-balance
method by a few crore in draw years; Monte-Carlo with reported percentiles for both value and FY28 cash, and a
note on input correlation.

## Real-world task

**E10.24–25** Rubric: mapping documented; tie-outs pass or gaps explained; drivers sourced from history; checks
zero; reverse DCF stated; the output table; the Excel version with checks visible and at least one hard-code found
by a reviewer (there is always one).
