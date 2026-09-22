# 06.2 · Cost of capital

> **Why this matters:** the discount rate is the exchange rate between the future and the present. Move it by one
> percentage point and a long-duration valuation moves by 10–15%. It is also the number analysts most often
> fudge — nudging WACC until the DCF agrees with the price they already believed. This lesson gives you a
> defensible way to build it for an Indian company, a sense of the plausible range, and the honesty to treat it as a
> hurdle you set rather than a truth you discover.

**Learning objectives** — after this lesson you can:

- Build a cost of equity with CAPM for an Indian company: risk-free rate, equity risk premium, beta — and know the
  weaknesses of each input.
- Choose a risk-free rate and ERP that are consistent (currency, inflation, horizon) and defend them with current
  data.
- Estimate beta three ways (regression, adjusted, bottom-up) and explain why the regression is unreliable for
  Indian small caps.
- Compute the after-tax cost of debt from a rating and the WACC with target weights, and reproduce the Kaveri
  reference WACC of 12.19%.
- State practical WACC ranges for Indian large, mid and small caps, and explain the trader's view of WACC as a hurdle.

**Prerequisites:** [06.1 What value is](01-what-is-value.md),
[04.5 Leverage, solvency & liquidity](../04-financial-analysis/05-leverage-solvency-liquidity.md)  ·  **Time:** ~90 min

---

## 1. What the discount rate represents

The **cost of capital** is the return investors could earn on alternative investments of equivalent risk — the
opportunity cost of putting money into *this* company. Three consequences:

1. It is set by the market's alternatives, not by the company's wishes or its historical cost of borrowing.
2. It should reflect only risk that cannot be diversified away (**systematic** risk). Company-specific risks — a
   state agency not paying Kaveri — belong in the cash-flow scenarios, not the discount rate ([06.4](04-dcf-in-practice.md)).
3. Each cash-flow stream is matched with its own rate: **FCFF** (to all capital providers) with the **WACC**;
   **FCFE** or dividends (to shareholders) with the **cost of equity**.

$$\text{WACC} = \frac{E}{D+E}\,k_e + \frac{D}{D+E}\,k_d(1 − t)$$

where $k_e$ is the cost of equity, $k_d$ the pre-tax cost of debt, $t$ the tax rate (interest is tax-deductible),
and the weights are *target* market-value weights.

## 2. Cost of equity: CAPM

The **Capital Asset Pricing Model** says the expected return on a stock is the risk-free rate plus a premium
proportional to its systematic risk:

$$k_e = r_f + \beta \times \text{ERP}$$

- $r_f$: **risk-free rate** — the yield on a default-free bond in the currency of the cash flows, matched to their
  horizon.
- **ERP**: **equity risk premium** — the extra return investors demand for holding the equity market rather than
  the risk-free asset.
- $\beta$: the stock's sensitivity to the market — how much its returns move for a 1% move in the index.

CAPM is theoretically elegant, empirically weak (betas explain little of the cross-section of returns; small,
cheap and high-quality stocks earn more than it predicts), and universally used anyway because the alternatives
(multi-factor models, implied costs of capital) add estimation problems of their own. Use it with judgement and
show your inputs.

### 2.1 The risk-free rate

