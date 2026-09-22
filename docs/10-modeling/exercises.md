# Module 10 · Exercises

Most problems are done in Python with `tools/fi/model.py`; some are Excel-oriented. Verify against the
[solutions](solutions.md) only after running your own code.

## Warm-up

**E10.01** Draw the model flow (inputs → schedules → statements → valuation → outputs) and state the one exception
to "no backward links".

**E10.02** List the seven conventions of [10.1 §2](01-model-architecture.md) and the error each prevents.

**E10.03** Why is cash the plug, and what is a revolver?

**E10.04** Name the three historical tie-outs and one common cause of each failing.

**E10.05** State the reclassification decisions the course makes for other income, exceptional items, leases and
interest classification.

**E10.06** What does `Assumptions.kaveri_base()` set for growth, margins, D&A, capex, NWC, tax, payout, interest and
debt repayments?

## Core

**E10.07** Load the Kaveri history and assert, in code, that total assets equal total liabilities and equity and
that cash reconciles every year from the 31-Mar-2020 opening cash of ₹34.0 Cr.

**E10.08** Rebuild FY26's retained-earnings and gross-block roll-forwards from the history frame and confirm they
close.

**E10.09** Run `project()` with the base assumptions and print the checks; report FY27–FY29 revenue, EBITDA, PAT,
cash and equity; confirm the FCFF series matches the reference DCF.

**E10.10** Build a segment revenue forecast for FY27–29 (agri +6.5%/yr from 606.2; industrial +9%, +12%, +12% from
355.9; solar +18%, +27%, +25% from 355.9) and compare totals with the reference growth path.

**E10.11** Convert the reference NWC assumption (22% of revenue from FY29) into receivable days, holding inventory
80 days and payables 61 days on COGS (COGS = 65% of revenue), OCA 3% and OCL 5%.

**E10.12** Recompute FY27 finance costs from the debt schedule (opening borrowings ₹188 Cr at 8.9%; leases ₹18.2 Cr
at 8.5%) and FY28 after a ₹20 Cr term-loan repayment.

**E10.13** Run the receivables stress (`nwc_pct=0.277`) and the margin-down case (`ebitda_margin=[0.133, 0.138] +
[0.14]*8`); report the value per share of each and the FY27 cash.

**E10.14** Set `nwc_pct=0.30` and `min_cash=40`; report the revolver draws by year and the effect on FY28 finance
costs.

**E10.15** Build the three scenarios of [10.4 §1](04-scenarios-sensitivities-qa.md) as `Assumptions` objects,
project each, and report value per share; confirm ₹168/₹320/₹416 to within a rupee.

**E10.16** Produce a tornado table for growth (×0.8/×1.2), margin (∓1 pp), capex (4.5%/2.5%), WACC (±0.5 pp) and
terminal NWC (25%/19%); rank the drivers.

**E10.17** Using `fi.valuation.sensitivity`, build a growth-scale × margin-shift grid (0.75–1.4 × −2 pp…+2 pp) and
mark the cells above ₹390.

**E10.18** Run the QA checklist of [10.4 §4](04-scenarios-sensitivities-qa.md) on `build_kaveri_model.py` and list
which items it satisfies, which are n/a, and which you would add.

**E10.19** Change the dividend payout to 60% and rerun; report the value per share and the FY29 cash balance;
explain why one changes and the other does not.

**E10.20** *Excel.* Describe, step by step, how you would build the Kaveri model's working-capital schedule in Excel
with days-based inputs, colour coding, one formula per row and a check row.

## Stretch

**E10.21** Extend `Assumptions`/`project()` conceptually (describe the changes; implement if you can) to model
leases properly: ROU additions, amortisation, interest, payments — as `generate.py` does.

**E10.22** Add an interest-on-average-debt option with a fixed three-iteration loop and compare FY27 interest with
the opening-balance method.

**E10.23** Build a Monte-Carlo wrapper around `project()` (growth scale, margin shift, NWC) and report P10/P50/P90
of value per share and of FY28 cash.

## Real-world task

**E10.24** Map a real NSE-listed manufacturer's statements (via `fetch_statements` or a Screener export) into the
Kaveri layout for the last three years; tie them out; set drivers from its own history; run `project()`; value it;
run a reverse DCF at the market price; and write the one-table-and-three-sentences output. Document every mapping
assumption.

**E10.25** Present the same model in Excel (statements, checks, a scenario switch and a data table) following the
conventions, and have someone else find a hard-code in it.
