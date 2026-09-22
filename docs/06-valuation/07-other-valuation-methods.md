# 06.7 · Other valuation methods

> **Why this matters:** DCF and multiples cover most companies most of the time. But a bank has no meaningful
> FCFF, a holding company is worth its parts minus a discount, a cement plant is often priced per tonne, a
> distressed equity is a call option, and an exploration licence is worth more than its expected cash flows. Each
> of these needs a method that fits the asset. This lesson gives you the rest of the toolkit and — more importantly
> — shows that every method is the same idea (discounted cash to owners) seen from a different angle.

**Learning objectives** — after this lesson you can:

- Apply the dividend discount model and know when it is the right tool.
- Compute a residual-income (excess-return) valuation and show it equals a DCF when assumptions are consistent.
- Build a sum-of-the-parts valuation and apply a holding-company discount with an argued basis.
- Use asset-based methods (book, replacement cost, liquidation, NAV) and capacity/reserve multiples for the
  sectors where they apply.
- Explain equity as a call option on the firm (Merton) and real options in capex and exploration, in language a
  derivatives trader will recognise.

**Prerequisites:** [06.3 DCF step by step](03-dcf-step-by-step.md), [06.5 Relative valuation & multiples](05-relative-valuation-and-multiples.md)  ·  **Time:** ~100 min

---

## 1. Dividend discount model (DDM)

The oldest equity model: a share is worth the present value of its dividends.

$$P_0 = \sum_{t=1}^{\infty}\frac{D_t}{(1+k_e)^t} \quad \xrightarrow{\text{constant growth}} \quad P_0 = \frac{D_1}{k_e − g}$$

Multi-stage versions forecast dividends explicitly for some years and apply the Gordon formula after. **Use it
when dividends are the cash flow that actually reaches you and are set by policy**: mature utilities, REITs/InvITs
(where distributions are mandated), PSUs with dividend guidelines, MNC subsidiaries that upstream most profit. **Do
not use it** for companies that retain most earnings — the model then values the payout policy, not the business
(a company paying nothing has a DDM value of zero until you assume a future payout, which is just a disguised FCFE
model).

Nirmal Finance paid ₹30 Cr on 11 Cr shares in FY26 (DPS ₹2.73, payout ~12.5%). A single-stage DDM at $k_e$ 13%
and g 6% gives 2.73 × 1.06 / 0.07 = **₹41** — against a price of ₹402. The gap is not a mispricing; it is the
model telling you the value is in *retained* earnings compounding at 15% RoE, which the DDM cannot see.

## 2. Residual income (excess-return) model

**Residual income** is profit above the charge for the equity capital used to earn it:

$$\text{RI}_t = \text{PAT}_t − k_e \times B_{t−1} = (\text{ROE}_t − k_e) \times B_{t−1}$$

Value is current book value plus the present value of future residual income:

$$V_0 = B_0 + \sum_{t=1}^{\infty}\frac{(\text{ROE}_t − k_e)\,B_{t−1}}{(1+k_e)^t}$$

With constant ROE and growth this collapses to the justified P/B of [06.5](05-relative-valuation-and-multiples.md):

$$V_0 = B_0 + \frac{(\text{ROE} − k_e)\,B_0}{k_e − g} \;\;\Rightarrow\;\; \frac{V_0}{B_0} = \frac{\text{ROE} − g}{k_e − g}$$

### 2.1 Nirmal Finance

Book value ₹1,695.3 Cr (FY26), RoE 15.1%, $k_e$ 13%, long-run g 6%:

```python
bv, roe, ke, g = 1695.3, 0.151, 0.13, 0.06
ri = (roe - ke) * bv                        # 35.6 Cr of excess return next year
value = bv + ri / (ke - g)                  # 2,204 Cr
print(round(value), round(value / 11.0), round(value / bv, 2))
# 2204  ₹200/share  1.30x book
```

The model says Nirmal is worth ~1.3x book (₹200) if it earns 15% for ever with 6% growth; at ₹402 (2.6x book)
the market expects far more ([06.6](06-reverse-dcf-and-expectations.md) §4). The strength of the residual-income
form is that it *starts* from book value — a large, observable anchor — and only the excess return is forecast, so
errors in the terminal are proportionally smaller than in a DCF where everything is forecast. That is why it is the
natural model for banks and insurers ([07.1](../07-special-valuation/01-banks-and-nbfcs.md), [07.2](../07-special-valuation/02-insurers-amcs-exchanges.md)).

