# 09.7 · The forensic checklist

> **Why this matters:** the six preceding lessons contain more tests than anyone can hold in their head. A
> checklist turns them into a procedure: forty items, each with *where to look*, *what threshold*, and *how bad*.
> Run it on every company before the valuation, and run it again every year you hold the stock. Applied to Kaveri
> Pumps it produces the module's verdict — and a template you will reuse in the capstone and the private casebook.

**Learning objectives** — after this lesson you can:

- Run a 40-point forensic checklist organised by statement and by governance, with sources and thresholds.
- Score it consistently (0–3 per item), aggregate to a RAG rating, and translate the rating into analytical
  actions (adjust, discount, monitor, avoid).
- Complete the checklist for Kaveri FY26 and defend the result.

**Prerequisites:** [09.1](01-why-and-how-numbers-lie.md)–[09.6](06-forensic-scoring-models.md)  ·  **Time:** ~90 min (plus ~3 hours to run it on a real company the first time)

---

## 1. Scoring

| Score | Meaning |
|:--|:--|
| 0 | Clean — the test passes clearly |
| 1 | Watch — mildly adverse, explained, or one-year |
| 2 | Concern — adverse trend or unexplained; requires adjustment of the numbers or a valuation discount |
| 3 | Disqualifying — evidence of manipulation, fraud, or governance that removes minorities' claim; do not invest until resolved |

Aggregate: sum of scores (max 120), count of 2s and 3s, and an overall **RAG**: *Green* (total ≤ 12, no 3s,
≤ 2 twos), *Amber* (13–30, no 3s), *Red* (any 3, or > 30). The aggregate matters less than the pattern: five 2s in
the revenue section mean something different from five 2s scattered across the sheet.

## 2. The checklist

### A. Revenue and receivables (10)

| # | Test | Where | Threshold for 2 | Kaveri FY26 |
|:--|:--|:--|:--|:--:|
| A1 | Receivables growth vs revenue growth (3 years) | BS, P&L | > 1.5x for 2+ years | **2** (2.1–2.4x for three years) |
| A2 | DSO trend | Compute | +10 days/yr, or > peers by 30 days | **2** (61 → 96) |
| A3 | Ageing: > 6-month bucket share and growth | Schedule III ageing | > 15% of receivables or doubling | **2** (18%, doubled) |
| A4 | Allowance coverage of overdues | Receivables note | < 15% of > 6-month bucket, or falling | **2** (6.4%, falling) |
| A5 | Unbilled revenue / contract assets vs revenue | Ind AS 115 note | Growing faster than revenue | 1 (not disclosed in the running example — the absence is the point) |
| A6 | Revenue policy changes / estimates | Accounting policies (diff YoY) | Any profit-raising change | 0 |
| A7 | Related-party revenue | RPT note | > 5% of revenue | 0 |
| A8 | Q4 concentration / Q1 drop | Quarterly | Q4 > 35% without seasonality | 0 (Q4 31% — seasonal) |
| A9 | Gross vs net presentation | Revenue note | Agent booked as principal | 0 |
| A10 | Customer concentration and new large customers | Ind AS 115 note | Top customer > 25%; new large customer with long terms | 1 (two state agencies dominate solar overdues) |

### B. Costs, assets, provisions (10)

| # | Test | Where | Threshold for 2 | Kaveri FY26 |
|:--|:--|:--|:--|:--:|
| B1 | Capex/D&A vs capacity growth | PP&E note; capacity disclosure | > 2x with no capacity | 0 |
| B2 | CWIP ageing; suspended projects | CWIP ageing | > 2 years; > 25% of net block | 0 |
| B3 | Intangibles under development / capitalised development | Intangibles note | Growing faster than revenue | 0 |
| B4 | Capital advances and other non-current assets | Notes | Unexplained > 5% of assets | 0 |
| B5 | Capitalised borrowing costs | Note; implied interest rate | Implied rate < borrowing rate by 2 pp | 0 |
| B6 | Depreciation rate / useful-life changes | PP&E note; Ind AS 8 | Rate falling; life extended | 0 |
| B7 | Provision roll-forward: reversals | Provisions note | Reversals > 20% of opening | 0 |
| B8 | Exceptional items frequency | P&L, 5 years | > 2 of 5 years, same type | 0 (2 of 6, different types) |
| B9 | Inventory days and finished-goods mix | Inventory note | +10 days/yr; FG growing fastest | 0 (steady) |
| B10 | Bank stock statements vs books | Schedule III disclosure | Any material discrepancy | 0 |

### C. Cash flow (8)

