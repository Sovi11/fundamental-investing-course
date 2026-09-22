# 04.7 · Quality of earnings

> **Why this matters:** two companies can report the same ₹100 Cr of profit, one backed by ₹110 Cr of cash from
> customers and the other by ₹40 Cr of cash plus ₹60 Cr of estimates, one-offs and related-party invoices. The
> market eventually prices the difference; the analyst's job is to price it first. "Quality of earnings" is the
> discipline of asking how much of reported profit is *real, recurring and available to shareholders*.

**Learning objectives** — after this lesson you can:

- Compute cash-flow and balance-sheet accrual ratios and explain the Sloan anomaly.
- Separate recurring from non-recurring earnings and normalise for one-offs, other income and tax anomalies.
- Spot capitalised costs, related-party revenue, "adjusted" metrics and other devices that lift reported profit
  without lifting cash.
- Build and apply a quality-of-earnings scorecard, and interpret Kaveri's FY24–FY26 score.
- Explain when a low score means fraud, when it means aggression, and when it means a legitimately growing business.

**Prerequisites:** [02.5 The cash-flow statement](../02-accounting/05-the-cash-flow-statement.md),
[04.4 Working capital & cash conversion](04-working-capital-and-cash-conversion.md),
[04.6 Per-share metrics & ratio dashboard](06-per-share-metrics-and-ratio-dashboard.md)  ·  **Time:** ~90 min

---

## 1. What "quality" means

High-quality earnings have four properties:

| Property | Test | Where it fails |
|:--|:--|:--|
| **Cash-backed** | CFO ≈ PAT + D&A over a cycle; accruals small | Receivables and inventory growing faster than sales; capitalised costs |
| **Recurring** | Same profit would recur next year without help | Exceptional gains, treasury income, tax credits, provision write-backs |
| **Operating** | Comes from the business, not from financing or accounting choices | Other income, FX gains, revaluation gains, changed depreciation lives |
| **Attributable** | Belongs to *your* shares | Minority interests, ESOP dilution, profits trapped in subsidiaries, related-party leakage |

Quality is a spectrum, not a verdict. A start-up burning cash to grow has low cash-backing and may be fine; a
mature company with a sudden drop in cash-backing usually is not. The skill is to measure, then explain.

## 2. Accruals — the core measurement

**Accruals** are the part of profit that is not cash: the estimates, timing differences and balance-sheet build-ups
that accounting layers on top of cash flow. Two standard measures:

**Cash-flow accruals ratio** (Sloan, 1996):

$$\text{Accruals}_{CF} = \frac{\text{PAT} − \text{CFO}}{\text{Average total assets}}$$

**Balance-sheet accruals ratio** (Richardson et al.): the growth in net operating assets:

$$\text{Accruals}_{BS} = \frac{\text{NOA}_t − \text{NOA}_{t−1}}{(\text{NOA}_t + \text{NOA}_{t−1})/2}, \qquad
\text{NOA} = \text{operating assets} − \text{operating liabilities}$$

Sloan's finding — the **accruals anomaly** — was that companies with high accruals subsequently earn *lower* stock
returns and see profits mean-revert down, because accrual-heavy earnings are less persistent than cash earnings.
Investors, on average, do not discount for it enough. The effect has weakened in the US as it became known but
still shows up in less efficient markets and in small caps.

### 2.1 Kaveri FY21–FY26

`fi.forensics.accruals_ratio(pat, cfo, avg_total_assets)` gives the cash-flow version; the balance-sheet version is
built from the running example's balance sheets (NOA = net block + CWIP + ROU + intangibles + inventory +
receivables + other current assets − payables − other current liabilities − DTL).

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| PAT (₹ Cr) | 32.8 | 47.2 | 62.6 | 86.4 | 97.4 | 90.5 |
| CFO (₹ Cr) | 50.8 | 65.7 | 66.6 | 86.6 | 60.9 | 65.1 |
| CFO / PAT | 155% | 139% | 106% | 100% | 63% | 72% |
| Cash-flow accruals ratio | −3.1% | −3.0% | −0.6% | 0.0% | +3.7% | +2.3% |
| Net operating assets (₹ Cr) | 382.8 | 402.4 | 506.4 | 670.6 | 765.9 | 864.8 |
| Balance-sheet accruals ratio | 1.3% | 5.0% | 22.9% | 27.9% | 13.3% | 12.1% |
| Receivables growth | — | 10% | 23% | 32% | 40% | 29% |
| Revenue growth | — | 24% | 15% | 15% | 16% | 12% |

