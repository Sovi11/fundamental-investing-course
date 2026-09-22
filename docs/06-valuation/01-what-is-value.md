# 06.1 · What value is

> **Why this matters:** every technique in this module — DCF, multiples, reverse DCF, residual income — is a way of
> computing one quantity: the present value of the cash a business will hand its owners. If you understand that
> quantity and what drives it, the techniques are bookkeeping. If you don't, the techniques become rituals that
> produce whatever number you wanted. This lesson is the short, rigorous foundation: value = cash, discounted; and
> the three things that move it are growth, return on capital and risk.

**Learning objectives** — after this lesson you can:

- Define intrinsic value and distinguish it from price, book value and relative value.
- Derive the value-driver formula $V = \frac{\text{NOPAT}_1(1 − g/\text{ROIC})}{\text{WACC} − g}$ from a growing
  perpetuity, and use it to show that growth creates value only when ROIC > WACC.
- Explain why a great company can be a bad investment and a mediocre company a good one.
- Separate price, value and expectations, and state what an investor actually bets on.
- Compute the steady-state value of Kaveri Pumps from the formula and reconcile it with the full DCF.

**Prerequisites:** [01.5 Time value of money](../01-markets-101/05-time-value-and-returns-math.md),
[04.3 Returns on capital](../04-financial-analysis/03-returns-on-capital.md)  ·  **Time:** ~75 min

---

## 1. Three kinds of "value"

| Term | Definition | What it is good for | What it is not |
|:--|:--|:--|:--|
| **Intrinsic value** | The present value of all future cash flows the asset will deliver to its owner, discounted at a rate reflecting their risk | The anchor; the number you compare price with | Observable. It is an estimate with a distribution, not a point |
| **Relative value** | What similar assets are priced at (multiples) | A cross-check; a way to see what the market pays for comparable growth/returns | A substitute for intrinsic value — if the peers are mispriced, so is the comparison |
| **Book value** | Accounting equity: assets − liabilities at (mostly) historical cost | A floor for asset-heavy businesses and lenders; the base for ROE | A measure of what the business is worth — brands, people and franchises are not on it |
| **Price** | What the last buyer paid | The thing you compare value with | Value. Price is set by the marginal trade; value by the cash flows |

John Burr Williams (1938) wrote the definition that still stands: the value of any asset is the present value of
its future cash flows. For a bond the cash flows are contractual; for a share they are the dividends and buybacks the
company will pay over its life (equivalently, the free cash flows it generates, since those must eventually be paid
out or reinvested to produce later payouts).

$$V_0 = \sum_{t=1}^{\infty} \frac{CF_t}{(1+r)^t}$$

Everything else in valuation is about estimating $CF_t$ and $r$, and about the shortcuts (multiples, perpetuities)
that make the infinite sum tractable.

## 2. The value-driver formula

Start with the growing perpetuity from [01.5](../01-markets-101/05-time-value-and-returns-math.md): a cash flow of
$CF_1$ next year, growing at $g$ forever, discounted at $r$, is worth

$$V_0 = \frac{CF_1}{r − g} \qquad (g < r)$$

For a business, the cash flow to all capital providers is **free cash flow to the firm**: operating profit after tax
(NOPAT) *minus* the reinvestment needed to grow. From the reinvestment identity in
[04.3](../04-financial-analysis/03-returns-on-capital.md), to grow NOPAT at rate $g$ with a return on new capital of
ROIC you must reinvest a fraction $g/\text{ROIC}$ of NOPAT:

$$\text{FCFF}_1 = \text{NOPAT}_1 − \text{Reinvestment}_1 = \text{NOPAT}_1\left(1 − \frac{g}{\text{ROIC}}\right)$$

Substitute into the perpetuity, with $r = \text{WACC}$:

$$\boxed{V_0 = \frac{\text{NOPAT}_1 \left(1 − \dfrac{g}{\text{ROIC}}\right)}{\text{WACC} − g}}$$