### 2.2 Why residual income equals DCF

If accounting is "clean surplus" (all gains and losses flow through profit, so $B_t = B_{t−1} + \text{PAT}_t −
\text{Dividends}_t$), then substituting $\text{Dividends}_t = \text{PAT}_t − (B_t − B_{t−1})$ into the DDM and
rearranging gives the residual-income formula exactly. Different presentation, identical value. Discrepancies in
practice come from inconsistent assumptions — a terminal growth in one model that implies a different reinvestment
than the other — not from the method. Use the equivalence as a check: build both, and if they differ, find the
inconsistent assumption.

## 3. Sum-of-the-parts (SOTP) and holding-company discounts

A company that owns several distinct businesses, or stakes in other companies, is valued **part by part**, each with
the method suited to it, then summed and adjusted for the parent's own net debt and costs.

### 3.1 Worked example — Sahyadri Industries (fictional)

| Part | Basis | Value ₹ Cr |
|:--|:--|--:|
| Auto-components business (100% owned) | DCF; or 10x EV/EBIT on ₹180 Cr EBIT | 1,800 |
| 60% stake in a listed bearings company | Market value of the stake: 60% × ₹2,500 Cr market cap | 1,500 |
| 25% stake in an unlisted NBFC | 1.2x book on ₹400 Cr of book × 25% | 120 |
| Surplus land (Pune, 40 acres) | Valuer's report, less 30% for realisation and tax | 210 |
| Cash at parent | Balance sheet | 150 |
| Parent net debt | Balance sheet | (300) |
| Capitalised holdco costs (₹15 Cr/yr ÷ 12%) | Perpetuity of unallocated corporate expenses | (125) |
| **Gross SOTP** | | **3,355** |
| Holding-company discount on listed/unlisted stakes (30% of 1,620) | See below | (486) |
| **Equity value** | | **2,869** |
| Shares (Cr) | | 10 |
| **Value / share** | | **₹287** |

Each part carries its own risks and the whole is only as good as its weakest valuation (the land and the unlisted
stake are the soft spots).

### 3.2 The holding-company discount

Indian listed holdcos — companies whose main asset is stakes in other listed companies — typically trade at
**30–70% discounts** to the market value of what they hold (verify current figures for names such as Bajaj Holdings,
Tata Investment Corporation, Maharashtra Scooters, Pilani Investment and Bombay Burmah; discounts widen and narrow
with sentiment and with expectations of restructuring). The discount has real causes, and you should price them
rather than assume "it will close":

| Cause | How to size it |
|:--|:--|
| **Tax leakage**: selling the stake triggers capital-gains tax; dividends received are taxable at the holdco and again at the shareholder | Estimate the tax on an eventual sale or on dividend pass-through |
| **No control / no access**: minorities in the holdco cannot force a sale or distribution; cash sits with the promoter's chosen entity | The larger the promoter's control and the poorer the payout history, the larger the discount |
| **Holdco costs**: staff, listing, treasury | Capitalise them |
| **Illiquidity** of the holdco stock | Compare traded value with the parts' liquidity |
| **Restructuring optionality** (in the other direction): a merger, demerger or buyback can collapse the discount overnight | Assign a probability and timing ([12.3](../12-macro-special-sits/03-special-situations.md)) |

A 30% discount on a liquid stake held by a promoter with a history of restructuring is defensible; 60% on a holdco
that has never distributed anything and never will is also defensible. What is not defensible is picking the
number that makes the SOTP work.

**Conglomerate discount** is the operating-company cousin: a company running five unrelated businesses often
trades below the sum of the parts because capital allocation across them is opaque, the best business is diluted
by the worst, and the market applies the *lowest* segment's multiple to the whole. Demergers are the usual cure —
which is why they tend to create value ([12.3](../12-macro-special-sits/03-special-situations.md);
[case I12 ITC](../13-case-studies/india/12-itc-value-trap-or-not.md)).

## 4. Asset-based methods

