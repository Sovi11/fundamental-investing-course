# 15.3 · Worked example — Kaveri, end to end

> **Why this matters:** the course has analysed Kaveri Pumps & Motors lesson by lesson: its accounts in Module 02,
> its ratios in 04, its management in 05, its value in 06, its forensics in 09, its model in 10 and its memo in
> 11.3. This lesson puts those pieces in the order a real case runs, as the casebook stores them. It shows which
> stage produced each piece and what each gate decided. Kaveri is fictional, which lets the example be complete
> without pretending to know the future of a real company.

**Learning objectives** — after this lesson you can:

- Follow one company through all six stages and point to the deliverable of each.
- See how a gate can partly fail (a good business at a bad price) and still produce a useful decision.
- Write forecasts that can be scored, and set up the quarterly update and post-mortem before the outcome is known.

**Prerequisites:** [15.1](01-the-case-study-method.md), [15.2](02-templates.md), the
[Kaveri running example](../appendix/running-example/kaveri-pumps.md)  ·  **Time:** ~90 min

!!! info "Where the files are"
    Every stage below exists as a file in the private casebook under `cases/KAVERIPMP/`, with the decision in
    `journal/2026-09-22-KAVERIPMP.md`. The numbers are the running example's. Nothing here is a view on a real
    company.

---

## 1. Stage 0 — the queue

`queue/QUEUE.md`, 10 August 2026, two days after the Q1 FY27 results:

| Ticker | Why interesting (one line) | Source | Status |
|:--|:--|:--|:--|
| KAVERIPMP | Down ~25% since March on a Q1 miss and a new promoter pledge; 26× P/E against a 5-year median of 41× — forced selling or a broken story? | 52-week-low screen + results calendar | kill test |

The reason given is **forced selling, or a misunderstanding**: specific enough to test.

---

## 2. Stage 1 — kill test

`cases/KAVERIPMP/00-kill-test.md`, 18 September 2026, price ₹390, market cap ₹2,340 Cr. Thirty minutes.

**Business in three sentences.**

1. Kaveri makes agricultural, domestic and industrial pumps and motors in Coimbatore and Hosur, sold through
   ~1,800 dealers in 14 states.
2. Since FY23 it has sold solar pumping systems to state agencies under PM-KUSUM, now 27% of revenue.
3. Farmers buy on dealer relationships, reliability and service; states buy on tender price.

| Metric | Value | Comment |
|:--|--:|:--|
| Revenue CAGR FY21–26 | 16.6% | FY23–26: 14.7%, driven by solar |
| EBITDA margin (range) | 12.0–15.4% | Peaked FY24; 13.8% FY26; 12.6% Q1 FY27 |
| ROCE (range) | 12.5–19.2% | Falling since FY24 |
| CFO ÷ PAT | 96% (5-year), 78% (3-year) | Above the 60% disqualifier, but falling |
| Net debt ÷ EBITDA | 0.8× | From net cash in FY22 |
| Receivable days | 57 → 96 (FY22–26) | The obvious question |
| Dilution | 6.00 → 6.07 Cr diluted | ESOPs; immaterial |

| People | Finding |
|:--|:--|
| Promoter holding | 58.4% |
| Pledge | **6% of promoter holding, new (Nov-2025)**, for a promoter-group real-estate venture |
| Auditor | Mandatory rotation in FY25; no resignation |
| SEBI / regulatory | None |
| Related-party purchases | 10.4% of material cost (Kaveri Castings), up from 6.5% in FY21 |

| Forensic quick score | Value | Flag? |
|:--|--:|:--|
| Beneish M | −2.14 | No (below −1.78), but DSRI-driven and trending up |
| Piotroski F | 4 | Weak |
| Accruals ratio | 2.3% | Elevated but below 10% |
| Implied yield on cash | 7.4% | No — the cash is real |

| Multiple | Now | 5-year median | Peer median |
|:--|--:|--:|--:|
| P/E | 25.9× | 40.7× | 34.7× |
| EV/EBITDA | 13.7× | 20.7× | 20.8× |
| P/B | 3.3× | 4.4× | — |

**Disqualifiers:** none fires. The pledge is well under 20%, CFO ÷ PAT is 78%, M is below the line and the business
is explainable.

**Verdict: TRIAGE.** The one question: *is the solar growth creating value, or is it buying revenue with
receivables?*

---

## 3. Stage 2 — triage

`01-case-study.md`, triage section. Three hours on the FY26 annual report, four call transcripts and the "A/Stable"
rating rationale. Eight lines:

