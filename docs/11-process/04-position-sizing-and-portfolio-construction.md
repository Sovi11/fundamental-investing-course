# 11.4 · Position sizing & portfolio construction

> **Why this matters:** two investors with identical stock picks end up with different results because of how
> much they bought, how concentrated they were, and how much cash they held when the market gapped down. Sizing
> is where valuation uncertainty ([06.8](../06-valuation/08-margin-of-safety-and-expected-value.md)), forensic
> risk ([09.7](../09-forensics/07-the-forensic-checklist.md)) and liquidity meet the portfolio. This lesson gives
> the rules — Kelly and its fractions, max-loss, liquidity limits, concentration, cash — and shows why a trader's
> instinct to size by edge-over-variance is right, and why the inputs need humility.

**Learning objectives** — after this lesson you can:

- Compute Kelly-optimal fractions from a scenario tree and explain why fractional Kelly is used.
- Apply the max-loss rule and take the lower of it and fractional Kelly.
- Set liquidity limits from average traded value and impact cost.
- Choose a concentration level and manage factor, sector and correlation exposure.
- Treat cash as a position and manage drawdowns and portfolio-level risk with a pre-mortem.

**Prerequisites:** [06.8](../06-valuation/08-margin-of-safety-and-expected-value.md), [11.3](03-writing-an-investment-memo.md)  ·  **Time:** ~80 min

---

## 1. Kelly: size by edge over variance

The Kelly criterion maximises the expected logarithm of wealth — the long-run growth rate — for a repeated bet.
For a binary bet with probability $p$ of winning $b$ times the stake and $q = 1 − p$ of losing it:

$$f^* = \frac{p\,b − q}{b}$$

For a continuous approximation with expected excess return $\mu − r$ and variance $\sigma^2$:

$$f^* \approx \frac{\mu − r}{\sigma^2}$$

For a scenario tree with returns $r_i$ and probabilities $p_i$, solve numerically for the $f$ that maximises
$\sum_i p_i \ln(1 + f r_i)$.

### 1.1 Kaveri at ₹260 — and why the naive answer is absurd

```python
import numpy as np
def kelly(ps, rs):
    fs = np.linspace(0, 1.0, 2001); best = (0, -1e9)
    for f in fs:
        if any(1 + f * r <= 0 for r in rs): continue
        g = sum(p * np.log(1 + f * r) for p, r in zip(ps, rs))
        best = max(best, (f, g), key=lambda t: t[1])
    return best
# Reference scenarios from ₹260: bear ₹168 (−35%), base ₹320 (+23%), bull ₹416 (+60%)
print(kelly([0.25, 0.50, 0.25], [-0.35, 0.23, 0.60]))          # f* > 100%: the tree has no tail below −35%
# Add a governance-jump tail: 10% chance of −80%
print(kelly([0.10, 0.20, 0.45, 0.25], [-0.80, -0.35, 0.23, 0.60]))   # f* ≈ 0.46 → quarter-Kelly ≈ 12%
print(kelly([0.15, 0.20, 0.40, 0.25], [-0.80, -0.35, 0.23, 0.60]))   # f* ≈ 0.21 → quarter-Kelly ≈ 5%
```

| Scenario tree (from ₹260) | Expected return | Full Kelly | Half | Quarter |
|:--|--:|--:|--:|--:|
| Three-point reference (worst −35%) | +17.7% | > 100% | > 50% | > 25% |
| + 10% chance of a −80% governance jump | +10.3% | 46% | 23% | 12% |
| + 15% chance of −80% | +5.2% | 21% | 11% | 5% |
| Continuous: μ 18%, σ 40%, r 7% | | 69% | 34% | 17% |
| Continuous: μ 12%, σ 45%, r 7% | | 25% | 12% | 6% |

Three lessons:

1. **Kelly is only as good as the tail you feed it.** The three-point tree says "bet everything" because its
   worst case is −35%. Add the tail the forensic checklist warns about and the answer falls by three-quarters.
   Always include a jump scenario for single stocks.
2. **Fractional Kelly is the practice.** Full Kelly assumes you know the probabilities; you don't. Half-Kelly
   gives ~75% of the growth rate with far smaller drawdowns; quarter-Kelly is common for single-stock positions
   where estimation error is large. Use full Kelly as a *ceiling*, never a target.
3. **Kelly sizes for growth, not for sleep.** Even quarter-Kelly implies 40–50% drawdowns are possible over a
   long enough sample; the max-loss rule is the second constraint.

## 2. The max-loss rule

$$\text{Position size} \le \frac{\text{Maximum acceptable loss to the portfolio from this position}}{\text{Bear-case loss}}$$