This is the **value-driver formula** (McKinsey's name; the "key value driver" formula). Three inputs — growth,
return on invested capital, cost of capital — and one line of algebra. It is the most important equation in the
course, because it makes precise a claim most investors only hold as intuition.

### 2.1 Growth only creates value when ROIC > WACC

Divide both sides by NOPAT to get the **value multiple** $V/\text{NOPAT}$, and tabulate it for a WACC of 12%:

| ROIC \ g | 0% | 3% | 6% | 9% |
|:--|--:|--:|--:|--:|
| 8% (< WACC) | 8.3x | 6.9x | 4.2x | −4.2x (nonsense: growth needs more reinvestment than NOPAT) |
| **12% (= WACC)** | **8.3x** | **8.3x** | **8.3x** | **8.3x** |
| 16% | 8.3x | 9.0x | 10.4x | 14.6x |
| 24% | 8.3x | 9.7x | 12.5x | 20.8x |
| 40% | 8.3x | 10.3x | 14.2x | 25.8x |

```python
w = 0.12
for roic in (0.08, 0.12, 0.16, 0.24, 0.40):
    print(roic, [round((1 - g / roic) / (w - g), 1) for g in (0.0, 0.03, 0.06, 0.09)])
```

Read the middle row first. **When ROIC equals WACC, the value multiple is 1/WACC = 8.3x regardless of growth.**
Growing at 9% is worth exactly the same as not growing at all, because every rupee reinvested to produce the growth
earns just its cost — the new capital is worth what it cost, no more. Now read down the columns: at ROIC above WACC,
faster growth raises the multiple, steeply; at ROIC below WACC, faster growth *lowers* it. A company earning 8% on
capital that grows at 6% is worth half as much as the same company standing still.

This is why [04.3](../04-financial-analysis/03-returns-on-capital.md) insisted on incremental ROIC, why
[05.3](../05-business-analysis/03-moats-and-competitive-advantage.md) called the moat the largest input to the terminal
value, and why "growth stock" and "value stock" is a false dichotomy: growth is an input to value, with a sign that
depends on ROIC.

### 2.2 Kaveri in steady state

Kaveri's FY26 NOPAT is ₹100.3 Cr. Suppose the company were already in its terminal state — growing 5.5% a year for
ever with a 12.19% WACC (the reference valuation's inputs) — and ask what value different terminal ROICs imply:

```python
nopat = 100.3; w = 0.1219; g = 0.055
for ronic in (0.12, 0.15, 0.18, 0.25):
    v = nopat * (1 + g) * (1 - g / ronic) / (w - g)
    print(ronic, round(v), round((v - 140.5 - 18.2) / 6.07))
# 0.12 → EV ≈ 857, ≈ ₹115/share
# 0.15 → EV ≈ 1,001, ≈ ₹139/share
# 0.18 → EV ≈ 1,098, ≈ ₹155/share
# 0.25 → EV ≈ 1,234, ≈ ₹177/share
```

Two lessons. First, the assumed return on new capital moves the value by 50% across a plausible range — that is the
moat judgement, in rupees. Second, all of these are far below the ₹320 base case and the ₹390 price, which tells you
that most of Kaveri's value in the full DCF comes from the *explicit* forecast years of 10–14% growth at rising
margins, not from the steady state. [06.3](03-dcf-step-by-step.md) builds that forecast; [06.6](06-reverse-dcf-and-expectations.md)
asks whether the price already assumes it.

## 3. Price, value and expectations

Ben Graham's formulation: price is what you pay, value is what you get. The modern refinement (Rappaport and
Mauboussin, *Expectations Investing*) adds a third object: the **expectations embedded in the price**. A stock price
is a forecast — it is the value that results from *some* set of assumptions about growth, ROIC and risk. You do not
need to know intrinsic value with precision; you need to know whether the market's implied assumptions are too
high or too low.

| Object | How you get it | What you do with it |
|:--|:--|:--|
| Price | Observe | — |
| Your estimate of value | Forecast cash flows; discount | Compare with price; size the gap against your uncertainty |
| Market's implied expectations | Solve the DCF backwards for the growth/margin that justifies the price | Ask: is *that* forecast plausible? Where specifically do I disagree? |

!!! tip "Trader's lens"
    This is exactly the implied-vs-realised structure of options. Nobody prices an option by forecasting the
    payoff; they back out the implied vol and ask whether realised vol will be higher or lower. A share price backs
    out implied growth (and implied ROIC persistence). Your edge is a view on *realised* growth vs implied — and,
    as with vol, the view is only worth expressing when the gap is large relative to your estimation error. Reverse
    DCF ([06.6](06-reverse-dcf-and-expectations.md)) is the implied-vol calculator for equities.

## 4. Why a great company can be a bad investment

Take a business with ROIC of 40% and growth of 9% — the top-right cell, 25.8x NOPAT. If the market prices it at
50x NOPAT, the buyer is paying for a return-and-growth combination that the formula cannot produce at a 12% WACC:
they need ROIC to stay at 40% *and* growth to exceed 9% for decades, *or* the cost of capital to be much lower. If
instead growth fades to 6% (still excellent), the multiple should be 14.2x — the investor loses 70% of their money
while the company keeps compounding beautifully. Cisco in 2000 ([case G3](../13-case-studies/global/03-cisco-2000.md))
and Asian Paints at 80x in 2021 ([case I2](../13-case-studies/india/02-asian-paints-compounder.md)) are this cell.

The mirror image: a business with 14% ROIC and 4% growth is worth ~8.9x NOPAT; priced at 6x because it is boring
and out of favour, it offers a 50%+ return to fair value without any heroics. Coal India at single-digit P/Es in
2020–22 had this profile. "Quality" is not a valuation; it is an input.

## 5. What is *not* in the formula — and where it hides

- **Risk** appears only through WACC. In practice you handle it three ways: in the discount rate (systematic risk),
  in the cash-flow scenarios (business-specific risk; [06.4](04-dcf-in-practice.md)), and in the margin of safety
  you demand between value and price ([06.8](08-margin-of-safety-and-expected-value.md)). Never in all three at once
  for the same risk.
- **Time to fade**: the formula assumes ROIC and g are constant for ever. Real companies fade toward WACC; the DCF's
  explicit period plus a terminal assumption is how you model the path.
- **Non-operating assets and claims**: cash, investments, debt, leases, minorities, options — the bridge from
  enterprise value to equity value per share ([06.3](03-dcf-step-by-step.md)).
- **Inflation**: g and WACC must be in the same terms (both nominal ₹ or both real). Indian valuations are almost
  always nominal ₹ with a 5–6% terminal g reflecting ~4% inflation plus modest real growth.

## 6. Worked example — two companies, one formula

**Sahyadri Bearings** (fictional): NOPAT next year ₹120 Cr, ROIC on new capital 20%, sustainable growth 6%.
**Tapti Textiles** (fictional): NOPAT next year ₹120 Cr, ROIC 9%, growth 6%. Both have WACC 12%, net debt ₹200 Cr,
10 Cr shares.

```python
def value(nopat1, roic, g, wacc=0.12, net_debt=200, shares=10):
    ev = nopat1 * (1 - g / roic) / (wacc - g)
    return round(ev), round((ev - net_debt) / shares)
print(value(120, 0.20, 0.06))   # EV 1,400 → ₹120/share
print(value(120, 0.09, 0.06))   # EV 667  → ₹47/share
print(value(120, 0.09, 0.00))   # EV 1,000 → ₹80/share  (Tapti is worth MORE if it stops growing)
```

Same profit, same growth, same risk; Sahyadri is worth 2.5x Tapti per share — and Tapti's shareholders would be
₹33/share better off if management stopped expanding. That last line is the practical content of the formula: for a
sub-WACC business, the best capital allocation is to return cash, and a "growth strategy" is value destruction
with a press release ([05.5](../05-business-analysis/05-management-and-capital-allocation.md)).

!!! warning "Common mistakes"
    - Using the formula with g ≥ WACC (infinite value) or g > ROIC (negative reinvestment) — both are input errors.
    - Applying a high multiple to "quality" without checking that the ROIC–growth combination justifies it.
    - Treating book value as a floor for a business that burns cash — book value can go to zero.
    - Forgetting that NOPAT in the numerator is *next* year's, and that reinvestment is already netted out (do not
      subtract capex again).
    - Mixing real growth with a nominal discount rate.

