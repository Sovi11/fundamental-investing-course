# 15.1 · The case-study method

> **Why this matters:** research time is the scarcest input you have, and most ideas do not deserve it. A
> stage-gated method spends five minutes on every idea, thirty on most, three hours on a few and weeks on very
> few. Each gate asks one question that can end the work. The gates also protect you from sunk cost: a case that
> has taken three weeks feels as though it ought to end in a purchase. Written gates make "no" the default and
> "yes" the thing that has to be earned.

**Learning objectives** — after this lesson you can:

- Run the six stages from queue to post-mortem, with the deliverable and gate question for each.
- Budget time across a funnel of ideas, and read your own funnel statistics as a test of your filters.
- Rank evidence by quality and know which stage needs which kind.
- Record probabilistic forecasts and score them with the Brier score.
- Keep a casebook that can be audited later: dated, sourced, append-only.

**Prerequisites:** [11.2 The research process](../11-process/02-the-research-process.md),
[11.6 Decision journals](../11-process/06-behavioural-finance-and-decision-journals.md)  ·  **Time:** ~60 min

---

## 1. The six stages

| Stage | Time | Deliverable (casebook file) | Gate question — stop if the answer is no |
|:--|:--|:--|:--|
| **0. Queue** | 5 min | One line in `queue/QUEUE.md` | Is there a plausible reason this is mispriced, and can I understand the business? |
| **1. Kill test** | 30 min | `cases/<T>/00-kill-test.md` | Does it pass every disqualifier (governance, forensic scores, leverage, explainability)? |
| **2. Triage** | 3 h | Triage section of `01-case-study.md` | Can I state a variant perception in one sentence, with evidence that could refute it, and is the payoff asymmetric? |
| **3. Deep dive** | 2–3 weeks | Full `01-case-study.md`, `model/`, `forensic-checklist.md`, `scuttlebutt/` | Do the numbers, the people and the price all pass? Do I know what breaks the thesis? |
| **4. Memo & decision** | 1 day | `02-thesis.md`, sizing, `journal/YYYY-MM-DD-<T>.md` | Would I hold this as my only position for three years at twice the size? If not, size down or pass |
| **5. Monitor** | 1 h a quarter | `cases/<T>/updates/YYYY-QN.md` | Has a thesis-breaker fired? Is the price beyond the bull case? |
| **6. Post-mortem** | 2 h | `cases/<T>/post-mortem.md` | Was the outcome due to process or luck? Which filter would have caught the error earlier? |

The casebook's `PROCESS.md` holds the operational version, including the stage-1 disqualifiers and the stage-2
reading list. This lesson explains why each stage exists and how to do it well.

### Stage 0 — the queue

An idea enters with one line: ticker, date, source, and *why it might be mispriced*. The reason matters more than
the idea. Choose one of:

- **neglect** — low coverage, small size, an unfashionable sector;
- **complexity** — a conglomerate, a demerger, a lender with odd accounting;
- **forced selling** — index deletion, a fund redemption, a promoter pledge;
- **cyclical trough**;
- **misunderstanding** — the market extrapolating a trend you think is ending;
- **none**.

"It's a great company" is not a reason; great companies are usually priced as such. Ideas come from screens,
annual-report reading, special-situation calendars, case-study patterns and conversations
([11.1](../11-process/01-idea-generation.md)).

### Stage 1 — the kill test

Thirty minutes, and strict. Fill the template from Screener, `tools/pull.py` and the latest shareholding pattern,
and nothing else. The disqualifiers are rules, not suggestions:

- Beneish M above −1.78 with no explanation;
- CFO ÷ PAT below 60% over three years (for a non-lender);
- a promoter pledge above 20% of the promoter holding;
- an auditor resignation with unexplained reasons;
- unresolved SEBI enforcement against the promoters;
- a business you cannot explain in three sentences;
- no plausible reason for mispricing.

Each disqualifier comes from a Module 13 case where ignoring it was expensive. The kill test does not decide whether
to buy. It decides whether the company is worth three hours.

### Stage 2 — triage

Three hours with the latest annual report (MD&A, auditor's report, related-party note, contingent liabilities,
borrowings, receivables ageing), four earnings-call transcripts and the credit-rating rationale. The output is
eight lines:

1. unit economics;
2. industry position;
3. the say-do record (guidance against delivery);
4. the two or three KPIs that drive value;
5. a first reverse DCF — what the price implies ([06.6](../06-valuation/06-reverse-dcf-and-expectations.md));
6. the variant perception in one sentence;
7. the evidence that would refute it;
8. a rough upside-to-downside.

If you cannot write line 6, stop. There may be nothing wrong with the company, but you have no edge in it.

### Stage 3 — the deep dive

This is where the modules become a work plan:

