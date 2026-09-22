# Module 06 · Valuation

**What this module does.** Builds valuation from first principles — value is discounted cash, and growth
creates value only when returns exceed the cost of capital — through cost of capital, a full DCF (built line by
line on Kaveri and reproducing the course's ₹320 reference), DCF in practice (sensitivities, scenarios, the
fifteen mistakes), relative valuation, reverse DCF and expectations investing, the other methods (DDM, residual
income, SOTP, asset-based, capacity multiples, options), and margin of safety as a distribution.

**Why it matters.** Everything before this module produces inputs; everything after uses outputs. The module's
central move — reading the price as a forecast and disagreeing with it specifically — is the investor's version
of implied volatility.

## Lessons

| # | Lesson | One line | Time |
|:--|:--|:--|:--|
| 06.1 | [What value is](01-what-is-value.md) | Intrinsic vs relative vs book; the value-driver formula; price, value, expectations | 75 min |
| 06.2 | [Cost of capital](02-cost-of-capital.md) | rf, ERP, beta (three ways), cost of debt, WACC; Indian ranges; WACC as a hurdle | 90 min |
| 06.3 | [DCF step by step](03-dcf-step-by-step.md) | Drivers, explicit forecast, terminal value done right, discounting, the bridge; ₹320 reproduced | 120 min |
| 06.4 | [DCF in practice](04-dcf-in-practice.md) | Sensitivity grids, scenarios and weights, sanity checks, the fifteen mistakes, honest presentation | 90 min |
| 06.5 | [Relative valuation & multiples](05-relative-valuation-and-multiples.md) | Every multiple matched; justified P/E and P/B derived; peers, bands, why Indian multiples are high | 90 min |
| 06.6 | [Reverse DCF & expectations](06-reverse-dcf-and-expectations.md) | Price → implied growth/margin/WACC; variant perception; a live-data reverse DCF | 90 min |
| 06.7 | [Other valuation methods](07-other-valuation-methods.md) | DDM, residual income, SOTP and holdco discounts, NAV/replacement/liquidation, EV/tonne, Merton, real options | 100 min |
| 06.8 | [Margin of safety, expected value & asymmetry](08-margin-of-safety-and-expected-value.md) | Downside first; expected value and payoff asymmetry; Monte Carlo; the price at which Kaveri works | 80 min |

## Connections

- Back: [04.3](../04-financial-analysis/03-returns-on-capital.md) (ROIC and reinvestment), [05.3](../05-business-analysis/03-moats-and-competitive-advantage.md)
  (the fade), [01.5](../01-markets-101/05-time-value-and-returns-math.md) (discounting).
- Forward: [Module 07](../07-special-valuation/index.md) adapts the methods to lenders, insurers, cyclicals,
  loss-makers, holdcos and infra; [Module 10](../10-modeling/index.md) builds the model; [11.3–11.4](../11-process/03-writing-an-investment-memo.md)
  turn the distribution into a memo and a size.
- Reference: [Kaveri valuation page](../appendix/running-example/kaveri-valuation.md); `tools/fi/valuation.py`.

## You're ready to move on when you can…

- [ ] Derive the value-driver formula and show why growth at ROIC = WACC is worthless.
- [ ] Build Kaveri's WACC (12.19%) and defend each input with a current source.
- [ ] Reproduce ₹320/share from the drivers, decompose it by period and by assumption, and state the implied
      exit multiple.
- [ ] Produce the WACC × g and growth × margin grids and the three-scenario weighted value (₹306).
- [ ] Compute justified P/E and P/B and explain what a 26x or 35x multiple assumes.
- [ ] Reverse-solve ₹390 for implied growth (14.1%), margin, WACC and terminal g, and write a variant perception.
- [ ] Value a lender by residual income, a holdco by SOTP with an argued discount, and explain equity as a call.
- [ ] Compute expected return and upside/downside from an entry price and state the price at which Kaveri is a
      bet worth taking (~₹220–260).

**Tested by:** [Mock 3 — Valuation](../14-mocks/03-mock-valuation.md).

[Exercises](exercises.md) · [Solutions](solutions.md)