## Key terms

| Term | Meaning |
|:--|:--|
| **Intrinsic value** | Present value of all future cash flows to the owner, at a risk-appropriate discount rate |
| **Relative value** | Value inferred from the prices of comparable assets (multiples) |
| **Growing perpetuity** | $CF_1/(r − g)$: the value of a cash flow growing at g for ever |
| **Free cash flow to the firm (FCFF)** | NOPAT + D&A − capex − ΔNWC: cash available to all capital providers |
| **Reinvestment rate** | Share of NOPAT reinvested = g / ROIC in steady state |
| **Value-driver formula** | $V = \text{NOPAT}_1(1 − g/\text{ROIC})/(\text{WACC} − g)$ |
| **Value multiple** | $V/\text{NOPAT}$; equals $1/\text{WACC}$ when ROIC = WACC |
| **RONIC** | Return on *new* invested capital, the ROIC that matters for growth's value |
| **Expectations (implied)** | The growth/return assumptions that make a DCF equal the market price |
| **Fade** | The decline of ROIC toward WACC over time as competition acts |
| **Margin of safety** | The gap between estimated value and price demanded to absorb estimation error |

## Check your understanding

1. A company has ROIC = WACC = 11%. Management announces a plan to double growth from 4% to 8% by reinvesting
   more. What happens to value?
