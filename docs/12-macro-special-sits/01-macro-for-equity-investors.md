# 12.1 · Macro for equity investors

> **Why this matters:** a bottom-up investor does not forecast GDP — but every valuation carries macro inputs
> (the risk-free rate, inflation in the growth rate, the rupee in exporters' margins) and every sector has a
> macro variable that dominates its earnings. The point of macro for a stock-picker is not prediction; it is to
> know which macro variable your portfolio is unknowingly betting on, and what happens to each holding when it
> moves. As of September 2026, with crude high, the rupee weak, CPI rising toward 5% and the RBI on hold at 5.25%,
> that question is live.

**Learning objectives** — after this lesson you can:

- Explain how interest rates affect equity value through the discount rate and why long-duration growth stocks
  are rate-sensitive.
- Trace inflation, the rupee, RBI policy, fiscal capex and crude through to sector margins and demand.
- Read the earnings cycle and distinguish top-down from bottom-up uses of macro.
- Map which macro variables matter for which sectors, and audit a portfolio's macro exposure.

**Prerequisites:** [06.2 Cost of capital](../06-valuation/02-cost-of-capital.md), [08 Sector playbooks](../08-sectors/index.md)  ·  **Time:** ~70 min

---

## 1. Rates and equity duration

A share's value is the PV of cash flows stretching decades ahead; like a bond, it has **duration** — the
sensitivity of value to the discount rate. Growth stocks whose cash flows are mostly far in the future have
long duration; mature, high-payout stocks have short duration. From the Gordon model, $V = CF_1/(r − g)$:

$$\frac{dV/V}{dr} = −\frac{1}{r − g}$$

At $r$ = 12% and $g$ = 5.5% (Kaveri's terminal), duration is 1/0.065 ≈ 15: a 1-pp rise in the discount rate cuts
value ~15%. At $g$ = 9% (a growth stock), duration is 33. This is why the 2022 rate shock hit long-duration
growth stocks hardest, and why a rising G-sec yield ([06.2](../06-valuation/02-cost-of-capital.md): 7.07% in
September 2026, up from ~6.5% at the reference valuation date) lowers every DCF by 5–10% before any change in
the business.

The channels from rates to equities:

| Channel | Mechanism | Who is most exposed |
|:--|:--|:--|
| Discount rate | Higher rf → higher $k_e$ and WACC → lower PV | Long-duration growth; REITs/InvITs and utilities (bond proxies) |
| Relative value | Earnings yield vs bond yield — when the 10-year G-sec at 7%+ exceeds the Nifty's earnings yield (~5% at 19.5x), the "equity risk premium" as the market prices it is thin | Whole market; the "Fed model" with Indian caveats |
| Corporate borrowing costs | Interest expense; refinancing; capex hurdle | Levered cyclicals, infra, real estate, NBFCs (funding cost) |
| Consumer credit | EMIs for housing, autos, durables | Housing finance, autos, retail |
| Bank margins | Repo cuts compress NIMs for repo-linked lenders faster than deposit costs fall; hikes do the reverse | Banks ([08.1](../08-sectors/01-banks-and-lending.md)) |
| Flows | Higher deposit rates and G-sec yields compete with equity SIPs | Small caps and high-multiple names most flow-dependent |

## 2. Inflation and margins

Inflation enters three ways: through the nominal growth rate (revenue grows with prices), through costs
(input inflation vs pricing power, [04.2](../04-financial-analysis/02-margins-and-cost-structure.md)), and
through the discount rate (nominal rf embeds expected inflation). The consistency rule from [06.2](../06-valuation/02-cost-of-capital.md)
— nominal with nominal — means that a rise in expected inflation is *roughly* neutral for a company with full
pricing power (higher g, higher r) and *negative* for one without (higher r, same g, lower margins).

September 2026: CPI 4.82% in August (highest since Dec-2024), WPI 9.9% ([Trading Economics](https://tradingeconomics.com/india/inflation-cpi);
[Crisil](https://www.outlookbusiness.com/opinions-and-blogs/next-phase-of-indias-inflation-cycle-may-already-be-taking-shape-crisil-economist)),
with the gap between wholesale and consumer inflation signalling *input-cost pressure not yet passed to
consumers* — a margin squeeze coming for companies without pricing power, and a test of moats
([05.3](../05-business-analysis/03-moats-and-competitive-advantage.md)) for those with it.

## 3. The rupee

A weaker INR raises revenue and margins for exporters (IT services, pharma exports, textiles, auto components —
roughly 30–50 bps of EBIT margin per 1% depreciation for IT, net of hedges) and raises costs for importers
(oil marketing companies, airlines, electronics assemblers, companies with USD debt). It also drives the
inflation–rates loop (imported inflation → RBI). The rupee's drivers — crude (India imports ~85% of its oil),
FPI flows, the dollar, RBI intervention — are themselves the macro variables of other sectors, so the exposures
compound: a crude spike weakens the rupee, hurts OMCs twice and helps IT once.

## 4. RBI policy transmission

| RBI instrument | Transmission | Lag | Equity effect |
|:--|:--|:--|:--|
| Repo rate (5.25%, on hold since mid-2026 with a neutral stance; 125 bps of cuts in 2025 — [ClearTax](https://cleartax.in/s/repo-rate)) | Bank lending rates (repo-linked retail loans immediately; MCLR with a lag), deposit rates, G-sec yields | 0–6 months | Banks' NIMs; borrowers' costs; discount rates |
| Liquidity (CRR, OMOs, VRR/VRRR) | Short-term rates, credit availability, NBFC funding | Weeks | NBFC spreads; CP markets |
| Macroprudential (risk weights on unsecured/NBFC loans; LTV caps) | Credit growth in targeted segments | Quarters | Consumer lenders, fintech, MFIs |
| FX intervention | Rupee path | Days | Exporters/importers |
| Regulatory (ECL for banks from Apr-2027; gold-loan rules; scale-based NBFC norms) | Provisions, capital, business models | Years | [08.1](../08-sectors/01-banks-and-lending.md) |

The stance matters as much as the rate: a "neutral" RBI facing 5% CPI with a weak rupee is more likely to hold or
tighten than to cut — which changes the rate assumption in every model built during the 2025 cutting cycle.

## 5. Fiscal policy and government capex

The Union Budget sets the demand for a third of the industrial universe: capex of ₹12.2 lakh Cr for FY27, railways
₹2.9 lakh Cr, defence capital ₹2.2 lakh Cr ([08.5](../08-sectors/05-industrials-capital-goods-defence.md)). The
fiscal deficit path (consolidation toward ~4.5% of GDP and a debt-to-GDP anchor — verify the current targets)
determines how long that lasts; state finances determine whether state agencies pay their bills (Kaveri's solar
receivables are a state-finance exposure). Tax changes (GST rationalisation in 2025; income-tax cuts) move
consumption; PLI and duties move manufacturing ([05.2 §7](../05-business-analysis/02-industry-analysis.md)).

## 6. Crude and commodities

Crude is India's macro swing factor: above $100/bbl (as in 2026) it widens the current account, weakens the
rupee, raises inflation, squeezes OMC marketing margins and airline costs, lifts upstream producers, and
pressures fiscal room via LPG compensation. Other commodities matter by sector: copper and steel (Kaveri's
gross margin; autos; durables), palm oil and crude derivatives (FMCG, paints), coal (power, cement, steel), gold
(jewellers, gold-loan NBFCs), agricultural prices and the monsoon (rural demand: two-wheelers, tractors, FMCG,
pumps).

## 7. The earnings cycle

Aggregate corporate earnings in India move in cycles of 3–7 years driven by credit, capex and commodity margins:
FY04–08 (capex and credit boom), FY09–13 (post-crisis fade; corporate NPAs), FY14–20 (weak; bank clean-up),
FY21–24 (margin expansion, deleveraging, PSU and bank profits), FY25–26 (slowing: Nifty EPS growth in single
digits; margins peaking; banks' NIMs compressing). Where the cycle sits determines whether "normalised" margins
are above or below current ones ([07.3](../07-special-valuation/03-cyclicals-and-commodities.md)) and how much of a
low index multiple (19.5x, below its 5-year median of ~22x — [IndexPE](https://indexpe.in/nifty-50)) is cheapness
versus earnings risk.

## 8. Top-down vs bottom-up

Bottom-up investors use macro in three limited ways: (i) as *inputs* to valuation (rf, inflation, FX), updated
when they move; (ii) as *scenarios* for sector-specific risks (crude for OMCs, monsoon for rural names); and
(iii) as a *portfolio audit* — the table below, applied to every holding, to see which single variable the
portfolio is really long or short. What they do not do is forecast the variable and position for it — the base
rate for macro forecasting is poor, and the edge is in the companies.

## 9. The sector × macro matrix

| Sector | Rates | Inflation | INR (weaker) | Crude (higher) | Fiscal capex | Monsoon/rural | Flows |
|:--|:--|:--|:--|:--|:--|:--|:--|
| Banks | NIM (cuts −, hikes +); credit demand | Credit cost via borrowers | — | — | + (PSU lending) | Rural credit quality | Deposit competition |
| NBFCs | Funding cost (−) | | | | | Vehicle/MFI books | Bond-market access |
| IT services | Valuation duration (−) | Wage inflation | **+** | — | — | — | FPI-heavy ownership |
| FMCG | Duration (−) | Input costs (−), pricing power test | Palm/crude derivatives (−) | Packaging (−) | GST | **+** demand | |
| Autos | Financing (−) | Steel/aluminium (−) | Imports (−); exports (+) | Fuel (−) | Roads (+) | **+** 2W/tractors | |
| Capital goods/defence/rail | Capex hurdle | Steel (−) | Imports (−) | | **++** | | |
| Pharma | | | **+** exports | | | | FDA, US policy dominate |
| Metals/cement | Capex (−) | Realisation (+) | Import parity (+) | Energy (−) | **+** demand | | China dominates |
| Oil & gas | | | OMCs (−); upstream (+) | OMCs (−−); upstream (++) | Excise policy | | |
| Power/utilities | Duration (−) | Regulated pass-through | Imported coal (−) | | **+** | Demand | |
| Real estate | **−−** (EMIs) | Construction cost (−) | | | | | HNI flows |
| Telecom | Levered (−) | Tariffs | Equipment (−) | | Spectrum policy | | |
| Small caps generally | (−) | | | | | | **DII/SIP flows dominate** |

Flows deserve a line of their own in 2026: DIIs put a record ₹8.5 lakh Cr into equities in FY26 while FPIs
withdrew ₹1.8 lakh Cr, taking FPI ownership of NSE-listed stocks to a 15-year low of 15.8% and DIIs to 17%
([SEBI annual report via OmmCom](https://ommcomnews.com/business-news/rs-8-5-lakh-crore-dii-inflows-dwarf-fpi-outflows-in-fy26-sebi/)).
Domestic flows have replaced foreign flows as the marginal buyer — which supports valuations while SIPs continue
and is the regime risk if they stop ([12.2](02-market-cycles-and-sentiment.md)).

!!! tip "Trader's lens"
    Macro for a stock-picker is the factor exposure report. You would not run a vol book without knowing its
    net vega and rate sensitivity; do not run an equity book without knowing its net rate duration, crude beta,
    rupee beta and flow dependence. The matrix above is the risk report; the hedges are in
    [11.7](../11-process/07-fundamentals-meets-derivatives.md); and the discipline is the same — measure the
    exposure, decide whether you want it, and hedge what you don't.

!!! info "India notes"
    - Data sources: RBI (policy statements, DBIE database), MOSPI (CPI, IIP, GDP), PPAC (crude and fuel),
      CEA (power), Budget documents, SEBI flow data — all free ([05.7](../05-business-analysis/07-scuttlebutt-and-primary-research.md)).
    - The new CPI series (base 2024 = 100, from 2026) changes weights; compare like with like when reading
      inflation history.
    - India's rate cycle is short and RBI communication matters: read the MPC statement and minutes, not the
      headline.

!!! warning "Common mistakes"
    - Using a stale risk-free rate in every model (rebuild rf from today's G-sec).
    - Mixing real and nominal.
    - Forecasting macro and positioning for it with single stocks.
    - Not knowing the portfolio's aggregate exposure (ten "unrelated" small caps all long domestic flows).
    - Treating a low index P/E as cheap without the earnings-cycle context.

## Key terms

| Term | Meaning |
|:--|:--|
| **Equity duration** | Sensitivity of equity value to the discount rate; ≈ 1/(r − g) for a growing perpetuity |
| **Earnings yield** | Earnings ÷ price; the inverse of P/E |
| **Repo rate / stance** | RBI's policy rate and its bias (accommodative, neutral, withdrawal) |
| **Transmission** | The pass-through of policy rates to lending and deposit rates |
| **Macroprudential** | Regulatory tools (risk weights, LTV caps) targeting credit segments |
| **Fiscal deficit / capex** | Government borrowing and capital spending |
| **Current account** | Trade and income balance; crude is India's largest import |
| **Earnings cycle** | Multi-year swings in aggregate corporate profits |
| **Top-down / bottom-up** | Investing from macro to stocks / from stocks with macro as input |
| **Flow regime** | The dominant marginal buyer (FPI vs DII/SIP) and its stability |

## Check your understanding

1. Rebuild Kaveri's base value with the G-sec at 7.07% instead of 6.5% (from [06.3 §8](../06-valuation/03-dcf-step-by-step.md)) and
   express the change as an implied duration.
<details><summary>Answer</summary>WACC rises ~55 bps to 12.74%; value falls from ₹320 to ~₹293, −8.4% for +0.55 pp →
duration ≈ 15, matching 1/(12.19% − 5.5%) ≈ 15.</details>

2. Crude rises to $110 and stays. List the first-order effect on OMCs, upstream, IT services, FMCG and the RBI.
<details><summary>Answer</summary>OMCs: marketing margins turn negative if pump prices are frozen (−); upstream:
higher realisations net of windfall tax (+); IT: rupee weakens → margins (+); FMCG: packaging and crude-derivative
inputs (−), plus weaker rural demand if inflation rises; RBI: imported inflation and a weaker rupee → less room to
cut, possible tightening (rates −).</details>

3. Why does a "neutral" RBI stance at 5.25% with CPI at 4.8% and rising matter more to a small-cap growth
   portfolio than to a bank?
<details><summary>Answer</summary>Small-cap growth stocks are long-duration and flow-dependent: a rate path that
stops falling (or rises) lowers their DCF values most and competes with SIP flows; a bank's NIM actually benefits
from a pause in cuts. Same macro, opposite sign.</details>

4. Your portfolio is ten Indian small caps. What is its dominant macro exposure, and how would you know?
<details><summary>Answer</summary>Almost certainly domestic flows (DII/SIP) and liquidity, then rates (duration).
Know it by tallying the matrix for each holding and by checking the correlation of the portfolio with the
small-cap index and with monthly SIP data.</details>

## Go deeper

- RBI Monetary Policy Statements and MPC minutes (rbi.org.in) — read the latest before updating any model's rf.
- The Union Budget's "Budget at a Glance" and the Economic Survey — the fiscal and capex frame.
- Aswath Damodaran's notes on equity duration and rates.
- [12.2 Market cycles & sentiment](02-market-cycles-and-sentiment.md) — flows and valuation regimes.
- Sources cited: [ClearTax repo rate](https://cleartax.in/s/repo-rate); [Trading Economics CPI](https://tradingeconomics.com/india/inflation-cpi);
  [IndexPE Nifty P/E](https://indexpe.in/nifty-50); [SEBI FY26 flows via OmmCom](https://ommcomnews.com/business-news/rs-8-5-lakh-crore-dii-inflows-dwarf-fpi-outflows-in-fy26-sebi/).

---
[← Previous: 11.7 Fundamentals × derivatives](../11-process/07-fundamentals-meets-derivatives.md) · [Module index](index.md) · [Next: 12.2 Market cycles & sentiment →](02-market-cycles-and-sentiment.md)
