# Module 06 · Exercises

Use `tools/fi/valuation.py` (`dcf_from_drivers`, `kaveri_base_drivers`, `kaveri_reference`, `reverse_dcf`,
`justified_pe`, `justified_pb`, `sensitivity`) wherever it helps; verify every number before opening the
[solutions](solutions.md).

## Warm-up

**E06.01** Define intrinsic value, relative value and book value, and state one situation where each is the most
useful.

**E06.02** Write the value-driver formula and state its three inputs and its two constraints (g < WACC; g < ROIC).

**E06.03** Define: risk-free rate, equity risk premium, beta, cost of debt, WACC; and state the currency-consistency
rule.

**E06.04** What is the difference between FCFF and FCFE, and which discount rate goes with each?

**E06.05** Write the justified forward P/E and justified P/B formulas.

**E06.06** Define reverse DCF and variant perception in one sentence each.

**E06.07** State the three properties of a good scenario set.

## Core

**E06.08** A cash flow of ₹12 Cr next year grows at 5% for ever; the discount rate is 12%. Value it. Then compute
the value multiple (V/NOPAT) for a company with NOPAT growing 6% at ROIC 18% and WACC 12%, and again at ROIC 12%.

**E06.09** Using the value-driver table in [06.1 §2.1](01-what-is-value.md), explain to a colleague in three
sentences why "growth is good" is only half true.

**E06.10** Build a cost of equity for an Indian mid-cap with today's G-sec at 7.07%, ERP 6.0% and beta 1.2; then a
WACC with 15% debt at 9.0% pre-tax and a 25.17% tax rate.

**E06.11** Four peers have regression betas 1.10, 0.95, 1.25, 1.05 with D/E 0.10, 0.05, 0.30, 0.15; the target has D/E
0.27; tax 25.17%. Compute the bottom-up beta.

**E06.12** From the Kaveri drivers (FY27 revenue growth 10%, EBITDA margin 13.3%, D&A 3.4%, capex 3.5%, NWC 25% of
revenue vs FY26 NWC ₹365.0 Cr, tax 25.17%), compute FY27 revenue, EBITDA, EBIT, NOPAT, capex, ΔNWC and FCFF.

**E06.13** Compute the terminal value at end-FY36 from NOPAT₃₆ ₹332.1 Cr, g 5.5%, RONIC 18%, WACC 12.19%; then the
value if FCFF₃₆ (₹275.6 Cr) were simply grown at 5.5% — and explain the difference.

**E06.14** Discount the ten FCFFs (108.5, 114.2, 124.5, 132.0, 157.3, 179.3, 202.5, 226.5, 251.1, 275.6) at 12.19% with the
mid-year convention, add the PV of a ₹3,638.7 Cr terminal value, and complete the bridge (net debt 140.5, leases
18.2, 6.07 Cr shares).

**E06.15** Compute the implied exit EV/EBITDA of the reference terminal value (FY36 EBITDA ₹568.5 Cr) and the value
per share if a 10x exit multiple were used instead.

**E06.16** Recompute the probability-weighted value with weights 40/40/20 (bear/base/bull) and the expected return
from ₹300.

**E06.17** Compute Kaveri's justified forward P/E and P/B with ROE 15%, $k_e$ 12.5%, g 5%. Compare with the trailing
P/E at ₹390 (25.9x) and explain the gap.

**E06.18** Value Kaveri at the peer-median P/E (34.7x) and the peer-median EV/EBITDA (20.8x). Reconcile with the
DCF's ₹320 in three sentences.

**E06.19** Using `reverse_dcf`, solve for the implied uniform growth at ₹300 and at ₹450 (base margins). Interpret.

**E06.20** A bank trades at 3.0x book with $k_e$ 13% and long-run growth 7%. Compute the implied RoE; the bank earns
16%. Write the variant perception (either direction) in the required form.

**E06.21** Residual income: book value ₹2,000 Cr, RoE 17%, $k_e$ 12.5%, g 6%. Value the equity and the P/B.

**E06.22** SOTP: a holdco owns 40% of a listed company (mcap ₹10,000 Cr) and 100% of an unlisted business worth
₹1,500 Cr on DCF; net cash ₹200 Cr; holdco costs ₹10 Cr/yr; $k_e$ 12%; 8 Cr shares. Compute gross NAV per share and
the value at 35% and 55% discounts on the listed stake.

**E06.23** Merton: asset value ₹800 Cr, asset vol 35%, debt face ₹600 Cr due in 2 years, rf 7%. Compute equity value
and the risk-neutral default probability (use the code in [06.7 §5.1](07-other-valuation-methods.md)). What happens
to equity if asset vol rises to 50%?

**E06.24** From ₹260, compute Kaveri's expected return and upside/downside ratio on the reference scenarios; then
with a fourth scenario — a 10% chance of ₹80 (governance jump) — rescaling the others proportionally.

**E06.25** Run the Monte-Carlo sketch in [06.8 §4](08-margin-of-safety-and-expected-value.md) with correlated
growth and margin draws (e.g., margin shift = 0.5 × growth-scale deviation + noise). Report P10/P50/P90 and
P(value < 390), and compare with the independent-draw version.

## Stretch

**E06.26** Explain, with the Gordon model, why a company's value can *fall* when its growth accelerates.

**E06.27** Design a two-stage DCF for a company with 25% growth for five years fading linearly to 6% by year ten,
ROIC 30% fading to 15%, WACC 11%. Implement it with `dcf_from_drivers` (choose a base) and report TV share of EV.

**E06.28** Write the fifteen DCF mistakes as a one-page checklist you would run on a broker's model, with the
question that detects each.

**E06.29** For the NSE IPO (September 2026), write the price-implied expectations you would want to back out
before deciding whether to subscribe, and the data you would need.

## Real-world task

**E06.30** Pick a listed Indian non-financial company. Using `fi.data.fetch_statements`, build a driver-based DCF
(`dcf_from_drivers`) with a documented base case, run WACC × g and growth × margin grids, three scenarios with
probabilities, and a reverse DCF at the current price. Write the one-table-and-three-sentences output of
[06.4 §5](04-dcf-in-practice.md).

**E06.31** For a listed Indian bank or NBFC, compute the implied RoE from its P/B and compare with its actual and
five-year average RoE. State the expectation that matters.