Reading it:

- Through FY24 the cash-flow accruals ratio was zero or negative — profit was fully cash-backed (CFO/PAT ≥ 100%).
  The balance-sheet ratio spiked in FY23–24 because of the Hosur plant (capex is an operating-asset build, and a
  legitimate one).
- From FY25 the pattern flips: **positive cash-flow accruals of 2–4% of assets and CFO/PAT of 63–72%**, with the
  balance-sheet build now in *receivables* (growing 2–3x faster than revenue) rather than plant. Sloan's threshold
  for "high accruals" is roughly the top decile of the market — typically above +5% — so Kaveri is elevated, not
  extreme. But the direction and the reason (state-agency dues) are what an analyst should be modelling.

!!! tip "Trader's lens"
    Accruals are unrealised P&L. A book that shows large mark-to-model gains and little realised cash is not
    necessarily wrong, but you demand a haircut and you watch the realisations. CFO/PAT is the realised-to-total
    ratio of a company's profit; a persistent gap is the accounting equivalent of a desk that never seems to close
    its winners.

## 3. Recurring vs non-recurring

Normalising earnings means removing what will not recur and adding back what was unusually absent. Work through
the P&L from the bottom up:

| Item | Test | Kaveri |
|:--|:--|:--|
| **Exceptional items** | Cash or non-cash? Truly one-off? Tax effect? | FY25 land gain ₹14.0 Cr (cash, one-off): after-tax ₹10.5 Cr, 11% of PAT. FY21 VRS ₹7.5 Cr cost. |
| **Other income** | What share of PBT? Would it survive a return of cash to shareholders or a capex programme? | ₹3.9 Cr, 3% of PBT — immaterial |
| **Provision write-backs** | Look in other income and other expenses for "provisions no longer required written back" | None disclosed |
| **Tax anomalies** | Effective rate vs statutory; deferred tax credits; MAT credit recognition | 25.2% both years — clean |
| **Subsidy / grant income** | Policy-dependent; PLI receipts, export incentives | Not applicable |
| **FX and MTM gains** | Volatile; strip from run-rate | None |
| **Changed estimates** | Longer useful lives, lower ECL provisioning, changed inventory method | ECL allowance is ₹4.0 Cr against ₹62.4 Cr of receivables > 6 months overdue (6.4% coverage) — a judgement that flatters profit |

The last row deserves a number. Suppose a prudent allowance on the >6-month bucket were 25% rather than 6.4%:
the extra charge would be (0.25 − 0.064) × 62.4 = ₹11.6 Cr pre-tax, ₹8.7 Cr post-tax — about **10% of FY26 PAT**.
Reported EPS ₹15.1 would be closer to ₹13.6. That adjustment is not a claim of wrongdoing (the allowance may be
justified if the states always pay eventually); it is the cost of *your* scepticism, and it belongs in your model.

## 4. Devices that raise reported profit without raising cash

Each is covered in depth in [Module 09](../09-forensics/index.md); here is the checklist an earnings-quality review
runs through, with the tell-tale in the numbers.

