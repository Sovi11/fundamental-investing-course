# 15.2 · Templates

> **Why this matters:** a template is a checklist that looks like a document. It makes sure the same questions are
> asked of every company, so that cases can be compared with each other and with their outcomes. It also makes it
> obvious when a question has been skipped. The templates below are the ones in the casebook's `templates/`
> folder, reproduced here so you can see them without cloning the private repository.

**Learning objectives** — after this lesson you can:

- Say which template belongs to which stage of the [case-study method](01-the-case-study-method.md), and what each
  field is for.
- Fill a field well rather than just filling it, using the example lines given for each template.
- Scaffold a new case in the casebook with one command.

**Prerequisites:** [15.1 The case-study method](01-the-case-study-method.md)  ·  **Time:** ~45 min

---

## 1. The set

| Stage | Template | File in the casebook | Worked on Kaveri in |
|:--|:--|:--|:--|
| 1 | Kill test | `templates/00-kill-test.md` | [15.3 §2](03-worked-example-kaveri.md#2-stage-1-kill-test) |
| 2–3 | Full case study | `templates/01-full-case-study.md` | [15.3 §3–4](03-worked-example-kaveri.md#3-stage-2-triage) |
| 3 | Forensic checklist (40 tests) | `templates/06-forensic-checklist.md` | [09.7](../09-forensics/07-the-forensic-checklist.md) |
| 4 | One-page thesis | `templates/02-one-page-thesis.md` | [15.3 §5](03-worked-example-kaveri.md#5-stage-4-memo-sizing-and-the-journal) |
| 4 | Decision journal | `templates/04-decision-journal.md` | [15.3 §5](03-worked-example-kaveri.md#5-stage-4-memo-sizing-and-the-journal) |
| 5 | Quarterly update | `templates/03-quarterly-update.md` | [15.3 §6](03-worked-example-kaveri.md#6-stage-5-a-quarterly-update) |
| 6 | Post-mortem | `templates/05-post-mortem.md` | [15.3 §7](03-worked-example-kaveri.md#7-stage-6-the-post-mortem) |

To start a case, run this from the casebook root:

```bash
python tools/new_case.py GENUSPOWER.NS "Genus Power Infrastructures"
```

It creates `cases/GENUSPOWER.NS/` from the templates, filled with the company name, ticker and date. Then pull the
data with `python tools/pull.py GENUSPOWER.NS`, which prints the ratio dashboard and forensic quick scores that the
kill test asks for.

---

## 2. Stage 1 — kill test

Thirty minutes, six boxes, one verdict. The discipline is in box 6: you must tick a *reason for mispricing*.
"None obvious" is a legitimate answer, and it usually means KILL.

| Field | Filled badly | Filled well |
|:--|:--|:--|
| Business in three sentences | "Leading pump maker with strong brand" | "Makes agricultural and industrial pumps and motors, sold through 1,800 dealers in 14 states; since FY23 also sells solar pumping systems to state agencies under PM-KUSUM, now 27% of revenue." |
| Why mispriced | "Undervalued" | "Misunderstanding: the market capitalises tender-driven solar growth at an agri-franchise multiple." |
| Verdict | "Looks interesting" | "TRIAGE — the one question: is the solar growth creating or destroying value, given 96 receivable days?" |


??? example "Kill test — `templates/00-kill-test.md`"

    ````markdown
    # Kill test — {{COMPANY}} ({{TICKER}})

    Date: {{DATE}} · Price: ₹ · Market cap: ₹ Cr · Source: Screener.in + `tools/pull.py`

    ## 1. The business in three sentences

    1.
    2.
    3.

    ## 2. Numbers (5 years)

    | Metric | Value | Comment |
    |:--|--:|:--|
    | Revenue CAGR (5y) | | |
    | EBITDA margin (range) | | |
    | ROCE (range) | | |
    | CFO / PAT (avg) | | |
    | Net debt / EBITDA | | |
    | Receivable days (trend) | | |
    | Dilution (share count 5y) | | |

    ## 3. People

    | Check | Finding |
    |:--|:--|
    | Promoter holding & 3-year trend | |
    | Pledge (% of promoter holding) | |
    | Auditor changes / resignations (5y) | |
    | SEBI / regulatory actions | |
    | Related-party transactions (% of revenue or cost) | |
    | Promoter remuneration (% of PAT) | |

    ## 4. Forensic quick scores (from `tools/pull.py`)

    | Score | Value | Threshold | Flag? |
    |:--|--:|--:|:--|
    | Beneish M (8-var) | | > −1.78 | |
    | Piotroski F | | < 4 | |
    | Accruals ratio | | > 10% | |
    | Implied yield on cash | | < 3% with high cash | |

    ## 5. Valuation snapshot

    | Multiple | Now | 5y median | Peers (3) |
    |:--|--:|--:|--:|
    | P/E (TTM) | | | |
    | EV/EBITDA | | | |
    | P/B | | | |

    ## 6. Why might it be mispriced?

    - [ ] Neglect / low coverage   - [ ] Complexity   - [ ] Forced selling   - [ ] Cyclical trough
    - [ ] Misunderstanding of the business   - [ ] None obvious

    ## Verdict

    - [ ] **KILL** — reason:
    - [ ] **TRIAGE** — the one question triage must answer:
    ````


---

## 3. Stages 2–3 — the full case study

This file starts as the triage section and grows into the complete study. Its sections follow the course's
modules, so each one has a lesson behind it. The two sections most often skimped are:

- **section 3 (reading the filings)**, where the notes and the say-do table live;
- **section 5 (scuttlebutt)**, the only evidence the market may not already have.


??? example "Full case study — `templates/01-full-case-study.md`"

    ````markdown
    # {{COMPANY}} ({{TICKER}}) — full case study

    Started: {{DATE}} · Analyst: Pravar · Status: triage / deep dive / memo / monitoring / closed

    > One-paragraph summary of the situation and the question this study answers.

    ## 0. Sources used

    | Document | Date | Link / path | Notes |
    |:--|:--|:--|:--|
    | Annual report FY | | | |
    | Concall transcripts (Q… to Q…) | | | |
    | Credit-rating rationale | | | |
    | DRHP / offer documents (if any) | | | |
    | Regulator / industry data | | | |

    ## 1. Business (Module 05)

    - What it sells, to whom, how it makes money; unit economics.
    - Segment table (revenue, margin, growth, share of profit).
    - Value chain position; customer and supplier concentration.
    - Industry structure (five forces summary), capital cycle stage, regulation.
    - Moat: source, evidence in the numbers (ROIC > WACC for how long? pricing power? share trend?), erosion risks.

    ## 2. History and numbers (Module 04)

    Paste the ratio dashboard from `tools/pull.py` (10 years where available).

    | Metric | Y-9 | … | Y-1 | Y0 | Comment |
    |:--|--:|--:|--:|--:|:--|

    - Growth decomposition (volume × price × mix; organic vs acquired).
    - Margin structure and operating leverage.
    - Returns on capital (DuPont; incremental ROIC over 3/5 years).
    - Working capital and cash conversion (CCC trend; CFO/EBITDA; FCF).
    - Leverage, liquidity, maturity profile, off-balance-sheet items.
    - Quality of earnings scorecard.

    ## 3. Reading the filings (Module 03)

    - Auditor's report: opinion type, KAMs, EoM, CARO remarks.
    - Notes that matter: related parties, contingent liabilities, borrowings & covenants, receivables ageing, CWIP ageing,
      revenue policy changes, exceptional items, tax reconciliation.
    - Concall themes over 8 quarters; say-do table.

    | Quarter | Guidance / claim | Delivered | Score |
    |:--|:--|:--|:--|

    ## 4. Forensics and governance (Modules 05.6, 09)

    - Forensic checklist score (attach `forensic-checklist.md`): overall RAG and the top three items.
    - Governance checklist: board, auditor, RPTs, pledges, remuneration, capital-raising history, group structure.
    - Standalone vs consolidated cash; loans to subsidiaries/related parties.

    ## 5. Scuttlebutt and data checks (Module 05.7)

    | Date | Source (type, no names needed) | What I asked | What I learned | Confidence |
    |:--|:--|:--|:--|:--|

    Alternative data / government data checked:

    ## 6. Valuation (Modules 06–07)

    - Model: `model/` (three statements, base/bull/bear; assumptions table).
    - DCF summary: WACC, terminal growth, value/share by scenario, TV share of EV, sensitivity grid.
    - Multiples: vs own history bands and peer table.
    - **Reverse DCF:** the price implies … ; my base case is … ; the gap is explained by …
    - Probability-weighted value and payoff asymmetry (upside/downside ratio, expected value).

    ## 7. Thesis (Module 11)

    - **Variant perception** (one sentence).
    - Thesis in three bullets.
    - Catalysts with expected timing.
    - Key risks; pre-mortem ("it is 2029 and this lost 50% — why?").
    - **Thesis-breakers** (specific, observable, dated).

    ## 8. Decision

    - Action, size (quarter-Kelly vs max-loss → lower; forensic overlay; liquidity check), entry plan, monitoring KPIs and schedule.
    - Journal entry: `journal/{{DATE}}-{{TICKER}}.md`.

    ## 9. Updates

    Quarterly updates live in `updates/`. Log of material changes to the thesis:

    | Date | Change | Action |
    |:--|:--|:--|
    ````


Section 4 attaches the forensic checklist: the 40-test sheet from [09.7](../09-forensics/07-the-forensic-checklist.md),
with the same thresholds and RAG bands:

- **Green:** 12 or less, with no 3s and at most two 2s;
- **Amber:** 13–30, with no 3s;
- **Red:** any 3, or over 30.

The template has blank score and note columns. The Kaveri copy in `cases/KAVERIPMP/` is fully scored, at 18
(Amber).

---

## 4. Stage 4 — one-page thesis and decision journal

The thesis is the memo of [11.3](../11-process/03-writing-an-investment-memo.md) compressed to one page. The
journal records the decision *and the state of mind it was taken in*, before the order is placed.

| Field | Filled badly | Filled well |
|:--|:--|:--|
| Thesis-breaker | "If fundamentals deteriorate" | "Receivable days at 30-Sep-2026 (H1 balance sheet, due Nov-2026) below 80, with > 6-month overdues falling" |
| Confidence | "High" | "65% that the price is within the base-case range (₹280–₹340) in two years" |
| Mood | (left blank) | "Irritated at missing the 2024 rally; watch for wanting to be 'in' something" |


??? example "One-page thesis — `templates/02-one-page-thesis.md`"

    ````markdown
    # {{COMPANY}} ({{TICKER}}) — one-page thesis

    Date: {{DATE}} · Price ₹ · Mcap ₹ Cr · Recommendation: BUY / WATCH / AVOID · Horizon: … · Size: …% of portfolio

    **What the market believes:** …

    **What I believe (variant perception):** …

    **Why I'm right (three bullets, each with a number):**
    1. …
    2. …
    3. …

    **Key numbers**

    | | FY-2 | FY-1 | FY0 | FY+1E | FY+2E |
    |:--|--:|--:|--:|--:|--:|
    | Revenue (₹ Cr) | | | | | |
    | EBITDA margin | | | | | |
    | PAT (₹ Cr) | | | | | |
    | ROCE | | | | | |
    | CFO / PAT | | | | | |
    | Net debt / EBITDA | | | | | |

    **Valuation:** base ₹… (method), bull ₹…, bear ₹…, probability-weighted ₹…; price implies … growth / … margin.
    Upside/downside ratio: …

    **Catalysts:** (1) … by …; (2) … by …

    **Thesis-breakers — I am wrong if:** (1) …; (2) …; (3) …

    **Monitoring:** KPIs …, sources …, cadence …

    **Pre-mortem (one line):** …

    **Position management:** entry plan …; add if …; trim if …; exit if …
    ````

??? example "Decision journal — `templates/04-decision-journal.md`"

    ````markdown
    # Decision — {{DATE}} — {{TICKER}} — {{ACTION}}

    **Decision:** buy / add / trim / sell / pass — … shares at ₹… (≈ ₹… , …% of portfolio)

    **What I believe:** (thesis in two lines)

    **What the market believes:** 

    **Why the market is wrong / why now:** 

    **What I expect to see, and by when:**

    | Expectation | By when | How I'll know |
    |:--|:--|:--|

    **What would make me reverse this decision:** 

    **Sizing logic:** quarter-Kelly … vs max-loss … → lower … → forensic overlay … → chosen …; liquidity check: ADV ₹… Cr, position = … days

    **Confidence (0–100):** …   **Mood / context (be honest):** …

    **Pre-mortem:** it is three years later and this went badly because …

    ---
    *Review this entry at the next quarterly update and at exit. Grade the process, not the outcome.*
    ````


---

## 5. Stage 5 — quarterly update

One hour, filled in *before* you read the broker notes or look at the price reaction. The thesis-breaker table
carries forward from the thesis unchanged. You may not rewrite a breaker because it fired.


??? example "Quarterly update — `templates/03-quarterly-update.md`"

    ````markdown
    # {{COMPANY}} ({{TICKER}}) — quarterly update {{QUARTER}}

    Date: {{DATE}} · Price ₹ · Position: …% · Cost ₹ · P&L since entry: …%

    ## Results vs expectations

    | Metric | Expected | Actual | Delta | Comment |
    |:--|--:|--:|--:|:--|
    | Revenue | | | | |
    | EBITDA / margin | | | | |
    | PAT | | | | |
    | KPI 1 | | | | |
    | KPI 2 | | | | |
    | Working capital / cash | | | | |

    ## Concall: what management said (and didn't)

    - Guidance change:
    - Say-do update (add a row to the case file):
    - Questions not answered / evasive answers:

    ## Thesis-breaker check

    | Breaker | Status (green/amber/red) | Evidence |
    |:--|:--|:--|

    ## Valuation now

    Price vs scenarios (bear ₹… / base ₹… / bull ₹…); what the price implies now.

    ## Action

    - [ ] Hold   - [ ] Add   - [ ] Trim   - [ ] Exit
    Why (two lines):
    Journal entry: `journal/{{DATE}}-{{TICKER}}.md` (only if action ≠ hold)
    ````


---

## 6. Stage 6 — post-mortem

Write it on exit, or three years after any decision, including decisions to pass. The key box is "one change to
the process". A post-mortem that changes nothing has only told a story.


??? example "Post-mortem — `templates/05-post-mortem.md`"

    ````markdown
    # Post-mortem — {{COMPANY}} ({{TICKER}})

    Entry: {{DATE}} at ₹… · Exit: … at ₹… · Holding period: … · Return: …% (vs Nifty 500 …%) · Peak/trough drawdown: …

    ## What I said would happen vs what happened

    | Expectation (from the journal) | Outcome | Right / wrong / partly |
    |:--|:--|:--|

    ## Which scenario played out, and why

    ## Was the result process or luck?

    - Process errors (analysis, sizing, timing, behaviour):
    - Bad/good luck (macro, unforecastable events):

    ## What was knowable at entry that I missed?

    ## One change to the process

    (The single filter, checklist item or rule that would have caught this earliest.)

    ## Lessons mapped to course modules

    | Lesson | Module |
    |:--|:--|
    ````


---

## Key terms

| Term | Meaning |
|:--|:--|
| **Template** | A fixed set of questions in document form, used for every case so that cases can be compared |
| **Scaffold** | The case folder created from the templates by `tools/new_case.py` |
| **Say-do table** | Guidance against delivery, quarter by quarter; lives in section 3 of the case study |
| **Thesis-breaker** | A dated, observable test that would falsify the thesis; carried unchanged into every update |

## Check your understanding

1. Which template do you open after a quarterly result, and what must you not do before filling it in?
<details><summary>Answer</summary>`03-quarterly-update.md`. Do not read the sell-side's take or look at the price
reaction first. Otherwise the update records the market's interpretation instead of testing your thesis.</details>

2. Rewrite "management seems competent" as a case-file entry that can be checked.
<details><summary>Answer</summary>A say-do row, for example: "May-2025: guided FY26 growth 15–18% and margin 15%+;
delivered 12.5% and 13.8% — miss on both." Competence is then scored from the record, not asserted.</details>

3. Why does the kill test ask for the *reason* a stock might be mispriced, and not just whether it looks cheap?
<details><summary>Answer</summary>A low multiple usually has a reason the market already knows. Naming a specific
source of mispricing — neglect, complexity, forced selling, a cyclical trough or a misunderstanding — is what makes
the idea researchable and falsifiable. Without one, there is no edge to find.</details>

## Go deeper

- Atul Gawande, *The Checklist Manifesto* — why checklists work in complex, expert domains.
- The casebook's `PROCESS.md` — the operational rules each template serves.

---
[← Previous: 15.1 The case-study method](01-the-case-study-method.md) · [Module index](index.md) · [Next: 15.3 Worked example — Kaveri →](03-worked-example-kaveri.md)
