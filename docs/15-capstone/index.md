# Module 15 · Capstone — Your Own Case Studies

**What this module does.** It turns the course into a practice. Modules 00–14 taught the method on companies whose
endings are known, or on fictional ones built to teach. The capstone applies the same method to real, live
companies. You choose them, the outcome is unknown, and you will find out later whether you were right. The work
lives in a private **casebook** repository, separate from this public course.

**Why it matters.** Case studies with known endings train pattern recognition. They cannot train judgement, because
hindsight is always in the room. The only way to learn whether *your* process works is to write down a decision
before the outcome, with the reasons, probabilities and the evidence that would prove you wrong, and then score it.
A trader keeps a P&L by strategy. An investor needs the equivalent: a record of decisions that can be marked against
reality.

## The public / private split

| | Public course (this site) | Private casebook |
|:--|:--|:--|
| Repository | `fundamental-investing-course` | `fundamental-investing-casebook` (private) |
| Contains | Lessons, exercises, fictional companies, historical cases, mocks, tools | Your real cases: kill tests, full case files, models, memos, decision journal, quarterly updates, post-mortems |
| Why | Teaching material, safe to share | Positions, sizes and unpublished views should not be public; it also frees you to be wrong in writing |
| Links | Templates are described in [15.2](02-templates.md) | `templates/` holds the fill-in versions; `tools/` imports the course library |

The casebook's `tools/pull.py` imports the course's `fi` library from a sibling checkout (`../course`), so both
repos sit side by side on disk.

## Lessons

| # | Lesson | One line | Time |
|:--|:--|:--|:--|
| 15.1 | [The case-study method](01-the-case-study-method.md) | Six stage gates from idea to post-mortem; time budgets; the funnel; calibration | 60 min |
| 15.2 | [Templates](02-templates.md) | Every template in the casebook, with what each field is for and a filled example line | 45 min |
| 15.3 | [Worked example — Kaveri, end to end](03-worked-example-kaveri.md) | The whole method on the running example, stage by stage, as the casebook stores it | 90 min |
| 15.4 | [Grading rubric & review](04-grading-rubric-and-review.md) | Scoring a case; a red-team review protocol (peer or AI); calibration and the annual process review | 45 min |

## What the capstone asks of you

1. **Three full case studies in the first six months**, each on a different kind of situation:
   - **a long idea** you would own;
   - **an "avoid"** — a popular stock you conclude is overpriced or flawed, written with the same rigour;
   - **a lender, a cyclical or a special situation**, where the method has to change
     ([07](../07-special-valuation/index.md), [12.3](../12-macro-special-sits/03-special-situations.md)).
2. **Twenty kill tests** in the same period. Most should end in "kill". The funnel is the point: it shows your
   filters working and keeps the deep dives for ideas that have earned them.
3. **Quarterly updates** on every full case, for as long as you own the stock or it stays on the watchlist.
4. **A post-mortem** on every exit, and on every case after three years whether or not you acted.
5. **An annual process review** ([15.4](04-grading-rubric-and-review.md)): your calibration, your hit rate by type
   of idea, and one change to the process.

!!! warning "Real money"
    The capstone is where research meets your capital. Nothing in this course is investment advice. The sizing
    rules in [11.4](../11-process/04-position-sizing-and-portfolio-construction.md) exist so that no single case
    can do serious damage while you learn whether your process has an edge. Start small: the first year's job is to
    produce a *record*, not a return.

## Connections

- Back: everything, and specifically [11.2 research process](../11-process/02-the-research-process.md),
  [11.3 memo](../11-process/03-writing-an-investment-memo.md), [11.4 sizing](../11-process/04-position-sizing-and-portfolio-construction.md),
  [11.5 monitoring](../11-process/05-monitoring-and-selling.md),
  [11.6 decision journals](../11-process/06-behavioural-finance-and-decision-journals.md),
  [09.7 forensic checklist](../09-forensics/07-the-forensic-checklist.md) and the
  [stock-pitch mock](../14-mocks/06-stock-pitch-mock.md).
- Forward: your own record.

## You're ready to call the course finished when you can…

- [ ] Show twenty dated kill tests and three complete case files in the casebook.
- [ ] Point to each case's thesis-breakers and say which have fired.
- [ ] State your calibration: of the things you called 70% likely, how many happened?
- [ ] Name one change you have made to your own process because a post-mortem told you to.
