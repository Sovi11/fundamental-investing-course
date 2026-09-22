# 06.4 · DCF in practice: sensitivity, scenarios, mistakes

> **Why this matters:** a DCF that produces one number is a false precision machine. The same model, used
> properly, produces a *distribution* — a base case, the range around it, the scenarios that bound it, and a clear
> statement of which assumptions matter. That is what an investment decision needs. This lesson turns the Kaveri
> reference DCF into that distribution and catalogues the fifteen ways DCFs usually go wrong.

**Learning objectives** — after this lesson you can:

- Build and read two-way sensitivity tables and know which pairs of inputs to tabulate.
- Construct bull/base/bear scenarios that are internally consistent stories, assign probabilities, and compute a
  probability-weighted value.
- Interpret the terminal value's share of EV and the "implied exit multiple" as sanity checks.
- Recognise the fifteen most common DCF mistakes in your own and other people's models.
- Present a DCF honestly: value as a range with named drivers, not a target price.

**Prerequisites:** [06.3 DCF step by step](03-dcf-step-by-step.md)  ·  **Time:** ~90 min

---

## 1. Sensitivity tables

A **sensitivity table** varies two inputs across a grid and shows the value at each combination. It answers "how
wrong can I be before the conclusion changes?" The classic pair is WACC × terminal growth, because those are the
inputs analysts argue about most and the ones with the least evidence behind them.

### 1.1 WACC × terminal growth (Kaveri, base-case operating assumptions)

| WACC \ g | 4.0% | 4.5% | 5.0% | **5.5%** | 6.0% |
|:--|--:|--:|--:|--:|--:|
| 11.2% | ₹350 | ₹359 | ₹369 | ₹381 | ₹395 |
| 11.7% | ₹324 | ₹331 | ₹339 | ₹348 | ₹359 |
| **12.2%** | ₹301 | ₹307 | ₹313 | **₹320** | ₹328 |
| 12.7% | ₹281 | ₹285 | ₹290 | ₹296 | ₹302 |
| 13.2% | ₹263 | ₹266 | ₹270 | ₹274 | ₹279 |

```python
from fi.valuation import kaveri_reference
print(kaveri_reference()["sensitivity"].round(0))
```

Reading it: the *entire* grid — every combination of a plausible WACC (11–13%) and terminal growth (4–6%) —
sits below the ₹390 price. That is a stronger statement than "the base case is ₹320": it says no reasonable
discount-rate or terminal-growth choice rescues the price *with these operating assumptions*. If the price is
right, the operating forecast must be wrong. That directs the next table.

### 1.2 Growth × margin (the operating pair)

| 10-yr revenue CAGR \ terminal EBITDA margin | 13.5% | 14.5% | **15.5%** | 16.5% | 17.5% |
|:--|--:|--:|--:|--:|--:|
| 8.1% | ₹214 | ₹241 | ₹268 | ₹295 | ₹322 |
| **10.8% (base)** | ₹255 | ₹287 | **₹320** | ₹352 | ₹385 |
| 12.9% | ₹293 | ₹331 | ₹369 | ₹407 | ₹445 |
| 15.1% | ₹338 | ₹383 | ₹427 | ₹471 | ₹515 |

(Grid generated with `fi.valuation.sensitivity` over `dcf_from_drivers`; growth rows scale the base path by 0.75×,
1×, 1.2× and 1.4×; margin columns shift the whole margin path.) Here the price *is* reachable: roughly 13% growth
with a 16% margin, or 15% growth with ~14.5%. Now the debate is concrete — is 13–15% ten-year growth with margins at
the best peer's level a base case or a bull case?

```python
from fi.valuation import dcf_from_drivers, kaveri_base_drivers, sensitivity
d = kaveri_base_drivers()
def val(cagr_scale, margin):
    g = [x * cagr_scale for x in d["growth"]]
    m = [margin - (0.155 - x) for x in d["ebitda_margin"]]    # shift the whole margin path
    return dcf_from_drivers(**{**d, "growth": g, "ebitda_margin": m})["per_share"]
tbl = sensitivity(val, rows={"cagr_scale": [0.75, 1.0, 1.2, 1.4]}, cols={"margin": [0.135, 0.145, 0.155, 0.165, 0.175]})
```