| Device | How it works | Tell-tale |
|:--|:--|:--|
| **Aggressive revenue recognition** | Book sales early (bill-and-hold, channel stuffing, percentage-of-completion optimism) | Receivables and unbilled revenue outgrow sales; Q4 spikes; DSO rising |
| **Capitalising operating costs** | Move salaries/R&D/interest into CWIP, intangibles-under-development or capital advances | Soft assets growing; capex far above D&A without new capacity; low "opex" vs peers |
| **Extending useful lives** | Lower depreciation | D&A falling as % of gross block; note on change in estimates |
| **Under-provisioning** | Lower ECL on receivables, warranty, gratuity | Allowance as % of overdue falling; provision releases |
| **Related-party revenue or purchases** | Sell to or buy from promoter entities at chosen prices | RPT note; margins that diverge from peers; receivables from related parties |
| **"Adjusted" metrics** | Exclude ESOP costs, "one-time" costs that recur, restructuring | Gap between adjusted and reported widening every year |
| **Cookie-jar reserves** | Over-provide in good years, release in bad | Provisions moving inversely to underlying profit |
| **Big bath** | Dump every cost into one "kitchen-sink" year, so the next year looks like a recovery | A huge exceptional loss followed by suspiciously smooth growth |
| **Other-income dependence** | Treasury gains, asset sales, dividends from investments | Other income / PBT rising; operating profit flat |

## 5. The quality-of-earnings scorecard

Score each item 0 (clean), 1 (watch) or 2 (concern). Ten items; a total ≥ 8 or any single "concern" with no
explanation means the reported profit should not be used unadjusted. `tools/fi/forensics.forensic_summary` provides
the quantitative inputs (Beneish M, Piotroski F, accruals, cash yield) for the first block.

| # | Item | Test / threshold | FY24 | FY25 | FY26 |
|:--|:--|:--|:--:|:--:|:--:|
| 1 | CFO / PAT (3-yr avg) | 0: > 90% · 1: 75–90% · 2: < 75% | 0 (115%) | 1 (90%) | 2 (78% → FY26 alone 72%) |
| 2 | Cash-flow accruals ratio | 0: < 2% · 1: 2–5% · 2: > 5% | 0 | 1 (3.7%) | 1 (2.3%) |
| 3 | Receivables growth vs revenue growth | 0: ≤ · 1: up to 1.5x · 2: > 1.5x for 2+ years | 2 (32% vs 15%) | 2 (40% vs 16%) | 2 (29% vs 12%) |
| 4 | Beneish M-score | 0: < −2.2 · 1: −2.2 to −1.78 · 2: > −1.78 | 0 (−2.32) | 1 (−1.98) | 1 (−2.14) |
| 5 | Exceptional / non-recurring items as % of PAT | 0: < 5% · 1: 5–15% · 2: > 15% | 0 | 1 (11%) | 0 |
| 6 | Other income as % of PBT | 0: < 10% · 1: 10–25% · 2: > 25% | 0 | 0 | 0 |
| 7 | Related-party transactions | 0: < 5% of costs/revenue · 1: 5–10% · 2: > 10% or rising fast | 1 (8.2%) | 1 (9.1%) | 2 (10.4%, rising 5 years) |
| 8 | Provisioning adequacy | 0: allowance ≥ 25% of >6m overdue · 1: 10–25% · 2: < 10% | 1 | 2 (10%) | 2 (6.4%) |
| 9 | Effective tax rate vs statutory | 0: within 3 pp · 1: 3–10 pp · 2: > 10 pp unexplained | 0 | 0 | 0 |
| 10 | Governance events (auditor change, pledge, qualified opinion, CFO exit) | 0: none · 1: one, explained · 2: unexplained or multiple | 0 | 1 (auditor rotation — mandatory, explained) | 1 (new promoter pledge, 6%) |
| | **Total** | | **4** | **10** | **11** |

Kaveri's score moves from 4 (clean) to 11 (needs resolution) in two years. No single item screams fraud —
the Beneish score never crosses the line, tax is clean, other income is trivial. What the scorecard says is
narrower and more useful: *reported profit of ₹90.5 Cr overstates the cash-generating power of this business by
something like 20–30% until the solar receivables either get collected or get provided for, and the related-party
purchase line needs an explanation that is not in the annual report.* That sentence is what goes in your memo.

## 6. A second worked example — Meru Software (from 02.3)

Meru's FY26 reported PAT was ₹332.5 Cr. Its cash-flow statement shows CFO of ₹298 Cr; capex ₹60 Cr; ESOP charge
₹48 Cr; other income ₹96 Cr (of which ₹12 Cr FX gain); goodwill impairment ₹30 Cr (non-cash, exceptional); and
receivables rose from ₹420 Cr to ₹460 Cr on revenue growth of 9%.

