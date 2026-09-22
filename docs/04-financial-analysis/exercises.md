# Module 04 · Exercises

Use the [Kaveri](../appendix/running-example/kaveri-pumps.md) and [Nirmal](../appendix/running-example/nirmal-finance.md)
pages; compute with Python (`tools/fi/ratios.py` where useful) before checking the [solutions](solutions.md).

## Warm-up

**E04.01** Compute Kaveri's revenue CAGR for FY21–FY26 and FY23–FY26, and explain why the two differ.

**E04.02** Define gross, EBITDA, EBIT and PAT margin and state what a move in each (with the others stable)
tells you.

**E04.03** Define ROE, ROCE and ROIC with numerators and denominators as the course uses them, and say which is
pre-tax.

**E04.04** Define DIO, DSO, DPO and the cash conversion cycle, stating the base (revenue or COGS) for each.

**E04.05** Define net debt, net debt/EBITDA, interest cover and DSCR.

**E04.06** Define basic EPS, diluted EPS, BVPS, payout ratio and FCF yield.

**E04.07** What is the accruals ratio and why does a high value predict lower future returns?

## Core (Kaveri unless stated)

**E04.08** Decompose FY23–FY26 revenue growth by segment (agri 550.6 → 606.2; industrial 262.2 → 355.9; solar
61.2 → 355.9): compute each segment's CAGR and its share of the total increase. What does this say about the
"14.7% CAGR"?

**E04.09** Build the FY26 common-size P&L (materials, employees, other expenses, D&A, finance costs as % of
revenue) and compare with FY24. Which line explains most of the EBITDA-margin decline?

**E04.10** Using the fixed/variable split from [04.2](02-margins-and-cost-structure.md) (contribution ₹348.8 Cr,
fixed costs ₹214.7 Cr, EBIT ₹134.1 Cr), compute the degree of operating leverage and the EBIT if revenue falls 10%
with an unchanged contribution margin.

**E04.11** Run a margin bridge for FY24 → FY26 with segment gross margins of agri 40%, industrial 36%, solar 22%
(FY24) and 40%, 36%, 24% (FY26), and revenue shares 57/29/14 and 46/27/27. Separate the mix and rate effects.

**E04.12** Compute FY26 ROE (avg equity 671.7), ROCE (EBIT + other income 138.0; avg capital employed 868.1) and
ROIC (NOPAT at 25.17%; avg invested capital 836.8). Reconcile ROCE and ROIC.

**E04.13** Run the 3-step DuPont for FY26 (net margin, asset turnover on avg assets 1,089.7, leverage on avg
equity 671.7) and the 5-step version (tax burden, interest burden using EBIT incl. other income). Which factor drove
the ROE change from FY24 (16.5%)?

**E04.14** Compute incremental ROIC for FY24 → FY26 (NOPAT 91.4 → 100.3; invested capital 690.6 → 886.8) and compare
with the average ROIC. Interpret.

**E04.15** Compute the FY26 reinvestment rate (capex 52.0 incl. intangibles; ΔNWC 89.7; D&A 47.8; NOPAT 100.3) and
the growth it supports at a 12% ROIC. Compare with actual revenue growth.

**E04.16** Compute FY26 inventory days (on materials 858.0), receivable days (on revenue), payable days (on
materials) and the cash conversion cycle; then NWC (inventory + receivables + OCA − payables − OCL) as % of revenue.

**E04.17** If receivable days were 80 instead of 96 at FY26 year-end, how much cash would have been released?
What would CFO and FCF have been?

**E04.18** Compute FY26 CFO/EBITDA, CFO/PAT, FCF (CFO − capex on PP&E and intangibles) and the three-year (FY24–26)
versions.

**E04.19** Estimate FY26 maintenance capex using the D&A proxy and state growth capex; discuss whether the proxy
is reasonable for a company that just built a plant.

**E04.20** Compute FY26 net debt (ex-leases and incl. leases), net debt/EBITDA, debt/equity, interest cover
(EBIT/finance costs) and DSCR ((EBITDA − current tax)/(interest + ₹20 Cr scheduled term-loan repayment)).

**E04.21** Stress: revenue −15%, EBITDA margin 10%, working-capital debt +₹60 Cr, interest scaled with debt.
Compute interest cover and net debt/EBITDA (use the method in [04.5 §3.1](05-leverage-solvency-liquidity.md)).

**E04.22** List every off-balance-sheet or contingent item in Kaveri's notes with its amount and how you would
treat it in adjusted net debt.

**E04.23** Compute FY26 basic and diluted EPS, BVPS, DPS paid, payout ratio (on FY26 PAT), and at ₹390: P/E, P/B,
EV/EBITDA (EV incl. leases) and FCF yield.

**E04.24** Compute the FY26 cash-flow accruals ratio ((PAT − CFO)/avg assets) and score Kaveri on the ten-item
quality scorecard of [04.7 §5](07-quality-of-earnings.md), justifying each score in one line.

**E04.25** *Nirmal Finance.* Build the FY26 RoA tree (% of average assets 6,831.4) and convert to RoE via
leverage. Then compute RoE if credit cost rose to 4.0% of average loans (6,350) with everything else unchanged.

**E04.26** *Peer comparison (fictional peer set on the Kaveri page).* Compute each peer's PAT margin and rank the
five companies on ROCE, margin, growth and leverage. Where does Kaveri sit, and does its P/E discount look
justified?

## Stretch

**E04.27** A company reports ROCE of 22% on closing capital employed with 30% growth in capital during the year.
Recompute an approximate ROCE on average capital and explain the bias.

**E04.28** Two companies have ROE of 18%: A with D/E 0.1 and B with D/E 2.0. Estimate each one's ROA (after-tax
cost of debt 6%) and describe what happens to each ROE if ROA falls 4 pp.

**E04.29** Kaveri's asset turnover has been flat at ~1.2 since FY22 while ROE rose then fell. Using the DuPont
decomposition, write three sentences for a memo on what this implies for where research time should go.

**E04.30** Construct a fictional company whose EBITDA margin rises every year while FCF falls every year, and
explain the mechanism in the statements.

## Real-world task

**E04.31** Using `tools/fi/data.py` (`fetch_statements`) or a Screener export, build a five-year ratio dashboard
(growth, margins, ROE/ROCE/ROIC, days, CCC, CFO/EBITDA, FCF, net debt/EBITDA, interest cover) for a listed Indian
manufacturer. Write ten lines reading the dashboard top to bottom as a story.

**E04.32** For the same company, compute the quality-of-earnings scorecard and the three-year incremental ROIC;
state the single most important question the numbers raise for the concall.
