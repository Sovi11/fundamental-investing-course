# 09.2 · Revenue red flags

> **Why this matters:** revenue is the number the market rewards most and the number management can move most
> easily — by recognising it early, recognising it gross, recognising it from friends, or recognising it before
> it exists. Every revenue trick leaves a mark on the balance sheet, because a sale that is not cash must become a
> receivable, an unbilled asset or an inventory that never left. This lesson catalogues the tricks and the marks,
> and works through Kaveri's receivables to draw the line between *aggressive*, *risky* and *fabricated*.

**Learning objectives** — after this lesson you can:

- Recognise the main revenue-manipulation techniques (channel stuffing, bill-and-hold, round-tripping, gross vs
  net, percentage-of-completion abuse, related-party sales, one-off revenue) and the accounting rule each bends.
- Read the receivables signals: DSO, receivables growth vs revenue growth, ageing, allowance coverage, unbilled
  revenue, the Beneish DSRI.
- Distinguish a revenue-recognition problem from a customer-credit problem and from a genuine business-mix change.
- Apply the tests to Kaveri FY24–FY26 and state the verdict with evidence.

**Prerequisites:** [02.2 Accrual accounting & revenue recognition](../02-accounting/02-accrual-accounting-and-revenue-recognition.md),
[04.7 Quality of earnings](../04-financial-analysis/07-quality-of-earnings.md), [09.1](01-why-and-how-numbers-lie.md)  ·  **Time:** ~80 min

---

## 1. Where revenue can go wrong

Ind AS 115 says revenue is recognised when control of goods or services passes to the customer, in the amount
the company expects to be entitled to, allocated across performance obligations. Each clause can be stretched:

| Technique | What the company does | Rule bent | Balance-sheet mark |
|:--|:--|:--|:--|
| **Channel stuffing** | Ships more to dealers/distributors than they can sell, with extended credit, discounts or return rights, to book sales this quarter | "Control passes" — but with return rights or unlimited credit it hasn't economically | Receivables and DSO jump; Q4 spikes; next-quarter sales fall; returns and discounts rise |
| **Bill-and-hold** | Invoices goods that remain in the company's own warehouse | Control has not passed | Inventory doesn't fall while revenue rises; receivables from customers who haven't taken delivery |
| **Round-tripping / circular sales** | Sells to an entity that sells back (or to a related party that resells), often through a chain, to create volume | Substance over form; related-party disclosure | Sales and purchases both inflated; related-party receivables and payables; thin margins on the traffic |
| **Gross vs net** | Books the full transaction value as revenue when acting as an agent (platforms, travel, distributors) | Principal vs agent test | Revenue large, gross margin tiny; "GMV" presented as revenue |
| **Percentage-of-completion (POC) abuse** | Overstates the stage of completion or understates cost-to-complete on long contracts (EPC, real estate before 2018, software projects) | Over-time recognition requires reliable measurement | Unbilled revenue / contract assets grow faster than billings; margins high until the loss is recognised in one lump |
| **Related-party sales** | Sells to promoter entities at chosen prices and terms | Ind AS 24 disclosure; arm's-length assertion | Related-party receivables rising; margins diverge from third-party sales |
| **One-off / non-operating revenue in operations** | Puts asset sales, grants, insurance claims, "other operating income" into revenue | Classification | Revenue growth not matched by volumes; other operating income rising |
| **Fictitious revenue** | Invents customers and invoices (Satyam: 7,000+ fake invoices) | Everything | Receivables that never collect; cash that isn't there; tax paid on profits that don't exist (or not paid — the tax reconciliation catches it) |
| **Early recognition of multi-element deals** | Books a licence + maintenance contract entirely upfront | Allocation to performance obligations | Deferred revenue too low relative to the business model |
| **Change of policy or estimate** | Switches from completion to POC, or shortens the "acceptance" period | Ind AS 8 disclosure of changes | The change note; a one-year jump in growth |

## 2. The receivables signals

Everything above shows up in one place first. Run these tests on every company, every year:

