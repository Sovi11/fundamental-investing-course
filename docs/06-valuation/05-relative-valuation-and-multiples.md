# 06.5 · Relative valuation & multiples

> **Why this matters:** most valuation conversations in the market happen in multiples — "it's at 25 times", "the
> sector trades at 12x EBITDA". Multiples are fast, comparable and easy to communicate, which is why they are also
> the easiest way to fool yourself: a multiple is a DCF with the assumptions hidden. This lesson makes the hidden
> assumptions visible, so you can use multiples as a cross-check on intrinsic value rather than a substitute for it.

**Learning objectives** — after this lesson you can:

- Define and compute the standard multiples (P/E, EV/EBITDA, EV/EBIT, P/B, P/S, EV/Sales, FCF yield, dividend
  yield, PEG) with numerator and denominator correctly matched.
- Derive the justified P/E and justified P/B from the Gordon model and explain what each multiple implicitly
  assumes about growth, return and risk.
- Choose a peer set, use trailing vs forward multiples, and read historical valuation bands.
- Explain why Indian multiples are structurally high and what that implies for cost-of-equity assumptions.
- Value Kaveri Pumps against its peer set and reconcile the answer with the DCF.

**Prerequisites:** [06.1 What value is](01-what-is-value.md), [06.3 DCF step by step](03-dcf-step-by-step.md),
[04.6 Per-share metrics & ratio dashboard](../04-financial-analysis/06-per-share-metrics-and-ratio-dashboard.md)  ·  **Time:** ~90 min

---

## 1. What a multiple is

A **multiple** is a price divided by a fundamental: how many rupees of price per rupee of earnings, book value,
sales or cash flow. Two families, and the first rule is never to mix them:

| Family | Numerator | Denominator must be… | Multiples |
|:--|:--|:--|:--|
| **Equity multiples** | Market capitalisation (or price per share) | A flow or stock that belongs to **shareholders only** (after interest) | P/E, P/B, P/S (sloppy — sales belong to everyone), dividend yield, FCFE yield |
| **Enterprise multiples** | Enterprise value = market cap + debt + leases + minorities + preference − cash & investments | A flow that belongs to **all capital providers** (before interest) | EV/EBITDA, EV/EBIT, EV/Sales, EV/FCFF, EV/capacity |

P/EBITDA is a mismatch (equity price over a pre-interest flow) and so is EV/PAT. The mismatch matters most when
leverage differs across the companies being compared.

### 1.1 Definitions and Kaveri at ₹390

| Multiple | Formula | Kaveri (18-Sep-2026) | Notes |
|:--|:--|--:|:--|
| P/E (trailing) | Price ÷ last 12-month EPS | 390 / 15.08 = **25.9x** | On reported EPS; on adjusted EPS the same (no FY26 exceptional) |
| P/E (forward) | Price ÷ next-year EPS estimate | Depends on your FY27 forecast; at a base-case FY27 PAT of ~₹95 Cr, ~24.6x | Consensus is thin for small caps |
| EV/EBITDA | (Mcap + net debt + leases) ÷ EBITDA | (2,340 + 140.5 + 18.2) / 181.9 = **13.7x** | Basic shares × price; leases in EV since EBITDA is after ROU amortisation... see India note |
| EV/EBIT | ÷ EBIT | 2,498.7 / 134.1 = **18.6x** | Better than EBITDA for asset-heavy companies |
| P/B | Price ÷ book value per share | 390 / 117.7 = **3.3x** | Meaningful only with ROE alongside |
| P/S; EV/Sales | ÷ revenue | 1.8x; 1.9x | For loss-makers or margin-normalisation arguments |
| FCF yield | FCF ÷ market cap | 13.1 / 2,340 = **0.6%** | The number that should worry a buyer at ₹390 |
| Dividend yield | DPS ÷ price | 4.0 / 390 = **1.0%** | |
| PEG | P/E ÷ expected EPS growth (%) | 25.9 / 12 ≈ 2.2 | A rule of thumb with no theoretical basis; > 2 is "expensive" in folklore |