| Method | Value = | Best for | Trap |
|:--|:--|:--|:--|
| **Book value** | Accounting equity | Lenders (loans are near fair value); a first floor for asset-heavy companies | Historical cost: land bought in 1975 at ₹2 Cr; brands at zero |
| **Adjusted book / NAV** | Assets marked to market − liabilities | Real-estate companies (land bank and projects at DCF or market value), holdcos, investment companies, REITs/InvITs | Valuer optimism; ignoring tax and time to realise |
| **Replacement cost** | What it would cost to build the assets today | Cyclicals at trough (cement, steel, hotels, power plants): a stock trading below replacement cost signals no new capacity will come until prices rise | Ignores whether anyone *would* rebuild; obsolescence |
| **Liquidation value** | What assets would fetch in a forced sale − all liabilities and costs | Distress; Graham's net-net (current assets − all liabilities > market cap) | Realisation haircuts (inventory 50%, receivables 70–80%, plant 20–40%); time and legal costs; in India, IBC recoveries have averaged ~30–35% of admitted claims for creditors — equity typically gets nothing |
| **EV per unit of capacity** | EV ÷ installed capacity | Cement (EV/tonne), steel (EV/tonne), power (EV/MW), hotels (EV/room), hospitals (EV/bed), telecom (EV/subscriber) | Capacity ≠ utilisation ≠ profit; location and vintage differ |
| **EV per unit of reserves** | EV ÷ proven reserves | Oil & gas (EV/boe), mining (EV/tonne of reserve) | Reserve quality, cost of extraction, commodity price deck |

### 4.1 EV/tonne — a cement sketch

Suppose Indian cement capacity costs roughly ₹700–1,000 Cr per million tonnes to build (brownfield cheaper, greenfield
dearer; verify against recent announcements), and a mid-sized company with 20 MT of capacity trades at an EV of
₹12,000 Cr — **₹600 Cr/MT**, below replacement cost. Two readings: the market expects utilisation and prices to stay
poor (so the capacity is worth less than its cost), or the stock is cheap relative to what any acquirer would have to
pay to build it. The 2022–24 consolidation wave in Indian cement (acquisitions at ₹800–1,200 Cr/MT — verify deal
values) made the second reading profitable for a while. EV/tonne is a sanity check on a DCF for a capacity
business, not a substitute: it says nothing about the cash the tonnes will generate.

## 5. Option-based views

### 5.1 Equity as a call on the firm (Merton, 1974)

A company's assets are worth $V$; it has debt of face value $D$ due at time $T$. At maturity, shareholders receive
$\max(V_T − D, 0)$ — they pay the debt and keep the rest, or hand the keys to the lenders. That is a **call option
on the firm's assets with strike D**. Debt is a risk-free bond minus a put on the assets.