```python
pat, cfo, oi, fx_gain, impair, t = 332.5, 298.0, 96.0, 12.0, 30.0, 0.245
recurring_pat = pat + impair * (1 - t) - fx_gain * (1 - t)    # add back impairment, strip FX gain: 346.1
operating_pat = recurring_pat - (oi - fx_gain) * (1 - t)      # strip treasury income: 282.7
cfo_to_pat = cfo / pat                                         # 0.90
rec_growth = 460/420 - 1                                       # 9.5% vs revenue +9%: in line
print(round(recurring_pat,1), round(operating_pat,1), round(cfo_to_pat,2), round(rec_growth,3))
# 346.1 282.7 0.9 0.095
```

Quality verdict: cash-backed (CFO/PAT 90%, receivables in line with sales), recurring profit slightly *above*
reported (the impairment was a one-off hit), but a third of it is treasury income. For valuation, use operating PAT
of ~₹283 Cr on a software multiple and add the ₹1,200 Cr of cash separately. High quality, wrongly labelled.

## 7. When low quality is fine — and when it isn't

| Situation | Low CFO/PAT because… | Verdict |
|:--|:--|:--|
| Fast-growing distributor or B2B manufacturer | Working capital scales with sales; receivables are to creditworthy customers and turn on time | Acceptable if DSO is stable and funding is available; model the cash need |
| Project/EPC company | Milestone billing; retention money; unbilled revenue | Acceptable if ageing is disclosed and customers are sound; watch unbilled/revenue |
| Company selling to governments or PSUs | Slow but ultimately reliable payers | Acceptable with a discount for time; dangerous when concentrated in a few state agencies with budget problems (Kaveri) |
| Mature company with stable sales | No reason for working capital to grow | **Not acceptable** — profit is being manufactured |
| Any company where receivables growth ≫ sales growth for 3+ years | — | **Not acceptable** without a specific, verifiable explanation |

!!! info "India notes"
    - The Schedule III receivables **ageing schedule** (mandatory since FY22) gives the buckets you need for item 8:
      < 6 months, 6–12 months, 1–2 years, 2–3 years, > 3 years, split disputed/undisputed. Compare the allowance
      with the older buckets every year.
    - The auditor's **Key Audit Matters** often name revenue recognition or receivables recoverability — that is the
      auditor telling you where the judgement is. A KAM on receivables plus rising accruals is a strong prompt.
    - Screener.in shows "Cash from operating activity" on the cash-flow tab; divide by net profit for a quick
      CFO/PAT series across ten years.

!!! warning "Common mistakes"
    - Using one year's CFO/PAT: working capital is lumpy; use three-year sums.
    - Penalising a company mid-capex on balance-sheet accruals without checking whether the build is plant
      (visible, productive) or soft assets (receivables, capital advances, intangibles under development).
    - Treating a below-threshold Beneish score as a clean bill of health — the model is a screen, not proof.
    - Confusing non-cash with non-recurring: ESOP expense is non-cash but recurring; a land-sale gain is cash but
      non-recurring.
    - Forgetting the tax effect when adjusting (a ₹14 Cr gain is ₹10.5 Cr of PAT).
    - Anchoring on "adjusted EBITDA" definitions supplied by the company.

## Key terms

