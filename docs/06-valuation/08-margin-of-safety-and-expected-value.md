# 06.8 · Margin of safety, expected value & asymmetry

> **Why this matters:** you have now built a value of ₹320 for a stock priced at ₹390, with a bear case of ₹168
> and a bull case of ₹416. The decision is not "is ₹320 right?" — it never will be exactly — but "given how wrong I
> could be, does this price pay me to take the risk?" That is what margin of safety means when you stop treating
> it as a slogan and start treating it as a distribution. This lesson turns the valuation outputs of Module 06 into
> a decision input for Module 11.

**Learning objectives** — after this lesson you can:

- Restate Graham's margin of safety as a statement about the distribution of value, not a fixed discount.
- Compute expected value and payoff asymmetry across scenarios, and explain why downside analysis comes first.
- Run a simple Monte-Carlo simulation of a DCF's inputs and read the resulting value distribution.
- Connect uncertainty in value to position sizing (a preview of Kelly and the max-loss rule in
  [11.4](../11-process/04-position-sizing-and-portfolio-construction.md)).
- State, for Kaveri at ₹390, exactly what would have to change for it to become attractive — and at what price it
  already is.

**Prerequisites:** [06.4 DCF in practice](04-dcf-in-practice.md), [06.6 Reverse DCF & expectations](06-reverse-dcf-and-expectations.md)  ·  **Time:** ~80 min

---

## 1. Margin of safety, restated

Benjamin Graham's idea: buy only when price is well below your estimate of value, so that errors in the estimate,
bad luck and the unknowable are absorbed before you lose money. The traditional rule of thumb — "a third off" — is a
crude way of saying something precise:

> Your estimate of value is a random variable with a mean and a spread. The margin of safety is the distance
> between price and that distribution, measured in units of its spread.

Three consequences that the slogan hides:

1. **The required margin depends on the spread.** A 20% discount to a value you can estimate within ±10% (a
   regulated utility) is a large margin; a 40% discount to a value you can only place within ±60% (a biotech, a
   turnaround) is a small one.
2. **The margin is about the downside, not the mean.** A stock priced at your mean value with a fat left tail is
   dangerous; one priced *above* your mean with almost no downside (net cash, hard assets, contracted revenue) may
   be fine.
3. **Uncertainty is not symmetric.** Business risks are skewed: things break faster than they are built. The left
   tail of a value distribution is usually longer than the right — which is why downside analysis comes first.

!!! tip "Trader's lens"
    Margin of safety is the edge divided by the standard error of the edge — a Sharpe ratio for one position. A
    2% mispricing with a 1% estimation error is a better trade than a 30% mispricing with a 40% error. And
    because business outcomes are negatively skewed, the "expected value" of an equity position is like the P&L of
    a short-put book: mostly small positive, occasionally large negative. The margin of safety is the premium you
    demand for that skew.

## 2. Downside first

Before any upside analysis, answer: **what can I lose, and how likely is it?** Not the worst imaginable case — the
plausible bad case — and the mechanism by which it happens.

| Downside source | Kaveri | Sizing |
|:--|:--|:--|
| Operating bear case | State dues stuck; growth 3–8%; margin 12–13%; NWC stays high | ₹168/share (−57% from ₹390) — the reference bear case |
| Balance-sheet stress | Working-capital lines cut; forced provisioning; rights issue | The stress test in [04.5](../04-financial-analysis/05-leverage-solvency-liquidity.md) showed no insolvency, but a ₹60 Cr write-off would cut PAT by ~50% in the year it lands |
| Governance jump | Pledge invocation; related-party revelations; auditor issues | Historical base rate for Indian small caps with a governance score of ~7: a meaningful minority suffer a 30%+ gap-down within three years (order-of-magnitude judgement, not a statistic) |
| De-rating | Multiple falls from 26x to the 15–18x an ex-growth industrial commands, even with flat earnings | ₹15.1 × 16 = ₹240 (−38%) with no change in profit |
| Liquidity | Small cap; exit takes days in a drawdown | Impact cost of 2–5% on the way out |

The de-rating line is the one most investors forget. Kaveri does not need to have a crisis to lose you a third of
your money; it only needs to stop being seen as a growth company.

