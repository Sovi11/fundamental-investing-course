# 09.3 · Expense & asset red flags

> **Why this matters:** if revenue is the front door for manipulation, expenses are the back door: a cost that
> should hit this year's profit is parked on the balance sheet as an asset, or a provision that should be taken is
> not, or one that was taken is quietly released. The result is the same — profit today borrowed from tomorrow —
> and the mark is the same: balance-sheet accounts that grow without earning anything.

**Learning objectives** — after this lesson you can:

- Recognise capitalisation of operating costs, perpetual CWIP, useful-life games, soft-asset growth, inventory
  bloat, cookie-jar provisions, big baths and recurring "exceptional" items.
- Test for each using ratios and notes: capex vs D&A vs capacity, CWIP ageing, intangibles under development,
  provision roll-forwards, inventory days by category, the Beneish AQI/DEPI/SGAI indices.
- Distinguish legitimate capitalisation (Ind AS 16/23/38) from abuse.
- Apply the tests to Kaveri.

**Prerequisites:** [02.7 Deeper cuts: assets & expenses](../02-accounting/07-deeper-cuts-assets-and-expenses.md),
[09.2](02-revenue-red-flags.md)  ·  **Time:** ~75 min

---

## 1. Capitalising operating costs

Accounting allows some outlays to be recorded as assets: the cost of building a plant (Ind AS 16), borrowing costs
during construction of a qualifying asset (Ind AS 23), development costs once technical and commercial feasibility
is demonstrated (Ind AS 38), software developed for internal use. The abuse is stretching "asset" to cover costs
that create no future benefit — salaries, marketing, repairs, routine software, interest on general borrowings —
so that they bypass the P&L.

| Signal | Test | Warning level |
|:--|:--|:--|
| Capex far above D&A without capacity growth | Capex ÷ D&A for 3 years vs capacity/volume growth | Capex/D&A > 2x with volumes flat |
| CWIP that never completes | CWIP ageing schedule (Schedule III since FY22: < 1y, 1–2y, 2–3y, > 3y; projects "temporarily suspended") | CWIP > 2 years old; CWIP > 25% of net block with no commissioning |
| Intangibles under development | Note; growth vs R&D expense | Growing faster than revenue; capitalised share of R&D rising |
| Capital advances | Loans & advances note | Large, growing, to unnamed or related parties |
| Capitalised borrowing costs | Note; implied interest rate = finance cost ÷ average debt | Implied rate well below the company's borrowing rate |
| "Other non-current assets" / "other assets" | Growing unexplained | Any soft asset > 5% of total assets without a clear description |
| Beneish AQI | (1 − (current assets + PP&E + securities)/total assets)ₜ ÷ same ₜ₋₁ — the growth in "soft" assets | > 1.1 |

**Kaveri**: capex/D&A was 4.5x in FY24 — but that was the Hosur plant, CWIP went to zero on commissioning, gross
block rose ₹216 Cr, and motor capacity appeared (3.5 lakh units). Legitimate. AQI is 0.97 in FY26 (soft assets are
just ₹8 Cr of software). Clean on this test.

## 2. Depreciation and useful-life games

Lengthening useful lives or switching methods (SLM vs WDV) lowers depreciation and raises profit with no cash
effect. Schedule II of the Companies Act gives indicative lives; deviations must be disclosed and justified.

| Test | Formula | Warning |
|:--|:--|:--|
| Depreciation rate | D&A ÷ average gross depreciable block | Falling over time without a mix change |
| Beneish DEPI | Depreciation rateₜ₋₁ ÷ depreciation rateₜ | > 1.1 (depreciation slowing) |
| Change-in-estimate note | Ind AS 8 disclosure | Any change that raises profit; compare with peers' lives |
| Impairment | Ind AS 36 testing of CWIP, goodwill, idle assets | Idle/suspended plant not impaired |

**Kaveri**: DEPI 0.95 in FY26 (depreciation rate slightly *rising*); 0.76 in FY25 because the new plant raised the
rate. Clean.

## 3. Provisions: too little, too much, released

