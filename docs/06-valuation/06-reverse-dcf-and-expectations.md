# 06.6 · Reverse DCF & expectations investing

> **Why this matters:** you will never know a company's intrinsic value to within 20%. But you can know, almost
> exactly, what the *market* is assuming — because the price is public and the model is yours. Reverse DCF turns
> valuation from a forecasting contest into a disagreement test: here is what ₹390 requires; do I believe it? For
> anyone who has ever backed an implied volatility out of an option price, this is the natural way to think about
> equities, and it is the single most useful technique in the module.

**Learning objectives** — after this lesson you can:

- Explain expectations investing (Rappaport & Mauboussin) and why price should be read as a forecast.
- Solve a DCF backwards for implied growth, implied margin, implied cost of capital or implied terminal growth,
  using `fi.valuation.reverse_dcf`.
- Identify the "expectation that matters" and state a variant perception.
- Run a reverse DCF on Kaveri (₹390 ⇒ ~14.1% ten-year growth) and interpret it.
- Run a reverse DCF on a real Indian company from live data with the course tools.

**Prerequisites:** [06.3 DCF step by step](03-dcf-step-by-step.md), [06.4 DCF in practice](04-dcf-in-practice.md)  ·  **Time:** ~90 min

---

## 1. Price as a forecast

A conventional DCF goes forecast → value → compare with price. Expectations investing reverses the arrow:
price → implied forecast → compare with *your* forecast. The advantages:

1. **It removes the anchor.** You do not have to defend a point estimate of value; you have to defend a view that
   the market's implied assumption is too high or too low — a narrower, more testable claim.
2. **It exposes what you are betting on.** The implied growth, margin or return is the thing you must have a
   variant view about; if you don't, you have no edge, however good the company.
3. **It handles high multiples honestly.** Instead of "35x is too expensive", it says "35x requires 16% growth for
   twelve years with margins at 18%; here is why I think 11% and 15% are more likely".

!!! tip "Trader's lens"
    This is implied vol, exactly. The option price is observed; the model (Black–Scholes) is agreed; the unknown
    (σ) is solved for; and the trade is realised-vs-implied. In a reverse DCF the stock price is observed, the model
    (DCF) is yours, the unknown (growth, margin, RONIC) is solved for, and the trade is realised-vs-implied
    fundamentals. The same discipline applies: you are not paid for knowing the "true" vol; you are paid when
    realised differs from implied in the direction you bet, and you lose when it doesn't — regardless of how
    beautiful your model was.

## 2. Mechanics

Fix every input except one; find the value of that input that makes the DCF equal the price. `fi.valuation.reverse_dcf`
does the bisection:

```python
from fi.valuation import dcf_from_drivers, kaveri_base_drivers, reverse_dcf
d = kaveri_base_drivers()               # the reference base case; d["cmp"] is not stored — price is ₹390

# 1. Implied uniform revenue growth (all other drivers at base)
implied_g = reverse_dcf(390, lambda g: dcf_from_drivers(**{**d, "growth": [g] * 10})["per_share"])
# → 0.1413  (14.1% a year for FY27–FY36)

# 2. Implied flat EBITDA margin (base growth path)
implied_m = reverse_dcf(390, lambda m: dcf_from_drivers(**{**d, "ebitda_margin": [m] * 10})["per_share"], lo=0.10, hi=0.30)
# → 0.174  (17.4% every year — above the best peer's 16.8%)

# 3. Implied WACC (base operating case) — value falls as WACC rises, so flip the search
implied_w = reverse_dcf(-390, lambda w: -dcf_from_drivers(**{**d, "wacc": w})["per_share"], lo=0.07, hi=0.20)
# → 0.1107  (11.1% — about 110 bps below the reference WACC)

# 4. Implied terminal growth (base operating case)
implied_tg = reverse_dcf(390, lambda g: dcf_from_drivers(**{**d, "g": g})["per_share"], lo=0.0, hi=0.11)
# → 0.083  (8.3% for ever — above nominal GDP; implausible)
```

