# Kaveri Pumps — reference valuation (course "house view")

!!! note "Why this page exists"
    Several lessons value Kaveri Pumps & Motors (fictional). To keep the course consistent they all use the
    **assumptions and outputs on this page**, produced by `tools/running_example/valuation.py`. Lessons may
    *vary* assumptions to teach sensitivity, but must quote these as the base case. This is a teaching
    example — not a view on any real security.

## Assumptions (valuation date 31-Mar-2026; base year FY26)

| Driver | Base case |
|:--|:--|
| Revenue growth FY27→FY36 | 10.0%, 14.0%, 14.0%, 13.0%, 12.0%, 11.0%, 10.0%, 9.0%, 8.0%, 7.0% (FY27 cut below the 15–18% guidance after the weak Q1) |
| EBITDA margin | 13.3%, 14.2%, 14.8%, 15.2%, 15.5%, 15.5%, 15.5%, 15.5%, 15.5%, 15.5% |
| D&A | 3.4% of revenue |
| Capex | 3.5% of revenue every year |
| Net working capital | 25% of revenue FY27, 23% FY28, 22% from FY29 (FY26 actual: 27.7%) — assumes solar receivables partly normalise |
| Capacity | Hosur motors plant at 57% utilisation, so capex stays near maintenance + automation levels |
| Tax rate | 25.17% |
| Risk-free rate (India 10-yr G-sec) | 6.5% |
| Equity risk premium (India) | 6.0% |
| Beta | 1.05 |
| Cost of equity (CAPM) | 12.80% |
| Pre-tax / post-tax cost of debt | 8.9% / 6.66% |
| Target debt / capital | 10% |
| **WACC** | **12.19%** |
| Terminal growth (nominal ₹) | 5.5% |
| Terminal reinvestment | consistent with RONIC 18%: reinvestment rate = g / RONIC = 30.6% of NOPAT |
| Discounting | mid-year convention (cash flow of year *t* discounted by (1+WACC)^(t−0.5)); TV discounted 10 full years |
| Equity bridge | EV − net debt ₹140.5 Cr − lease liabilities ₹18.2 Cr; ÷ 6.07 Cr diluted shares |

## Base-case projection (₹ Cr)

| ₹ Cr | FY27 | FY28 | FY29 | FY30 | FY31 | FY32 | FY33 | FY34 | FY35 | FY36 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Revenue | 1,449.8 | 1,652.8 | 1,884.2 | 2,129.1 | 2,384.6 | 2,646.9 | 2,911.6 | 3,173.6 | 3,427.5 | 3,667.4 |
| Growth | 10.0% | 14.0% | 14.0% | 13.0% | 12.0% | 11.0% | 10.0% | 9.0% | 8.0% | 7.0% |
| EBITDA | 192.8 | 234.7 | 278.9 | 323.6 | 369.6 | 410.3 | 451.3 | 491.9 | 531.3 | 568.5 |
| EBITDA margin | 13.3% | 14.2% | 14.8% | 15.2% | 15.5% | 15.5% | 15.5% | 15.5% | 15.5% | 15.5% |
| D&A | 49.3 | 56.2 | 64.1 | 72.4 | 81.1 | 90.0 | 99.0 | 107.9 | 116.5 | 124.7 |
| EBIT | 143.5 | 178.5 | 214.8 | 251.2 | 288.5 | 320.3 | 352.3 | 384.0 | 414.7 | 443.8 |
| NOPAT (EBIT × (1 − 25.17%)) | 107.4 | 133.6 | 160.7 | 188.0 | 215.9 | 239.7 | 263.6 | 287.4 | 310.3 | 332.1 |
| Capex | 50.7 | 57.8 | 65.9 | 74.5 | 83.5 | 92.6 | 101.9 | 111.1 | 120.0 | 128.4 |
| Net working capital | 362.5 | 380.1 | 414.5 | 468.4 | 524.6 | 582.3 | 640.5 | 698.2 | 754.1 | 806.8 |
| Increase in NWC | -2.5 | 17.7 | 34.4 | 53.9 | 56.2 | 57.7 | 58.2 | 57.6 | 55.9 | 52.8 |
| **FCFF** = NOPAT + D&A − capex − ΔNWC | 108.5 | 114.2 | 124.5 | 132.0 | 157.3 | 179.3 | 202.5 | 226.5 | 251.1 | 275.6 |
| Discount factor (mid-year) | 0.9441 | 0.8416 | 0.7502 | 0.6687 | 0.5960 | 0.5313 | 0.4736 | 0.4221 | 0.3763 | 0.3354 |
| PV of FCFF | 102.4 | 96.1 | 93.4 | 88.3 | 93.8 | 95.3 | 95.9 | 95.6 | 94.5 | 92.4 |

## Result

| Item | ₹ Cr |
|:--|--:|
| Sum of PV of FCFF, FY27–FY36 | 947.7 |
| Terminal-year FCFF (FY37) | 243.3 |
| Terminal value at end-FY36 = FCFF₍FY37₎ / (WACC − g) | 3,638.7 |
| PV of terminal value | 1,152.3 |
| **Enterprise value** | **2,100.0** |
| Less: net debt | (140.5) |
| Less: lease liabilities | (18.2) |
| **Equity value** | **1,941.3** |
| **Value per share (6.07 Cr diluted shares)** | **₹320** |
| Terminal value as % of EV | 55% |
| Current market price (18-Sep-2026) | ₹390 |
| Implied upside / (downside) vs CMP | -18% |

Timing note: the valuation date is 31-Mar-2026 but the price is from 18-Sep-2026. Rolling the equity value forward
~0.47 years at the cost of equity gives ₹338 (a ~6% uplift, ignoring
dividends). Lessons may ignore the roll-forward for simplicity, but should mention that it exists.

## Sensitivity — value per share (₹)

| WACC \ g | 4.0% | 4.5% | 5.0% | 5.5% | 6.0% |
|:--|--:|--:|--:|--:|--:|
| 11.2% | ₹350 | ₹359 | ₹369 | ₹381 | ₹395 |
| 11.7% | ₹324 | ₹331 | ₹339 | ₹348 | ₹359 |
| 12.2% | ₹301 | ₹307 | ₹313 | ₹320 | ₹328 |
| 12.7% | ₹281 | ₹285 | ₹290 | ₹296 | ₹302 |
| 13.2% | ₹263 | ₹266 | ₹270 | ₹274 | ₹279 |

## Scenarios

| Scenario | Key assumptions | Value / share | Probability |
|:--|:--|--:|--:|
| Bull | solar dues clear, growth 15–17% fading to 8%, EBITDA margin to 16.5%, NWC to 19% of sales | ₹416 | 25% |
| Base | as above | ₹320 | 50% |
| Bear | state dues stay stuck, growth 3–8%, EBITDA margin 12–13%, NWC stays ~27–29% of sales | ₹168 | 25% |
| **Probability-weighted** | | **₹306** | |

## Reverse DCF — what does ₹390 imply?

Holding base-case margins, capex, working capital, WACC (12.19%) and terminal growth
(5.5%) fixed, the market price of ₹390 is justified by a **uniform revenue growth
of 14.1% a year for FY27–FY36**. Compare with the 10-year base case CAGR of
10.8% and the FY23–FY26 historical CAGR of
14.7%.

*Trader's lens:* this is the fundamental analogue of backing out implied volatility from an option price — the
question is not "what is it worth?" but "what growth is the market already paying for, and do I disagree?"