With a 3% portfolio-loss budget per position: Kaveri at ₹260 (bear −35%) → **8.6%**; at ₹390 (bear −57%) → 5.3%;
with an −80% jump as the reference loss → 3.75%. The rule is crude and that is its virtue: it needs only the
bear case, it caps the damage from being wrong about probabilities, and it scales with the margin of safety.

**Take the lower of fractional Kelly and the max-loss size** (the course's rule; also the rule in the casebook
`PROCESS.md`), then apply the qualitative overlays:

| Overlay | Adjustment |
|:--|:--|
| Forensic/governance rating | Green: none; Amber: halve; Red: no position |
| Liquidity (§3) | Cap at the liquidity limit |
| Thesis maturity | New position: start at half the target, add on confirmation (a fired *positive* breaker) |
| Correlation with existing holdings | Reduce if the thesis variable is shared (two solar-exposed names) |

Kaveri at ₹260 with Amber: min(quarter-Kelly ~5–12%, max-loss 8.6%) ≈ 5–8% → halved for Amber → **~4%**, which
is the memo's number ([11.3](03-writing-an-investment-memo.md)).

## 3. Liquidity

A position you cannot exit is a different position. Limits:

- **Position ≤ N days of average daily traded value (ADV)** at a participation rate you can sustain. Common: the
  position should be exitable in ≤ 5 days at ≤ 20% of ADV — i.e., position ≤ 1× ADV. For a ₹1 Cr portfolio and a
  4% (₹4 lakh) position, a stock with ₹3 Cr ADV is fine (1.3% of one day's volume); a stock with ₹20 lakh ADV is
  not (two days at 100% participation — and in a drawdown, ADV halves).
- **Impact cost**: NSE publishes impact cost for the top stocks; for small caps assume 1–3% each way in normal
  markets and 5–10% in stress; net it from the bear case.
- **Float and holder concentration**: a stock where five holders own 40% of the float gaps on any one of them
  selling.
- **F&O ban / ASM**: surveillance actions restrict trading exactly when you want out
  ([01.4](../01-markets-101/04-indian-market-structure.md)).

## 4. Concentration and diversification

| Number of positions | Character | Suits |
|:--|:--|:--|
| 5–8 | Concentrated; each position 10–20%; every one must be a high-conviction, deeply researched name | Full-time investors with a strong process and a long horizon; the Buffett/Munger model |
| 10–15 | The practical sweet spot for an individual: enough diversification to survive one thesis failure (a 7% position going to zero costs 7%), few enough to know each well | Most readers of this course |
| 20–30 | Diversified; idiosyncratic risk mostly gone; returns converge to the factors you own | Part-time investors; those who want the process without the variance |
| 50+ | An index with extra steps | — |

Diversification arithmetic: with 10 equal positions of 35% vol and 0.5 pairwise correlation, portfolio vol is
~26%; with 25 positions, ~25% — beyond ten or fifteen names, adding stocks removes little risk because the
common factor (correlation) dominates. What *does* reduce risk further is diversifying the **thesis variables**:
ten stocks that all depend on the capex cycle are one position.

Factor and sector exposure: tally the portfolio by sector, by style (value/growth/quality), by size, by
interest-rate sensitivity and by "what has to go right" (thesis variable). A portfolio of researched Indian
small caps is *long* the small-cap factor, *long* domestic flows, *short* liquidity — a regime bet whether or
not you intended it ([12.2](../12-macro-special-sits/02-market-cycles-and-sentiment.md)). Know it; hedge it if you
did not intend it ([11.7](07-fundamentals-meets-derivatives.md)).

## 5. Cash as a position

Cash is the option to buy at the prices a drawdown offers, and the buffer that stops a drawdown from forcing
sales. Indian markets gap: small-cap indices fell 30–60% in 2008, 2018–20 and in the 2024–25 correction (verify
magnitudes), with liquidity vanishing at the lows. Rules of thumb used by concentrated Indian investors: 10–30%
cash through the cycle, higher when the watchlist has no triggers near current prices (which is itself the
valuation signal), lower when triggers are firing. The cost of cash is the yield gap (liquid funds ~6–7% vs
expected equity returns); the benefit is the ability to act when the max-loss rule would otherwise say no.

## 6. Drawdown management and the portfolio pre-mortem

- **Portfolio max-loss**: if every position hit its bear case simultaneously (they correlate in a crash), what is
  the portfolio loss? With ten 5% positions each with −40% bears, −20%; add the market factor and −30% is the
  stress. Decide in advance whether that is acceptable; if not, cut sizes, not conviction.
- **Drawdown rules**: pre-commit to a review (not necessarily a sale) at −15% and −25% portfolio drawdowns:
  re-underwrite every position, re-run the thesis-breakers, check liquidity. The rule exists so that the review
  happens *before* the panic.
- **Portfolio pre-mortem**: "It is 2028 and the portfolio is down 40% while the Nifty is down 15% — how?" The
  answer is usually a shared thesis variable, a liquidity mismatch, or one Red-flag name that was sized as Green.

!!! tip "Trader's lens"
    This is the lesson that translates most directly. Edge/variance sizing, fractional Kelly, max-loss limits,
    liquidity-adjusted position limits, factor exposure, drawdown-triggered reviews — a desk's risk framework
    applied to a slow book. The differences: the "variance" is your own estimation error as much as the stock's
    vol; the tail is a governance jump you cannot hedge; and the feedback loop is years, so the discipline has to
    be pre-committed rather than learned from the P&L in time to matter.

!!! info "India notes"
    - SEBI's mutual-fund rules (10% single-stock cap for schemes) and PMS/AIF norms are useful benchmarks for
      what regulators consider prudent concentration; an individual is free to concentrate more — with the
      liquidity caveat.
    - Small-cap liquidity is thinner than the traded-volume figures suggest: delivery volumes, not gross turnover,
      are the honest ADV.
    - Margin-funded equity (MTF) is available from brokers; leverage on a concentrated small-cap book is how
      max-loss rules get violated by the lender rather than the investor.

!!! warning "Common mistakes"
    - Full Kelly on a three-point scenario tree.
    - Sizing by conviction without a bear case (conviction is not a number).
    - Ignoring liquidity until the exit.
    - Ten positions with one thesis variable.
    - Zero cash in a market with no watchlist triggers in reach.
    - Averaging a max-loss breach into a larger max-loss breach.

## Key terms

| Term | Meaning |
|:--|:--|
| **Kelly criterion** | The bet size that maximises expected log wealth (long-run growth) |
| **Fractional Kelly** | A fixed fraction (half, quarter) of the Kelly size, used because inputs are estimates |
| **Max-loss rule** | Position size ≤ acceptable portfolio loss ÷ bear-case loss |
| **Jump scenario** | A tail outcome (governance, fraud, regulation) added to the scenario tree |
| **ADV** | Average daily traded value |
| **Impact cost** | Price movement caused by one's own trading |
| **Concentration** | Number and weight of positions |
| **Thesis variable** | The driver a position's thesis depends on; the true unit of diversification |
| **Factor exposure** | The portfolio's tilt to size, style, sector, rates, flows |
| **Cash as a position** | Holding cash deliberately as optionality and buffer |
| **Portfolio pre-mortem** | A narrative of how the whole portfolio failed |

## Check your understanding

1. Compute the max-loss size for a stock with a −45% bear case under a 2% loss budget, and the quarter-Kelly size
   if full Kelly is 30%. Which applies?
<details><summary>Answer</summary>Max-loss: 2%/45% = 4.4%; quarter-Kelly: 7.5%. Take the lower: 4.4%; then apply
governance and liquidity overlays.</details>

2. Why does adding a 10% chance of −80% cut the Kelly size from over 100% to 46% when it changes the expected
   return only from +17.7% to +10.3%?
<details><summary>Answer</summary>Kelly maximises log wealth, which is dominated by the worst outcomes: a −80%
result at a 50% position size is a −40% portfolio hit, and the log penalty for large losses is severe. Expected
return is linear; growth is not — tails matter far more to sizing than to the mean.</details>

3. A ₹2 Cr portfolio wants a 6% position in a stock with ₹1.5 Cr delivery ADV. Is it liquid enough?
<details><summary>Answer</summary>Position = ₹12 lakh = 0.8× ADV — exitable in about four days at 20% participation
in normal markets, roughly at the limit; in a stress with ADV halved, eight days. Acceptable at 6% but not larger;
size 4–5% if the thesis has a dated jump risk.</details>

4. Your ten positions are all beneficiaries of government capex. What is the effective number of positions?
<details><summary>Answer</summary>Closer to one or two: the thesis variable (capex continuing) is shared, so the
correlation in the scenario that matters is near 1. Diversify the thesis variables, or size the whole cluster as
one position.</details>

## Go deeper

- Edward Thorp, "The Kelly Criterion in Blackjack, Sports Betting and the Stock Market" (2006) — the canonical
  practitioner's paper.
- William Poundstone, *Fortune's Formula* (2005) — the history and the fractional-Kelly argument.
- Mohnish Pabrai, *The Dhandho Investor* — Kelly-inspired concentration for value investors, and its limits.
- The casebook `PROCESS.md` sizing rule and the terminal's `sizing.py` — the same rules coded.

---
[← Previous: 11.3 Writing an investment memo](03-writing-an-investment-memo.md) · [Module index](index.md) · [Next: 11.5 Monitoring & selling →](05-monitoring-and-selling.md)
