# 11.6 · Behavioural finance & decision journals

> **Why this matters:** every technique in this course is executed by a brain that anchors on the first number
> it sees, seeks evidence for what it already believes, feels losses twice as strongly as gains, and tells itself
> stories. The biases are not ignorance — the best-informed analysts have them — and they cannot be removed by
> knowing about them. They can be *contained* by process: base rates, checklists, pre-mortems, decision journals
> that separate the quality of a decision from the quality of its outcome. This lesson is that toolkit.

**Learning objectives** — after this lesson you can:

- Recognise the biases that matter most for fundamental investors and the specific decisions each corrupts.
- Use base rates and the outside view to discipline forecasts.
- Separate process from outcome and grade decisions accordingly.
- Keep a decision journal and use pre-mortems and checklists as debiasing tools.

**Prerequisites:** [11.3](03-writing-an-investment-memo.md), [11.5](05-monitoring-and-selling.md)  ·  **Time:** ~60 min

---

## 1. The biases that matter, and where they bite

| Bias | What it does | Where it corrupts the process | Containment |
|:--|:--|:--|:--|
| **Confirmation** | Seek and weight evidence that supports the existing view | Reading the annual report after forming a view; scuttlebutt with leading questions; ignoring the bear case | Write "what the market believes" first; the pre-mortem; assign someone (or yourself, formally) to argue the short case; log expected vs found |
| **Anchoring** | Cling to the first number (the price, last year's growth, the sell-side target) | Valuation drifting toward the price; guidance taken as the base case | Build the value before looking at the price; reverse DCF as the *only* use of price; scenario values before probabilities |
| **Narrative fallacy** | Prefer stories to statistics; a coherent story feels true | "India's irrigation potential" doing the work of numbers; management's story on the call | Every claim gets a number and a source; the say-do table |
| **Overconfidence** | Ranges too narrow; probabilities too extreme | Point-estimate valuations; 80/10/10 scenario weights | Sensitivity grids; Monte Carlo; calibration tracking of your own forecasts |
| **Recency / extrapolation** | Weight the last data point; extend trends | Peak-cycle margins as normal; FY23–26 growth as the future | 10-year histories; mean reversion; the capital cycle |
| **Loss aversion & the disposition effect** | Losses hurt ~2× gains; sell winners, hold losers | Holding broken theses; trimming winners too early | Thesis-breakers as stops on facts; re-underwriting; cost basis banned from the review |
| **Sunk cost** | Weight past effort or past price | Averaging down because "I've done the work"; holding at a loss | The re-underwrite question; a kill log that celebrates kills |
| **Commitment / consistency** | Public positions harden | Defending a memo after the facts change | Date and freeze memos; write updates as new documents; reward changed minds |
| **Social proof / herding** | Follow others, especially in groups and bull markets | Buying because a famous investor holds it; sector fads (defence, EV, solar) | Own thesis or no position; the "why now / why me" test |
| **Availability** | Judge probability by ease of recall | Over-weighting the last fraud or the last multibagger | Base rates |
| **Authority** | Management, brokers, famous investors | Guidance taken as fact; sell-side targets as anchors | Say-do tracking; reports read last |
| **Hindsight** | "I knew it" | Post-mortems that flatter; case studies read backwards | Contemporaneous journals; the "knowable then" discipline of [Module 13](../13-case-studies/index.md) |

Two meta-points. First, biases compound: anchoring on the price plus confirmation from the story plus
authority from management produces a memo that agrees with the market and recommends buying anyway. Second, the
antidotes are *structural*, not willpower — the order in which you read documents, the templates you fill, the
journal you keep.

## 2. Base rates and the outside view

Daniel Kahneman's distinction: the **inside view** builds a forecast from the specifics of the case ("this
management, this product, this market"); the **outside view** asks what happened to the reference class ("what
share of Indian mid-caps that grew 15% for three years grew 15% for the next ten?"). The inside view is almost
always too optimistic; the outside view anchors it.

| Forecast | Inside view | Outside view (reference class; verify with data) |
|:--|:--|:--|
| Kaveri grows 14% for 10 years | Solar opportunity, motors ramp, dealer network | Of companies with ₹1,000–2,000 Cr revenue growing 12–16% over the prior three years, perhaps a quarter sustain double digits for a decade; the median fades to mid-single digits by year 6–8 (Mauboussin's US base rates; Indian data are thinner but similar in shape) |
| A turnaround under new management works | Credible CEO, clear plan | Most announced turnarounds do not restore prior margins within three years |
| An acquisition creates value | Synergies, strategic fit | The majority of acquisitions do not earn their cost of capital |
| A new entrant fails to dent the leader | Distribution, brand, decades of loyalty | Well-funded entrants with a distribution base usually take 5–15% share within three years (paints, 2024–26) |
| A stock down 60% on a governance event recovers | The business is intact | Rarely to prior highs; often to zero |

Method: name the reference class; find the distribution of outcomes (Mauboussin's *Base Rate Book* for US
companies; build your own from Screener exports for India); place your inside-view forecast within it; adjust
toward the base rate unless you can articulate why this case is different — and then adjust only partly.

## 3. Process vs outcome

| | Good outcome | Bad outcome |
|:--|:--|:--|
| **Good process** | Deserved success | Bad luck — the decision was right |
| **Bad process** | Dumb luck — dangerous, because it teaches the wrong lesson | Deserved failure |

Over any short period, outcomes are dominated by luck; over years, by process. The only thing you control is the
process, so it is the only thing worth grading. A position that loses 30% because a state agency defaulted, after
a memo that named that risk, priced it, sized for it and set a breaker that fired — is a *good* decision. A
position that doubles after a memo with no variant perception and no breakers is a *bad* decision that got paid.
Grade them that way in the journal, and over fifty decisions the grades, not the P&L, tell you whether you are
getting better.

## 4. The decision journal

For every buy, add, trim, sell and deliberate hold-through-a-breaker, one dated entry (casebook
`04-decision-journal.md`):

| Field | Why |
|:--|:--|
| Decision, size, price | The record |
| What I believe; what the market believes; why the market is wrong | The thesis, frozen |
| What I expect to see, by when, and how I'll know | Falsifiable predictions — the calibration record |
| What would reverse the decision | Pre-committed exit |
| Confidence (0–100%) | Calibration: over time, do 70%-confidence calls come true ~70% of the time? |
| Mood / context (honest) | To catch decisions made angry, euphoric, tired, or after a loss |
| Pre-mortem (one line) | The failure story |

Review: at each quarterly update and at exit, re-read the entry *before* looking at the result; grade process
(0–5) and outcome (0–5) separately; note what you would do differently. After 30–50 entries, tabulate:
calibration (confidence vs hit rate), which sources produced good decisions, which biases recur in your own
entries (they will).

## 5. Checklists and pre-mortems

- **Checklists** (Gawande; Pabrai's investing checklist) convert known failure modes into questions that must be
  answered before acting. The course's are the kill test, the forensic checklist ([09.7](../09-forensics/07-the-forensic-checklist.md)),
  the governance checklist ([05.6](../05-business-analysis/06-corporate-governance-india.md)), the model QA list
  ([10.4](../10-modeling/04-scenarios-sensitivities-qa.md)) and the memo structure ([11.3](03-writing-an-investment-memo.md)).
  Their power is that they are run *every time*, including when the idea is obviously good — especially then.
- **Pre-mortems** (Klein): before committing, write the story of how it failed, from the future, in detail. It
  surfaces risks the memo's risk list missed because the format asks a different question ("how did it happen?"
  rather than "what could happen?") and it licenses dissent — including your own.
- **Red team**: argue the opposite case in writing, as strongly as you can, before the decision; the casebook's
  case template has a section for it. If you cannot write a convincing short case, you have not understood the
  bull case either.

!!! tip "Trader's lens"
    Traders have an advantage here: the P&L teaches fast, positions are marked daily, and most desks already grade
    process (risk limits honoured? size right? edge real?) separately from outcome. The difference in fundamental
    investing is the feedback delay — years, not hours — which is exactly why the journal has to be *written*:
    memory rewrites the reasons once the outcome is known. Treat the journal as the trade blotter of a slow desk.

!!! info "India notes"
    Indian markets add specific behavioural traps: the promoter narrative (charismatic founders on calls and in
    the press), the retail momentum of 2020–24 in small caps and IPOs (social proof at scale), "multibagger"
    culture (availability and survivorship), and the tendency to treat cheapness in PSUs and cyclicals as safety
    (anchoring on low P/E). The base-rate discipline is the answer to all four.

!!! warning "Common mistakes"
    - Believing that knowing the biases prevents them.
    - Journals written after the outcome.
    - Grading decisions by P&L.
    - Confidence levels never checked against results.
    - Skipping the checklist when the idea feels certain.

## Key terms

| Term | Meaning |
|:--|:--|
| **Confirmation bias** | Seeking and over-weighting evidence that supports an existing belief |
| **Anchoring** | Over-reliance on an initial reference number |
| **Narrative fallacy** | Preferring coherent stories to statistical evidence |
| **Disposition effect** | Selling winners too early and holding losers too long |
| **Sunk-cost fallacy** | Letting past costs or effort influence a forward-looking decision |
| **Base rate / outside view** | The distribution of outcomes for a reference class, used to anchor a forecast |
| **Calibration** | The match between stated confidence and realised frequency |
| **Process vs outcome** | Judging decisions by their quality at the time, not by their result |
| **Decision journal** | Contemporaneous record of a decision's reasoning, predictions and confidence |
| **Pre-mortem** | A failure narrative written before the decision |
| **Red team** | A deliberate argument for the opposite conclusion |

## Check your understanding

1. You read the Kaveri chairman's letter first, then the notes. Which bias is at work and what is the fix?
<details><summary>Answer</summary>Anchoring and narrative: the letter's story frames how the notes are read (the
receivables become "temporary" before the ageing schedule is seen). Fix: read the auditor's report and notes
first; the letter last ([11.2](02-the-research-process.md)).</details>

2. A position bought with a full memo and a 3% max-loss size fell 40% when the bear case materialised, and the
   breaker fired; you sold. Grade the decision.
<details><summary>Answer</summary>Process: good (thesis, sizing, breaker, execution). Outcome: bad. It is a
"bad luck" cell — unless the memo's bear probability was unreasonably low, in which case the process error was
in the probability, and that is the lesson.</details>

3. Your journal shows that decisions logged at 80% confidence came true 55% of the time. What do you do?
<details><summary>Answer</summary>You are overconfident by ~25 pp; widen ranges, shrink probabilities toward
50%, and size smaller until calibration improves. Track by decision type — the miscalibration may be
concentrated (e.g., in growth forecasts).</details>

4. Why is a pre-mortem more useful than a risk list for finding correlated failures?
<details><summary>Answer</summary>A risk list enumerates independent items; a pre-mortem narrates a sequence, which
naturally links them (receivables dispute → provisions → covenant pressure → promoter pledge → auditor caution)
— the chain is the real bear case, and only a story reveals it.</details>

## Go deeper

- Daniel Kahneman, *Thinking, Fast and Slow* (2011), chapters on the outside view and the planning fallacy.
- Michael Mauboussin, *The Success Equation* (2012) and *The Base Rate Book* (Credit Suisse, 2016).
- Annie Duke, *Thinking in Bets* (2018) — process vs outcome, "resulting".
- Atul Gawande, *The Checklist Manifesto* (2009); Gary Klein, "Performing a Project Premortem" (HBR, 2007).
- Mohnish Pabrai's investing checklist (various talks) — an example of a personal checklist built from
  post-mortems.

---
[← Previous: 11.5 Monitoring & selling](05-monitoring-and-selling.md) · [Module index](index.md) · [Next: 11.7 Fundamentals × derivatives →](07-fundamentals-meets-derivatives.md)