## 3. Expected value and asymmetry

With scenario values and probabilities, the expected value and the payoff asymmetry are arithmetic:

| Scenario | Probability | Value | Return from ₹390 | Prob. × return |
|:--|--:|--:|--:|--:|
| Bear | 25% | ₹168 | −56.9% | −14.2% |
| Base | 50% | ₹320 | −17.9% | −9.0% |
| Bull | 25% | ₹416 | +6.7% | +1.7% |
| **Expected** | | **₹306** | **−21.5%** | |

$$\text{Upside/downside ratio} = \frac{P(\text{up}) \times \text{gain}}{P(\text{down}) \times \text{loss}}
= \frac{0.25 \times 6.7\%}{0.75 \times \bar{L}}$$

where the probability-weighted loss across bear and base is (0.25 × 56.9 + 0.50 × 17.9)/0.75 = 30.9%, giving a
ratio of 1.7 / 23.2 ≈ **0.07**. For a long position you want this ratio comfortably above 1 — typically 2–3 for a
concentrated position. At ₹390 Kaveri is not a marginal call; it is the wrong side of a lopsided bet.

Now find the price at which it *becomes* a reasonable bet. Holding the scenario values fixed:

| Entry price | Expected return | Upside/downside ratio | Verdict |
|:--|--:|--:|:--|
| ₹390 | −21.5% | 0.07 | Avoid |
| ₹306 (= EV) | 0% | 1.0 | Fair — no margin |
| ₹260 | +17.7% | 3.0 | Attractive: base and bull pay well; bear loses 35% |
| ₹220 | +39.1% | 7.6 | Very attractive: bear loses only 24% |
| ₹168 (= bear) | +82% | large | Priced for the bear case |

```python
scen = {"bear": (0.25, 168), "base": (0.50, 320), "bull": (0.25, 416)}
def ev_ratio(price):
    rets = {k: (p, v / price - 1) for k, (p, v) in scen.items()}
    er = sum(p * r for p, r in rets.values())
    up = sum(p * r for p, r in rets.values() if r > 0); dn = -sum(p * r for p, r in rets.values() if r < 0)
    return round(er, 3), round(up / dn, 2) if dn else float("inf")
for px in (390, 306, 260, 220, 168): print(px, ev_ratio(px))
```

This is the practical meaning of margin of safety for Kaveri: **around ₹220–260**, the price at which even the base
case pays a double-digit return and the bear case is survivable. It is also a *watchlist trigger* — a number to
write down now, before the price gets there and the narrative changes.

## 4. From scenarios to a distribution: Monte Carlo

Three scenarios are a coarse distribution. A **Monte-Carlo simulation** draws every uncertain input from a
distribution, runs the DCF thousands of times and produces the full histogram of value. It is not more accurate —
the input distributions are your guesses — but it exposes interactions (a bad growth draw *and* a bad margin
draw) and gives tail probabilities the three-point tree cannot.

```python
import numpy as np
from fi.valuation import dcf_from_drivers, kaveri_base_drivers
d = kaveri_base_drivers(); rng = np.random.default_rng(42); vals = []
for _ in range(10_000):
    g_scale = rng.normal(1.0, 0.20)                 # growth path scaled ±20%
    m_shift = rng.normal(0.0, 0.012)                # margin path shifted ±1.2 pp
    nwc = rng.normal(0.22, 0.03)                    # terminal NWC/revenue
    w = max(0.10, rng.normal(0.1219, 0.006))        # WACC ±60 bps
    ronic = max(0.13, rng.normal(0.18, 0.03))       # terminal return on new capital
    growth = [x * g_scale for x in d["growth"]]
    margin = [max(0.08, x + m_shift) for x in d["ebitda_margin"]]
    nwc_path = [max(0.15, nwc + 0.03), max(0.15, nwc + 0.01)] + [max(0.15, nwc)] * 8
    vals.append(dcf_from_drivers(**{**d, "growth": growth, "ebitda_margin": margin,
                                    "nwc_pct": nwc_path, "wacc": w, "ronic": ronic})["per_share"])
v = np.array(vals)
print(f"mean ₹{v.mean():.0f}  median ₹{np.median(v):.0f}  P10 ₹{np.percentile(v,10):.0f}  P90 ₹{np.percentile(v,90):.0f}")
print(f"P(value < ₹390) = {(v < 390).mean():.0%}   P(value < ₹250) = {(v < 250).mean():.0%}")
# mean ₹324  median ₹316  P10 ₹236  P90 ₹420
# P(value < ₹390) = 83%   P(value < ₹250) = 15%
```