1. **Unit economics.** Agri pumps carry ~40% gross margin and are paid in ~60 days through dealers. Solar carries
   22–24% gross margin, is paid in 6–12 months by state agencies, and needs bank guarantees (₹96 Cr outstanding).
2. **Industry position.** Mid-pack in a fragmented cluster. ROCE of 16% against 14–24% for four peers; the fastest
   grower (Konkan, 38% CAGR) is also a solar-tender business.
3. **Say-do: 0 for 5 on the scoreable items** ([05.5](../05-business-analysis/05-management-and-capital-allocation.md)):
   - growth and margin guidance missed;
   - receivable-day guidance missed twice, and worsening;
   - capex overshot;
   - the "states clearing dues in Q4" claim failed;
   - then the receivable-days KPI was withdrawn in Q1 FY27.
4. **Value-driving KPIs.** Receivable days and the ageing of overdues; solar share and margin; Hosur motor
   utilisation (57%).
5. **Reverse DCF.** ₹390 implies **14.1% revenue growth for ten years** at base-case margins — essentially
   FY23–26 continued ([kaveri-valuation](../appendix/running-example/kaveri-valuation.md)).
6. **Variant perception.** The growth was a mix shift into a segment with structurally worse economics, and the
   market is capitalising it at a franchise multiple.
7. **What would refute it.** Receivable days below 80 and growth of 15% or more by Q3 FY27.
8. **Rough payoff at ₹390.** Bull ~₹416 (+7%) against bear ~₹168 (−57%). **Not asymmetric.**

**Gate decision.** The variant perception passes; the asymmetry fails *at this price*. The method says stop, but
there is a legitimate third outcome: a **watchlist deep dive**. The business is within circle, the stock is falling,
and the useful output is not "buy or not" but "*at what price and on what evidence* would I buy?" That was recorded
as the reason to continue, so it cannot later be mistaken for momentum.

---

## 4. Stage 3 — deep dive

In practice this takes two to three weeks. For Kaveri, each piece was built in a course lesson:

| Work | Where it was done | Result |
|:--|:--|:--|
| Ten-year history and ratio dashboard | [04.6](../04-financial-analysis/06-per-share-metrics-and-ratio-dashboard.md) | Incremental ROIC FY24–26 **4.6%**, against a 12.2% WACC; ROIC down from 15.1% to 12.0% |
| Working capital | [04.4](../04-financial-analysis/04-working-capital-and-cash-conversion.md) | Cash conversion cycle 80 → 115 days; receivables at 70 days would release ₹94 Cr |
| Moat and capital cycle | [05.3](../05-business-analysis/03-moats-and-competitive-advantage.md), [05.4](../05-business-analysis/04-capital-cycle-and-competition.md) | Dealer franchise in agri; no moat in tender solar, where capacity is entering |
| Management and governance | [05.5](../05-business-analysis/05-management-and-capital-allocation.md), [05.6](../05-business-analysis/06-corporate-governance-india.md) | Say-do 0/5; KPI withdrawn; new pledge; rising related-party purchases |
| Forensic checklist | [09.7](../09-forensics/07-the-forensic-checklist.md) | **18/120, six 2s, no 3s → Amber**. EPS adjusted ₹15.1 → ~₹13.6 for provisioning |
| Three-statement model | [10.5](../10-modeling/05-build-along-kaveri-model.md) | Base, bull and bear driven by solar share, receivable days and margin |
| Valuation | [kaveri-valuation](../appendix/running-example/kaveri-valuation.md), [06.4](../06-valuation/04-dcf-in-practice.md) | Base **₹320** (WACC 12.19%, g 5.5%); bull ₹416; bear ₹168; weighted ₹306 (25/50/25) or ₹286 (35/45/20) |
| Relative value | [06.5](../06-valuation/05-relative-valuation-and-multiples.md) | 26× against a 35× peer median, but on lower ROCE and much weaker cash conversion: fair within an expensive group |

**Scuttlebutt log** (`scuttlebutt/log.md`; illustrative, because the company is fictional):

| Date | Source | Asked | Learned | Confidence |
|:--|:--|:--|:--|:--|
| 12-Sep | Coimbatore agri-pump dealer (competitor's and Kaveri's) | Sell-through, credit terms, price moves | Agri demand flat; no Kaveri price increase since FY25; dealer credit unchanged at ~45 days | Medium |
| 14-Sep | State PM-KUSUM progress dashboard (public) | Installations and payment status for Kaveri's two largest states | Installations on track; the states' disbursement of central subsidy is behind by two quarters | Medium–high |
| 16-Sep | Former solar project manager (industry, not Kaveri) | How tender contractors are paid | Payment follows commissioning plus state inspection; 9–14 months is normal; disputes over installation quality are common | Medium |

