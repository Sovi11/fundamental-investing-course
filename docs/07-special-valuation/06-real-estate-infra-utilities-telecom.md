# 07.6 · Real estate, infrastructure, utilities & telecom

> **Why this matters:** these sectors build things that last decades, borrow heavily to do it, and depend on
> governments for land, tariffs, concessions and spectrum. Their accounting is unusual (a developer's revenue
> arrives years after the sale; a toll road's value is a concession that expires), their balance sheets are
> leveraged by design, and their cash flows are either contracted (utilities, annuity roads) or brutally cyclical
> (real estate, telecom price wars). Each needs its own metric — pre-sales, order book, regulated equity, ARPU —
> before the standard valuation tools can be applied.

**Learning objectives** — after this lesson you can:

- Analyse a real-estate developer through pre-sales, collections, cash flows and NAV, and explain why reported
  revenue lags.
- Analyse infrastructure companies by contract type (BOT, HAM, EPC), order book and working capital, and value
  InvITs/REITs on yield and NAV.
- Value a regulated utility on its regulated equity base and CERC/SERC return norms, and separate regulated from
  merchant exposure.
- Analyse a telecom operator through ARPU, subscribers, capex intensity, spectrum and AGR liabilities, and apply
  EV/EBITDA with a capex lens.

**Prerequisites:** [06.7 Other valuation methods](../06-valuation/07-other-valuation-methods.md),
[04.5 Leverage, solvency & liquidity](../04-financial-analysis/05-leverage-solvency-liquidity.md)  ·  **Time:** ~100 min

---

## 1. Real estate

### 1.1 Why the P&L is useless for a developer

Under Ind AS 115 (from FY19), Indian residential developers recognise revenue on **completion** (when control
passes — typically at possession/occupation certificate), not as construction progresses. A project sold in year 1
and delivered in year 4 shows *no revenue for three years*, then all of it at once. Reported revenue, margins and
P/E therefore describe projects launched years ago; they say nothing about the business being done now.

The operating metrics that matter are disclosed in investor presentations, not the P&L:

| Metric | Definition | Reading |
|:--|:--|:--|
| **Pre-sales (bookings)** | Value of units sold in the period (₹ Cr and sq ft) | The real top line; growth and price realisation per sq ft |
| **Collections** | Cash received from customers in the period | The real cash flow; collections/pre-sales lag ~1–2 years |
| **Launches and inventory** | New projects launched; unsold inventory in months of sales | Pipeline and demand |
| **Operating cash flow (company-defined)** | Collections − construction spend − overheads − taxes | Funds land purchases and deleveraging |
| **Land bank / development pipeline** | Acres or sq ft of developable land, by location | The option value; also the capital sink |
| **Net debt / equity; debt / pre-sales** | | Developers die of debt in downturns (2013–19); post-2020 the listed leaders deleveraged |
| **Joint-development share** | Share of projects on JD/JV land (asset-light) vs owned land | Capital intensity |

### 1.2 NAV valuation

Value each project (and the land bank) on its cash flows, sum, adjust for corporate debt and rental assets:

**Godavari Developers** (fictional), 20 Cr shares, cost of equity 14%:

| Project | Sales value (₹ Cr) | Construction + other cost (% of sales) | Net cash flow (₹ Cr) | Years to complete (cash flow assumed at mid-point) | PV (₹ Cr) |
|:--|--:|--:|--:|--:|--:|
| A (launched, 70% sold) | 1,200 | 65% | 420 | 3 | 345 |
| B (launched, 40% sold) | 800 | 55% | 360 | 4 | 277 |
| C (planned) | 2,000 | 40% (owned land, low cost) | 1,200 | 5 | 865 |
| **PV of development projects** | | | | | **1,487** |
| Land bank (not yet planned), at market value less 30% | | | | | 600 |
| Rental assets (office park): ₹150 Cr NOI ÷ 8% cap rate | | | | | 1,875 |
| Less net debt | | | | | (900) |
| **NAV** | | | | | **3,062** |
| **NAV per share** | | | | | **₹153** |

```python
ke = 0.14
projects = [(1200, 0.65, 3), (800, 0.55, 4), (2000, 0.40, 5)]
pv = sum(s * (1 - c) / (1 + ke) ** (y / 2) for s, c, y in projects)     # 1,487
nav = pv + 600 + 150 / 0.08 - 900                                       # 3,062
print(round(pv), round(nav), round(nav / 20))
```

Developers have traded at discounts to NAV of 20–50% in bad times and at premiums in booms (verify current
levels for the listed leaders). The NAV is only as good as its inputs: price per sq ft assumptions, absorption
(how fast planned projects sell), cost inflation, and the cap rate on rental assets — show sensitivities to each.
The **cap rate** (net operating income ÷ value) for Grade-A Indian offices has been roughly 7.5–9% (verify), which
is why REITs matter here.

### 1.3 REITs and InvITs

**REITs** (offices, malls, warehouses) and **InvITs** (roads, power transmission, pipelines, telecom towers) are
SEBI-regulated trusts that must hold mostly completed, income-generating assets, distribute at least 90% of net
distributable cash flow, and cap leverage (49% of asset value, with rating conditions — verify the current SEBI
REIT/InvIT regulations). They are valued on:

- **Distribution yield** vs the 10-year G-sec: a spread of 100–300 bps has been typical for the listed office REITs
  (verify), wider for InvITs with finite-life road concessions whose distributions include return *of* capital.
- **NAV** (independent valuer's asset values, disclosed half-yearly) — price/NAV around 0.8–1.1x.
- **Growth**: contracted rent escalations, mark-to-market on lease renewals, occupancy, and acquisitions funded
  at yields above the cost of capital.
- **Concession life** (InvITs): a road InvIT's distributions stop when concessions expire unless it keeps acquiring.

Distributions are taxed by component (interest, dividend, return of capital, rental) — verify the current
treatment, which changed in 2023–24.

## 2. Infrastructure

Contract structure determines the economics; know which one you are looking at:

| Model | Who bears what | Cash-flow character | Metric | Valuation |
|:--|:--|:--|:--|:--|
| **EPC (engineering, procurement, construction)** | Contractor builds for a fixed price; owner bears traffic/demand | Lumpy; thin margins (8–15% EBITDA); working-capital heavy (retention, mobilisation advances, BGs) | Order book, book-to-bill, execution rate, margin by contract | P/E on normalised margins; DCF of order-book conversion |
| **BOT toll (build-operate-transfer)** | Concessionaire finances, builds, collects tolls for 15–30 years | Traffic risk; high leverage at project level; concession expires | Traffic growth, toll escalation (WPI-linked), concession life | Project DCF to end of concession; equity IRR |
| **BOT annuity / HAM (hybrid annuity)** | Authority pays fixed annuities (HAM: 40% during construction, 60% as annuities with interest) | Contracted; NHAI counterparty; inflation-indexed | Annuity schedule, cost of debt | DCF at a lower discount rate; bond-like |
| **Airports, ports** | Regulated (AERA for airports; TAMP/market for ports) tariffs plus non-aero/commercial revenue | Regulated core + growth optionality | Passenger/cargo volumes, regulated asset base, non-aero yield | RAB-based for regulated part; DCF for commercial |
| **InvIT-held assets** | As above, pooled | Distributions | Yield, NAV | See §1.3 |

Two checks specific to Indian infrastructure: **receivables from government entities** (NHAI is a good payer;
state agencies and DISCOMs less so — Kaveri's solar receivables are the same problem in miniature), and
**claims/arbitration** (disputed amounts with authorities can exceed a year's profit; read the contingent-asset
disclosures). Order-book based valuation assumes execution: check the historical order-book-to-revenue conversion
and margin per contract type before capitalising a "₹50,000 Cr order book".

## 3. Regulated utilities

Regulated power generation (thermal, hydro), transmission and distribution, and gas pipelines earn a return set by
a regulator (CERC for inter-state; SERCs for intra-state; PNGRB for gas) on a **regulated equity base**:

$$\text{Regulated profit} \approx \text{Regulated equity} \times \text{allowed RoE} + \text{incentives} − \text{disallowances}$$

Under CERC's 2024–29 tariff regulations the base RoE is **15.5% for thermal generation and 15.0% for
transmission** (run-of-river hydro 15.5%; pumped storage 17%), grossed up for tax, with incentives for availability
and penalties for under-performance ([Power Line summary](https://powerline.net.in/2024/02/05/roe-adjustments-key-highlights-of-cercs-draft-tariff-regulations/);
[CERC notification](https://cercind.gov.in/regulations/notification-2024.pdf)). The regulated model makes the
business bond-like:

- **Value ≈ regulated equity × justified P/B**, where justified P/B = (RoE − g)/($k_e$ − g). With allowed RoE
  15.5%, $k_e$ 11% (low risk) and growth in the equity base of 6%: (0.155 − 0.06)/(0.11 − 0.06) = **1.9x book** on the
  regulated equity. Growth comes from *capex* that gets added to the regulated base — the regulated utility is one
  of the few businesses where capex is directly value-creating at a known return.
- **Risks**: regulatory resets every five years; disallowance of capex or costs; DISCOM receivables (state
  distribution companies are chronic late payers — the government's late-payment-surcharge rules of 2022 improved
  this); merchant exposure (power sold outside PPAs at market prices — cyclical, higher return, higher risk);
  fuel and availability.
- **Renewables** differ: tariffs are fixed by competitive bidding (not RoE-regulated), so returns depend on the
  bid tariff, capex per MW, PLF (plant load factor) and financing cost; counterparty (SECI/DISCOM) risk remains.
  Value on project DCFs at the contracted tariff over the PPA life (25 years), with the equity IRR as the metric.
- **Power exchanges** (IEX) are platforms, not utilities — see [07.2](02-insurers-amcs-exchanges.md).

Separate the regulated, the contracted (PPA) and the merchant businesses in any utility's model; they deserve
different discount rates and multiples.

## 4. Telecom

Indian telecom is the textbook capital cycle ([05.4](../05-business-analysis/04-capital-cycle-and-competition.md);
[case I10](../13-case-studies/india/10-vodafone-idea-telecom-war.md)): a dozen operators in 2010, three private
players plus BSNL by 2019 after Jio's 2016 entry collapsed tariffs. The metrics:

| Metric | Definition | Reading |
|:--|:--|:--|
| **ARPU** | Average revenue per user per month | The price variable; rose from ~₹100 (2019) to ~₹200+ after the 2019, 2021 and 2024 tariff hikes (verify current levels by operator) |
| **Subscribers; active (VLR) subscribers; 4G/5G mix** | | Volume and mix; the industry gains ARPU by moving users to higher-value plans |
| **Churn** | Monthly subscriber loss | Vodafone Idea's continued loss of subscribers to the two leaders is the visible sign of a weak balance sheet |
| **EBITDA margin** | 40–55% for the leaders post-Ind AS 116 | High fixed costs → tariff hikes fall almost entirely to EBITDA |
| **Capex intensity** | Capex ÷ revenue: 20–40% in network build phases (5G) | The reason EBITDA is not free cash flow |
| **Net debt / EBITDA incl. spectrum and AGR liabilities** | Deferred spectrum payments to DoT are debt in economic substance; AGR dues after the 2019 Supreme Court judgment | Vodafone Idea's total liabilities to government exceeded its EV; the government converted dues to equity (2023, 2025 — verify stakes) |
| **Spectrum holdings and renewals** | Bands, expiry, cost | Renewal auctions are recurring capex |

Valuation: **EV/EBITDA** (8–12x for the Indian leaders in recent years — verify) *including* spectrum liabilities in
EV, cross-checked with a DCF where capex intensity fades as the 5G build completes; and always a **free-cash-flow**
view — EBITDA − capex − spectrum payments − interest — which is what pays down the debt. For a distressed operator the
Merton lens ([06.7](../06-valuation/07-other-valuation-methods.md)) is the honest one: the equity is an option on
tariff hikes and government forbearance.

Tower companies (Indus Towers) and fibre/data-centre assets are the picks-and-shovels: contracted tenancies, lower
risk, InvIT-like economics, but with customer concentration in three operators (one of them weak).

!!! tip "Trader's lens"
    These sectors are where duration lives in equities. A regulated utility or an office REIT is a long-dated
    bond with an equity wrapper — its price moves with the 10-year yield more than with its own news, and the
    spread to G-secs is the valuation. Telecom, by contrast, is a levered call on an oligopoly's pricing discipline:
    the payoff is convex to ARPU (fixed costs) and to the regulator's tolerance. Know which duration you are
    holding; a portfolio of "infrastructure" can be a rates trade or a policy trade, and they hedge differently.

!!! info "India notes"
    - Real estate: RERA (2016) forces escrow of 70% of customer collections into the project account, which
      protects buyers and constrains developers' cash flexibility; read the RERA registrations for launch
      timelines.
    - Roads: NHAI's HAM model and toll-operate-transfer (TOT) monetisation are the main pipelines; NHAI's own
      balance sheet and payment record are part of every road company's analysis.
    - Power: the DISCOM problem (state utilities' losses and dues) is the sector's structural risk; the
      Electricity (Late Payment Surcharge) Rules, 2022 and RDSS reforms changed the payment discipline — verify
      current receivable levels for generators.
    - Telecom: AGR liabilities, spectrum usage charges, and the 2021 relief package (moratorium, equity
      conversion option) define Vodafone Idea's survival; the government's stake and any further conversions
      change the share count materially — check the latest before valuing per share.

!!! warning "Common mistakes"
    - Valuing a developer on trailing P/E or revenue growth.
    - Capitalising an order book without checking conversion and margin history.
    - Treating a regulated utility's allowed RoE as the market's RoE (it is on *regulated* equity, not total equity,
      and after disallowances).
    - Excluding spectrum and AGR liabilities from telecom EV.
    - Comparing EV/EBITDA across companies with different lease intensity (towers, fibre) without Ind AS 116 adjustment.
    - Ignoring concession expiry in InvIT/BOT valuations.

## Key terms

| Term | Meaning |
|:--|:--|
| **Pre-sales / bookings** | Value of residential units sold in a period, before revenue recognition |
| **Collections** | Cash received from customers during a period |
| **Completion method** | Revenue recognised when control transfers (Ind AS 115 for Indian developers) |
| **NAV (real estate)** | PV of project cash flows + land + rental assets − debt |
| **Cap rate** | Net operating income ÷ property value |
| **REIT / InvIT** | Listed trusts holding income-generating real estate / infrastructure; ≥ 90% distribution |
| **EPC / BOT / HAM** | Construction-only / build-operate-transfer (toll or annuity) / hybrid annuity contract models |
| **Order book; book-to-bill** | Unexecuted contracts; new orders ÷ revenue |
| **Regulated equity base** | The equity on which a regulator allows a return |
| **Allowed RoE** | The regulator-set return (CERC 2024–29: 15.5% thermal, 15% transmission) |
| **PPA** | Power purchase agreement: long-term contracted tariff |
| **Merchant power** | Power sold at market prices outside PPAs |
| **PLF** | Plant load factor: actual generation ÷ capacity |
| **ARPU** | Average revenue per user per month |
| **AGR** | Adjusted gross revenue — the base for telecom licence fees; the 2019 Supreme Court ruling created large dues |
| **Spectrum liabilities** | Deferred payments to the government for spectrum; debt-like |

## Check your understanding

1. Godavari Developers reports FY26 revenue down 40% while pre-sales rose 25%. Explain.
<details><summary>Answer</summary>Revenue reflects projects completed in FY26 (sold years earlier); pre-sales are
this year's bookings, recognised only at completion in 2–4 years. The business is growing; the P&L is describing
the past. Look at pre-sales, collections and operating cash flow.</details>

2. Recompute Godavari's NAV per share if the cap rate on the office park rises to 9% and project C's sales value
   falls 20%.
<details><summary>Answer</summary>Rental = 150/0.09 = 1,667 (−208); C: 1,600 × 0.6 = 960 cash flow; PV = 960/1.14^2.5
= 692 (−173). NAV = 3,062 − 208 − 173 = ₹2,681 Cr → ₹134/share (−12%).</details>

3. A transmission company adds ₹2,000 Cr of regulated equity through capex at the 15% allowed RoE. What is the
   value created at $k_e$ 11%, g 6%?
<details><summary>Answer</summary>Justified P/B = (0.15 − 0.06)/(0.11 − 0.06) = 1.8x → ₹2,000 Cr of equity deployed
becomes ~₹3,600 Cr of value, i.e. ~₹1,600 Cr created — capex is value-creating by construction as long as the
regulator allows it into the base and $k_e$ stays below the allowed RoE.</details>

4. Why should spectrum liabilities be treated as debt when computing a telecom operator's EV?
<details><summary>Answer</summary>They are fixed, contractual, interest-bearing obligations to the government
arising from an asset purchase (spectrum) — economically identical to a loan financing a capex item. Excluding them
understates EV and overstates the equity's share of enterprise value.</details>

5. A road InvIT yields 12% against a 7% G-sec. Is that spread a bargain?
<details><summary>Answer</summary>Not necessarily: part of the distribution is return of capital on finite
concessions (the assets run off), so the yield overstates the perpetual return; traffic risk on toll roads and NHAI
counterparty risk on annuities also apply. Compare on NAV and on the IRR to concession expiry, not headline yield.</details>

## Go deeper

- SEBI (REIT) Regulations, 2014 and (InvIT) Regulations, 2014, as amended — the structural rules; the listed REITs'
  half-yearly valuation reports.
- CERC (Terms and Conditions of Tariff) Regulations, 2024 — the regulated-return norms cited above
  ([CERC](https://cercind.gov.in/regulations/notification-2024.pdf)).
- NHAI annual reports and the Ministry of Road Transport's HAM/TOT documents — for road economics.
- TRAI quarterly performance indicator reports — subscribers, ARPU, market share by operator.
- [Case I10 Vodafone Idea](../13-case-studies/india/10-vodafone-idea-telecom-war.md) — the capital cycle and equity-as-option in one company.

---
[← Previous: 07.5 Holdcos, conglomerates, PSUs & MNC subsidiaries](05-holdcos-conglomerates-psus-mncs.md) · [Module index](index.md) · [Next: 08.1 Banks & lending →](../08-sectors/01-banks-and-lending.md)