| # | Test | Where | Threshold for 2 | Kaveri FY26 |
|:--|:--|:--|:--|:--:|
| C1 | CFO/EBITDA, 3-year cumulative | CFS | < 50% (non-lender) | **2** (42%) |
| C2 | CFO/PAT, 3-year cumulative | CFS | < 75% | 1 (78% over three years; FY26 alone 72%) |
| C3 | Implied yield on cash | Other income ÷ avg cash | < 3% when rates 6–7% | 0 (7.4%) |
| C4 | Cash-rich but borrowing | BS | Cash > 20% of assets with debt > 1x EBITDA and low yield | 0 |
| C5 | Supplier finance / factoring / bills discounted | Payables note; contingents | Any undisclosed programme; payable days jump | 0 |
| C6 | Loans, ICDs, guarantees to related/group entities | Loans note; RPT; CARO iii–iv | Any material | 0 |
| C7 | Investments in unlisted/obscure entities | Investments note | Growing; unexplained | 0 |
| C8 | Standalone vs consolidated cash and flows | Both statements | Cash trapped; parent funding losses | n/a |

### D. Governance and people (12)

| # | Test | Where | Threshold for 2 | Kaveri FY26 |
|:--|:--|:--|:--|:--:|
| D1 | Promoter pledge | SAST Reg 31 | > 10% of holding, or rising | 1 (6%, new) |
| D2 | Auditor: size, resignation, opinion, KAMs | Audit report; announcements | Mid-term resignation (3); qualified (2–3) | 1 (KAM on receivables; rotation only) |
| D3 | KMP changes | Announcements | Two in 24 months | 0 |
| D4 | Related-party purchases / expenses | RPT note | > 5% of costs or rising | **2** (10.4% of materials, rising 5 years) |
| D5 | Royalty / brand fees | RPT note | > 3% of sales or rising | 0 |
| D6 | Preferential issues / warrants to promoters | Announcements | Any before news; repeated | 0 |
| D7 | Fund-raising vs reported cash | Announcements; BS | Raising while cash-rich | 0 |
| D8 | Managerial remuneration | Board's report | > 8% of PAT; up in loss year | n/a (not in running example) |
| D9 | Board independence in substance; independent-director exits | Report; announcements | Vague-reason exits | n/a |
| D10 | SEBI / exchange / NFRA / RBI actions; ASM/GSM history | Regulators' sites | Any substantive order | 0 (fictional) |
| D11 | Disclosure quality: KPIs dropped, definitions changed | Presentations over 8 quarters | Any KPI withdrawn when adverse | 1 (receivable days withdrawn) |
| D12 | Stated vs actual promoter holding; connected entities | Shareholding pattern; MCA21 | "Public" holders at company address | 0 |

### E. Scores and cross-checks (bonus items; do not add to the total)

| Model | Kaveri FY26 | Flag |
|:--|--:|:--|
| Beneish M | −2.14 | No (trend adverse) |
| Altman Z | 6.99 | No |
| Piotroski F | 4 | Deteriorating |
| Accruals | 2.3% | Elevated |
| C-score (approx.) | 2–3 | Watch |

## 3. Kaveri — the result

| Section | Score | 2s and 3s |
|:--|--:|:--|
| A. Revenue & receivables | 10 | four 2s (A1–A4) |
| B. Costs, assets, provisions | 0 | — |
| C. Cash flow | 3 | one 2 (C1) |
| D. Governance | 5 | one 2 (D4) |
| **Total** | **18** | **six 2s, no 3s** → **Amber** |

**Verdict.** No evidence of fabrication or fraud: the cash is real, the assets are real, the costs are honest, the
auditor is engaged. The problems cluster in one place — a solar receivables book from state agencies that is
growing, ageing and under-provided — plus a rising related-party purchase line and a small, new promoter pledge.
Together they are **yellow flags that need resolution, not red flags that end the analysis**:

1. **Adjust**: provide 25–30% on the > 6-month bucket in your own numbers (EPS ₹15.1 → ~₹13.6); model NWC at 26–28% of
   revenue in the bear case; treat the Kaveri Castings purchases as a ₹5–10 Cr/yr margin question until the
   supplier's margins are disclosed.
2. **Discount**: governance/forensic discount via scenario weights (bear 35%) or WACC (+50–75 bps), not both.
3. **Monitor** (quarterly): receivable days and ageing; provisioning; state payment news; the pledge; RPT purchase
   share; whether the withdrawn KPI returns.
4. **Escalate to Red if**: the auditor's KAM turns into a qualification; a state agency disputes a claim; the pledge
   exceeds 15%; a CFO leaves; or contract assets appear and grow.

That verdict, with the checklist attached, is the forensic section of the memo in
[11.3](../11-process/03-writing-an-investment-memo.md) and the `forensic-checklist.md` in the casebook template.

## 4. Running it on a real company — the workflow