| Test | Formula / source | Threshold that warrants a question |
|:--|:--|:--|
| **Days sales outstanding (DSO)** | Receivables ÷ revenue × 365 | Rising 10+ days a year; far above peers |
| **Receivables growth ÷ revenue growth** | | > 1.5x for two or more years |
| **Beneish DSRI** | (Rec/Rev)ₜ ÷ (Rec/Rev)ₜ₋₁ | > 1.2 (Beneish's manipulator mean was ~1.47 vs 1.03 for non-manipulators) |
| **Ageing** | Schedule III ageing buckets (< 6m, 6–12m, 1–2y, 2–3y, > 3y; disputed/undisputed) | Older buckets growing faster than total; > 6-month bucket > 15% of receivables |
| **Allowance coverage** | ECL allowance ÷ receivables > 6 months | Falling coverage as ageing lengthens |
| **Unbilled revenue / contract assets** | Contract-balances note (Ind AS 115) | Growing faster than revenue; large relative to quarterly revenue |
| **Deferred revenue / advances** | Contract liabilities | Falling while revenue grows (the company is consuming its backlog or booking early) |
| **Q4 share of annual revenue** | | > 35% without seasonal reason; Q1 falling after a big Q4 |
| **Related-party receivables** | RPT note | Any material amount; growing |
| **Cash collections** | Revenue − Δreceivables (or the direct-method CFS if given) | Collections growing much slower than revenue |
| **Customer concentration** | Ind AS 115 note (> 10% customers) | A new large customer appearing with long terms |

### 2.1 Kaveri FY21–FY26

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| Revenue (₹ Cr) | 612.0 | 758.0 | 874.0 | 1,006.0 | 1,172.0 | 1,318.0 |
| Receivables (₹ Cr) | 107.3 | 118.4 | 146.1 | 192.9 | 269.7 | 346.7 |
| DSO (days) | 64 | 57 | 61 | 70 | 84 | 96 |
| Receivables growth ÷ revenue growth | — | 0.43 | 1.53 | 2.12 | 2.41 | 2.29 |
| DSRI (Beneish) | — | 0.89 | 1.07 | 1.15 | 1.20 | 1.14 |
| Solar share of revenue | 3% | 4% | 7% | 14% | 22% | 27% |
| > 6-month overdue (₹ Cr) | — | — | — | — | 31.0 | 62.4 |
| ECL allowance (₹ Cr) / coverage of > 6m | — | — | — | — | 3.1 / 10% | 4.0 / 6.4% |

Three consecutive years of receivables growing more than twice as fast as revenue, DSRI above 1.1 for three years,
the > 6-month bucket doubling, and coverage falling. On the tests alone this is a **red flag**. The forensic question
is *which kind*:

| Hypothesis | What it predicts | Evidence for | Evidence against |
|:--|:--|:--|:--|
| **A. Business mix** — solar tenders have long contractual payment cycles; receivables reflect a real, disclosed change in customers | DSO rises in step with solar share; overdues concentrated in a few state agencies; peers selling to the same states show the same pattern; eventual collection with delay | Solar share 7% → 27% tracks DSO 61 → 96; overdues are "mostly two state nodal agencies" | Coverage of overdues *falling* is a choice, not a mix effect |
| **B. Credit risk** — the customers are real but may not pay (state agency budget problems) | Overdues age into the 1–2 year bucket; provisions or write-offs eventually; management "fully recoverable" language | > 6-month bucket doubled; management's repeated "recoverable" claim; KPI withdrawn | No write-offs yet; states historically pay late but pay |
| **C. Recognition** — revenue booked before acceptance/installation, or on tenders not yet fully executed | Unbilled revenue/contract assets rising; revenue ahead of installations; BGs invoked; disputes | Not disclosed in the running example — the *absence* of a contract-assets breakdown is a question | Segment revenue matches order-book burn (₹290 → ₹410 Cr order book with ₹356 Cr of solar revenue is consistent with execution) |
| **D. Fabrication** — the sales do not exist | Cash yield anomalies, tax anomalies, customers unverifiable | None: cash yield 7.4%, tax rate 25.2%, customers are named state agencies whose tenders are public | — |

Verdict: **A + B** — a real mix shift into a slow-paying, concentrated customer base, with **aggressive
provisioning** on top. Not C or D on the available evidence, but C cannot be excluded without the contract-balances
note and a check of tender award data ([05.7](../05-business-analysis/07-scuttlebutt-and-primary-research.md)). The
memo language: "receivables risk is credit and working-capital risk, not (on present evidence) a recognition
problem; the provisioning is optimistic by ~₹10–12 Cr; the disclosure withdrawal is the item to press on".

That is the shape of every revenue investigation: the tests flag; the hypotheses compete; the notes and outside
data decide; the verdict has a confidence level and a next step.

## 3. Patterns from the cases

| Case | Revenue technique | The mark that was visible |
|:--|:--|:--|
| Satyam (2009) — [I1](../13-case-studies/india/01-satyam-2009.md) | Fictitious invoices and customers | Receivables and cash both high; interest income far below what the cash should earn; margins above peers |
| Manpasand (2018–19) — [I14](../13-case-studies/india/14-manpasand-vakrangee-small-cap-flags.md) | Growth claims inconsistent with capacity and distribution; alleged GST fraud via fake invoicing | Revenue per plant and per distributor implausible; auditor resignation citing lack of information |
| Enron (2001) — [G4](../13-case-studies/global/04-enron-2001.md) | Gross booking of energy trades (merchant model); mark-to-market on long contracts | Revenue exploded to $100 bn with tiny margins; ROIC collapsed; cash flow negative |
| Wirecard (2020) — [G9](../13-case-studies/global/09-wirecard-2020.md) | Third-party acquiring revenue through partners in Asia, with cash in "escrow" | Most profit from the segment with least disclosure; cash unverifiable; FT reporting |
| Valeant (2015) — [G8](../13-case-studies/global/08-valeant-2015.md) | Sales through a controlled specialty pharmacy (Philidor) | Channel inventory; undisclosed control relationship |

## 4. Where to look, in order

1. **Revenue note** (Ind AS 115): disaggregation; contract balances (receivables, contract assets, contract
   liabilities) and their movement; performance-obligation timing.
2. **Receivables note**: ageing schedule; allowance movement; disputed/undisputed; related-party receivables.
3. **Accounting policies**: revenue policy text vs last year's (diff them); any change in estimates.
4. **Auditor's report**: KAMs on revenue (auditing standards presume revenue fraud risk; a KAM is routine — read
   *what* the auditor tested and whether the language changed).