| Term | Meaning |
|:--|:--|
| **Quality of earnings** | The degree to which reported profit is cash-backed, recurring, operating and attributable to shareholders |
| **Accruals** | The non-cash component of profit; PAT − CFO (cash-flow view) or the change in net operating assets (balance-sheet view) |
| **Accruals anomaly (Sloan)** | High-accrual companies subsequently show lower earnings persistence and stock returns |
| **Net operating assets (NOA)** | Operating assets − operating liabilities; excludes cash, investments and debt |
| **Normalised (recurring) earnings** | Profit adjusted to remove non-recurring items, with tax effects |
| **Exceptional item** | Material one-off shown separately on the P&L |
| **Provision write-back** | Reversal of an earlier provision into profit |
| **Cookie-jar reserve** | Over-provisioning in good years to release in bad ones |
| **Big bath** | Loading every possible charge into one bad year |
| **Capitalisation** | Recording an outlay as an asset rather than an expense |
| **Related-party transaction (RPT)** | Dealings with promoters, directors, group companies or their relatives |
| **Expected credit loss (ECL) allowance** | Ind AS 109 provision against receivables that may not be collected |
| **Ageing schedule** | Breakdown of receivables (or CWIP) by how long outstanding |
| **Scorecard** | A structured, weighted checklist producing a comparable quality score |

## Check your understanding

1. Kaveri's three-year (FY24–26) CFO/PAT is 78%. Compute it, and explain why the three-year number is preferred.
<details><summary>Answer</summary>(86.6 + 60.9 + 65.1) / (86.4 + 97.4 + 90.5) = 212.6 / 274.3 = 77.5%. Working-capital
timing (a large collection in the first week of April versus the last week of March) swings single-year CFO by
tens of crores; three-year sums smooth timing without hiding trends.</details>

2. If Kaveri provided 25% against its >6-month receivables, what would FY26 EPS be?
<details><summary>Answer</summary>Extra provision = (0.25 − 4.0/62.4) × 62.4 = 15.6 − 4.0 = ₹11.6 Cr pre-tax;
post-tax 11.6 × 0.7483 = ₹8.7 Cr; PAT 90.5 − 8.7 = 81.8; EPS = 81.8 / 6.0 = ₹13.6.</details>

3. A company's balance-sheet accruals ratio is 30% but its cash-flow accruals ratio is 0%. What is happening?
<details><summary>Answer</summary>Net operating assets grew fast (30%) but CFO matched PAT — so the growth is in
investing assets (capex/CWIP, which sits outside CFO), not working capital. A plant build. Check that capex is
producing capacity, then judge it on incremental ROIC rather than accruals.</details>

4. Why is "adjusted EBITDA excluding ESOP cost" a lower-quality measure than reported EBITDA?
<details><summary>Answer</summary>ESOP cost is recurring compensation paid in shares; excluding it overstates the
profit available to existing shareholders while the dilution it represents is real. If the adjustment is accepted,
the diluted share count must be used — companies rarely do both.</details>

5. Meru's other income is ₹96 Cr. Why does the quality review treat it differently from Kaveri's ₹3.9 Cr?
<details><summary>Answer</summary>Materiality: 22% of Meru's PBT vs 3% of Kaveri's. Treasury income is recurring
but not operating; it deserves a cash-like valuation and would disappear if cash were returned. At 22% it changes
the multiple; at 3% it does not.</details>

6. Give one legitimate and one illegitimate reason for receivables growing 40% on 16% revenue growth.
<details><summary>Answer</summary>Legitimate: a deliberate shift to a customer segment with longer but reliable
payment terms (e.g., government tenders with 90–180 day cycles), disclosed and priced into margins. Illegitimate:
booking sales to dealers who have not ordered (channel stuffing) or to state agencies before contractual
acceptance, so that receivables represent revenue that has not really been earned. The ageing schedule and
subsequent-year collections distinguish them.</details>

## Go deeper

- Richard Sloan, "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings?",
  *The Accounting Review* (1996) — the original accruals-anomaly paper.
- Howard Schilit, *Financial Shenanigans* (4th ed.) — the taxonomy behind Section 4.
- Charles Mulford & Eugene Comiskey, *The Financial Numbers Game* — earnings-quality analysis with worked cases.
- [Module 09](../09-forensics/index.md) and [case I1 Satyam](../13-case-studies/india/01-satyam-2009.md) — where the
  scorecard becomes forensic.

---
[← Previous: 04.6 Per-share metrics & ratio dashboard](06-per-share-metrics-and-ratio-dashboard.md) · [Module index](index.md) · [Next: 05.1 Business models & unit economics →](../05-business-analysis/01-business-models-and-unit-economics.md)