For Indian-rupee cash flows use the **10-year Government of India bond yield**. As of 18-Sep-2026 it was about
**7.07%** ([Trading Economics](https://tradingeconomics.com/india/government-bond-yield)); it had been near 6.5% in
early 2026 before rising on supply and global yields. The reference valuation, dated 31-Mar-2026, uses **6.5%** —
so an analyst valuing Kaveri today would start ~55 bps higher. That single input change lowers the base value by
roughly ₹25–30/share (see the sensitivity in [06.4](04-dcf-in-practice.md)): discount rates are not stable, and
neither are DCF values.

Two consistency rules:

- **Currency and inflation.** ₹ cash flows → ₹ risk-free rate, which embeds ~4% expected Indian inflation. If you
  model in USD (some IT companies), use the US Treasury yield and USD-denominated cash flows. Never mix. The
  difference between the Indian and US 10-year yields (~3 pp) is mostly the expected inflation differential and
  should be mirrored in the growth rates.
- **Default risk.** Purists strip a sovereign default spread from emerging-market government yields (India's
  rating is BBB-/Baa3, investment grade; the spread is small). Most Indian practitioners use the G-sec yield
  unadjusted and put country risk into the ERP. Do one or the other, not both.

### 2.2 The equity risk premium

Three ways to estimate it:

| Method | How | India figure (Sep-2026) | Weakness |
|:--|:--|:--|:--|
| **Historical** | Average excess return of equities over bonds over decades | Indian data since ~1990 gives 5–8% depending on window and index; Nifty's ~12–13% nominal return vs ~7–8% G-sec | Short, noisy history; survivorship |
| **Damodaran's country-risk build-up** | Mature-market ERP (4.17% in the 2026 workbook) + a country risk premium from India's sovereign rating/CDS scaled by equity vs bond volatility | **7.31%** total ERP for India in the July 2026 update ([Damodaran, ERPs by country, Jul-2026](https://www.linkedin.com/pulse/equity-risk-premiums-country-july-2026-update-aswath-damodaran-zti8c); [country risk data](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html)) | Mechanical; USD-based (apply to a USD rf, or accept the approximation with ₹ rf) |
| **Implied** | Solve the market's DCF backwards: what ERP makes the index's expected cash flows equal its price? | Varies with index level; at Nifty ~20–22x forward earnings, implied ERPs of 5–6% over G-secs are typical | Depends on the growth assumption used for the index |

The reference valuation uses **6.0%** — between the implied figure and Damodaran's build-up, and typical of Indian
sell-side practice (5.5–7%). Reasonable people differ by 1–2 pp here; what matters is that you *state* the number,
*source* it, and *keep it consistent* across the companies you compare.

!!! info "India notes"
    A persistent puzzle: Indian equities trade at high multiples (Nifty 20–25x, mid/small caps higher) that imply a
    *low* cost of equity, while textbook builds (7% rf + 6–7% ERP + beta ≈ 13–14%) say it should be high. Explanations
    offered: structural domestic flows (SIPs), scarcity of quality growth, expectations of faster earnings growth,
    and simple overvaluation. The valuation consequence is that a 13% cost of equity will make most Indian quality
    stocks look expensive — which may be correct, and is the reason reverse DCF ([06.6](06-reverse-dcf-and-expectations.md))
    is more useful here than a point estimate.

### 2.3 Beta

Beta measures how a stock's returns co-move with the market's. Three estimates:

**1. Regression beta.** Regress the stock's weekly or monthly returns on the index's (Nifty 500 is a better market
proxy than Nifty 50 for mid/small caps) over 2–5 years:

```python
import numpy as np, pandas as pd, yfinance as yf     # disable VPN first
px = yf.download(["KAVERIPMP.NS", "^CRSLDX"], period="5y", interval="1wk")["Close"]   # fictional ticker
r = np.log(px).diff().dropna()
beta = r.cov().iloc[0, 1] / r.iloc[:, 1].var()
```

Problems in India: thin trading (stale prices bias beta toward zero), short histories, high estimation error
(standard errors of 0.2–0.4 are common), and betas that change with leverage and business mix. A 0.6 regression
beta for an illiquid small cap does *not* mean it is low-risk.

**2. Adjusted beta.** Bloomberg's shrinkage toward 1: $\beta_{adj} = 0.67\,\beta_{raw} + 0.33$. Recognises that
betas mean-revert and estimation error is large.

**3. Bottom-up beta.** Average the *unlevered* betas of listed peers in the same business, then re-lever for the
company's own capital structure (Hamada):

$$\beta_{unlevered} = \frac{\beta_{levered}}{1 + (1 − t)\,D/E}, \qquad
\beta_{levered} = \beta_{unlevered}\,[1 + (1 − t)\,D/E]$$

Suppose four listed pump/motor peers have regression betas of 1.10, 0.95, 1.25, 1.05 with D/E of 0.10, 0.05, 0.30,
0.15:

```python
t = 0.2517
peers = [(1.10, 0.10), (0.95, 0.05), (1.25, 0.30), (1.05, 0.15)]
unlev = [b / (1 + (1 - t) * de) for b, de in peers]        # 1.02, 0.92, 1.02, 0.94
avg_u = sum(unlev) / len(unlev)                             # 0.975
kaveri_beta = avg_u * (1 + (1 - t) * 0.27)                  # D/E 0.27 → 1.17
print([round(x, 2) for x in unlev], round(avg_u, 3), round(kaveri_beta, 2))
```

Bottom-up betas have lower error (averaging) and reflect the business rather than one stock's trading history. The
reference valuation uses **1.05** — between a plausible regression and the bottom-up 1.17; a slightly higher beta
would lower the value further.

### 2.4 Kaveri's cost of equity

$$k_e = 6.5\% + 1.05 \times 6.0\% = 12.80\%$$

```python
from fi.valuation import capm, wacc
ke = capm(rf=0.065, beta=1.05, erp=0.06)                 # 0.1280
```

Sensitivity — the honest way to present any cost of equity:

| ERP \ β | 0.90 | 1.05 | 1.20 |
|:--|--:|--:|--:|
| 5.0% | 11.0% | 11.8% | 12.5% |
| 6.0% | 11.9% | **12.8%** | 13.7% |
| 7.0% | 12.8% | 13.9% | 14.9% |

(All at rf 6.5%; add ~0.6 pp across the board at today's 7.07% G-sec.) The plausible range is 11–15% — a spread
that moves Kaveri's value by roughly ±30%. Precision beyond one decimal is theatre.

## 3. Cost of debt

The **pre-tax cost of debt** is what the company would pay to borrow *today* for the long term — not the average
rate on its existing loans (which may be old, subsidised or short-term):

| Source | Method | Kaveri |
|:--|:--|:--|
| Traded bonds | Yield to maturity on the company's NCDs | None traded |
| Credit rating | G-sec yield + typical spread for the rating (AAA ~40–80 bps; AA ~80–150; A ~150–300; BBB ~300–500 bps — indicative; verify against current corporate-bond spreads) | "A" rating → 6.5% + ~2.4% ≈ **8.9%** (reference) |
| Synthetic rating | Map interest cover to a rating (Damodaran's tables), then to a spread | Interest cover 7.9x → roughly A/A+ → consistent |
| Actual borrowing rate | Finance cost ÷ average debt | 8.7% — consistent with the rating-based figure |

After tax: $k_d(1 − t) = 8.9\% \times (1 − 0.2517) = 6.66\%$. The tax shield exists only if the company pays tax;
loss-makers get no shield until they turn profitable.

## 4. Weights and the WACC

Use **target** weights at **market** values. Book weights understate equity for most companies (market cap ≫ book
equity) and overstate the debt share. Kaveri: market cap ≈ ₹2,370 Cr at ₹390 vs net debt ~₹160 Cr → current
market weight of debt ≈ 6%; the reference valuation uses a **10% target** (management may lever modestly). The
difference is small here; for a highly levered company the choice matters and should be stated.

$$\text{WACC} = 0.90 \times 12.80\% + 0.10 \times 6.66\% = \mathbf{12.19\%}$$

```python
w = wacc(ke=0.1280, kd_pre_tax=0.089, tax_rate=0.2517, debt_weight=0.10)   # 0.1219
```

### 4.1 Practical ranges for Indian companies (nominal ₹, Sep-2026)

| Segment | Cost of equity | WACC | Notes |
|:--|:--|:--|:--|
| Large-cap, stable (FMCG, IT majors) | 11–12.5% | 10.5–12% | Beta ~0.7–0.9; little debt |
| Large-cap, cyclical/levered (metals, autos, infra) | 13–15% | 10–12% | Higher beta; cheap debt lowers WACC but not risk |
| Mid-cap industrial (Kaveri's peer group) | 12.5–14.5% | 11.5–13.5% | Beta ~1.0–1.2; liquidity |
| Small-cap / micro-cap | 14–18% | 13–17% | Add a liquidity/size premium of 1–3 pp — regression betas understate risk |
| Banks / NBFCs | 12–15% (use $k_e$ directly; WACC is not meaningful) | — | [07.1](../07-special-valuation/01-banks-and-nbfcs.md) |
| Regulated utilities, REITs/InvITs | 10–12% | 8.5–10% | Contracted cash flows; high leverage at low cost |

Sell-side reports on Indian companies commonly show WACCs of 10–12% and cost of equity of 11–13%. When you see
a WACC below the G-sec yield plus 3%, or a small cap discounted at a large-cap rate, you are looking at an input
chosen to fit an answer.

## 5. WACC as a hurdle, not a truth

The academic framing says WACC is the "correct" rate. The practitioner's framing — Buffett's, and the one a trader
will recognise — is that the discount rate is the **return you require** for tying up capital in this risk, and
that it should be a hurdle you set consistently rather than a number you estimate to two decimals. Two consequences:

- Use the *same* hurdle for comparable risks, so that your valuations rank opportunities correctly. Ranking
  is what a portfolio needs; absolute precision is what nobody has.
- Put company-specific risk in the scenarios and the margin of safety. A 20% discount rate to "reflect the
  receivables risk" is a hidden, unauditable haircut; a bear case with a ₹60 Cr write-off and a 35% probability is
  an explicit one you can argue about.

!!! tip "Trader's lens"
    WACC is the funding rate of the trade. A market-maker does not agonise over whether their cost of capital is
    11.9% or 12.3%; they know the desk's hurdle and whether an edge clears it by a margin that survives estimation
    error. Treat the DCF the same way: the question is not "is the value ₹320?" but "does the expected return from
    ₹390, across scenarios, clear a 13% hurdle by enough to compensate for how wrong I could be?"

!!! warning "Common mistakes"
    - Using the company's historical average borrowing rate as $k_d$.
    - Book-value weights.
    - A regression beta from an illiquid stock, taken at face value.
    - Mixing a ₹ risk-free rate with a USD ERP without acknowledging it (or mixing real growth with nominal rates).
    - Loading company-specific risk into WACC *and* the scenarios *and* the margin of safety.
    - Reporting WACC to two decimals without a sensitivity table.
    - Forgetting that the reference rf (6.5%) is dated: rebuild rf from today's G-sec when you value anything now.

## Key terms

| Term | Meaning |
|:--|:--|
| **Cost of capital** | Return investors could earn on alternatives of equivalent risk; the discount rate |
| **WACC** | Weighted average of the after-tax cost of debt and cost of equity at target market weights |
| **Cost of equity ($k_e$)** | Return equity investors require; by CAPM, $r_f + \beta \times \text{ERP}$ |
| **Risk-free rate** | Yield on a default-free bond in the cash flows' currency; India: 10-yr G-sec |
| **Equity risk premium (ERP)** | Expected excess return of the equity market over the risk-free rate |
| **Country risk premium** | Extra premium for a country's sovereign/market risk, added to a mature-market ERP |
| **Beta** | Sensitivity of a stock's returns to the market's; systematic risk |
| **Adjusted beta** | Regression beta shrunk toward 1 (0.67β + 0.33) |
| **Bottom-up (unlevered/relevered) beta** | Peer-average business beta, re-levered for the company's D/E |
| **Cost of debt ($k_d$)** | Current long-term borrowing rate; after tax, $k_d(1 − t)$ |
| **Tax shield** | The reduction in tax from deductible interest |
| **Target weights** | The long-run intended debt/equity mix at market values |
| **Hurdle rate** | The minimum return an investor requires; the practitioner's discount rate |
| **Size / liquidity premium** | Extra return demanded for small, illiquid stocks beyond CAPM |

## Check your understanding

1. Rebuild Kaveri's WACC with today's G-sec yield (7.07%), everything else unchanged.
<details><summary>Answer</summary>$k_e$ = 7.07 + 1.05 × 6.0 = 13.37%; $k_d$ = 7.07 + 2.4 = 9.47% pre-tax → 7.09% after
tax; WACC = 0.9 × 13.37 + 0.1 × 7.09 = 12.74%. About 55 bps higher than the reference 12.19%.</details>

2. A small-cap chemicals company has a regression beta of 0.55 against Nifty 50 over three years, trades ₹40 lakh a
   day, and is 25% net-debt-financed. What cost of equity would you use, and why not 6.5 + 0.55 × 6 = 9.8%?
<details><summary>Answer</summary>The 0.55 is an artefact of thin trading (stale prices) and index mismatch. Use a
bottom-up beta from liquid chemicals peers (likely 1.0–1.3 relevered), a Nifty 500 benchmark, and add a 1–3 pp
size/liquidity premium: $k_e$ of 14–16%. A 9.8% cost of equity for an illiquid small cap would produce absurd values.</details>

3. Peers' unlevered beta averages 0.90. What is the relevered beta for a company with D/E of 1.0 at a 25% tax rate,
   and what does it do to $k_e$ at rf 7%, ERP 6%?
<details><summary>Answer</summary>β = 0.90 × (1 + 0.75 × 1.0) = 1.575; $k_e$ = 7 + 1.575 × 6 = 16.45%. Leverage
raises the cost of equity — which is why cheap debt does not lower WACC as much as the weights suggest.</details>

4. Why should Kaveri's state-receivables risk *not* be handled by raising WACC?
<details><summary>Answer</summary>It is company-specific (diversifiable) and discrete — either the states pay or they
don't. A higher WACC penalises every cash flow in every year by a fudge factor no one can audit; a bear scenario
with an explicit write-off and probability is transparent, and it lets you ask what would change the probability.</details>

5. An analyst values an Indian IT company in USD with a 4.5% US Treasury rf and a 5% ERP, then applies a 10% nominal
   ₹ growth rate. What is wrong?
<details><summary>Answer</summary>Currency inconsistency: USD discount rate (embedding ~2–2.5% US inflation) against ₹
growth (embedding ~4% Indian inflation) overstates value. Either convert cash flows to USD and grow them at USD
rates, or use the ₹ G-sec rf with ₹ cash flows.</details>

## Go deeper

- Aswath Damodaran, *Investment Valuation* (3rd ed.), chapters 7–8; and his annual ERP/country-risk updates
  ([Jul-2026 country ERPs](https://www.linkedin.com/pulse/equity-risk-premiums-country-july-2026-update-aswath-damodaran-zti8c),
  [2026 country-risk paper](https://aswathdamodaran.substack.com/p/country-risk-determinants-measures)).
- McKinsey, *Valuation*, chapter on cost of capital — the target-weights, bottom-up-beta approach used here.
- Michael Mauboussin & Dan Callahan, *Cost of Capital: A Practical Guide to Measuring Opportunity Cost*
  (Morgan Stanley, 2023).
- Current data: [India 10-year G-sec yield](https://tradingeconomics.com/india/government-bond-yield); RBI's
  bulletin for corporate-bond spreads by rating.

---
[← Previous: 06.1 What value is](01-what-is-value.md) · [Module index](index.md) · [Next: 06.3 DCF step by step →](03-dcf-step-by-step.md)