The scuttlebutt supports line 6 of the triage: the slow payments are **structural to the channel**, not a one-off.
That is exactly the point management's "fully recoverable" language avoids.

**Gate: numbers, people, price.**

- *Numbers:* pass, with adjustments.
- *People:* Amber — the say-do record, the pledge and the related-party purchases.
- *Price:* fail at ₹390.

**Thesis-breakers** were written before the memo (next section).

---

## 5. Stage 4 — memo, sizing and the journal

The full memo is the sample in [11.3 §3](../11-process/03-writing-an-investment-memo.md). The casebook's one-page
thesis (`02-thesis.md`) compresses it:

> **Kaveri Pumps & Motors (KAVERIPMP) · 22-Sep-2026 · ₹390 · market cap ₹2,340 Cr · WATCH — do not buy above ₹260 ·
> horizon 2–3 years · size 0 now; 4% at ₹260 with receivable days < 85**
>
> **Market believes:** a pump franchise growing ~14% for a decade with margins recovering to 15.5% (reverse DCF).
>
> **I believe:** growth is a mix shift into tender solar with worse economics. I expect 9–11% growth, margins near
> 14% and a ₹10–15 Cr provisioning catch-up.
>
> **Why:**
>
> 1. Solar went from 7% to 27% of revenue at ~23% gross margin against ~40% in agri.
> 2. CFO ÷ PAT fell from 100% to 63–72%; receivable days rose from 61 to 96; overdues of more than six months
>    doubled to ₹62 Cr, with 6.4% coverage.
> 3. Incremental ROIC of 4.6% against a 12.2% WACC.
>
> **Valuation:** bear ₹168 / base ₹320 / bull ₹416; weighted ₹306 (₹286 with a governance-weighted bear). At ₹390,
> the expected return is −22% and the probability-weighted upside-to-downside ratio is 0.07.
>
> **I'm wrong if:**
>
> 1. H1 FY27 receivable days are below 80, with overdues falling (Nov-2026).
> 2. Q2–Q3 FY27 growth is above 14% with margins above 14.5% (Feb-2027).
> 3. Hosur utilisation is above 70% by FY27 year-end.
>
> **Kill:** pledge above 15%; auditor qualification; CFO exit.

**Sizing at the trigger** ([11.4](../11-process/04-position-sizing-and-portfolio-construction.md)). At ₹260:

- max-loss: 3% ÷ 35% bear loss = **8.6%**;
- quarter-Kelly on a tree with a 10–15% governance tail: **~5–12%**;
- the lower, halved for Amber: **~4%**;
- liquidity: to be checked at the time against average daily value.

**The journal entry** (`journal/2026-09-22-KAVERIPMP.md`) — a decision *not* to buy is still a decision:

> **Decision:** PASS at ₹390; WATCH with a trigger at ₹260 *and* receivable days < 85.
> **What I believe:** see thesis. **What the market believes:** 14% growth for ten years.
> **Expectations, with dates:** see the forecast register below.
> **What would reverse this:** any two thesis-breakers by Feb-2027, which moves the weighted value to ~₹330 and the
> verdict to "fair, not cheap".
> **Confidence:** 65% that Kaveri trades below ₹330 on 22-Sep-2027.
> **Mood:** calm; mild pull to "do something" after a long research effort, noted and resisted.
> **Pre-mortem:** if I am wrong, it is because the states paid, and the market was right to look through the
> working capital.