Rules for sensitivity tables: pick pairs that are *independent* (WACC and g; growth and margin) rather than pairs
that move together; centre the grid on the base case; extend it far enough to include the market price so the
reader can see what it takes; and never show a table without saying which cell you believe.

## 2. Scenarios

Sensitivities vary inputs mechanically. **Scenarios** vary them *together* as coherent stories, which is how the
world actually moves: if state dues stay stuck, growth is lower *and* margins are lower *and* working capital is
higher, all at once.

### 2.1 Kaveri's three scenarios (from the reference valuation)

| | Bear | Base | Bull |
|:--|:--|:--|:--|
| Story | The two state agencies delay further; Kaveri slows solar bidding; provisions; motors ramp stalls; copper stays high | Dues clear over 2 years; solar grows selectively; Hosur ramps to 75–80% utilisation; margins recover toward FY24 | Dues clear within a year; a large tender pipeline; industrial motors win share; margins reach the best peer's |
| Revenue growth path | 3% FY27, then 7–8%, fading to 5% | 10%, 14%, 14%, 13%, … 7% | 15%, 17%, 16%, 15%, … 8% |
| EBITDA margin | 12.0% → 13.0% | 13.3% → 15.5% | 14.0% → 16.5% |
| NWC / revenue | 29% → 27% | 25% → 22% | 23% → 19% |
| WACC, g, RONIC | unchanged | 12.19%, 5.5%, 18% | unchanged |
| **Value / share** | **₹168** | **₹320** | **₹416** |
| Probability | 25% | 50% | 25% |

$$\text{Probability-weighted value} = 0.25 \times 168 + 0.50 \times 320 + 0.25 \times 416 = \mathbf{₹306}$$

```python
r = kaveri_reference()
print({k: round(v) for k, v in r["scenarios"].items()}, round(r["probability_weighted"]))
# {'Bull': 416, 'Base': 320, 'Bear': 168} 306
```

Three design rules:

1. **Scenarios are stories, not haircuts.** "Bear = base × 0.8" is not a scenario. Each one should name the
   specific things that happen and derive the drivers from them.
2. **Keep WACC constant across scenarios.** Risk is being handled in the cash flows; changing the discount rate too
   double-counts ([06.2](02-cost-of-capital.md)).
3. **Probabilities are a judgement — write down why.** 25/50/25 is a default; Kaveri's say-do record
   ([05.5](../05-business-analysis/05-management-and-capital-allocation.md)) and governance score
   ([05.6](../05-business-analysis/06-corporate-governance-india.md)) might justify 35/45/20, which gives
   0.35 × 168 + 0.45 × 320 + 0.20 × 416 = **₹286**. The point is that the weights are visible and arguable.

### 2.2 What the scenarios tell you that the base case cannot

- The **downside** (₹168, −57% from ₹390) is far larger than the **upside** (₹416, +7%). At ₹390 the payoff is
  asymmetric *against* you: a 25% chance of losing half against a 25% chance of a single-digit gain. This is the
  margin-of-safety argument of [06.8](08-margin-of-safety-and-expected-value.md) in numbers.
- The **base case alone** (₹320) would be a "watch" verdict; the distribution makes it an "avoid at this price".
- The bear case identifies the **monitoring variables**: state payment news, receivable days, provisioning,
  Hosur utilisation. If those move, the probabilities move, and so does the value.

## 3. Sanity checks on any DCF

| Check | Kaveri reference | Reading |
|:--|:--|:--|
| Terminal value as % of EV | 55% | Normal for a 10-year growth fade; > 75% = the explicit forecast is decorative |
| Implied exit EV/EBITDA | 6.4x FY36 EBITDA | Reasonable for a 5.5%-growth industrial; if it came out at 15x, the terminal inputs are too generous |
| Implied terminal P/E | TV / (NOPAT₃₆ × (1+g)) ≈ 3,639 / 350 ≈ 10.4x forward NOPAT | Consistent with 1/(WACC − g) × (1 − g/RONIC) |
| Reinvestment consistency | Terminal reinvestment 30.6% of NOPAT for 5.5% growth at 18% RONIC | If the model reinvested 10% and grew 5.5%, it would be claiming a 55% RONIC |
| Year-10 ROIC | NOPAT₃₆ / IC₃₆ — check it is not absurd (> 40%) or below WACC | Kaveri's FY36 NOPAT of ₹332 Cr on NWC of ₹807 Cr plus a fixed-asset base growing with capex ≈ D&A implies a ROIC in the high teens — near the FY24 peak, consistent with the 18% terminal RONIC |
| FCFF vs history | FY27 FCFF ₹109 Cr vs FY26 actual FCF ₹13 Cr | Flag it: the model needs the working-capital story to be true |
| Growth vs industry | 10.8% 10-year CAGR vs industry mid-single digits ex-solar | Requires share gain or solar; say so |

