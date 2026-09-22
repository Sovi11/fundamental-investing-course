# 09.1 · Why and how numbers lie

> **Why this matters:** every analytical technique in Modules 04–07 takes the reported numbers as raw material.
> Forensic accounting asks whether the raw material is sound. Most of the time it is — bent a little in the
> company's favour, within the rules. Occasionally it is not, and the investor who cannot tell the difference
> loses everything: Satyam, Enron, Wirecard, Manpasand, DHFL. This module teaches the spectrum from conservative
> to fraudulent, the incentives that push companies along it, the taxonomy of tricks, and the evidence that
> exposes them.

**Learning objectives** — after this lesson you can:

- Place a company's accounting on the conservative → aggressive → fraudulent spectrum and explain why the
  distinction matters for what you do next.
- Identify the incentives (targets, pledges, fund-raising, bonuses, covenants) that predict manipulation, and the
  fraud triangle.
- Use Schilit's taxonomy — earnings, cash-flow and key-metric manipulation — as a map of the module.
- Explain who catches fraud and how often, and why that should change how you read an auditor's opinion.
- Set up the forensic mindset: "what would I expect to see if this were untrue?"

**Prerequisites:** [04.7 Quality of earnings](../04-financial-analysis/07-quality-of-earnings.md),
[05.6 Corporate governance](../05-business-analysis/06-corporate-governance-india.md)  ·  **Time:** ~70 min

---

## 1. The spectrum

Accounting requires estimates: how long a plant lasts, how many receivables will be collected, when a contract's
revenue is earned, whether a cost creates a future benefit. Every estimate has a range, and management chooses
where in the range to sit.

| Position | What it looks like | Consequence for you |
|:--|:--|:--|
| **Conservative** | Short useful lives, high provisions, revenue recognised late, costs expensed | Reported profit understates economic profit; hidden reserves; usually a buy signal when combined with cash generation (though it can also hide *problems* behind a cushion) |
| **Neutral** | Estimates at the centre of the range, consistent over time | Numbers mean what they say |
| **Aggressive** | Long lives, thin provisions, early recognition, capitalised costs — each defensible alone | Reported profit overstates economic profit; the gap reverses later (write-downs, "one-offs"); requires adjustment, not avoidance |
| **Manipulated** | Choices made *to hit a number* and changed when convenient; disclosure withdrawn when unfavourable | The numbers are a target-seeking output; the trend is unreliable; heavy discount or avoid |
| **Fraudulent** | Fictitious transactions, forged documents, non-existent cash, undisclosed liabilities | The numbers are fiction; the equity is usually worth nothing by the time it is revealed |

The boundaries are blurred, and companies move along the spectrum over time — usually toward the right as
pressure builds. Kaveri Pumps in FY26 ([04.7](../04-financial-analysis/07-quality-of-earnings.md)) is *aggressive*:
a 6.4% allowance on >6-month overdues, rising related-party purchases, a withdrawn KPI — nothing fraudulent, but
each choice in the company's favour. That diagnosis determines the response: adjust the numbers, weight the bear
case, monitor; not "sell everything".

## 2. Incentives: why companies bend