!!! info "India notes"
    - Screener.in's P/E uses trailing consolidated EPS when available; its "EV/EBITDA" uses EBITDA *including*
      other income for some layouts. Rebuild multiples yourself from the statements for anything that matters.
    - Since Ind AS 116 (FY20), EBITDA is after the rent that now sits in depreciation and interest; consistency
      requires lease liabilities in EV. Pre-FY20 historical EV/EBITDA bands are not comparable for lease-heavy
      companies (retail, airlines, QSR, hotels) without adjustment.
    - Indian P/Es are usually quoted on **consolidated** EPS; some databases still default to standalone. Check.

## 2. What a multiple assumes: justified P/E and P/B

Start from the Gordon growth model for a share paying dividends that grow at $g$:

$$P_0 = \frac{D_1}{r − g} = \frac{E_1 \times \text{payout}}{r − g}$$

Divide by next year's earnings:

$$\frac{P_0}{E_1} = \frac{\text{payout}}{r − g}$$

Sustainable growth is $g = (1 − \text{payout}) \times \text{ROE}$, so $\text{payout} = 1 − g/\text{ROE}$:

$$\boxed{\left(\frac{P}{E}\right)_{\text{fwd}} = \frac{1 − g/\text{ROE}}{r − g}}$$

This is the equity-side twin of the value-driver formula in [06.1](01-what-is-value.md). A P/E is a bet on three
things: growth, the return on retained earnings, and the cost of equity. Multiply both sides by $E_1/B_0 = \text{ROE}$
to get the **justified P/B**:

$$\boxed{\frac{P}{B} = \frac{\text{ROE} − g}{r − g}}$$

P/B exceeds 1 only when ROE exceeds the cost of equity — which is why P/B is the natural multiple for banks and
NBFCs ([07.1](../07-special-valuation/01-banks-and-nbfcs.md)) and why "cheap on P/B" means nothing without ROE.

```python
from fi.valuation import justified_pe, justified_pb
justified_pe(0.135, 0.128, 0.055)          # Kaveri: ROE 13.5%, ke 12.8%, g 5.5% → 8.1x forward
justified_pb(0.135, 0.128, 0.055)          # → 1.10x
```

### 2.1 The uncomfortable table

Justified forward P/E for a cost of equity of 12.8%:

| ROE \ g | 4% | 6% | 8% | 10% |
|:--|--:|--:|--:|--:|
| 12% | 7.6x | 7.4x | 7.0x | 6.0x |
| 15% | 8.3x | 8.8x | 9.7x | 11.9x |
| 20% | 9.1x | 10.3x | 12.5x | 17.9x |
| 30% | 9.8x | 11.8x | 15.3x | 23.8x |
| 40% | 10.2x | 12.5x | 16.7x | 26.8x |

```python
for roe in (0.12, 0.15, 0.20, 0.30, 0.40):
    print(roe, [round(justified_pe(roe, 0.128, g), 1) for g in (0.04, 0.06, 0.08, 0.10)])
```

Read it against the market: Kaveri at 25.9x trailing, its peers at 30–40x, and the Nifty at 20–22x forward. At a
12.8% cost of equity, a 26x P/E requires a *perpetual* combination like ROE 40% and 10% growth — nothing in the
Indian engineering sector delivers that in perpetuity. The resolution is one of three things: (a) the market's
cost of equity is much lower than 12.8% (structural flows, scarcity — [06.2](02-cost-of-capital.md)); (b) the
growth is not perpetual but a 10–15-year phase that the single-stage formula cannot represent (use a two-stage
model or the DCF); (c) the multiples are too high. Usually it is some of each, and the honest analyst says so
rather than picking the one that suits the position.

## 3. Choosing peers and the comparison

A peer is a company with **similar growth, similar returns on capital and similar risk** — not merely the same
industry. Two pump companies with ROCEs of 25% and 12% are not peers for valuation, whatever the sector tag says.
Build the table with the value drivers next to the multiples so the reader can see whether a discount or premium is
deserved.