Read the output as a trader reads a P&L distribution: the median (₹316) sits near the base case; the 10th–90th
percentile band is ₹236–420 — a ±30% range that is the honest precision of this valuation; and **83% of the
simulated values are below the ₹390 price**. The simulation does not say Kaveri is worth ₹316; it says that under
these input distributions, paying ₹390 is a bet on the top fifth of outcomes.

Caveats that matter: the inputs were drawn independently (in reality bad growth and bad margins go together —
correlating them fattens the left tail); the distributions are normal (business inputs are skewed); and the
whole exercise inherits the base drivers. Use it to see the *shape*, never to claim a probability to two decimals.

## 5. Uncertainty and position size — a preview

The width of the distribution should set the position size, not just the decision to buy. Two rules from
[11.4](../11-process/04-position-sizing-and-portfolio-construction.md), previewed here:

- **Kelly-style sizing** says the optimal fraction of capital to bet is proportional to edge ÷ variance: a stock
  with 30% expected return and a ±30% value range deserves a much larger position than one with 30% expected return
  and a ±80% range. Most investors use half or quarter Kelly because the inputs are estimates.
- **Max-loss sizing** says: size the position so that the *bear case* loses no more than a fixed fraction of the
  portfolio (say 2–3%). For Kaveri at ₹260 (bear loss −35%), a 3% max-loss rule caps the position at ~8.5% of the
  portfolio; at ₹390 (bear loss −57%) the cap is ~5% — and the expected return is negative anyway.

The point of doing valuation as a distribution is that it feeds both rules directly. A single target price feeds
neither.

## 6. Kaveri: what would have to change

Bring the module together in one table — the conditions under which the conclusion flips, each tied to an
observable:

| For Kaveri to be attractive at ₹390, you need… | Observable test | Where you would see it |
|:--|:--|:--|
| Bull-case operating outcome as the *base* case: 15%+ growth, margin → 16.5%, NWC → 19% | Two quarters of 15%+ growth with receivable days < 80 and EBITDA margin > 15% | Q2–Q3 FY27 results; investor presentation (if the KPI returns) |
| Or a lower market cost of equity (~11.5%) applied consistently | Nifty and peer multiples holding or rising while G-secs fall | Macro — [12.1](../12-macro-special-sits/01-macro-for-equity-investors.md) |
| Or a price near ₹220–260 with the base case intact | The stock falling ~35–45% without the bear case materialising (e.g., a market-wide small-cap sell-off) | Price; check that receivables and provisioning have not worsened |
| And no governance deterioration | Pledge not rising; RPT purchases stable as % of costs; no auditor/KMP changes | SAST filings; annual report; announcements |

That is the output of an entire valuation module for one company: not a target price, but a *map* of prices and
events to decisions. It goes into the memo in [11.3](../11-process/03-writing-an-investment-memo.md) and the
monitoring plan in [11.5](../11-process/05-monitoring-and-selling.md).

!!! info "India notes"
    Indian small caps have historically shown larger drawdowns than the index in sell-offs (2008, 2018, the 2024–25
    correction — verify magnitudes), and liquidity vanishes at exactly the moment a margin of safety is tested. Add
    an explicit liquidity haircut to the bear case for any stock where your position would exceed a few days of
    average traded value, and prefer to *set* watchlist prices in calm markets rather than decide in falling ones.

!!! warning "Common mistakes"
    - Treating "a third off my DCF" as a margin of safety regardless of how uncertain the DCF is.
    - Computing expected value with probabilities chosen to make the answer positive.
    - Ignoring the de-rating path — a stock can lose 40% with earnings flat.
    - Running a Monte Carlo with independent normal inputs and quoting the tail probabilities as if they were real.
    - Buying at fair value with no margin because "the base case is conservative" — the base case is the *mean*, and
      you need the price below the *distribution*.
    - Letting the decision drift with the narrative instead of the pre-written triggers.