## 4. The fifteen most common DCF mistakes

| # | Mistake | Why it is wrong | Fix |
|:--|:--|:--|:--|
| 1 | Terminal g ≥ WACC, or g > long-run nominal GDP | Infinite or implausible value | g ≤ 5–6% in ₹; below WACC by a margin |
| 2 | Growth without reinvestment | Free growth; violates g = RR × ROIC | Use the value-driver terminal; check capex/NWC against growth |
| 3 | Exit multiple as the terminal | Imports today's market pricing; usually a growth multiple applied to a mature year | Value-driver formula; use the multiple only as a check |
| 4 | Explicit period too short (5 years for a 15% grower) | Fade never happens; terminal carries 80%+ | 10 years, with a visible fade |
| 5 | Hockey-stick margins | Margins jump above every peer with no mechanism | Cap at the best peer; require a driver for every step |
| 6 | Double-counting risk | High WACC *and* bear scenarios *and* a big haircut | Systematic risk in WACC; specific risk in scenarios; estimation error in margin of safety |
| 7 | Inconsistent inflation | Real growth with nominal WACC, or USD rates with ₹ flows | Same currency and inflation basis throughout |
| 8 | Ignoring dilution | ESOPs, warrants, convertibles left out | Diluted share count via treasury-stock method; warrant cash in the bridge |
| 9 | Book debt used blindly | Missing leases, guarantees, disputed taxes; or subtracting gross debt without adding cash | Full bridge ([06.3 §7](03-dcf-step-by-step.md)) |
| 10 | Circular WACC | Weights depend on the equity value being computed | Target weights, fixed |
| 11 | Other income in FCFF *and* cash in the bridge | Double-counts the treasury | Exclude other income from EBIT; add cash once |
| 12 | Mid-year convention misapplied | Applied to TV, or forgotten for FCFF | FCFF at t − 0.5; TV at N |
| 13 | Valuation date ≠ price date | Comparing a March value with a September price | Roll forward at $k_e$, or restate the bridge to the latest balance sheet |
| 14 | Working capital as a % of *revenue growth* rather than revenue | Understates the cash absorbed | Model NWC as a level (days or % of revenue); ΔNWC falls out |
| 15 | Reverse-engineering inputs to the price | The model becomes a justification | Set inputs first, from evidence; run the reverse DCF separately and openly ([06.6](06-reverse-dcf-and-expectations.md)) |

Number 15 is the one that matters. Every other mistake is a technical error; this one is a discipline failure,
and it is the default behaviour of anyone who already owns the stock.

## 5. Presenting a DCF

A DCF output for a memo ([11.3](../11-process/03-writing-an-investment-memo.md)) is one table and three sentences:

| | Bear | Base | Bull | Prob.-weighted | Price |
|:--|--:|--:|--:|--:|--:|
| Value / share | ₹168 | ₹320 | ₹416 | ₹306 | ₹390 |
| Probability | 25% | 50% | 25% | | |
| Key assumption | State dues stuck; margin 12–13% | Dues clear in 2 yrs; margin → 15.5% | Dues clear in 1 yr; margin → 16.5% | | |

*Value is most sensitive to the terminal margin and return on new capital (±₹40/share each), then WACC (±₹27 per
50 bps); the working-capital normalisation is worth ₹23/share and is the assumption the next two quarters will test.
The market price of ₹390 requires the bull case's operating outcome at the base case's discount rate, or a ~14%
ten-year growth rate. At the current price the downside (−57%) exceeds the upside (+7%) by a wide margin.*

That is the whole output. A single target price with two decimals is a worse product than this, however much
work went into it.