| Work | Module | Output |
|:--|:--|:--|
| Ten-year history and ratio dashboard | [04](../04-financial-analysis/index.md), [10.2](../10-modeling/02-historicals-and-data.md) | `model/` historicals tab; dashboard |
| Business, moat, capital cycle, management | [05](../05-business-analysis/index.md) | Case-file sections 3–5 |
| Sector playbook | [08](../08-sectors/index.md) | The sector's KPIs, filled |
| Forensic checklist, fully scored | [09.7](../09-forensics/07-the-forensic-checklist.md) | `forensic-checklist.md` with a rating and adjustments |
| Three-statement model with scenarios | [10](../10-modeling/index.md) | `model/` with base, bull and bear |
| Valuation triangulated | [06](../06-valuation/index.md), [07](../07-special-valuation/index.md) | DCF or P/B–RoE, multiples, reverse DCF, scenario tree |
| Scuttlebutt: at least three primary checks | [05.7](../05-business-analysis/07-scuttlebutt-and-primary-research.md) | `scuttlebutt/` log |
| Macro and factor exposure | [12.1](../12-macro-special-sits/01-macro-for-equity-investors.md) | One paragraph on what has to go right |
| Pre-mortem | [11.6](../11-process/06-behavioural-finance-and-decision-journals.md) | Case-file risks section |

The gate question has three parts: the numbers, the people and the price. A great business with a price that
already assumes greatness fails on price. A cheap stock with a promoter who treats the company as a personal
treasury fails on people.

### Stage 4 — memo, sizing, decision

The memo follows [11.3](../11-process/03-writing-an-investment-memo.md). The one-page thesis (`02-thesis.md`) is
its compressed form.

Sizing follows [11.4](../11-process/04-position-sizing-and-portfolio-construction.md):

1. Take the lower of fractional Kelly (quarter-Kelly for single stocks, from a scenario tree that includes a tail)
   and the max-loss size (the portfolio-loss budget ÷ the bear-case loss).
2. Halve it for an Amber forensic rating; take no position on Red.
3. Cap it so the position can be exited in five days at 20% of average daily value.
4. Start new positions at half the target.

The decision goes into `journal/` *before* the order is placed. The entry records:

- what you believe;
- what you expect to see and by when;
- what would make you sell;
- your confidence as a probability;
- your mood — the one field people skip and later wish they had kept.

A decision not to buy gets a journal entry too.

### Stage 5 — monitoring

After each quarterly result, spend one hour on `updates/YYYY-QN.md`:

- KPIs against expectations;
- the say-do update;
- the status of each thesis-breaker;
- value against the scenarios;
- the action and why ([11.5](../11-process/05-monitoring-and-selling.md)).

The discipline is to fill the update *before* reading the sell-side's take and before looking at the share price.

### Stage 6 — post-mortem

On exit, or three years after the decision if you never acted, compare the outcome with each scenario. Separate
what was knowable from what was luck, and change one filter. Post-mortems on the ideas you *passed* on are as
valuable as those on positions: they show whether the kill test is killing the right things.

---

## 2. The funnel and its statistics

A healthy funnel over six months looks something like this:

| Stage | Count | Pass rate | Hours |
|:--|--:|--:|--:|
| Queued | 60 | — | 5 |
| Kill-tested | 20 | ~30% pass | 10 |
| Triaged | 6 | ~50% pass | 18 |
| Deep dives | 3 | ~1 in 3 bought | 150 |
| Positions | 1–2 | | |

The pass rates are diagnostics, not targets:

- **Kill-test pass rate near 100%:** the disqualifiers are not being applied, or the queue is already too filtered.
- **Every deep dive ends in a buy:** stage 3 has become confirmation. The three weeks feel like an investment that
  has to pay.
- **Every deep dive ends in a pass:** the triage gate is too loose. Stage 2 is not doing its job, and expensive time
  is being wasted.

Count your own. The first year's funnel is data about you.

---

## 3. The evidence hierarchy

Not all evidence is equal. For each claim in a case file, note which class it comes from:

| Rank | Class | Examples | Watch for |
|--:|:--|:--|:--|
| 1 | **Audited primary documents** | Annual report notes, auditor's report, cash-flow statement | Read the notes, not the highlights |
| 2 | **Regulatory and third-party data** | Exchange filings, shareholding patterns, rating rationales, MCA filings, industry data (SIAM, CEA, IBEF) | Definitions change; check the basis |
| 3 | **Primary research** | Dealer, customer, supplier and ex-employee conversations; product checks; site visits | Small samples; the people most willing to talk are unrepresentative |
| 4 | **Management's statements** | Earnings calls, presentations, interviews | Test against the say-do record before relying on them |
| 5 | **Sell-side and media** | Broker reports, news | Useful for consensus, weak as evidence; know the incentives |

A variant perception built on class 4–5 evidence is not a variant perception; it is someone else's view. The
strongest cases combine class 1 (the numbers say X) with class 3 (the channel confirms X before the numbers do).

---

## 4. Calibration: scoring your probabilities

Every case contains probabilities: scenario weights, the confidence in the journal, "70% likely by Q3". Most
people never check them. Traders will know the tool from forecasting: the **Brier score**,