5. **Quarterly pattern**: Q4 share; results vs concall commentary on "order timing".
6. **Outside the filings**: tender portals, dealer checks, competitors' receivable days, customer financial health
   (state finances for Kaveri).

!!! tip "Trader's lens"
    Revenue is a print; receivables are the open position. A desk that prints P&L but never closes positions is
    marking, not making. DSO rising is the equivalent of the book's average holding period lengthening while the
    marks stay flattering — you would ask for the last traded price (collections) and the counterparty's credit
    (ageing and provisioning). Same questions here.

!!! info "India notes"
    - The Schedule III ageing schedule (mandatory since FY22) is the single most useful forensic disclosure in
      Indian reports; earlier years require reading the notes for "outstanding for more than six months".
    - Government receivables are common (defence, railways, solar, water, DISCOMs) and slow by nature; the
      forensic question is provisioning and concentration, not existence.
    - GST e-invoicing and the e-way-bill system make pure invoice fabrication harder than in 2009; the modern
      Indian pattern is more often related-party circularity and POC optimism than invented customers.

!!! warning "Common mistakes"
    - Reading DSO alone without ageing (a stable DSO can hide a growing old bucket).
    - Treating all government receivables as safe or all as doubtful.
    - Ignoring contract assets/unbilled revenue in project companies.
    - Missing gross-vs-net: comparing a platform's "revenue" with a retailer's.
    - Concluding "fraud" from a mix shift, or "mix shift" from a fraud.