!!! tip "Trader's lens"
    Scenario weighting is expected-value pricing, and the asymmetry table is the payoff diagram. A trader would
    never take a position with a 25% chance of −57% and a 25% chance of +7% unless paid a large premium to do so
    — and here there is no premium; you are paying ₹390 for an expected ₹306. When the market's price sits above
    your probability-weighted value, you are short a put you did not sell. Reverse DCF tells you the strike.

!!! warning "Common mistakes"
    - Presenting the base case as "the" value.
    - Sensitivity tables that vary only WACC and g — the operating inputs usually matter more.
    - Scenarios built as percentage haircuts rather than stories.
    - Changing WACC across scenarios.
    - Probabilities that are secretly chosen to make the weighted value land near the price.

## Key terms

| Term | Meaning |
|:--|:--|
| **Sensitivity table** | A grid of values across two inputs, holding everything else constant |
| **Scenario** | A coherent set of assumptions describing one way the future could unfold |
| **Probability-weighted value** | Σ (probability × scenario value) |
| **Payoff asymmetry** | The ratio of upside to downside from the current price across scenarios |
| **Terminal value share** | PV of terminal value ÷ enterprise value |
| **Implied exit multiple** | Terminal value ÷ final-year EBITDA (or EBIT); a check on terminal assumptions |
| **Hockey stick** | A forecast in which margins or growth jump implausibly after a flat history |
| **Double-counting risk** | Penalising the same risk in the discount rate, the cash flows and the margin of safety |
| **Roll-forward** | Moving a valuation from its date to today at the cost of equity |
| **Tornado chart** | A ranked bar chart of value sensitivity to each input (see [10.4](../10-modeling/04-scenarios-sensitivities-qa.md)) |

## Check your understanding

1. From the WACC × g table, what is the value at 11.7% WACC and 5.0% g, and what does it mean that the whole table
   is below ₹390?
<details><summary>Answer</summary>₹339. It means no plausible discount-rate/terminal-growth combination justifies
the price under the base operating forecast; the price can only be justified by better operating outcomes (faster
growth, higher margins, quicker working-capital recovery).</details>

2. Recompute the probability-weighted value with 35/45/20 weights. What single fact would justify moving the
   weights that way?
<details><summary>Answer</summary>0.35 × 168 + 0.45 × 320 + 0.20 × 416 = 58.8 + 144.0 + 83.2 = ₹286. A fourth
consecutive quarter of rising >6-month overdues, or a state agency formally disputing a claim, would justify raising
the bear probability.</details>

3. Why should WACC be held constant across the bear, base and bull scenarios?
<details><summary>Answer</summary>The scenarios already capture the company-specific risk in the cash flows; raising
WACC in the bear case would count the same risk twice. WACC reflects systematic risk, which does not change with
the company's receivables outcome.</details>

4. A model shows terminal value at 82% of EV and an implied exit multiple of 16x EBITDA for a company growing 6%
   in the terminal year. What has gone wrong?
<details><summary>Answer</summary>Probably a short explicit period (the fade never happened), a terminal growth or
RONIC too high, or an exit multiple pulled from today's market. A 6%-growth mature company should not command 16x
EBITDA in perpetuity; the terminal assumptions need to be rebuilt with the value-driver formula.</details>

5. Kaveri's FY27 FCFF in the model is ₹109 Cr. Write the sentence you would put in the memo about this number.
<details><summary>Answer</summary>"The model's FY27 free cash flow of ~₹109 Cr compares with ₹13 Cr in FY26 and
depends almost entirely on receivable days falling from 96 toward 80; if Q2–Q3 FY27 results do not show this, the
base case should be re-weighted toward the bear case."</details>

## Go deeper

- McKinsey, *Valuation*, chapter on "Using Multiples" and the scenario-analysis material — the source of the
  sanity-check list.
- Aswath Damodaran, "The Dark Side of Valuation" lectures and his blog posts on scenario vs simulation approaches.
- [10.4 Scenarios, sensitivities & model QA](../10-modeling/04-scenarios-sensitivities-qa.md) — the spreadsheet/Python
  mechanics (data tables, tornado charts, stress tests).
- [06.8](08-margin-of-safety-and-expected-value.md) — from scenarios to a distribution and a position size.

---
[← Previous: 06.3 DCF step by step](03-dcf-step-by-step.md) · [Module index](index.md) · [Next: 06.5 Relative valuation & multiples →](05-relative-valuation-and-multiples.md)