**The forecast register.** These are the entries that will be scored ([15.1 §4](01-the-case-study-method.md#4-calibration-scoring-your-probabilities)):

| # | Forecast | Probability | Resolves | Source |
|--:|:--|--:|:--|:--|
| 1 | Receivable days at 31-Mar-2027 are 85 or more | 70% | May-2027 | FY27 results |
| 2 | FY27 revenue growth is below 14% | 75% | May-2027 | FY27 results |
| 3 | FY27 EBITDA margin is below 14.5% | 70% | May-2027 | FY27 results |
| 4 | The ECL allowance on the > 6-month bucket is raised to 15% or more in FY27 | 55% | Jul-2027 | FY27 annual report |
| 5 | The pledge is above 6% of promoter holding at any point before Sep-2027 | 35% | Sep-2027 | SAST filings |
| 6 | The stock is below ₹330 on 22-Sep-2027 | 65% | Sep-2027 | NSE close |

---

## 6. Stage 5 — a quarterly update

The first update is due after the Q2 FY27 results in November 2026. This is how `updates/2027-Q2.md` is set up
**now**, with the expected column filled in from the base case before the numbers arrive:

| Metric | Expected (base) | Actual | Delta | Comment |
|:--|--:|:--|:--|:--|
| Revenue growth (YoY) | 6–9% | — | | Q2 FY26 base: ₹263.6 Cr |
| EBITDA margin | 12.0–13.0% | — | | Q2 is seasonally weak (12.2% last year) |
| Receivable days (H1 balance sheet) | 95–105 | — | | Breaker 1 fires below 80 |
| > 6-month overdues | Up or flat | — | | Needs the H1 disclosure; note if withheld again |
| Pledge | 6% | — | | SAST, continuous |

The rules for filling it in:

1. Fill in the actual column from the filing, before reading any commentary.
2. Mark each breaker green, amber or red.
3. Re-run the scenario values only if a driver moved outside its range.
4. Write the action (here: stay on watch, or remove, or move the trigger) in two lines.

If receivable days are withheld again, that is itself a result: it adds a point on D11 of the forensic checklist,
and it moves the bear weight up.

---

## 7. Stage 6 — the post-mortem

Kaveri's post-mortem is due on 22 September 2029, three years after the decision, or earlier if the watch becomes
a position and the position is closed. It will be written against the forecast register and the three scenarios.
Four questions are fixed now, so that they cannot be chosen to flatter the outcome later:

1. Which scenario did the business follow (growth, margins, receivables), whatever the share price did?
2. Did the decision to pass cost money — did the stock beat the Nifty 500 from ₹390 — and was that knowable?
3. What is the Brier score on the six forecasts?
4. Did the watchlist trigger fire, and was it acted on?

The post-mortem ends, as the template requires, with **one change to the process**. If the pass turns out wrong
because the states paid, the candidate change is to require a payment-track-record check on the specific
counterparties, not the channel in general, before weighting a receivables-driven bear case.

---

## Key terms

| Term | Meaning |
|:--|:--|
| **Watchlist deep dive** | A deep dive whose output is a buy price and evidence trigger, not a purchase; recorded as such to avoid drift |
| **Trigger** | A price *and* an evidence condition that must both hold before buying |
| **Forecast register** | A dated list of probabilistic, scoreable forecasts taken from the journal |
| **Expected column** | The base-case values written into the quarterly update before results arrive |

## Check your understanding

1. The triage gate failed on asymmetry, yet the case continued. Why is that acceptable here, and what stops it
   becoming a habit?
<details><summary>Answer</summary>The deep dive's purpose changed: from "should I buy?" to "at what price and on what
evidence would I buy?". That is a real decision for a falling stock within circle. What keeps it honest is that the
reason is written down at the gate, the output is a trigger rather than a position, and the funnel statistics show
how often "watchlist deep dives" happen. If they become most deep dives, the gate is being bypassed.</details>

2. Rewrite forecast 6 in the register so that it tests the *business* rather than the share price.
<details><summary>Answer</summary>For example: "FY27 CFO ÷ EBITDA below 55% (FY27 annual report, Jul-2027): 70%."
Business forecasts separate analysis from market timing; price forecasts mix the two.</details>

3. Q2 FY27 shows receivable days of 78, with overdues down 30%. What happens, mechanically?
<details><summary>Answer</summary>Breaker 1 fires. Mark it red in the update and re-run the scenarios with lower
working-capital intensity: the bear weight falls and the weighted value rises towards ~₹330. If a second breaker
fires by February 2027, the verdict moves to "fair, not cheap" and the trigger price is reset. The forecast register
is **not** edited; forecast 1 will simply be scored when it resolves.</details>

## Go deeper

- The Kaveri pages: [running example](../appendix/running-example/kaveri-pumps.md) ·
  [reference valuation](../appendix/running-example/kaveri-valuation.md) · [memo](../11-process/03-writing-an-investment-memo.md) ·
  [forensic checklist](../09-forensics/07-the-forensic-checklist.md).
- The casebook folder `cases/KAVERIPMP/`, the same case in its working form.

---
[← Previous: 15.2 Templates](02-templates.md) · [Module index](index.md) · [Next: 15.4 Grading rubric & review →](04-grading-rubric-and-review.md)