## Key terms

| Term | Meaning |
|:--|:--|
| **Channel stuffing** | Pushing excess product into distribution to book sales early |
| **Bill-and-hold** | Invoicing goods that have not been delivered |
| **Round-tripping** | Circular transactions that create revenue without economic substance |
| **Gross vs net revenue** | Principal (gross) vs agent (net) presentation under Ind AS 115 |
| **Percentage-of-completion (POC)** | Over-time revenue recognition on long contracts based on progress |
| **Unbilled revenue / contract asset** | Revenue recognised but not yet invoiced |
| **Contract liability / deferred revenue** | Cash received before revenue is earned |
| **DSO** | Days sales outstanding = receivables ÷ revenue × 365 |
| **DSRI** | Beneish's days-sales-in-receivables index: this year's receivables/revenue ÷ last year's |
| **Ageing schedule** | Breakdown of receivables by time outstanding |
| **ECL allowance** | Expected-credit-loss provision against receivables |
| **Key audit matter (KAM)** | An area of significant auditor judgement highlighted in the audit report |

## Check your understanding

1. A distributor-led FMCG company shows Q4 revenue +30% YoY, Q1 −12% YoY, receivables +45% at year-end, and a
   new "extended credit scheme" in the other-expenses note. Diagnose.
<details><summary>Answer</summary>Channel stuffing: Q4 sales pulled forward with extended credit, Q1 pays for it,
receivables carry the unsold stock. Confirm with dealer inventory checks and the next Q2.</details>

2. Kaveri's DSRI was 1.20 in FY25 and 1.14 in FY26 — both above Beneish's 1.1 warning. Why does the lesson not
   conclude "manipulation"?
<details><summary>Answer</summary>Because DSRI is a screen, not a verdict: the mix shift to slow-paying state
tenders explains the rise; overdues are concentrated in named public agencies; cash yield and tax rate are normal;
and the order book is consistent with execution. The screen directs the investigation (provisioning, contract
assets, tender data); it does not replace it.</details>

3. Compute the provisioning shortfall if a prudent coverage of the > 6-month bucket were 30%.
<details><summary>Answer</summary>30% × 62.4 = 18.7 vs 4.0 booked → ₹14.7 Cr pre-tax, ₹11.0 Cr post-tax (12% of
FY26 PAT).</details>

4. A platform reports revenue of ₹5,000 Cr with a 4% gross margin; its peer reports ₹200 Cr with a 70% gross
   margin. What is probably happening?
<details><summary>Answer</summary>The first books gross (as principal) the transaction value on which it earns a
~4% take rate; the second books net (as agent). Economically similar businesses; restate both to net (₹200 Cr
each) before comparing.</details>

5. What would you look for to test hypothesis C (recognition) at Kaveri?
<details><summary>Answer</summary>The Ind AS 115 contract-balances note (contract assets/unbilled vs receivables),
the revenue policy text for solar systems (recognition at dispatch vs installation vs acceptance), tender-portal
award dates vs quarterly revenue, BG invocations, and dealer/agency checks on installations completed.</details>

## Go deeper

- Howard Schilit, *Financial Shenanigans* — Part Two, "Earnings Manipulation Shenanigans No. 1–2" (recording
  revenue too soon; bogus revenue).
- Ind AS 115 *Revenue from Contracts with Customers* — the five-step model and the contract-balances disclosures.
- Messod Beneish, "The Detection of Earnings Manipulation", *Financial Analysts Journal* (1999) — DSRI and the
  other indices ([09.6](06-forensic-scoring-models.md)).
- [Case I1 Satyam](../13-case-studies/india/01-satyam-2009.md) — read the confession letter's list of what was
  fabricated, then find each item in the FY08 balance sheet.

---
[← Previous: 09.1 Why and how numbers lie](01-why-and-how-numbers-lie.md) · [Module index](index.md) · [Next: 09.3 Expense & asset red flags →](03-expense-and-asset-red-flags.md)