$$\text{BS} = \frac{1}{N}\sum_{i=1}^{N}(p_i - o_i)^2$$

where $p_i$ is the probability you gave and $o_i$ is 1 if the event happened and 0 if not. Zero is perfect.
Always saying 50% scores 0.25.

Worked example — five dated forecasts from a casebook:

| Forecast | p | Happened? | (p − o)² |
|:--|--:|:-:|--:|
| Receivable days below 85 by March | 0.70 | 1 | 0.09 |
| FY guidance met | 0.70 | 0 | 0.49 |
| Pledge not increased within a year | 0.90 | 1 | 0.01 |
| Order-book growth above 20% | 0.60 | 1 | 0.16 |
| Rating downgrade within a year | 0.30 | 0 | 0.09 |
| **Brier score** | | | **0.168** |

With fifty or more forecasts, bucket them (all the ~70% calls together) and compare the hit rate with the
probability. If your 70% calls come true 50% of the time, you are overconfident, and your position sizes should
shrink until the record says otherwise. [15.4](04-grading-rubric-and-review.md) turns this into an annual review.

For a forecast to be scored, it has to be written so that it *can* be: a threshold, a date and a source.
"Receivables should improve" cannot be scored. "Receivable days below 85 in the 31-March balance sheet" can.

---

## 5. Record-keeping rules

1. **Date and source everything.** Every number in a case file carries a date and a source. For prices, write the
   date and the close.
2. **Append, never rewrite.** A past decision stays as it was written. If the view changes, write a new dated entry
   explaining why. A casebook that has been edited in hindsight is worthless as a record.
3. **Commit at each stage.** In git, one commit per stage per case ("KAVERIPMP: kill test — TRIAGE"). The history
   becomes an audit trail of what you knew when.
4. **Keep the kills.** A one-line kill with its reason is data. After a year, check whether the killed ideas did
   better or worse than the ones you bought.
5. **Keep the model with the memo.** The scenario values in the memo must be reproducible from the model version
   committed alongside it.

!!! note "Using AI tools in the casebook"
    AI assistants are useful for extracting tables from PDFs, summarising call transcripts, checking arithmetic and
    red-teaming a thesis ([15.4](04-grading-rubric-and-review.md) has a protocol). They are not a source of
    evidence. Verify every number they produce against the primary document. Do not let them write the variant
    perception, which is the part the whole exercise exists to train. Keep private positions out of tools that
    retain or share data.

---

## Key terms

| Term | Meaning |
|:--|:--|
| **Stage gate** | A checkpoint with one question that can end the research |
| **Kill test** | A 30-minute screen against fixed disqualifiers |
| **Triage** | A 3-hour read to find a variant perception, or fail to |
| **Funnel statistics** | Pass rates between stages; a diagnostic of your filters |
| **Evidence hierarchy** | Ranking of evidence by reliability: audited documents first, media last |
| **Brier score** | Mean squared error of probabilistic forecasts; 0 is perfect, 0.25 is always-50% |
| **Calibration** | Agreement between the probabilities you state and the frequencies that follow |
| **Append-only record** | A casebook in which past decisions are never edited, only followed by new dated entries |

## Check your understanding

1. You have done nine deep dives this year and bought all nine. What does that suggest, and what would you change?
<details><summary>Answer</summary>Stage 3 has turned into confirmation: the effort already spent makes "buy" feel
owed. Tighten the stage-2 gate, so that fewer ideas reach stage 3 without a clear variant perception. Add a
pre-committed "reasons to pass" section to the deep dive. Have someone red-team each case before the decision.</details>

2. Write "the company's margins should recover" as a forecast that can be scored.
<details><summary>Answer</summary>For example: "EBITDA margin at or above 14.5% in the FY27 audited accounts
(published by July 2027): 40%." It has a threshold, a date, a source and a probability.</details>

3. Your 80% forecasts have come true 11 times out of 20. What does that imply for position sizing?
<details><summary>Answer</summary>A 55% hit rate on 80% calls means you are overconfident. The Kelly inputs
(scenario probabilities) are too extreme, so sizes are too large. Shrink the probabilities towards the base rate,
or cut fractional Kelly further (quarter to eighth), until calibration improves.</details>

4. Why keep a post-mortem on a stock you passed on?
<details><summary>Answer</summary>It tests the filters. If the killed and passed ideas regularly beat the ones you
bought, the kill test or the triage gate is rejecting the wrong things. Without the record you cannot tell, because
the missed winners are otherwise invisible.</details>

## Go deeper

- Philip Tetlock and Dan Gardner, *Superforecasting* — calibration, Brier scores and how good forecasters update.
- Annie Duke, *Thinking in Bets* — separating decision quality from outcome quality.
- Michael Mauboussin, "The Base Rate Book" (Credit Suisse, 2016) — base rates for growth and returns, to anchor
  scenario probabilities.
- The casebook's `PROCESS.md` and `templates/`, described in [15.2](02-templates.md).

---
[← Module index](index.md) · [Next: 15.2 Templates →](02-templates.md)