Kaveri against the fictional peer set on the [running-example page](../appendix/running-example/kaveri-pumps.md) (market data 18-Sep-2026):

| Company | Mcap ₹ Cr | Rev growth (3-yr CAGR) | EBITDA margin | ROCE | Net debt / EBITDA | P/E | EV/EBITDA |
|:--|--:|--:|--:|--:|--:|--:|--:|
| Nilgiri Pumps | 6,850 | 13% | 16.8% | 24% | −0.4x | 39.8x | 24.5x |
| Sabarmati Motors & Drives | 3,900 | 17% | 15.2% | 21% | 0.1x | 33.1x | 21.4x |
| Deccan Flow Systems | 2,100 | 9% | 11.5% | 14% | 1.2x | 36.2x | 20.1x |
| Konkan Solar Pumps | 1,450 | 38% | 12.1% | 18% | 0.9x | 29.6x | 17.8x |
| **Peer median** | | 15% | 13.7% | 19.5% | 0.5x | **34.7x** | **20.8x** |
| **Kaveri** | 2,340 | 14.7% | 13.8% | 15.9% | 0.8x | **25.9x** | **13.7x** |

On the face of it Kaveri is *cheap*: a 25% discount to the peer median P/E and a 34% discount on EV/EBITDA. Applied
mechanically, the median P/E gives 34.7 × 15.08 = ₹523 — 34% above the price and 63% above the DCF. Which is right?

Look at the drivers. Kaveri's ROCE (15.9%) is the second-lowest in the set; its margin is median; its growth is
median; its balance sheet is the second-most levered; and it has the receivables problem the peers do not. A
discount is *deserved* — the question is how much. A regression of P/E on ROCE across the four peers (crude with
four points, but illustrative) gives roughly P/E ≈ 22 + 0.7 × ROCE(%), which at Kaveri's 15.9% implies ~33x — so
the peer set says Kaveri should trade at ~33x unless its receivables risk is worth a further 20% discount, which
brings you back to the mid-20s where it trades.

The relative valuation, done properly, therefore says: *Kaveri is priced roughly in line with its peers after
adjusting for lower returns and higher risk.* The DCF says: *the whole peer group is priced for growth and returns
that a 12.2% WACC cannot support.* Both can be true. Relative valuation tells you where a stock sits **within** a
possibly mispriced group; intrinsic valuation tells you whether the group is mispriced.

## 4. Trailing, forward and the historical band

- **Trailing** multiples use the last 12 months — known but stale. **Forward** multiples use the next 12 months'
  estimates — relevant but uncertain, and dependent on whose estimates. For fast growers the difference is large
  (Kaveri: 25.9x trailing vs ~24.6x forward on the base case); always say which.
- **Historical bands**: plot the trailing P/E (or EV/EBITDA) over 5–10 years with its median and ±1 standard
  deviation. Kaveri's trailing P/E ranged 34–48x at each March-end from FY21 to FY26 and now sits at 26x — a
  de-rating of 40% from its own history. A band tells you what the *market* has been willing to pay; it does not
  tell you what the stock is worth. Mean reversion to a band is a valid thesis only if the fundamentals that
  supported the band (growth, returns) are intact — and Kaveri's are not (ROIC down from 15% to 12%).
- **Multiples through a cycle**: for cyclicals, a low trailing P/E at peak earnings is a sell signal and a high P/E
  at trough earnings a buy signal ([07.3](../07-special-valuation/03-cyclicals-and-commodities.md)). Use normalised
  earnings or P/B.

## 5. Why Indian multiples are high — and what to do about it

Indian large caps have traded at 18–25x forward earnings for most of the last decade, mid and small caps often
higher, versus 12–16x for most emerging markets. The candidate explanations, each partly true:

