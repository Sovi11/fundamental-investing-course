# 15.4 · Grading rubric & review

> **Why this matters:** without feedback, practice only makes the habits you already have permanent. The capstone
> has no answer key, so the feedback has to be built. There are three layers: a rubric that scores each case file
> as it is written, a red-team review before any decision, and an annual review that scores your judgement against
> what actually happened. Only the last one grades outcomes, and it does so over enough decisions that luck starts
> to wash out.

**Learning objectives** — after this lesson you can:

- Score a case file on the eight-criterion rubric and know what "professional" looks like on each.
- Run a red-team review with a peer or an AI assistant, and use it to attack the case rather than to be reassured.
- Run the annual process review: calibration, hit rates by idea type, funnel statistics, sizing discipline and the
  behavioural log.
- Turn the review into one to three process changes, recorded in the casebook's `PROCESS.md`.

**Prerequisites:** [15.1](01-the-case-study-method.md)–[15.3](03-worked-example-kaveri.md),
[stock-pitch rubric](../14-mocks/06-stock-pitch-mock.md#rubric)  ·  **Time:** ~45 min

---

## 1. The case-file rubric

Score each completed case file (stages 1–4) from 1 to 5 on each criterion, and multiply by the weight. The
descriptors build on the [pitch rubric](../14-mocks/06-stock-pitch-mock.md#rubric), shifted towards the written
record.

| # | Criterion | Weight | 1 — weak | 3 — competent | 5 — professional |
|--:|:--|--:|:--|:--|:--|
| 1 | **Process followed** | 2 | Stages skipped; no gate decisions recorded | All stages present | Each gate decision written down with its reason, including the ones that nearly stopped the case |
| 2 | **Evidence** | 3 | Mostly management and media | Primary documents for every key number | Primary documents plus primary research; each claim tagged with its evidence class ([15.1 §3](01-the-case-study-method.md#3-the-evidence-hierarchy)) |
| 3 | **Business and returns** | 2 | Adjectives | ROIC history and a moat argument | Incremental returns, unit economics by segment, how the moat is changing |
| 4 | **Forensics and governance** | 2 | Not run | Checklist scored | Checklist scored, adjustments carried into the model, RAG rating justified, escalation triggers written |
| 5 | **Valuation** | 3 | One number | Scenarios and a cross-check | Method suited to the business; reverse DCF; scenario tree tied to drivers; sensitivities on the one or two drivers that matter |
| 6 | **Variant perception** | 3 | None, or "it's cheap" | Stated | Precise, with its evidence class and the specific evidence that would refute it |
| 7 | **Scoreable forecasts and breakers** | 3 | None | Thesis-breakers listed | A forecast register: thresholds, dates, sources, probabilities; breakers that were acted on when they fired |
| 8 | **Decision and sizing** | 2 | No decision, or a size from nowhere | Decision and size | Size derived from the course rules, with overlays and liquidity checked; journal entry written *before* the order |

Maximum 100 (weights sum to 20; ×5). **70 is the bar for acting on a case.** A case below 70 is not finished,
whatever the stock is doing.

Kaveri, scored ([15.3](03-worked-example-kaveri.md)):

| # | Criterion | Score | Points | Why |
|--:|:--|--:|--:|:--|
| 1 | Process | 5 | 10 | Gates recorded, including the partial triage failure |
| 2 | Evidence | 4 | 12 | Primary documents throughout; the scuttlebutt is thin (three checks) |
| 3 | Business | 4 | 8 | Segment economics and incremental ROIC; little on the industrial segment |
| 4 | Forensics | 5 | 10 | Scored, adjusted and carried into the weights, with escalation triggers |
| 5 | Valuation | 4 | 12 | Full tree and reverse DCF; no independent check of the terminal RONIC |
| 6 | Variant | 5 | 15 | Precise, with the refuting evidence stated |
| 7 | Forecasts | 5 | 15 | Six dated, sourced, probabilistic forecasts |
| 8 | Decision | 4 | 8 | Trigger sizing derived; liquidity left "to be checked" |
| | **Total** | | **90** | |

---

## 2. The red-team review

Before any decision to buy, and ideally before a decision to pass, give the case file to someone whose job is to
break it. A study partner is best. An AI assistant is a useful second, if it is used for attack rather than
agreement.

**Protocol (60–90 minutes):**

1. **Give the reviewer the case file, the model and the thesis — not your conclusion first.** Ask them to write the
   recommendation *they* would make from the evidence before reading yours.
2. **Steelman the other side.** The reviewer writes the strongest one-paragraph case for the opposite action. You
   must answer it in writing, with evidence, or concede it.
3. **Attack the three weakest numbers.** Which inputs, if wrong by a plausible amount, flip the decision? Each gets
   a sensitivity and a source check.
4. **Check the numbers.** The reviewer traces ten random numbers in the case file back to their stated sources. One
   error means the whole file is re-checked.
5. **Independent pre-mortem.** The reviewer writes their own "it is three years later and this failed", without
   seeing yours. Compare the two: what did they see that you did not?
6. **Record the outcome.** Add a "red-team" section to the case file listing what changed: probabilities,
   breakers, size, or nothing, and why.

**Using an AI assistant as the red team.** Useful prompts:

- "Here is my case file. Argue for the opposite recommendation, using only evidence in the file or in public filings
  you can cite."
- "List the five claims in this memo that rest on management statements rather than audited numbers."
- "Which of my thesis-breakers could not actually be observed by the date I gave, and why?"

The rules: verify every factual claim it makes against the primary source. Treat its arguments as prompts for your
own checking, not as evidence. Never let it change a probability without a reason you can state yourself.

---

## 3. The annual process review

Once a year, in a fixed week (after the annual-report season, say September), spend a day on the casebook itself.
Outcomes are graded here, in aggregate, and only here.

### 3.1 Calibration

Pool every resolved forecast from the forecast registers. Compute the Brier score, then bucket the forecasts:

| Stated probability | Forecasts | Came true | Hit rate | Reading |
|:--|--:|--:|--:|:--|
| 50–59% | 12 | 7 | 58% | Calibrated |
| 60–69% | 18 | 10 | 56% | Slightly overconfident |
| 70–79% | 15 | 8 | 53% | **Overconfident** |
| 80–89% | 6 | 5 | 83% | Calibrated (small sample) |
| **All** | **51** | | | Brier 0.23 (always-50% = 0.25) |

*(Illustrative numbers.)* A reading like this says the analyst's "70%" means about 55%. The fix is mechanical:
shrink stated probabilities towards 50% until the buckets line up. Because Kelly sizes on those probabilities, cut
the Kelly fraction too, until the record improves.

### 3.2 Hit rates by type of idea

| Split | Why it matters |
|:--|:--|
| By mispricing reason (neglect, complexity, forced selling, trough, misunderstanding) | Shows which *kind* of edge you actually have |
| By stage-1 source (screen, reading, special-situation calendar, conversation) | Shows where to spend idea-generation time |
| Positions against passes against kills, each measured against the Nifty 500 over the same period | Tests the filters: if kills beat buys, the kill test is killing the wrong things |
| By forensic rating at entry (Green/Amber) | Shows whether Amber cases earned their discount |

With a first-year sample of a handful of positions, these are hypotheses, not conclusions. Keep the table anyway;
year three is when it starts to speak.

### 3.3 Funnel and time

Pass rates between stages, and hours per stage, against the healthy funnel in
[15.1 §2](01-the-case-study-method.md#2-the-funnel-and-its-statistics). Two warning signs: every deep dive ending
in a buy, and monitoring hours falling to zero on positions that are doing well.

### 3.4 Sizing and behaviour

- **Sizing discipline.** Did any position exceed its rule-derived size, at entry or through drift? Did any fall
  below its trigger conditions and stay held?
- **Breaker discipline.** For every thesis-breaker that fired, what was done, and how long did it take?
- **The mood log.** Read the journal's mood fields next to the outcomes. Common findings are decisions taken
  "irritated" or "euphoric" doing worse, and adds made after a big up day. The field exists to find these patterns
  ([11.6](../11-process/06-behavioural-finance-and-decision-journals.md)).

### 3.5 Output: process changes

The review ends with one to three changes to `PROCESS.md`, each with:

- the evidence behind it;
- the date;
- a test that will show next year whether it worked.

The changelog at the bottom of `PROCESS.md` becomes the history of how your process learned. Example:

> **2027-09-20.** Kill-test disqualifier added: *receivable days up by more than 20 in two years, with the KPI
> withdrawn*. Evidence: two of three Amber cases with this pattern underperformed; the pattern was visible at kill
> test. Test: Amber cases admitted in FY28 underperform less.

---

## 4. When is the course finished?

When the capstone checklist in the [module index](index.md) is done: twenty kill tests, three full cases, forecasts
that have started to resolve, and one process change made because a post-mortem demanded it. After that there is
no course left, only the practice. The casebook is where it continues.

---

## Key terms

| Term | Meaning |
|:--|:--|
| **Case-file rubric** | Eight weighted criteria scoring the written case; 70 is the bar for acting |
| **Red team** | A reviewer, human or AI, whose job is to break the case before a decision |
| **Steelman** | The strongest version of the opposing argument |
| **Calibration buckets** | Forecasts grouped by stated probability, with the hit rate compared to the probability |
| **Process changelog** | Dated record in `PROCESS.md` of each rule change, its evidence and its test |

## Check your understanding

1. Your case file scores 64 on the rubric, and the stock has risen 12% since you started. What do you do?
<details><summary>Answer</summary>Finish the case. The rubric bar is about the quality of the decision, not the
price. A 64 means a criterion — usually evidence, variant perception or scoreable breakers — is not good enough to
act on. The price move is the market's information, not yours. Record the temptation in the journal's mood field.</details>

2. After a year, your 80% forecasts came true 5 times out of 6. Are you well calibrated?
<details><summary>Answer</summary>Possibly, but six forecasts cannot tell you. The sampling error on 6 trials is
huge; a true 60% forecaster gets 5 of 6 about 19% of the time. Keep pooling. Calibration needs dozens of forecasts
per bucket before it says much, which is why every case should produce several scoreable forecasts.</details>

3. An AI reviewer says your company's main customer "is known to be in financial difficulty". What do you do with
   that?
<details><summary>Answer</summary>Treat it as a lead, not evidence. Find the primary source (the customer's filings,
a rating action, court records) or discard the claim. If it holds up, it goes into the case file with that source;
if it cannot be traced, it goes nowhere.</details>

## Go deeper

- Philip Tetlock and Dan Gardner, *Superforecasting* — calibration training and the Brier score.
- Gary Klein, "Performing a Project Premortem", *Harvard Business Review* (2007).
- Annie Duke, *How to Decide* — decision reviews that separate process from luck.

---
[← Previous: 15.3 Worked example — Kaveri](03-worked-example-kaveri.md) · [Module index](index.md) · [Appendix: Glossary →](../appendix/glossary.md)