Fraud examiners describe a **fraud triangle**: *pressure* (a reason to need the number), *opportunity* (weak
controls, a compliant auditor, a dominant promoter), and *rationalisation* ("temporary", "everyone does it", "we'll
fix it next quarter"). Pressure is the part you can observe from outside:

| Pressure | Mechanism | Where to see it |
|:--|:--|:--|
| **Guidance and targets** | A promised 15–18% growth becomes a number to hit; the quarter is "made" by pulling sales forward | Say-do table ([05.5](../05-business-analysis/05-management-and-capital-allocation.md)); Q4 spikes |
| **Fund-raising** | An IPO, QIP or debt issue needs good numbers *now* | Timing of unusual improvements relative to offerings; DRHP restated financials vs later results |
| **Promoter leverage** | Pledged shares create a floor the promoter must defend; a falling stock triggers margin calls | Pledge disclosures; unusual announcements when the stock falls |
| **Covenants** | Net debt/EBITDA or DSCR tests must be met; EBITDA gets "helped" | Leverage near covenant levels; lease/other-income reclassifications |
| **Compensation** | Bonuses or ESOP vesting tied to revenue/EBITDA/EPS | Remuneration policy metrics |
| **Ratings** | A downgrade raises funding cost or closes markets (NBFCs) | Ratios hovering just above rating thresholds |
| **Survival** | A business losing money must show it is not (Enron 2001, DHFL 2018–19, Wirecard 2019–20) | Cash generation diverging from profit for years |

Opportunity in India is structurally higher where a promoter controls the board, the audit committee is
ornamental, and the auditor is small ([05.6](../05-business-analysis/06-corporate-governance-india.md)). The
combination of *pressure* (pledges, fund-raising) and *opportunity* (weak governance) is the screen.

## 3. Schilit's taxonomy — the map of this module

Howard Schilit's *Financial Shenanigans* organises manipulation into three families, each with named techniques.
The module follows the map:

| Family | Aim | Techniques | Lesson |
|:--|:--|:--|:--|
| **Earnings manipulation** | Overstate current profit (or understate it to create reserves for later) | Recording revenue too soon; recording bogus revenue; boosting income with one-time or unsustainable items; shifting current expenses to later periods (capitalising, long lives, under-provisioning); hiding expenses or losses (off-balance-sheet, misclassification); shifting current income to later periods (cookie jar); shifting future expenses to the current period (big bath) | [09.2](02-revenue-red-flags.md), [09.3](03-expense-and-asset-red-flags.md) |
| **Cash-flow manipulation** | Make operating cash flow look better than it is | Shifting financing inflows into CFO (factoring, supplier finance); shifting operating outflows into CFI (capitalising); boosting CFO with unsustainable items (working-capital timing, one-off collections); fictitious cash | [09.4](04-cash-flow-games.md) |
| **Key-metric manipulation** | Mislead with non-GAAP metrics | "Adjusted EBITDA", "contribution margin", "same-store sales" defined to flatter; changing definitions; dropping metrics; GMV instead of revenue | Throughout; [07.4](../07-special-valuation/04-high-growth-and-loss-making.md) |

To these the India edition adds a fourth: **governance-enabled extraction** — value moved to promoters through
related parties, group entities, pledges and issuances, which may leave the reported numbers accurate while making
them irrelevant to minorities ([09.5](05-governance-red-flags-india.md)).

## 4. Who catches fraud, and how often

The uncomfortable evidence (US studies of 1996–2004 frauds, e.g. Dyck, Morse & Zingales; and Indian experience):

| Detector | Share of cases (US, approx.) | Comment |
|:--|:--|:--|
| Employees / whistle-blowers | ~17% | The most common; India's Companies Act vigil mechanism and SEBI's informant rules exist but are used less |
| Media and analysts | ~14% and ~14% | Short-seller reports (Hindenburg, Muddy Waters, Citron; in India, several 2018–24 reports) and investigative journalism (the FT on Wirecard; Cobrapost on DHFL) |
| Regulators (SEC/SEBI) | ~7% | Usually late; SEBI's forensic audits typically follow a collapse |
| **Auditors** | **~10%** | Auditors detect a minority of frauds; Satyam (PwC), Wirecard (EY), Enron (Andersen) all had big-firm auditors |
| Short sellers | ~15% | Financially motivated, often right on the facts, sometimes wrong on the conclusion |
| Self-disclosure / collapse | Remainder | The fraud runs out of cash |

The practical lessons: an unqualified audit opinion is *necessary, not sufficient*; the people most likely to
find a problem are outside the company (read short reports and journalism seriously, then check the facts
yourself); and the earliest reliable signal is usually the *numbers themselves* — cash not matching profit for
years — which is exactly what this module teaches you to read.

!!! info "India notes"
    - India's major accounting failures cluster in three patterns: **fictitious cash and revenue** (Satyam 2009 —
      [case I1](../13-case-studies/india/01-satyam-2009.md)); **NBFC/HFC fund diversion and evergreening** (DHFL,
      IL&FS — [case I4](../13-case-studies/india/04-ilfs-dhfl-2018.md); several 2019–24 cases with forensic-audit
      findings); and **small-cap growth fabrication** (Manpasand, Vakrangee — [case I14](../13-case-studies/india/14-manpasand-vakrangee-small-cap-flags.md);
      Brightcom 2023; many SME-exchange names). Each had a recognisable signature in the numbers years before the
      collapse.
    - SEBI's tools: forensic audits ordered on listed companies (disclosed under LODR Reg 30 since 2020), interim
      orders freezing promoters, and the NFRA (National Financial Reporting Authority, 2018) which audits the
      auditors and has issued penalties and debarments in several cases — read NFRA orders on nfra.gov.in for a
      catalogue of audit failures.
    - The Companies Act, 2013 s.143(12) requires auditors to report suspected fraud above ₹1 Cr to the government;
      the CARO annexure asks about fraud noticed or reported. Read both.

## 5. The forensic mindset

Three habits that separate forensic reading from ordinary reading:

1. **Invert.** Don't ask "is this number right?" Ask "if this company were fabricating growth, what would the
   statements look like?" — then check whether they look like that. Fabricated revenue needs a home: receivables
   that don't get collected, or cash that isn't there, or inventory that doesn't move. Fabricated profit needs the
   cash-flow statement to disagree with the P&L, or CFO to be propped by something non-operating.
2. **Triangulate.** Every P&L claim has a balance-sheet and cash-flow counterpart. Revenue ↔ receivables ↔
   collections; profit ↔ retained earnings ↔ cash or debt; capex ↔ gross block ↔ capacity ↔ output. When the three
   disagree, the disagreement is the finding.
3. **Watch the disclosures, not just the numbers.** Changes in accounting policy, auditor, CFO, KPI definitions,
   fiscal year, segment reporting; delays in filing; "clarifications" to exchanges; the tone of the audit report.
   Silence where there was disclosure is itself data.

