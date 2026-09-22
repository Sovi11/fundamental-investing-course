# Module 09 · Exercises

Use `tools/fi/forensics.py` for the scores; Kaveri figures from the running-example page.

## Warm-up

**E09.01** Describe the five positions on the accounting spectrum and the analyst's response to each.

**E09.02** State the fraud triangle and give an observable proxy for each corner.

**E09.03** List Schilit's three families and two techniques in each.

**E09.04** Who detects fraud most often, and what does that imply about audit opinions?

**E09.05** Define: channel stuffing, bill-and-hold, round-tripping, gross vs net, POC abuse, cookie jar, big bath,
supplier finance, window dressing.

**E09.06** Write the Beneish M-score formula and its threshold; the Altman Z (original) formula and zones; the
nine Piotroski signals.

**E09.07** What is the "Satyam test" and what result would have exposed it?

## Core

**E09.08** *Receivables tests.* From Kaveri FY21–26 (receivables 107.3, 118.4, 146.1, 192.9, 269.7, 346.7; revenue
612, 758, 874, 1,006, 1,172, 1,318), compute DSO each year, receivables growth ÷ revenue growth each year, and DSRI
for FY24–26.

**E09.09** *Adjudication.* Using the four-hypothesis table of [09.2 §2.1](02-revenue-red-flags.md), write one line
of evidence for and against each hypothesis for Kaveri, and the verdict with a confidence level.

**E09.10** *Provisioning.* Kaveri's > 6-month overdues are ₹62.4 Cr with a ₹4.0 Cr allowance. Compute the
after-tax PAT and EPS effects of coverage at 20%, 30% and 50%.

**E09.11** *Capitalisation test (fictional).* A software company's intangibles under development rose ₹40 → ₹95 →
₹180 Cr over three years; R&D expense fell from 12% to 6% of ₹800 Cr revenue; EBITDA margin rose from 14% to 22%.
Restate year-3 EBITDA as if the incremental capitalisation were expensed, and comment.

**E09.12** *Depreciation.* A company extends the useful life of its plant from 12 to 20 years; gross depreciable
block ₹2,400 Cr, straight-line, no residual. Compute the annual depreciation before and after and the PAT effect
at 25% tax.

**E09.13** *Provision roll-forward.* Opening ₹80 Cr; charge ₹12 Cr; utilisation ₹15 Cr; reversal ₹30 Cr; closing?
Which line boosted profit and what would you ask?

**E09.14** *Interest on cash.* Company X: cash and bank ₹1,800 Cr (₹1,500 Cr prior year); interest income ₹28 Cr;
borrowings ₹1,200 Cr at ~9%. Compute the implied yield and the interest paid; interpret.

**E09.15** *Supplier finance.* A retailer's payable days jump from 40 to 85 in a year in which CFO doubled; the
notes mention a "vendor financing programme" of ₹900 Cr. Recompute net debt and net debt/EBITDA (EBITDA ₹1,200 Cr;
reported net debt ₹600 Cr).

**E09.16** *Standalone vs consolidated.* Standalone cash ₹15 Cr; consolidated cash ₹640 Cr; standalone loans to
subsidiaries ₹520 Cr; consolidated subsidiaries' PAT −₹90 Cr. Explain what is happening and what you would value.

**E09.17** *Beneish.* Run `forensic_summary(load_kaveri(), "FY26")` and report each index and the M-score. Which two
indices contribute most to the change from FY24's −2.32? Then recompute M by hand from the indices and the
coefficients.

**E09.18** *Altman.* Compute Kaveri's Z (original) at a market cap of ₹2,340 Cr (working capital 316.5; retained
earnings 676.1; EBIT incl. other income 138.0; sales 1,318; total assets 1,143.6; total liabilities 437.5); classify;
then Z″ using book equity ₹706.1 Cr.

**E09.19** *Piotroski.* Score Kaveri FY26 signal by signal (the tool gives the values) and explain which three
signals it lost since FY24 and why.

**E09.20** *Governance signals.* Rank these events by severity and justify: (a) mandatory auditor rotation; (b) a
6% promoter pledge for a private venture; (c) the CFO resigning three weeks before results; (d) RPT purchases rising
from 6.5% to 10.4% of materials over five years; (e) an independent director resigning citing "personal reasons"
two days after an audit-committee meeting.

**E09.21** *Operator pattern.* A stock trades 60 lakh shares a day with 3 lakh delivered; the top "public" holders
include three private companies at the company's registered address; the company announced ₹2,000 Cr of "orders"
in a year with ₹120 Cr of revenue; a preferential issue of warrants to "investors" was priced at the SEBI floor.
Which signals are present and what do you do?

**E09.22** *Checklist.* Score Kaveri on all 40 items of [09.7](07-the-forensic-checklist.md) yourself (before
reading the lesson's scores), compute the section totals and RAG, and write the four-part verdict.

**E09.23** *Escalation.* For each of the following, state whether Kaveri's RAG would change and why: (a) a KAM
becomes a qualification on receivables; (b) the pledge rises to 12%; (c) a state agency disputes ₹15 Cr; (d) the
company discloses contract assets of ₹40 Cr for the first time.

## Stretch

**E09.24** Design a fabricated-revenue scheme for a fictional manufacturer and then list, statement by statement,
the marks it would leave and the test that would catch each.

**E09.25** Explain why Beneish and Altman would both have passed Satyam in 2008, and which two disclosures would
have caught it.

**E09.26** Build a "forensic exclusion screen" for a Screener export (pledge, CFO/PAT, auditor change, ASM, RPT)
and estimate what share of a small-cap universe it would remove.

## Real-world task

**E09.27** Run `forensic_summary` on a real listed manufacturer using `fetch_statements` (map the rows as the
docstring describes). Report Beneish, Altman, Piotroski, accruals and cash yield with the mapping assumptions
stated.

**E09.28** For the same company, complete the 40-point checklist from its last two annual reports and exchange
filings, with page references, and write the verdict.

**E09.29** Read one SEBI final order on a small-cap manipulation case (2023–26). Summarise the mechanism in 150 words
and list the signals visible in public data before the order.