| Explanation | Evidence | Implication for you |
|:--|:--|:--|
| Higher nominal growth (GDP ~10–11% nominal) and a long runway | Earnings growth of listed companies has run 10–15% over long periods | Supports higher multiples, but only for companies that actually deliver it |
| Higher ROEs from a consumer-heavy, asset-light index composition | Nifty ROE ~14–16% vs ~10–12% for many EM indices | Justified-P/B logic supports a premium for the *right* companies |
| Scarcity of quality growth; few listed proxies for a large economy | Persistent premiums for leaders (paints, adhesives, exchanges) | Scarcity premia compress when supply arrives (Birla Opus; new listings) |
| Domestic flows (SIPs ~₹25,000+ Cr/month in 2025–26 — verify) and a rising equity-ownership base | Valuations held through FPI outflows | A flow-supported multiple is a regime, not a law; [12.2](../12-macro-special-sits/02-market-cycles-and-sentiment.md) |
| A lower effective cost of equity than CAPM builds suggest | Implied ERPs of 5–6% over G-secs rather than 7%+ | If you use 13–14% $k_e$, most Indian quality stocks look expensive; decide whether the market or the textbook is wrong, and be consistent |

The practical rule: use multiples *within* India, across peers and across time, and let the DCF with an explicit
cost of capital tell you when the whole market is stretched. And remember that multiples compress when growth
disappoints — a 35x stock that grows 8% instead of 15% loses half its value from the multiple alone.

## 6. Worked example — two lenders, P/B and ROE

**Nirmal Finance** (fictional running example): P/B 2.5x at ₹385 (Mar-26), RoE ~15%. A peer HFC trades at 4.0x book
with RoE ~18%. Justified P/B at a 13% cost of equity and 8% long-run growth:

```python
justified_pb(0.15, 0.13, 0.08)    # Nirmal: (0.15 − 0.08)/(0.13 − 0.08) = 1.4x
justified_pb(0.18, 0.13, 0.08)    # peer:   (0.18 − 0.08)/0.05 = 2.0x
```

Both trade well above their single-stage justified P/B (2.5x vs 1.4x; 4.0x vs 2.0x) — the market is paying for
growth above 8% for many years, or using a lower cost of equity. Relative to each other, Nirmal's discount (2.5x vs
4.0x for 3 pp less RoE) is larger than the justified gap (1.4x vs 2.0x) suggests, which is a starting point for a
thesis, *if* the RoE difference is not explained by asset-quality risk. [07.1](../07-special-valuation/01-banks-and-nbfcs.md)
finishes the job.

!!! tip "Trader's lens"
    A multiple is an implied vol quoted in the wrong units. "25x" tells you nothing until you decompose it into
    the growth, return and rate it implies — exactly as an IV of 30% tells you nothing until you know the
    realised vol, the skew and the event calendar. Peer tables are the vol surface: they tell you where the
    market prices comparable risk, not whether the surface is right. The justified-multiple formulas are the
    pricing model that converts between the two.

!!! warning "Common mistakes"
    - Mixing equity and enterprise numerators/denominators (P/EBITDA, EV/PAT).
    - Applying a peer median without adjusting for the value drivers (growth, ROIC, leverage, risk).
    - Peer sets chosen by sector tag rather than economics.
    - Trailing multiples on peak (or trough) earnings for cyclicals.
    - "It's below its 5-year average P/E" as a thesis without checking whether the fundamentals changed.
    - Ignoring leases in EV after Ind AS 116, or comparing pre- and post-FY20 bands.
    - PEG as if it were a theorem.
    - Reading a high P/B as expensive without ROE, or a low P/E as cheap without growth and returns.

## Key terms

