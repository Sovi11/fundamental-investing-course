# 11.7 · Fundamentals × derivatives

> **Why this matters:** an option-literate investor has tools most fundamental investors lack — the implied
> move around results as a benchmark for a fundamental surprise, implied vol and skew as the market's estimate of
> fundamental uncertainty, and structures that express a valuation view with defined risk or with income while
> waiting. This lesson maps fundamental conclusions onto derivative expressions, with Indian F&O practicalities
> as of September 2026. It is educational; nothing here is advice, and derivatives can lose more than the
> premium.

**Learning objectives** — after this lesson you can:

- Compare the implied move around a results date with your own estimate of the fundamental surprise.
- Read implied vol and skew as information about the market's fundamental uncertainty.
- Express fundamental views with options and futures: stock replacement, risk reversals, cash-secured puts at
  the buy price, covered calls on full-value positions, protective puts, collars, index/sector hedges, pairs,
  event structures.
- State the Indian practicalities: F&O eligibility, lot sizes, expiries, margins, the 2024–25 SEBI measures, and
  the tax treatment of F&O.

**Prerequisites:** [06.8 Margin of safety](../06-valuation/08-margin-of-safety-and-expected-value.md),
[11.4 Position sizing](04-position-sizing-and-portfolio-construction.md); option pricing basics assumed  ·  **Time:** ~75 min

---

## 1. Implied move vs fundamental surprise

Around a results date, the at-the-money straddle prices the market's expected absolute move. For a short-dated
ATM straddle, $\text{straddle} \approx 0.8\,\sigma\sqrt{T}\,S \approx E|S_T - S|$, so the implied mean absolute
move $\approx \text{straddle price} / \text{spot}$, and the one-standard-deviation move is about 1.25× that.
A fundamental analyst can estimate the *surprise* independently: your forecast vs consensus (or vs guidance), and
the stock's historical sensitivity to beats and misses (the post-earnings drift and the multiple's reaction).

| Situation | Reading |
|:--|:--|
| Your expected surprise is large; implied move is small | The option market has not priced the fundamental event — long the straddle or the directional leg; or simply size the equity view knowing the reaction may be large |
| Implied move is large; you expect a non-event | Sell the event vol (cash-secured put at your buy price if bullish; covered call if long) — the fundamental view gives you the strike |
| Implied move ≈ your estimate | No edge in the event; trade the fundamentals, not the date |

For Kaveri (fictional, so not F&O-eligible), the analysis in [Module 06](../06-valuation/index.md) says the
Q2/Q3 FY27 prints carry a *directional* fundamental risk (receivable days) that the memo's thesis-breakers
pre-specify. In a real F&O name, that is the setup for an event structure: a put spread into results if you expect
the breaker to fire, financed by the elevated pre-results vol.

## 2. Implied vol and skew as fundamental information

- **Implied vol level** is the market's estimate of the stock's uncertainty; compare it with the dispersion of
  your scenario values (Kaveri: a P10–P90 value band of ±30% around the median implies a lot of fundamental vol).
  A stock whose implied vol is far *below* your fundamental uncertainty is under-pricing the risk you see — a
  reason for a smaller equity position, or for owning optionality rather than delta.
- **Skew** (put IV > call IV) says how the market prices the left tail. Governance-flagged, levered or
  regulation-sensitive names should show steep skew; when they do not, the market is not pricing the jump risk
  the forensic checklist found ([09.5](../09-forensics/05-governance-red-flags-india.md)) — protective puts are
  cheap relative to the risk.
- **Term structure** around known dates (results, policy decisions, index rebalances) maps the event calendar.

The reverse-DCF analogy of [06.6](../06-valuation/06-reverse-dcf-and-expectations.md) extends: implied vol is the
market's *second moment* on fundamentals as the price is its *first*. A variant perception can be about either.

## 3. Expressing fundamental views