Each solve holds the others fixed, so the four answers are *alternative* ways the price could be right, not
simultaneous requirements. Together they map the space:

| For ₹390 to be fair, you need… | Implied value | Base case | Plausible? |
|:--|--:|--:|:--|
| Revenue growth (uniform, 10 years) | **14.1%** | 10.8% CAGR | Equals the FY23–26 historical CAGR (14.7%) — but that included the solar surge; sustaining it for ten more years needs share gains or a new segment |
| EBITDA margin (flat, 10 years) | 17.4% | 13.3% → 15.5% | Above the best peer (16.8%) and Kaveri's own peak (15.4%): no |
| WACC | 11.1% | 12.19% | Only if the market's cost of equity is ~11.5% — possible in the Indian flow regime, but then every stock is "cheap" |
| Terminal growth | 8.3% | 5.5% | No — above nominal GDP for ever |

The most *plausible* route to ₹390 is the growth one, so that is the **expectation that matters**: *the price
assumes Kaveri grows revenue ~14% a year for a decade with margins recovering to 15.5% and receivables normalising.*
Everything else in the analysis — the say-do record, the incremental ROIC of 4.6%, the industry map showing
mid-single-digit volume growth ex-solar, the state-payment risk — bears on whether that is likely.

## 3. Variant perception

A **variant perception** (the term is Michael Steinhardt's) is a well-founded view that differs from the
consensus embedded in the price. Reverse DCF gives it a precise form:

> The market expects X. I expect Y, because of evidence Z that the market is under-weighting. If I am right, the
> value is V; I will know I am right (or wrong) when W happens by date D.

For Kaveri, a bearish variant perception:

> The market expects ~14% revenue growth for ten years (implied by ₹390). I expect ~9–11%, because the solar
> segment that produced the FY23–26 surge is tender-driven, working-capital-heavy and now 27% of sales, and because
> management has missed its own guidance four quarters running. If I am right, value is ₹280–320. I will know by
> Q3 FY27 results (Feb-2027): revenue growth below 10% and receivable days above 85 would confirm; a clearance of
> the two state dues and a return to 15%+ growth would refute.

And a bullish one, for balance:

> The market expects ~14% growth; the bull case (15–17% fading to 8%, margin to 16.5%, NWC to 19%) is worth ₹416.
> I believe it because [state budget allocations for PM-KUSUM have been released / the Hosur plant has won an
> industrial-motor contract / …]. I will know by … .

The structure forces you to name evidence, a value and a falsification date. Most "theses" fail the test at the
first clause: they cannot say what the market expects.

## 4. Which expectation matters?

For a given company one or two drivers dominate the value; the reverse DCF should be run on those, not on all of
them. Find them with the sensitivity decomposition from [06.3 §8](03-dcf-step-by-step.md): the drivers with the
largest ₹/share swing per plausible unit of change.

| Company type | Expectation that usually matters | Reverse-solve for |
|:--|:--|:--|
| Growth company at a high multiple | Duration and rate of growth | Implied growth; implied years of growth before fade |
| Mature compounder | Return on new capital; fade | Implied RONIC; implied competitive-advantage period |
| Cyclical at a trough | Mid-cycle margin | Implied normalised margin |
| Turnaround / loss-maker | Terminal margin and time to reach it | Implied steady-state margin |
| Lender | Long-run RoE and credit cost | Implied RoE from P/B: RoE = g + P/B × (r − g) |
| Rate-sensitive (REIT, utility) | Cost of capital | Implied cap rate / cost of equity |

The lender case is a one-liner worth memorising. From the justified P/B, $\text{ROE}_{implied} = g + (P/B)(r − g)$.
Nirmal Finance at 2.5x book, $k_e$ 13%, g 8%: implied RoE = 8 + 2.5 × 5 = **20.5%**, against an actual ~15%. The
price assumes Nirmal becomes a materially better lender — that is the expectation to test.

## 5. A real-company reverse DCF with live data

The course tools fetch statements and price data for any NSE/BSE-listed company (disable any VPN first; Yahoo
Finance blocks many VPN exits). The steps, without hard-coding today's numbers (which will be stale by the time you
read this):