| Game | Mechanism | Test |
|:--|:--|:--|
| **Under-provisioning** | ECL on receivables, warranty, gratuity, litigation kept low to lift profit | Allowance ÷ overdue receivables; warranty provision ÷ sales vs history; actuarial assumptions (discount rate, salary growth) drifting favourably |
| **Cookie jar** | Over-provide in strong years; release in weak ones to smooth | Provision roll-forward (opening + charge − utilisation − *reversal* = closing): reversals appearing in weak quarters |
| **Big bath** | Load every possible charge into one bad year (new CEO, "restructuring"), so subsequent years compare well | A huge exceptional charge followed by suspiciously smooth improvement; provisions created in the bath year released later |
| **Recurring "exceptional" items** | Restructuring, impairment, "one-time" costs every year, excluded from "adjusted" profit | Count the years with exceptional items; sum them as a % of cumulative PAT |

**Kaveri**: under-provisioning on solar receivables is the live issue ([09.2](02-revenue-red-flags.md)) — ECL
coverage 6.4% of the > 6-month bucket, down from 10%. No cookie jar, no bath; two exceptional items in six years
(a VRS cost and a land gain), both genuinely one-off.

## 4. Inventory

| Signal | Test | Warning |
|:--|:--|:--|
| Inventory days rising | Inventory ÷ COGS × 365 | Rising 10+ days a year without a stated reason |
| Finished goods vs raw materials | Inventory note by category | Finished goods growing fastest = production ahead of sales (profit supported by absorption of fixed costs into unsold stock) |
| Change-in-inventories line | Large negative (stock build) repeatedly | Two or more years |
| Inventory write-downs | Note; NRV adjustments | None ever, in a business where obsolescence is normal (fashion, electronics) |
| Stock statements to banks vs books | Schedule III disclosure (since FY22) of discrepancies between quarterly returns filed with lenders and the books | Any material discrepancy — the company is telling its bank a different number |

**Kaveri**: inventory days 74–82 across the period on material cost; 80 in FY26 — steady. Clean, though the
FY26 running example does not break inventory into categories; a real analysis would.

## 5. SG&A and the cost lines

- **Beneish SGAI** = (SG&A/sales)ₜ ÷ (SG&A/sales)ₜ₋₁: a *falling* SG&A ratio while sales grow can be scale — or
  costs being capitalised. Kaveri: 1.01 (flat). Clean.
- **Employee cost per head** vs headcount growth: cost per head falling sharply while revenue per head rises is
  either automation or cost capitalisation/contract labour outside the line.
- **Other expenses** items that vanish (advertising, repairs, R&D) as margins expand — check whether they moved
  to the balance sheet.
- **Related-party purchases** at favourable prices boost margins (the reverse of the Kaveri case, where
  purchases from Kaveri Castings might be *too expensive*).

## 6. Goodwill and acquisitions

Acquisitions create goodwill and intangibles (customer relationships, brands) that are amortised or tested for
impairment. Games: allocating the purchase price to goodwill (not amortised) rather than to intangibles with
finite lives (amortised); delaying impairment of failed acquisitions; treating integration costs as
"exceptional" every year; presenting "adjusted" EPS before acquisition amortisation. Tests: goodwill ÷ equity;
impairment history vs the acquired unit's performance ([05.5 §2.2](../05-business-analysis/05-management-and-capital-allocation.md));
the share of revenue growth that is acquired vs organic.

## 7. Where to look

1. PP&E note: gross block roll-forward, CWIP ageing, capitalised borrowing costs, useful lives.
2. Intangibles note: internally generated vs acquired; intangibles under development ageing.
3. Provisions note: roll-forward with utilisation and reversals; contingent liabilities.
4. Inventory note: by category; write-downs; bank stock-statement reconciliation.
5. Accounting policies: capitalisation policy text, lives, changes.
6. Other expenses note: year-on-year for every line.
7. Auditor's report: KAMs on capitalisation, impairment, provisions; CARO clauses on fixed assets and inventory
   physical verification.

!!! tip "Trader's lens"
    Capitalised costs are losses deferred to the next mark — like rolling a losing position into a new expiry
    and booking the premium as an asset. The book looks fine until the roll stops. Watch the balance sheet's
    "unexplained assets" the way you would watch a book's unrealised losers: growth there is P&L not yet
    admitted.