## Key terms

| Term | Meaning |
|:--|:--|
| **Margin of safety** | The gap between price and estimated value, judged relative to the uncertainty of the estimate |
| **Expected value** | Probability-weighted average of scenario values |
| **Upside/downside ratio** | Probability-weighted gain ÷ probability-weighted loss from the current price |
| **Payoff asymmetry** | The shape of the return distribution — skew — from an entry price |
| **Downside analysis** | Identifying and sizing the plausible bad cases before the upside |
| **De-rating** | A fall in the valuation multiple independent of earnings |
| **Monte-Carlo simulation** | Repeated random sampling of inputs to produce a distribution of outputs |
| **Percentile band (P10–P90)** | The range containing the central 80% of simulated values |
| **Kelly criterion** | Bet size proportional to edge ÷ variance; usually applied fractionally |
| **Max-loss rule** | Position size chosen so the bear case costs no more than a fixed share of the portfolio |
| **Watchlist trigger** | A pre-set price or event at which a decision is re-examined |

## Check your understanding

1. Compute the expected return and upside/downside ratio for Kaveri at ₹280 with the reference scenarios.
<details><summary>Answer</summary>Returns: bear −40.0%, base +14.3%, bull +48.6%. Expected = 0.25 × (−40.0) + 0.5 ×
14.3 + 0.25 × 48.6 = −10.0 + 7.1 + 12.1 = +9.3%. Up = 7.1 + 12.1 = 19.3; down = 10.0; ratio 1.9. Borderline
interesting — a modest margin.</details>

2. Two stocks each have expected return +20%. A: values ₹80/₹120/₹150 (25/50/25) at price ₹100. B: values
   ₹40/₹130/₹200 at ₹100. Which has the larger margin of safety, and why is the expected return not enough?
<details><summary>Answer</summary>A: EV = 20 + 60 + 37.5 = 117.5 (+17.5%); B: EV = 10 + 65 + 50 = 125 (+25%).
B has the higher expected return but a 60% loss in its bear case vs 20% for A. Margin of safety is about the
distribution: A's worst case is survivable and its estimate is tighter; B needs a smaller position for the same
risk budget. Expected return ignores the variance and skew that sizing depends on.</details>

3. Why does a Monte-Carlo with independent inputs understate the left tail?
<details><summary>Answer</summary>Because bad outcomes cluster: a demand shock lowers growth *and* margins *and*
raises working capital at the same time. Independent draws average these out; correlated draws (or scenario trees,
which are implicitly correlated) produce fatter tails.</details>

4. Kaveri's P10–P90 band is ₹236–420. What is the "precision" of the valuation, and how should that affect the
   required discount?
<details><summary>Answer</summary>Roughly ±30% around the median — the honest precision of a small-cap industrial
DCF. With that spread, a 20% discount to the median is within the noise; a meaningful margin needs the price near or
below the P10–P25 range (₹236–272), which is consistent with the ₹220–260 trigger from the scenario analysis.</details>

5. State the difference between a margin of safety and a low P/E.
<details><summary>Answer</summary>A low P/E is a price relative to one year's earnings; a margin of safety is a
price relative to the distribution of intrinsic value. A 6x P/E on peak cyclical earnings or on a governance-flagged
company can carry no margin at all; a 30x P/E can carry one if the value distribution sits well above the price.</details>

## Go deeper

- Benjamin Graham, *The Intelligent Investor*, chapter 20, "Margin of Safety as the Central Concept of Investment".
- Seth Klarman, *Margin of Safety* (1991) — out of print; the chapters on risk and on the "value of uncertainty" are
  the modern statement.
- Michael Mauboussin, *The Success Equation* and his notes on base rates — for the probabilities.
- Howard Marks, memos "Risk Revisited" (2014) and "The Most Important Thing" — on downside first.
- [11.4 Position sizing & portfolio construction](../11-process/04-position-sizing-and-portfolio-construction.md) — where this lesson's distribution becomes a position.

---
[← Previous: 06.7 Other valuation methods](07-other-valuation-methods.md) · [Module index](index.md) · [Next: 07.1 Banks & NBFCs →](../07-special-valuation/01-banks-and-nbfcs.md)