```python
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")    # ₹ on Windows
from fi.data import fetch_statements, fetch_price_info, revenue_row
from fi.valuation import dcf_from_drivers, reverse_dcf, capm, wacc

t = "ASIANPAINT.NS"                                   # any NSE ticker
stm = fetch_statements(t, period="annual", in_crore=True)
info = fetch_price_info(t)
inc, bs = stm["income"], stm["balance"]

rev = float(revenue_row(inc).iloc[0])                 # latest FY revenue, ₹ Cr
ebitda_margin = float((inc.loc["ebitda"].iloc[0]) / rev) if "ebitda" in inc.index else 0.18   # inspect inc.index for the row name
net_debt = float(bs.loc["total_debt"].iloc[0] - bs.loc["cash_and_cash_equivalents"].iloc[0]) if "total_debt" in bs.index else 0.0
shares = info["shares_outstanding"] / 1e7             # crore
price = info["price"]

ke = capm(rf=0.0707, beta=info.get("beta") or 1.0, erp=0.06)
w = wacc(ke, kd_pre_tax=0.085, tax_rate=0.2517, debt_weight=0.05)

# Base drivers: hold margin, capex, NWC at recent levels; solve for growth
base = dict(base_revenue=rev, base_nwc=0.15 * rev, growth=[0.10] * 10, ebitda_margin=ebitda_margin,
            da_pct=0.03, capex_pct=0.04, nwc_pct=0.15, tax_rate=0.2517, wacc=w, g=0.055, ronic=0.25,
            net_debt=net_debt, leases=0.0, shares=shares)
implied = reverse_dcf(price, lambda g: dcf_from_drivers(**{**base, "growth": [g] * 10})["per_share"])
print(f"{t}: price ₹{price:,.0f} implies ~{implied:.1%} revenue growth for 10 years at a {ebitda_margin:.1%} margin, WACC {w:.1%}")
```

Read the printed row names of `inc` and `bs` before relying on them — Yahoo's labels vary by company
(`ebitda` may be absent; build it from operating income + D&A), and quarterly data for Indian companies is patchy
([tools appendix](../appendix/tools.md)). Then ask the only question that matters: *is that implied growth
plausible for this company for ten years?* Compare it with the last ten years' CAGR, the industry's growth, and the
company's reinvestment capacity ($g = \text{RR} \times \text{ROIC}$).

## 6. Limits of the method

- **The model is still yours.** Implied growth depends on the margin, reinvestment and WACC you held fixed;
  report the assumptions alongside the implied number, and run the solve on two or three drivers.
- **Implied ≠ consensus.** The price may embed expectations that no analyst holds — a takeover premium, forced
  buying by index funds, a squeeze. Reverse DCF tells you what the price *requires*, not what people *think*.
- **Non-operating value.** For holdcos, cash-rich companies or those with large investments, strip the
  non-operating assets before solving, or the implied operating growth will be understated.
- **Distribution, not point.** The implied growth is a single number; your view should be a range with a
  probability. The scenarios of [06.4](04-dcf-in-practice.md) are the way to compare.

!!! info "India notes"
    Indian sell-side "target prices" are usually built as forward EPS × a chosen multiple, not by DCF; their implied
    expectations are therefore hidden inside the multiple. When a report says "we value at 30x FY28E EPS", run the
    justified-P/E decomposition from [06.5](05-relative-valuation-and-multiples.md) or a reverse DCF to see what
    growth and returns the 30x needs — the analyst rarely states them.

!!! warning "Common mistakes"
    - Solving for one implied variable and calling it "the" expectation — run the map (growth, margin, WACC, g).
    - Forgetting that implied growth depends on the margin and reinvestment held fixed.
    - Comparing implied growth with last year's growth rather than a ten-year sustainable rate.
    - Using reverse DCF to *justify* the price ("well, 14% is only what they did last three years").
    - No falsification date: a variant perception without a "by when" is an opinion, not a thesis.