| Term | Meaning |
|:--|:--|
| **Multiple** | Price (equity or enterprise) divided by a fundamental (earnings, book, sales, cash flow) |
| **Equity vs enterprise multiple** | Numerator market cap vs EV; denominator after-interest vs before-interest |
| **Trailing / forward** | Multiples on the last 12 months' actuals / the next 12 months' estimates |
| **Justified P/E** | (1 − g/ROE)/(r − g): the forward P/E consistent with the Gordon model |
| **Justified P/B** | (ROE − g)/(r − g) |
| **PEG** | P/E ÷ expected growth rate (in %); a heuristic |
| **FCF yield** | Free cash flow ÷ market cap (or FCFF ÷ EV) |
| **Peer set / comparables** | Companies with similar growth, returns and risk used for relative valuation |
| **Historical band** | The range of a company's own multiple over time, with median and dispersion |
| **De-rating / re-rating** | A fall / rise in the multiple independent of earnings |
| **Multiple compression** | De-rating caused by slower growth or higher rates |
| **Scarcity premium** | A higher multiple paid because few comparable listed assets exist |

## Check your understanding

1. Compute Kaveri's EV/EBIT at ₹390 and explain why it is a better multiple than EV/EBITDA for comparing it with
   an asset-light peer.
<details><summary>Answer</summary>EV = 390 × 6.0 + 140.5 + 18.2 = 2,498.7; EV/EBIT = 2,498.7 / 134.1 = 18.6x.
EBITDA ignores depreciation, which is a real cost for a plant-heavy company; an asset-light peer with the same
EBITDA has higher EBIT and deserves a higher EV/EBITDA. EV/EBIT puts them on the same footing.</details>

2. What forward P/E is justified for a company with ROE 20%, $k_e$ 12.8% and g 8%? And if the market pays 30x?
<details><summary>Answer</summary>(1 − 0.08/0.20)/(0.128 − 0.08) = 0.6/0.048 = 12.5x. At 30x the market is
assuming either a much lower cost of equity (~10%), or that 8% growth is a mature-phase figure preceded by a decade
of much faster growth, which the single-stage formula cannot represent.</details>

3. Kaveri's trailing P/E fell from 48x (Mar-25) to 26x. Earnings fell 7%. How much of the 47% price decline (₹780
   → ₹390... adjusted for the dates) is de-rating?
<details><summary>Answer</summary>Price change ≈ (EPS change) × (multiple change): 0.93 × (26/48) = 0.93 × 0.54 =
0.50 → a 50% fall, of which −7% is earnings and roughly −46% is the multiple. Almost all de-rating — the market
changed its mind about growth and returns, not just about one year's profit.</details>

4. Why is P/S "sloppy"?
<details><summary>Answer</summary>Sales belong to all capital providers (they fund interest as well as profit), so
the consistent multiple is EV/Sales. P/S understates the cost of a levered company relative to an unlevered one.</details>

5. Two Indian NBFCs: A at 4x book with RoE 18%; B at 2x book with RoE 12%. Which is cheaper on a justified basis
   at $k_e$ 13%, g 8%?
<details><summary>Answer</summary>Justified P/B: A = (0.18 − 0.08)/0.05 = 2.0x, trades at 2.0× its justified level;
B = (0.12 − 0.08)/0.05 = 0.8x, trades at 2.5× its justified level. A is cheaper relative to what its returns
justify — a low P/B on a low-ROE lender is not cheap.</details>

## Go deeper

- Aswath Damodaran, *Investment Valuation*, chapters 17–20 (relative valuation) — the deepest treatment of what
  each multiple assumes.
- McKinsey, *Valuation*, "Using Multiples" — why EV/EBITA on forward numbers with a driver-matched peer set is the
  practitioner's standard.
- Screener.in's "Peers" tab for any stock — then rebuild it with ROCE, growth and leverage columns beside the
  multiples.
- [Case G3 Cisco](../13-case-studies/global/03-cisco-2000.md) and [case I2 Asian Paints](../13-case-studies/india/02-asian-paints-compounder.md)
  — multiples that no justified formula could support, and what happened next.

---
[← Previous: 06.4 DCF in practice](04-dcf-in-practice.md) · [Module index](index.md) · [Next: 06.6 Reverse DCF & expectations →](06-reverse-dcf-and-expectations.md)