<details><summary>Answer</summary>Nothing. With ROIC = WACC the value multiple is 1/WACC = 9.1x NOPAT whatever the
growth rate; the extra reinvestment earns exactly its cost. Shareholders should be indifferent — and suspicious of
the effort, since executing growth carries risk for no reward.</details>

2. Using the value-driver formula, what value multiple does a company with ROIC 30%, g 7%, WACC 12% deserve? What
   if the market prices it at 35x NOPAT — what is it assuming?
<details><summary>Answer</summary>(1 − 0.07/0.30)/(0.12 − 0.07) = 0.767/0.05 = 15.3x. A 35x price implies (holding
ROIC at 30%) g ≈ 10.1% for ever, or (holding g at 7%) a WACC of ~9.2%, or some combination — each of which is far
outside anything the formula finds plausible as a perpetuity.</details>

3. Recompute Kaveri's steady-state value per share with RONIC 18% but g of 4% instead of 5.5%.
<details><summary>Answer</summary>EV = 100.3 × 1.04 × (1 − 0.04/0.18)/(0.1219 − 0.04) = 104.3 × 0.778/0.0819 =
₹991 Cr; equity = 991 − 158.7 = 832; per share ≈ ₹137 — lower than at 5.5% growth (₹155) because with RONIC > WACC,
growth adds value.</details>

4. Why is "value = PV of dividends" consistent with valuing a company that pays no dividends?
<details><summary>Answer</summary>Retained cash either earns a return and funds larger future dividends/buybacks, or
it is wasted. FCFF-based valuation captures the cash that *could* be paid; if management never pays it out and never
earns a return on it, the value is genuinely lower — which the incremental-ROIC term already reflects.</details>

5. Tapti Textiles is worth more not growing than growing at 6%. What should its management do, and what typically
   stops them?
<details><summary>Answer</summary>Stop expanding, run for cash, return it (dividends/buybacks) or repay debt, and try
to raise ROIC (pricing, cost, capital discipline) before growing again. What stops them: incentives tied to size,
empire-building, the belief that scale will fix returns, and lenders/analysts who reward growth.</details>

## Go deeper

- Tim Koller, Marc Goedhart & David Wessels (McKinsey), *Valuation*, chapters 2–3 — the value-driver formula and its
  proof; the whole book is the reference for this module.
- John Burr Williams, *The Theory of Investment Value* (1938), chapter 5 — the original DCF.
- Alfred Rappaport & Michael Mauboussin, *Expectations Investing* (2001; revised 2021) — price as forecast.
- Warren Buffett, 1992 Berkshire letter — on why "growth" and "value" are joined at the hip.

---
[← Previous: 05.7 Scuttlebutt & primary research](../05-business-analysis/07-scuttlebutt-and-primary-research.md) · [Module index](index.md) · [Next: 06.2 Cost of capital →](02-cost-of-capital.md)