!!! info "India notes"
    - Schedule III's 2021 amendments added CWIP and intangibles-under-development **ageing schedules** and the
      **bank stock-statement reconciliation** — three disclosures that catch the commonest Indian asset games.
      Manpasand-type discrepancies between what was told to banks and what was in the books are now visible.
    - Ind AS 23 borrowing-cost capitalisation is widely used by capex-heavy companies; compare capitalised interest
      with the finance-cost line and with average debt to see how much interest is bypassing the P&L.
    - Schedule II useful lives are indicative; companies using longer lives must disclose and justify; compare
      across peers (e.g., telecom network assets, hotel buildings, wind turbines).

!!! warning "Common mistakes"
    - Penalising all capex above D&A (growth companies must invest) — check capacity and output.
    - Missing capitalised interest when computing interest cover.
    - Reading a provision "release" as good news.
    - Comparing gross margins across companies with different capitalisation policies (software, pharma R&D).
    - Forgetting that inventory absorption of fixed costs makes production, not sales, the profit driver in the
      short run.

## Key terms

| Term | Meaning |
|:--|:--|
| **Capitalisation** | Recording an outlay as an asset rather than an expense |
| **CWIP** | Capital work-in-progress: assets under construction, not yet depreciated |
| **Intangibles under development** | Capitalised development costs for projects not yet complete |
| **Capital advances** | Payments to suppliers for assets not yet delivered |
| **Useful life / depreciation method** | Period and pattern over which an asset's cost is expensed |
| **Impairment** | Write-down of an asset to recoverable amount (Ind AS 36) |
| **Provision roll-forward** | Opening + charge − utilisation − reversal = closing |
| **Cookie jar / big bath** | Over-provisioning for later release / concentrating charges in one period |
| **Absorption** | Allocation of fixed production costs into inventory |
| **Beneish AQI / DEPI / SGAI** | Asset-quality, depreciation and SG&A indices |
| **Goodwill** | Excess purchase price over identifiable net assets; tested for impairment, not amortised |

## Check your understanding

1. A software company's "intangibles under development" grew from ₹40 Cr to ₹180 Cr in three years while R&D
   expense fell from 12% to 6% of sales and margins rose. Interpret.
<details><summary>Answer</summary>Development costs are being capitalised instead of expensed; the margin
improvement is largely accounting. Restate by expensing the increase in capitalised development (or the gross
capitalisation) and check whether products actually launched.</details>

2. Kaveri's capex/D&A was 4.5x in FY24. Why is that not a red flag?
<details><summary>Answer</summary>The capex built a visible plant: CWIP fell to zero on commissioning, gross block
rose by ₹216 Cr, motor capacity of 3.5 lakh units appeared, and depreciation stepped up the next year. Capitalisation
abuse shows assets that never commission or produce.</details>

3. A provision roll-forward shows: opening 50, charge 10, utilisation 8, reversal 25, closing 27. What happened?
<details><summary>Answer</summary>₹25 Cr of a prior provision was released into profit — half the opening balance.
Ask what it was for, why it is no longer needed, and whether the release coincided with a weak operating quarter
(cookie jar).</details>

4. What does a discrepancy between quarterly stock statements filed with banks and the books tell you?
<details><summary>Answer</summary>That the company reported one inventory/receivables figure to its lenders (to
support drawing power on working-capital lines) and another to shareholders. One of them is wrong; both are
disclosed under Schedule III since FY22 — a direct integrity test.</details>

5. Why is finished-goods inventory growth more worrying than raw-material inventory growth?
<details><summary>Answer</summary>Raw-material build can be a purchasing decision (prices, supply security).
Finished-goods build means production outran sales; fixed costs were absorbed into stock rather than expensed, so
profit was supported by output no one bought — and the stock may need write-downs.</details>

## Go deeper

- Schilit, *Financial Shenanigans* — shenanigans No. 4 (shifting current expenses to a later period) and No. 6
  (shifting current income to a later period).
- Ind AS 16, 23, 36, 37, 38 — the capitalisation, borrowing-cost, impairment, provision and intangibles standards.
- Schedule III (Division II) as amended in 2021 — the ageing schedules and the bank-statement reconciliation.
- [Case G8 Valeant](../13-case-studies/global/08-valeant-2015.md) — acquisitions, adjusted metrics and amortisation.

---
[← Previous: 09.2 Revenue red flags](02-revenue-red-flags.md) · [Module index](index.md) · [Next: 09.4 Cash-flow games →](04-cash-flow-games.md)