## Key terms

| Term | Meaning |
|:--|:--|
| **Reverse DCF** | Solving a DCF backwards for the input value that makes model value equal the market price |
| **Expectations investing** | Reading price as a forecast and betting on revisions to that forecast |
| **Implied growth / margin / WACC** | The value of that input required by the price, others held fixed |
| **Expectation that matters** | The driver whose implied value the price most depends on and about which a view can be formed |
| **Variant perception** | A well-founded view that differs from the expectation embedded in the price |
| **Falsification test** | The observable outcome and date that would prove the variant perception wrong |
| **Implied RoE (lenders)** | $g + (P/B)(r − g)$: the RoE a P/B multiple requires |
| **Consensus** | The average of published analyst forecasts; not the same as price-implied expectations |

## Check your understanding

1. Kaveri's implied growth at ₹390 is 14.1%. At what price would the implied growth equal the base case's 10.8%
   CAGR?
<details><summary>Answer</summary>At ₹320 the *uniform* implied growth is ~11.1% — slightly above the base path's
10.8% CAGR because a flat 11.1% path front-loads less growth than the base path's 14% years and so needs a marginally
higher average to reach the same value. Any price above ₹320 implies more growth than the base case (with base
margins etc.).</details>

2. Compute the implied RoE for a bank at 3.2x book with $k_e$ 12.5% and g 7%. What would you check next?
<details><summary>Answer</summary>RoE = 7 + 3.2 × (12.5 − 7) = 7 + 17.6 = 24.6%. Check the bank's actual and
historical RoE; if it is 17%, the price assumes a large, sustained improvement — ask where it comes from (NIM, cost
ratio, credit cost, leverage) and whether that is plausible under RBI capital rules.</details>

3. Why does the implied WACC of 11.1% *not* by itself mean Kaveri is fairly priced?
<details><summary>Answer</summary>Because it assumes the base operating case is certain. An 11.1% cost of capital
is a statement about the whole market's risk pricing, not about Kaveri; if you accept it, you must apply it to
every stock, which makes the peers look cheaper still. The implied WACC tells you how much of the price is a
discount-rate regime rather than a company view.</details>

4. Write a variant perception for Nirmal Finance at ₹402 (2.6x FY26 book) using the implied-RoE formula.
<details><summary>Answer</summary>"At 2.6x book, $k_e$ 13%, g 8%, the price implies a sustained RoE of 8 + 2.6 × 5 =
21% versus the current ~15%. I expect RoE to stay 14–16% because credit costs are rising (1.3% → 1.9% over three
years) and cost-to-income has little further to fall; if I am right the justified P/B is ~1.4–1.6x, i.e. ₹215–245.
I will know by FY27 results: credit cost below 1.5% and RoE above 17% would refute me."</details>

5. An investor says "the market expects 20% growth, I expect 25%, so the stock is cheap". What is missing?
<details><summary>Answer</summary>Evidence for 25% that the market lacks; a value at 25% growth (is the gap worth
much after discounting?); the *other* implied drivers (maybe the price also assumes margin expansion the investor
hasn't checked); and a falsification test. Also the base rate: how many companies sustain 25% growth for a
decade?</details>

## Go deeper

- Alfred Rappaport & Michael Mauboussin, *Expectations Investing* (revised edition, 2021) — the method, with the
  "price-implied expectations" framework and turbo charts.
- Michael Mauboussin, "What Does a Price-Earnings Multiple Mean?" (Credit Suisse, 2014) — connects multiples to
  implied expectations.
- `tools/examples/kaveri_dcf_and_reverse_dcf.py` — the code behind this lesson's Kaveri numbers.
- [11.3 Writing an investment memo](../11-process/03-writing-an-investment-memo.md) — where the variant perception
  goes.

---
[← Previous: 06.5 Relative valuation & multiples](05-relative-valuation-and-multiples.md) · [Module index](index.md) · [Next: 06.7 Other valuation methods →](07-other-valuation-methods.md)