1. **Pull** the last three annual reports and the last eight quarterly results/presentations; the shareholding
   pattern and SAST/PIT filings; the auditor's reports; exchange announcements for three years; SEBI order search.
2. **Compute** the ratio items (A1–A4, B1, B5, B6, B9, C1–C4) with `tools/fi` — an afternoon the first time, an hour
   thereafter.
3. **Read** the notes for the disclosure items (A5–A10, B2–B4, B7, B10, C5–C8, D4–D7) — the longest part; keep a
   page reference for each score.
4. **Search** for the regulatory and people items (D1–D3, D8–D12).
5. **Score, aggregate, write the verdict** in the four-part form above (adjust / discount / monitor / escalate).
6. **Date it and file it.** The next year's run compares against it; the trend of the score is more informative
   than its level.

!!! tip "Trader's lens"
    A checklist is a pre-trade risk check. Nobody on a desk puts on size without the risk system clearing the
    trade, however good the idea looks; the forensic checklist is that system for a fundamental position. The
    "Amber" rating is the equivalent of a reduced limit — you can trade it, smaller, with tighter monitoring.

!!! info "India notes"
    The Indian disclosures that make this checklist workable from outside: Schedule III ageing schedules
    (receivables, CWIP, intangibles), the bank stock-statement reconciliation, Ind AS 115 contract balances, Ind
    AS 24 RPT notes, CARO 2020, LODR Reg 30 event disclosures, SAST Reg 31 pledges, PIT Reg 7 insider trades,
    half-yearly RPT filings, and SEBI's public order database. Most of them date from 2015–22 — the Indian
    forensic toolkit is much stronger than it was when Satyam happened.

!!! warning "Common mistakes"
    - Treating the total score as the answer instead of the pattern of 2s and 3s.
    - Scoring without page references (unrepeatable next year).
    - Running the ratio items and skipping the reading items — the reading is where the 3s are.
    - Applying manufacturer thresholds to lenders, platforms or project companies without adjustment.
    - Letting a Green rating end scepticism; letting an Amber rating end the analysis.

## Key terms

| Term | Meaning |
|:--|:--|
| **Forensic checklist** | A structured set of tests with sources, thresholds and scores |
| **RAG rating** | Red / Amber / Green summary of the checklist |
| **Disqualifying (3)** | A finding that removes the investment case until resolved |
| **Adjust / discount / monitor / escalate** | The four responses to forensic findings |
| **Page reference** | The citation to the filing page supporting each score |

## Check your understanding

1. Kaveri scores four 2s in section A and none in B. What does the pattern tell you that the total does not?
<details><summary>Answer</summary>The issue is concentrated in one mechanism — customer credit on solar tenders and
its provisioning — rather than spread across the accounts. That points to a specific business risk (state
payments) with a specific fix (provisioning, monitoring), not to pervasive manipulation.</details>

2. Which single new fact would move Kaveri to Red, and why?
<details><summary>Answer</summary>A qualified audit opinion on receivable recoverability (D2 → 3), or a state agency
formally disputing a claim (A3/A4 → 3): either converts a provisioning judgement into an acknowledged loss and
questions the revenue recognised on it.</details>

3. Adapt A1–A4 for an EPC contractor.
<details><summary>Answer</summary>Use unbilled revenue + retention + receivables as the base; compare growth with
revenue; age unbilled by contract; test coverage of disputed/arbitration receivables; add a test for cost-to-complete
estimate changes (margin revisions on contracts).</details>

4. Why is "no 3s" a necessary but not sufficient condition for Green?
<details><summary>Answer</summary>Several 2s in one section (Kaveri's A1–A4) indicate a real, if not disqualifying,
problem that changes the numbers and the risk; Green should mean "use the reported numbers as-is with normal
monitoring", which is not the case here.</details>

5. What goes in the casebook after the checklist is run?
<details><summary>Answer</summary>The scored sheet with page references, the RAG, the four-part verdict
(adjust/discount/monitor/escalate) with specific triggers and dates, and the score's history — so that next year's
run is a comparison, not a fresh start ([15.2 templates](../15-capstone/02-templates.md)).</details>

## Go deeper

- Schilit, *Financial Shenanigans*, Part Five — the "Fraud Detection Checklist".
- Charles Mulford & Eugene Comiskey, *Creative Cash Flow Reporting* — cash-flow section items.
- The Kaveri running-example pages — rerun every item with the tables there and confirm each score.
- [Module 15 capstone](../15-capstone/index.md) — the checklist as part of the full case-study method.

---
[← Previous: 09.6 Forensic scoring models](06-forensic-scoring-models.md) · [Module index](index.md) · [Next: 10.1 Model architecture →](../10-modeling/01-model-architecture.md)