$$E = V\,N(d_1) − D\,e^{−rT}\,N(d_2), \qquad d_1 = \frac{\ln(V/D) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 − \sigma\sqrt{T}$$

Worked example: asset value ₹1,000 Cr, asset volatility 30%, debt ₹700 Cr due in 3 years, risk-free 7%:

```python
from math import log, sqrt, exp
from statistics import NormalDist
N = NormalDist().cdf
V, D, s, r, T = 1000, 700, 0.30, 0.07, 3
d1 = (log(V / D) + (r + 0.5 * s * s) * T) / (s * sqrt(T)); d2 = d1 - s * sqrt(T)
E = V * N(d1) - D * exp(-r * T) * N(d2)
print(round(E, 1), round(V - E, 1), round(1 - N(d2), 3))
# equity 459.4  debt 540.6  risk-neutral P(default) 0.203
for s in (0.2, 0.3, 0.5):
    d1 = (log(V / D) + (r + 0.5 * s * s) * T) / (s * sqrt(T)); d2 = d1 - s * sqrt(T)
    print(s, round(V * N(d1) - D * exp(-r * T) * N(d2), 1))
# σ 20% → 438 ; 30% → 459 ; 50% → 528
```

What the model teaches that DCF cannot:

- **Equity in a levered firm is long volatility.** Raising asset volatility from 20% to 50% raises equity value
  from ₹438 Cr to ₹528 Cr *with no change in expected asset value* — the upside is kept, the downside is capped at
  zero. This is why shareholders of distressed companies favour risky bets ("gambling for resurrection") and why
  lenders write covenants against it.
- **Deep-OTM equity has value.** Vodafone Idea ([case I10](../13-case-studies/india/10-vodafone-idea-telecom-war.md))
  traded for years with negative net worth: its equity was an out-of-the-money, long-dated call on tariff hikes,
  government forbearance and equity conversion. Valuing it by DCF gives zero or negative; the option lens explains
  the price and its behaviour (huge gamma around policy news).
- **Debt has an implied credit spread.** Here the debt is worth ₹540.6 Cr for ₹700 Cr of face in 3 years — a yield
  of ~9.0%, 2 pp over risk-free, consistent with a 20% risk-neutral default probability.

The model's inputs (asset value and volatility) are not observable and must be backed out from equity value and
equity volatility (the KMV approach); as a *thinking tool* for levered equities it needs no calibration.

### 5.2 Real options

A **real option** is the right, not the obligation, to take a business decision later, after uncertainty resolves:
to expand a plant if demand arrives, to abandon a project if prices fall, to defer drilling until oil recovers,
to switch inputs. DCF values the expected path; it undervalues assets whose value comes from *flexibility*:

| Situation | Option | Why DCF misses it |
|:--|:--|:--|
| Exploration licence, patent, spectrum | Option to develop if the resource/technology/market proves out | Expected cash flow may be negative; the option is valuable because the loss is capped at the exploration cost |
| Modular capex (a plant built in phases; Kaveri's Hosur plant at 57% utilisation) | Option to expand cheaply | DCF with a fixed capex plan ignores the value of waiting for demand |
| Loss-making platform with a dominant position | Option to monetise (take-rate increase, adjacent categories) | Current cash flows negative; value is in the switch that management can flip later |
| Contract with exit clauses | Option to abandon | Downside truncated |

Value them qualitatively unless the option is the *whole* thesis; when it is (exploration, biotech, spectrum),
use a binomial tree or Black–Scholes with the project's PV as the underlying, the investment as the strike, and
time-to-decision as maturity — and be honest that the volatility input is a guess. The practical use for most
investors is to recognise which side of the option you are on: a company that has paid for flexibility it has not
yet used (spare capacity, a licence, a cash pile with a credible acquisition strategy) has value a DCF understates;
a company whose lenders hold the options (covenants, convertible debt, pledged shares) has value a DCF overstates.

!!! tip "Trader's lens"
    The Merton model is the bridge between your two worlds. Every levered equity is a call, every corporate bond
    is short a put, every covenant is a barrier feature, and every distressed stock's price is mostly time value.
    When you look at a company with net debt/EBITDA of 5x, ask the option questions: what is the strike (debt),
    the expiry (maturity ladder), the vol (asset/earnings volatility) and the moneyness (EV vs debt)? A DCF that
    produces a small positive equity value for such a company is not wrong, but the option lens tells you the
    distribution — mostly zero, occasionally a multi-bagger — and that is what position sizing needs.

!!! info "India notes"
    - Holdco discounts are unusually large in India because promoters rarely restructure holdcos and dividend
      pass-through is taxed; IiAS and broker research publish periodic discount tables — use them as base rates.
    - Real-estate NAVs: Indian developers' investor presentations show "NAV" built on their own price and
      absorption assumptions; rebuild it with a cash-flow model per project, a market cap rate for rental assets,
      and land at a discount to circle-rate-implied values.
    - Liquidation is rarely a floor for Indian equity: under the IBC, the waterfall (Section 53) puts secured
      creditors, workmen and unsecured creditors ahead of equity, and recoveries for financial creditors have
      averaged roughly a third of claims — equity almost always gets nothing. A "net-net" screen in India must
      therefore exclude any company where insolvency is plausible.

!!! warning "Common mistakes"
    - Valuing a growth company by DDM and concluding it is worthless.
    - Building a residual-income model with a terminal growth that implies a different reinvestment than the
      balance sheet — the two models then disagree and neither is checked.
    - SOTP with each part at its most flattering multiple, and a holdco discount chosen to hit the price.
    - Treating book value or replacement cost as a floor for a company that will keep destroying value.
    - Using EV/tonne without utilisation and regional price context.
    - Forgetting that the Merton equity value is *risk-neutral* — it prices the option, it does not forecast the
      real-world probability of survival.

## Key terms

| Term | Meaning |
|:--|:--|
| **Dividend discount model (DDM)** | Value = PV of expected dividends; single- or multi-stage |
| **Residual income (RI)** | PAT − $k_e$ × opening book value; profit above the equity charge |
| **Residual-income model** | Value = book value + PV of residual income; equivalent to DCF under clean-surplus accounting |
| **Clean-surplus accounting** | All gains/losses pass through profit, so $B_t = B_{t−1} + \text{PAT}_t − \text{Div}_t$ |
| **Sum-of-the-parts (SOTP)** | Valuing each business or stake separately and summing, net of parent debt and costs |
| **Holding-company discount** | Gap between a holdco's market value and the value of its holdings |
| **Conglomerate discount** | Below-sum valuation of a multi-business operating company |
| **NAV** | Net asset value: assets at market/appraised value − liabilities |
| **Replacement cost** | Cost to rebuild the assets today |
| **Liquidation value** | Forced-sale value of assets less all liabilities and costs |
| **Net-net** | Graham's screen: current assets − all liabilities > market cap |
| **EV/tonne, EV/MW, EV/room** | Enterprise value per unit of physical capacity |
| **Merton model** | Equity as a call option on firm assets with strike equal to debt |
| **Real option** | Managerial flexibility (expand, abandon, defer, switch) valued as an option |
| **Gambling for resurrection** | Levered equity holders' incentive to raise risk because their downside is capped |

## Check your understanding

1. A regulated utility pays out 70% of earnings, has ROE 12%, $k_e$ 10%. Justify a DDM value and compute the P/E.
<details><summary>Answer</summary>Sustainable g = 0.30 × 12% = 3.6%; P/E (forward) = 0.70/(0.10 − 0.036) = 10.9x.
DDM fits because payout is policy-driven and stable, and the retained 30% earns a regulated return close to the
cost of equity, so little value is lost by valuing dividends rather than FCFE.</details>

2. Compute Nirmal's residual-income value if RoE is 18% instead of 15.1%, other inputs unchanged. Compare with
   the price.
<details><summary>Answer</summary>RI = (0.18 − 0.13) × 1,695.3 = 84.8; value = 1,695.3 + 84.8/0.07 = ₹2,907 Cr =
₹264/share = 1.71x book — still below ₹402. The price needs ~21% RoE (from the implied-RoE formula), not 18%.</details>

3. In the SOTP example, what happens to the per-share value if the holdco discount is 50% and the land is
   excluded entirely?
<details><summary>Answer</summary>Discount 50% × 1,620 = 810 (vs 486); land −210. Equity = 3,355 − 810 − 210 =
2,335 → ₹234/share (vs ₹287). The range ₹234–287 (or wider) is the honest SOTP output.</details>

4. Why does raising asset volatility raise Merton equity value while leaving expected asset value unchanged?
<details><summary>Answer</summary>Equity is a call: it participates in upside above the debt and is truncated at
zero below it. Higher volatility fattens both tails, but only the upper tail changes equity's payoff — the extra
downside is borne by lenders. Value transfers from debt to equity without any change in the firm's total value.</details>

5. An exploration company's expected NPV of drilling is −₹50 Cr, but the option to drill after a seismic survey
   costing ₹10 Cr is worth +₹40 Cr. Explain how both can be true.
<details><summary>Answer</summary>The expected NPV averages over good and bad geology and commits to drilling in
both. The survey resolves the uncertainty first; the company drills only in the good case (large positive NPV) and
walks away in the bad case (losing only ₹10 Cr). The right to choose after learning is what the ₹40 Cr values.</details>

## Go deeper

- Stephen Penman, *Financial Statement Analysis and Security Valuation* — the residual-income approach in depth.
- Aswath Damodaran, *Investment Valuation*, chapters on option pricing applied to equity and real options; and his
  "Valuing Holding Companies / Conglomerates" notes.
- Robert Merton, "On the Pricing of Corporate Debt: The Risk Structure of Interest Rates", *Journal of Finance*
  (1974) — the original; readable for anyone who knows Black–Scholes.
- IiAS and sell-side reports on Indian holdco discounts — for base rates.
- Benjamin Graham, *Security Analysis*, on liquidation value and net-nets — with the IBC caveat above.

---
[← Previous: 06.6 Reverse DCF & expectations](06-reverse-dcf-and-expectations.md) · [Module index](index.md) · [Next: 06.8 Margin of safety, expected value & asymmetry →](08-margin-of-safety-and-expected-value.md)