!!! tip "Trader's lens"
    Forensic work is looking for a mismatch between the quoted price and the fill — profit that is quoted but never
    settles as cash. A company whose PAT does not turn into cash over three years is a counterparty whose trades
    never clear. You would stop dealing with them; here, you stop trusting the P&L and price the equity on what
    actually settles.

!!! warning "Common mistakes"
    - Treating "aggressive" as "fraudulent" (or the reverse). Aggression is adjusted for; fraud is avoided.
    - Believing the audit opinion settles the question.
    - Dismissing short-seller reports because of the messenger's incentive — check the facts.
    - Forgetting that conservative accounting can also hide things (a cushion released to smooth earnings).
    - Looking only at the P&L: the balance sheet and cash-flow statement are where manipulation leaves marks.

## Key terms

| Term | Meaning |
|:--|:--|
| **Forensic accounting** | Analysis of financial statements to detect manipulation, misstatement or fraud |
| **Aggressive accounting** | Estimates and policies chosen at the profit-flattering end of the acceptable range |
| **Earnings management** | Deliberate use of accounting choices to hit targets or smooth results |
| **Fraud triangle** | Pressure + opportunity + rationalisation |
| **Schilit's taxonomy** | Classification of shenanigans into earnings, cash-flow and key-metric manipulation |
| **Cookie-jar reserve** | Over-provisioning in good periods to release into profit later |
| **Big bath** | Concentrating charges into one bad period so future periods look better |
| **Whistle-blower / vigil mechanism** | Internal reporting channel for fraud; Companies Act s.177(9) |
| **NFRA** | National Financial Reporting Authority — India's audit regulator |
| **Forensic audit** | A special investigation, often SEBI- or lender-ordered, into suspected misstatement |
| **Short-seller report** | Published research by an investor positioned to profit from a price fall |

## Check your understanding

1. Classify each: (a) a company extends useful lives from 10 to 15 years, disclosed, industry-standard; (b) a
   company books revenue on goods shipped to a warehouse it controls; (c) a company provides 50% against all
   receivables over 90 days.
<details><summary>Answer</summary>(a) Aggressive if the change is to hit a number, neutral if genuinely aligned with
industry practice — check timing and disclosure; (b) fraudulent/manipulated (bill-and-hold to a controlled entity
is bogus revenue); (c) conservative — possibly creating a reserve; check whether it is later released.</details>

2. Why do pledged promoter shares raise the probability of accounting manipulation?
<details><summary>Answer</summary>They create pressure: a falling stock triggers margin calls and loss of control,
so the promoter has a direct personal stake in the reported numbers and the share price every quarter; combined
with control of the board (opportunity), the fraud triangle is two-thirds complete.</details>

3. A company's auditor is a Big-4 affiliate with an unqualified opinion. What does that tell you?
<details><summary>Answer</summary>That the statements passed a sample-based audit designed to detect material
misstatement — which historically catches a minority of frauds. It raises the bar for fabricating documents but
does not verify business substance; Satyam and Wirecard had Big-4 auditors. Necessary, not sufficient.</details>

4. Apply the inversion habit: if Kaveri's solar revenue were being booked before contractual acceptance, what would
   you expect to see?
<details><summary>Answer</summary>Receivables growing faster than revenue with an ageing bucket that lengthens each
year; unbilled revenue/contract assets rising; CFO/PAT falling; provisioning that does not keep pace; BGs rising; and
disclosure of receivable days withdrawn — most of which is in fact visible. The inversion does not prove
misstatement, but it tells you which notes to read and which questions to ask.</details>

5. Name the three families in Schilit's taxonomy and give one Indian example of each.
<details><summary>Answer</summary>Earnings manipulation (Manpasand's fabricated growth; Satyam's fictitious
revenue); cash-flow manipulation (Satyam's non-existent cash; NBFC evergreening that kept "collections" flowing); key-metric
manipulation (new-age companies' adjusted EBITDA and contribution definitions; Vakrangee's "franchise" metrics).</details>

## Go deeper

- Howard Schilit, Jeremy Perler & Yoni Engelhart, *Financial Shenanigans* (4th ed., 2018) — the taxonomy and the
  cases.
- Alexander Dyck, Adair Morse & Luigi Zingales, "Who Blows the Whistle on Corporate Fraud?", *Journal of Finance*
  (2010) — the detection statistics.
- NFRA orders and SEBI forensic-audit-related orders (nfra.gov.in; sebi.gov.in) — India's own catalogue.
- Dan McCrum, *Money Men* (2022) — the Wirecard investigation from the inside ([case G9](../13-case-studies/global/09-wirecard-2020.md)).

---
[← Previous: 08.11 Financial services ex-lending](../08-sectors/11-financial-services-ex-lending.md) · [Module index](index.md) · [Next: 09.2 Revenue red flags →](02-revenue-red-flags.md)
