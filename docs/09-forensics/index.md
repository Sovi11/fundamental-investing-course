# Module 09 · Forensic Accounting & Red Flags

**What this module does.** Teaches scepticism as a procedure: why and how numbers get bent (incentives, the
fraud triangle, Schilit's taxonomy); revenue, expense/asset and cash-flow red flags with their balance-sheet
marks; India's governance signals with base rates; the scoring models (Beneish, Altman, Piotroski, accruals) run
on Kaveri; and a 40-point checklist that produces a RAG verdict and a four-part response — adjust, discount,
monitor, escalate.

**Why it matters.** Every valuation assumes the inputs are honest. The cases in Module 13 — Satyam, Enron,
Wirecard, DHFL, Manpasand — show what happens when they are not, and that the marks were visible years in advance
to anyone who looked.

## Lessons

| # | Lesson | One line | Time |
|:--|:--|:--|:--|
| 09.1 | [Why and how numbers lie](01-why-and-how-numbers-lie.md) | The spectrum; incentives; the taxonomy; who catches fraud; the forensic mindset | 70 min |
| 09.2 | [Revenue red flags](02-revenue-red-flags.md) | Techniques and their receivables marks; Kaveri's receivables adjudicated | 80 min |
| 09.3 | [Expense & asset red flags](03-expense-and-asset-red-flags.md) | Capitalisation, CWIP, lives, provisions, inventory, SG&A, goodwill | 75 min |
| 09.4 | [Cash-flow games](04-cash-flow-games.md) | Reclassification, supplier finance, the Satyam interest test, cash that left, standalone vs consolidated | 75 min |
| 09.5 | [Governance red flags in India](05-governance-red-flags-india.md) | The signals ranked; stated vs actual holdings; the operator pattern; SEBI/NFRA as data | 70 min |
| 09.6 | [Forensic scoring models](06-forensic-scoring-models.md) | Beneish, Altman, Piotroski, accruals, C-score, Dechow — with the tools | 90 min |
| 09.7 | [The forensic checklist](07-the-forensic-checklist.md) | 40 items, scoring, RAG; Kaveri = Amber (18) | 90 min |

## Connections

- Back: [04.7](../04-financial-analysis/07-quality-of-earnings.md), [05.6](../05-business-analysis/06-corporate-governance-india.md),
  [03.3](../03-reading-filings/03-notes-to-accounts.md).
- Forward: the checklist feeds the memo ([11.3](../11-process/03-writing-an-investment-memo.md)), sizing overlays
  ([11.4](../11-process/04-position-sizing-and-portfolio-construction.md)) and the capstone template; the cases
  [I1](../13-case-studies/india/01-satyam-2009.md), [I14](../13-case-studies/india/14-manpasand-vakrangee-small-cap-flags.md),
  [G4](../13-case-studies/global/04-enron-2001.md), [G9](../13-case-studies/global/09-wirecard-2020.md).
- Tools: `tools/fi/forensics.py` (`beneish_m`, `altman_z`, `piotroski_f`, `accruals_ratio`, `cash_yield_check`,
  `forensic_summary`).

## You're ready to move on when you can…

- [ ] Place a company on the conservative → fraudulent spectrum with evidence and name the incentive.
- [ ] Run the receivables tests (DSO, growth ratio, ageing, coverage, DSRI) and adjudicate between mix, credit,
      recognition and fabrication.
- [ ] Find capitalised costs, CWIP ageing, provision releases and inventory games in the notes.
- [ ] Apply the interest-on-cash test and the cash-rich-but-borrowing test, and compare standalone with consolidated.
- [ ] Rank governance signals and search SEBI orders for a promoter.
- [ ] Compute Beneish, Altman and Piotroski for any company with the tools and state the mapping.
- [ ] Complete the 40-point checklist with page references and write the four-part verdict.

**Tested by:** [Mock 4 — Forensics & sectors](../14-mocks/04-mock-forensics-sectors.md).

[Exercises](exercises.md) · [Solutions](solutions.md)
