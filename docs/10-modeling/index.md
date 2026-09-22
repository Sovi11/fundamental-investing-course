# Module 10 · Financial Modelling

**What this module does.** Turns the driver logic of Modules 04–06 into a working three-statement model: the
architecture and conventions, building and tying out the historicals, forecasting each schedule (revenue,
costs, working capital, capex/D&A, debt/interest, tax, dividends, cash as the plug), scenarios/sensitivities/QA,
and a hands-on build of the Kaveri model in Python with `tools/fi/model.py` that reproduces ₹320 and then
stresses it.

**Why it matters.** A model is how you find out whether your assumptions are mutually consistent — and the only
way to see the balance sheet your forecast implies (Kaveri's model shows cash building to ₹220 Cr by FY29, which
raises a capital-allocation question no DCF alone would).

## Lessons

| # | Lesson | One line | Time |
|:--|:--|:--|:--|
| 10.1 | [Model architecture](01-model-architecture.md) | Inputs → schedules → statements → valuation → outputs; conventions; Excel vs Python | 60 min |
| 10.2 | [Building the historicals](02-historicals-and-data.md) | Sources, mapping, reclassification, normalisation, tie-outs, vendor pitfalls | 75 min |
| 10.3 | [Forecasting drivers](03-forecasting-drivers.md) | Revenue and cost builds, days-based NWC, capex/D&A, debt and circularity, tax, dividends, the plug; Kaveri FY27–29 | 100 min |
| 10.4 | [Scenarios, sensitivities & model QA](04-scenarios-sensitivities-qa.md) | Switches, data tables, tornado, stress tests, the 17-point review | 75 min |
| 10.5 | [Build-along: the Kaveri model in Python](05-build-along-kaveri-model.md) | The whole pipeline; the receivables stress; pointing it at a real company | 120 min hands-on |

## Connections

- Back: [02.6](../02-accounting/06-linking-the-three-statements.md), [06.3](../06-valuation/03-dcf-step-by-step.md),
  [06.4](../06-valuation/04-dcf-in-practice.md).
- Forward: the model is the engine of the memo ([11.3](../11-process/03-writing-an-investment-memo.md)) and the
  capstone ([15.3](../15-capstone/03-worked-example-kaveri.md)).
- Tools: `tools/fi/model.py`, `tools/examples/build_kaveri_model.py`, `tools/tests/test_model.py`.

## You're ready to move on when you can…

- [ ] Lay out a model with inputs in one place, checks on the summary page and cash as the only plug.
- [ ] Build and tie out five years of historicals for a real company from primary sources.
- [ ] Forecast every schedule from drivers and explain the circularity choice.
- [ ] Reproduce Kaveri's FY27–FY36 statements and the ₹320 value with `project()`; run the receivables stress.
- [ ] Produce scenario switches, two-way grids, a tornado and a stress test, and pass the QA checklist.
- [ ] Map a real company's Yahoo/Screener data into the model layout and run it.

**Tested by:** [Mock 3 — Valuation](../14-mocks/03-mock-valuation.md) (model-based problems) and the
[final exam](../14-mocks/05-final-exam.md) case.

[Exercises](exercises.md) · [Solutions](solutions.md)