| Fundamental conclusion | Expression | Why | Risk |
|:--|:--|:--|:--|
| Undervalued; want the upside with defined risk (e.g., a governance-Amber name) | **Stock replacement**: long-dated call (or call spread) instead of shares | Caps the loss at the premium — the right shape for a fat left tail | Premium decays; dividends forgone; needs a move within the tenor |
| Undervalued, but not at this price; happy to buy lower | **Cash-secured put at your buy price** (e.g., Kaveri at ₹260 if it were F&O-eligible) | Paid to wait for your entry; if assigned, you own it where you wanted | If the thesis breaks on the way down, you own a broken thesis at ₹260 — the put does not know why the stock fell |
| Long a position now near or above your bull case | **Covered call** at the bull-case strike | Monetises the part of the distribution you don't underwrite | Caps upside if you are wrong about the bull case; not a hedge against the downside |
| Long; a specific dated risk (results; regulatory decision) | **Protective put** or **collar** (put financed by a call) through the date | Buys survival through a jump | Cost; the collar caps upside |
| Bullish on the business, bearish on the sector/market | **Long stock, short Nifty/sector futures** (beta-weighted) | Isolates the alpha; removes the regime | Basis risk; margin; the hedge ratio drifts |
| Two similar companies, one mispriced vs the other | **Pair**: long A, short B (futures or stock lending) | Cancels sector and market | Short borrow/futures roll costs; pairs can diverge for years; both legs need a thesis |
| Bearish on a specific company (forensic findings) | **Long put spread**; **short futures** (with a stop) | Defined-risk short; India has no easy stock borrow for retail | Short squeezes; timing — frauds run longer than you can stay solvent |
| Strong view; want leverage without a margin call | **Risk reversal** (long call, short put) | Synthetic long with a cheaper entry when skew is steep | The short put is the full downside |
| Bullish but the implied move into results is large | **Sell the event vol** against the position (covered call or short put at the base-case value) | Harvest the event premium the fundamental view says is excessive | Wrong-way event |

The principle behind every row: **the fundamental work supplies the strike and the horizon** (bear, base, bull
values; thesis-breaker dates); the options market supplies the price of the distribution. Where the two
disagree, there is a trade; where they agree, express the view in the simplest instrument.

## 4. Hedging beta and the "long/short" book

A fundamental long/short book is long companies whose expectations are too low and short companies whose
expectations are too high, hedged to remove the market and sector factor with index futures (Nifty 50, Bank
Nifty, sector indices where liquid). Sizing follows [11.4](04-position-sizing-and-portfolio-construction.md) with
two additions: beta-weight the hedge (a 1.3-beta small cap needs 1.3× the notional in Nifty futures), and re-hedge
as betas drift. Shorts in India are constrained: retail stock borrowing is limited (SLB exists but is thin), so
shorts are mostly single-stock futures in the ~180–200 F&O-eligible names (verify the current list), with monthly
rolls and margin. That constraint is why most Indian "long/short" is really long stock / short index.

## 5. Indian practicalities (September 2026)

| Item | Current position (verify before trading) |
|:--|:--|
| **Eligible stocks** | Only stocks in the F&O segment (SEBI eligibility criteria on market-wide position limits, quarter-sigma, ADV; periodic inclusions/exclusions) have single-stock futures and options; most small caps do not — including anything like Kaveri |
| **Index derivatives** | Nifty 50 (NSE) and Sensex (BSE) weekly expiries — one weekly index per exchange since Nov-2024; Bank Nifty and others monthly only; lot sizes revised periodically (Nifty 65 from the Jan-2026 series, Bank Nifty 30 — [NSE circular](https://nsearchives.nseindia.com/content/circulars/FAOP70616.pdf); [lot sizes 2026](https://www.sahi.com/blogs/nifty-lot-size-2026-bank-nifty-sensex)) |
| **SEBI 2024–25 measures** | Larger contract sizes; one weekly expiry per exchange; upfront collection of option premium; intraday position-limit monitoring; removal of calendar-spread margin benefit on expiry day; expiry-day margin increases — see [07.2 §4.2](../07-special-valuation/02-insurers-amcs-exchanges.md) |
| **Margins** | SPAN + exposure for futures and short options; premium upfront for long options; peak-margin rules |
| **Physical settlement** | Single-stock F&O settle physically on expiry — an in-the-money short put becomes stock delivery (which, for a cash-secured put at your buy price, is the point) |
| **Position limits** | Client-level and market-wide limits; a stock in "ban" when MWPL is breached |
| **Costs** | STT on F&O (raised in Oct-2024: futures 0.02%, options 0.1% on premium — verify), exchange charges, GST, brokerage; the "true-to-label" rule (2024) changed how brokers pass on exchange charges |
| **Tax** | F&O profits and losses are **non-speculative business income** (slab rates; expenses deductible; losses carried forward 8 years against business income; tax audit thresholds by turnover — verify), separate from equity capital gains (STCG 20% / LTCG 12.5%). Intraday cash equity is speculative business income ([Tax2win](https://tax2win.in/guide/calculate-capital-gains-tax-on-shares)). A long-term investor who also runs options may want separate accounting and, at scale, a separate entity — take advice |

## 6. Where derivatives do not help

- **Thesis risk is not hedgeable** — a put protects against the price, not against being wrong about the
  business; and options on illiquid small caps (where most fundamental edge lives) do not exist.
- **Time**: a fundamental thesis plays out over 1–3 years; listed options in India are liquid for 1–3 months.
  Rolling costs and gaps between the thesis horizon and the option horizon eat the edge.
- **Complexity as procrastination**: a collar on a position you should sell is a way of not deciding.
- **Leverage**: a risk reversal on a stock with a governance flag is a levered bet on the thing the flag warns about.

!!! tip "Trader's lens"
    The course has spent eleven modules turning you into an analyst; this lesson is where the analyst hands the
    trader a strike. Keep the roles separate: the fundamental work decides *what* and *where* (bear/base/bull,
    breakers, dates); the derivatives desk decides *how* (delta, optionality, carry, hedge), and only when the
    market's price of the distribution differs from yours. When they agree, buy the stock.

!!! warning "Common mistakes"
    - Selling puts at a "buy price" without a thesis that survives the reasons the stock might get there.
    - Writing covered calls on a position whose bull case is the thesis.
    - Hedging a small-cap long with Nifty futures and calling it market-neutral (beta and idiosyncratic risk).
    - Ignoring physical settlement, ban periods and expiry-day margin rules.
    - Mixing F&O business income and capital gains without records.
    - Letting the instrument choose the idea.

## Key terms

| Term | Meaning |
|:--|:--|
| **Implied move** | The expected absolute price change priced by the ATM straddle for a period (≈ straddle ÷ spot; 1σ ≈ 1.25× that) |
| **Skew** | The difference between put and call implied vols at equal moneyness |
| **Stock replacement** | Holding calls (or call spreads) instead of shares to cap downside |
| **Cash-secured put** | Selling a put with cash reserved to buy the shares if assigned |
| **Covered call** | Selling a call against shares held |
| **Collar** | Long put + short call around a long stock position |
| **Risk reversal** | Long call + short put (synthetic long with skew) |
| **Beta-weighted hedge** | Index futures sized by the position's beta |
| **Pair trade** | Long one stock, short a similar one |
| **MWPL / ban period** | Market-wide position limit; trading restrictions when breached |
| **Physical settlement** | Delivery of shares on expiry for single-stock derivatives |
| **Non-speculative business income** | Indian tax classification of F&O profits |

## Check your understanding

1. A stock's ATM straddle into results costs 6% of spot; your fundamental analysis expects a small beat with the
   multiple unchanged, and the stock's history shows ±3% moves on in-line results. What is the trade, if any?
<details><summary>Answer</summary>Implied mean absolute move ≈ 6% (1σ ≈ 7.5%) vs an expected ~3%: the event vol is rich. If long, sell a
covered call (or, if wanting to add, a cash-secured put) at a strike consistent with the base case; if no
position, the edge is small and the risk of being wrong about the reaction is real — probably no trade.</details>

2. Kaveri (if it were F&O-eligible) trades at ₹390; your buy trigger is ₹260 with receivable days < 85. Why is a
   ₹260 cash-secured put a poor expression of that view?
<details><summary>Answer</summary>The put assigns you at ₹260 regardless of *why* the stock got there; the trigger
has a conditional (receivable days < 85) that the put cannot honour. If the fall is the bear case (dues stuck), you
own a ₹168 stock at ₹260. Only sell the put if you would buy at ₹260 unconditionally.</details>

3. You are long a 1.3-beta industrial at 4% of the portfolio and want to remove market risk. What is the hedge,
   and what does it not remove?
<details><summary>Answer</summary>Short Nifty futures with notional = 1.3 × 4% of portfolio (≈ 5.2%), rolled
monthly and re-weighted as beta changes. It removes market beta only — sector, style (small-cap) and
company-specific risk remain; it also costs the basis and roll.</details>

4. How are gains on a covered call taxed if the stock is delivered on expiry?
<details><summary>Answer</summary>The option premium is F&O business income; the share sale on physical settlement
is a capital-gains event (STCG/LTCG by holding period) — two regimes, two records. Take advice on the treatment of
settlement price vs strike.</details>

## Go deeper

- SEBI circulars on index-derivative measures (Oct-2024) and subsequent NSE/BSE circulars on lot sizes and
  expiries — primary sources; check before every trade.
- NSE's F&O eligibility list and MWPL data (nseindia.com).
- Euan Sinclair, *Positional Option Trading* — expressing views with options; a practitioner's text.
- [07.2](../07-special-valuation/02-insurers-amcs-exchanges.md) for the exchanges' side of the same rules;
  [06.7](../06-valuation/07-other-valuation-methods.md) for equity as an option.

---
[← Previous: 11.6 Behavioural finance & decision journals](06-behavioural-finance-and-decision-journals.md) · [Module index](index.md) · [Next: 12.1 Macro for equity investors →](../12-macro-special-sits/01-macro-for-equity-investors.md)
