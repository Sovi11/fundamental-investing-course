# 07.2 · Insurers, AMCs, exchanges & brokers

> **Why this matters:** India's listed financial sector is much more than banks. Life insurers sell forty-year
> promises and report profits that bear little relation to the value they create in a year; asset managers earn
> fees on money they do not own; exchanges and depositories are regulated near-monopolies whose profits swing with
> retail activity and with the regulator's mood. Each has its own metrics and its own valuation logic, and each is
> mis-analysed when forced into a P/E or a DCF template.

**Learning objectives** — after this lesson you can:

- Read a life insurer through embedded value, value of new business, VNB margin, persistency and product mix, and
  value it on P/EV.
- Read a general insurer through combined ratio, float and reserving.
- Analyse an asset manager through AUM mix, yields, flows, TER regulation and operating leverage.
- Analyse exchanges, depositories, brokers and RTAs through volumes, take rates and regulatory risk, with the
  2024–25 SEBI derivatives measures as the live example.
- Choose the right valuation approach for each.

**Prerequisites:** [07.1 Banks & NBFCs](01-banks-and-nbfcs.md), [06.7 Other valuation methods](../06-valuation/07-other-valuation-methods.md)  ·  **Time:** ~100 min

---

## 1. Life insurance

### 1.1 Why accounting profit is the wrong lens

A life insurer selling a 20-year policy incurs most of its costs (agent commission, underwriting, acquisition) in
year one and collects premiums and earns investment income for two decades. Under Indian accounting the first-year
strain depresses profit when the business is growing fastest; a shrinking insurer can show *rising* profit as old
policies mature. Statutory profit therefore tells you almost nothing about value creation. The industry's answer is
**embedded value** accounting, disclosed by all listed Indian life insurers (verify the current status of Ind AS
117 / IFRS 17 adoption for insurers, which IRDAI has been phasing in — as of 2026 embedded value remains the
primary valuation disclosure).

### 1.2 The metrics

| Metric | Definition | What it tells you |
|:--|:--|:--|
| **Embedded value (EV)** | Adjusted net worth + value of in-force business (PV of future profits from policies already sold, after cost of capital) | The economic book value; what the existing book is worth if no new policy were ever sold |
| **Value of new business (VNB)** | PV of expected future profits from policies sold *this year* | The value created by a year's selling — the insurer's "earnings" |
| **VNB margin** | VNB ÷ annualised premium equivalent (APE = 100% of regular premium + 10% of single premium) | Profitability of new sales; driven by product mix and expense efficiency (Indian listed insurers have reported VNB margins roughly in the 20–30% range in recent years — verify current disclosures) |
| **APE growth** | Growth in new-business volume | The volume driver |
| **Persistency** (13th, 25th, 37th, 61st month) | Share of policies still in force after 1, 2, 3, 5 years | Quality of sales; lapses destroy VNB that was already booked |
| **Product mix** | ULIP (unit-linked; low margin, market-sensitive) / participating / non-participating savings (high margin, interest-rate risk) / protection (highest margin) / annuities | Margin and risk profile |
| **Operating RoEV** | (EV growth from operations) ÷ opening EV | The economic return on the franchise, usually mid-to-high teens for good insurers |
| **Solvency ratio** | Available solvency margin ÷ required; IRDAI minimum 150% | Capital adequacy |
| **Channel mix** | Bancassurance / agency / direct / online | Distribution cost and dependence (bank-owned insurers rely on the parent bank) |

### 1.3 Valuation: P/EV and appraisal value

$$\text{Appraisal value} = \text{EV} + \text{Structural value} = \text{EV} + \text{VNB} \times \text{multiple}$$

The multiple on VNB is a growing-perpetuity of future years' new business: $\text{VNB}_1 / (k_e − g)$ with a fade.
In practice analysts quote **P/EV** (market cap ÷ embedded value): historically 2–4x for Indian private insurers
in growth phases, lower for LIC and for slower growers (verify current levels). The justified P/EV is

$$\frac{P}{EV} = 1 + \frac{\text{VNB}_1 / \text{EV}}{k_e − g} \;(\text{with fade})$$

**Worked example — Vindhya Life (fictional).** EV ₹20,000 Cr; VNB ₹1,600 Cr (VNB/EV 8%); operating RoEV 17%;
$k_e$ 12%; VNB growth 12% for ten years fading to 5%.

```python
ev, vnb, ke = 20000.0, 1600.0, 0.12
growth = [0.12] * 5 + [0.10, 0.08, 0.07, 0.06, 0.05]
pv, v = 0.0, vnb
for t, g in enumerate(growth, 1):
    v *= (1 + g); pv += v / (1 + ke) ** t
tv = v * 1.05 / (ke - 0.05); pv += tv / (1 + ke) ** 10
appraisal = ev + pv
print(round(pv), round(appraisal), round(appraisal / ev, 2))
# structural value ≈ 34,500; appraisal ≈ 54,500; P/EV ≈ 2.7x
```

A P/EV of 2.7x is what 8% VNB/EV and a decade of 12%→5% growth justify at a 12% cost of equity. At 3.5x the market
is assuming faster or longer growth, higher margins, or a lower $k_e$ — the reverse-DCF logic of
[06.6](../06-valuation/06-reverse-dcf-and-expectations.md) applies directly. Sensitivities that matter: persistency
(a 5-pp fall in 13th-month persistency can cut VNB by a tenth), interest rates (non-par guarantees), and equity
markets (ULIP AUM and fees).

## 2. General insurance

Non-life insurers (motor, health, fire, crop) write one-year contracts, so the accounting is more honest, and the
economics are Buffett's: **float** (premiums collected before claims are paid) invested for the insurer's benefit,
plus an underwriting result.

| Metric | Definition | Reading |
|:--|:--|:--|
| **Loss ratio** | Claims incurred ÷ net earned premium | Underwriting discipline; health and motor third-party run high |
| **Expense ratio** | Operating expenses + commissions ÷ net written premium | Distribution cost |
| **Combined ratio** | Loss ratio + expense ratio | < 100% = underwriting profit; Indian general insurers have often run above 100%, earning their profit on float investment income |
| **Float** | Reserves for unpaid claims + unearned premium | Interest-free capital if combined ratio ≤ 100%; check its cost when above |
| **Reserving adequacy** | Prior-year claim development (reserve releases or strengthening) | Persistent releases = conservative reserving (good); strengthening = past under-reserving (bad) |
| **Solvency ratio** | As for life; minimum 150% | |
| **Growth by segment** | Motor OD/TP, health retail vs group, crop, commercial | Mix drives loss ratios; crop is volatile and government-priced |

Valuation: P/E and P/B work (profits are annual), but adjust for float value and reserve quality. An insurer at 100%
combined ratio with float of 2x equity invested at 7% earns 14% on equity from float alone; that is the franchise.

## 3. Asset management companies (AMCs)

An AMC earns a percentage of assets under management (the **total expense ratio**, TER) for managing mutual funds.
The economics are the purest operating leverage in finance: revenue is AUM × yield; costs are mostly fixed
(people, technology) plus distributor commissions that scale with AUM.

| Metric | Definition | Reading |
|:--|:--|:--|
| **AUM and mix** | Equity / hybrid / debt / liquid / ETF-passive | Equity AUM yields ~4–8x what liquid/ETF AUM yields; mix drives revenue more than total AUM does |
| **Net flows vs mark-to-market** | Decompose AUM growth | Flows are the franchise; MTM is the market |
| **SIP book** | Monthly systematic inflows | Sticky, retail, the industry's structural tailwind (industry SIP flows ran above ₹25,000 Cr/month through 2025–26 — verify current AMFI data) |
| **Yield (revenue/avg AUM)** | Blended TER retained by the AMC after distributor share | Falls as AUM grows (SEBI's slab-based TER caps step down with scheme size) and as passive share rises |
| **Cost-to-income; operating margin** | | Best-in-class AMCs run 70%+ operating margins on core revenue |
| **Market share of equity AUM; flows** | | Consolidation toward the top 5–7 players |
| **Other income** | Treasury on the AMC's own surplus | Often 20–30% of PBT; value at cash-like multiples |

**Regulation is the swing factor.** SEBI sets TER caps by AUM slab and scheme type, has cut them several times
(2018 was the big reset), and periodically consults on further reductions, on distributor commission structures and
on performance-linked fees (verify the status of SEBI's 2025–26 TER and expense-rationalisation proposals). A 10-bp
TER cut on equity AUM flows straight to the AMC's revenue and, with fixed costs, disproportionately to profit.

Valuation: P/E (30–45x has been common for listed Indian AMCs in strong markets — verify), or better, **market cap
÷ AUM** (roughly 5–12% of equity AUM for the leaders, less for debt-heavy books) cross-checked with a DCF of
fee income under explicit TER-cut scenarios. The trader's instinct is right here: an AMC is a long-only leveraged
bet on the equity market with a regulator holding a call on the fee rate.

## 4. Exchanges, depositories, RTAs, brokers

### 4.1 The plumbing and its economics

| Business | Revenue driver | Take rate | Cost structure | Moat | Regulatory exposure |
|:--|:--|:--|:--|:--|:--|
| **Stock exchanges** (NSE — unlisted as of 2026 but heading to IPO, verify; BSE; MCX for commodities) | Traded volumes × transaction fee; listing fees; data; co-location; clearing | Basis points of turnover; per-lot in options | Mostly fixed (technology); huge operating leverage | Liquidity network effect + licence | Transaction-charge caps; product rules (weekly expiries, lot sizes); interoperability |
| **Depositories** (CDSL, NSDL) | Number of demat accounts (annual issuer charges, account maintenance) + transaction charges | Small fixed fees per account/transaction | Fixed | Duopoly licence + network | Fee caps; account-opening cycles |
| **Clearing corporations** | Clearing fees; margin float income | | | Licence | Margin rules |
| **Registrars (RTAs)** (CAMS, KFin) | AUM of mutual funds serviced × bps; folio counts; IPO/corporate registry | Small bps | Fixed | Duopoly with switching costs | AMC fee pressure flows through |
| **Brokers** (discount and full-service; listed: e.g. Angel One, Zerodha unlisted) | Orders × brokerage; interest on client float and margin funding; distribution | Per order or bps | Semi-variable (customer acquisition) | Weak — price competition; some scale in technology | Direct: brokerage caps, float rules (SEBI's "ASBA-like" client-fund handling), F&O curbs |

### 4.2 The 2024–25 SEBI derivatives measures — a live case

Index options had become the world's largest derivatives market by contract count, driven by Indian retail trading
weekly expiries. SEBI's study found most retail F&O traders lost money, and from November 2024 it phased in
measures: one weekly-expiry index per exchange, larger minimum contract sizes (Nifty lot from 25 to 75, later
adjusted; Bank Nifty weekly expiries withdrawn), upfront collection of option premiums, intraday position-limit
monitoring and removal of calendar-spread margin benefit on expiry day
([Zerodha summary](https://zerodha.com/z-connect/business-updates/sebis-new-rules-for-index-derivatives-heres-whats-changing);
[NSE lot-size circulars](https://nsearchives.nseindia.com/content/circulars/FAOP70616.pdf);
[lot sizes in 2026](https://www.sahi.com/blogs/nifty-lot-size-2026-bank-nifty-sensex)). Volumes in the affected
segments fell sharply; exchange and broker revenues that depended on retail options activity fell with them.

The analytical lessons:

1. **Regulatory take-rate risk is not hypothetical** for businesses whose revenue is a slice of a flow the regulator
   considers socially harmful. Model it as a scenario with a probability, not as a footnote.
2. **Volume is the state variable.** Build the exchange model as volumes × fee, and stress volumes (−30%, −50%) with
   costs fixed: the operating leverage that made the stock a multi-bagger works in reverse.
3. **Mix matters**: cash equities, index options, stock futures, commodities and currency have different fee
   structures and different regulatory sensitivities.
4. **Second-order effects**: fewer weekly expiries concentrated volume on the surviving ones (BSE's Sensex weekly
   gained share); brokers' float income rose with margin requirements; discount brokers' order counts fell. Every
   change in plumbing rules reallocates revenue across the chain.

!!! tip "Trader's lens"
    You have seen this from the other side. An exchange is short a put on retail participation and long the
    regulator's forbearance; a broker is the same with less moat. When you look at MCX's or BSE's P/E, decompose the
    earnings by product and ask which products SEBI, the ministry or a court could switch off, and what fraction of
    profit sits there. That is a jump-risk analysis, and it should be priced as one.

### 4.3 Valuation

Exchanges and depositories: DCF of fee income with explicit volume and take-rate scenarios (the regulator is a
scenario), cross-checked against global exchange multiples (typically 20–30x earnings for scaled, diversified
exchanges — verify) and against the value of the *non-volume* revenue (listing, data, technology) which deserves a
higher multiple than the volume revenue. Brokers: P/E with a cyclical haircut, and a close look at how much of profit
is float interest (rate-sensitive) versus brokerage (volume-sensitive). RTAs: DCF of servicing fees keyed to mutual-fund
AUM growth with AMC-fee-pressure pass-through.

## 5. Choosing the method — summary

| Business | Primary metric | Valuation | Key risk to scenario |
|:--|:--|:--|:--|
| Life insurer | EV, VNB, VNB margin, persistency | P/EV; appraisal value (EV + VNB multiple) | Persistency; product regulation (e.g., surrender-value rules of 2024); rates |
| General insurer | Combined ratio, float, reserving | P/E and P/B with float-adjusted RoE | Claims inflation (health), crop, pricing cycles |
| AMC | Equity AUM, flows, yield, margin | P/E; mcap/AUM; DCF under TER scenarios | TER cuts; passive shift; market drawdown |
| Exchange / depository | Volumes, take rate, product mix | DCF with regulatory scenarios; global exchange multiples | Regulatory product/fee changes; competing venue |
| Broker | Active clients, orders, float | P/E with cyclical haircut | Regulatory curbs; price competition; rates |
| RTA | Serviced AUM, folios | DCF; P/E | AMC fee pressure |

!!! info "India notes"
    - IRDAI's 2024 changes to surrender values (higher guaranteed surrender values earlier in a policy's life)
      reduced margins on non-par savings products and forced repricing — an example of product regulation moving
      VNB margins across the industry within a quarter (verify the specifics and subsequent margin trends).
    - Bank-owned insurers and AMCs (SBI, HDFC, ICICI groups) depend on the parent bank's distribution; check the
      bancassurance share and any regulatory push for "open architecture".
    - NSE's IPO (long delayed by regulatory issues; verify its status in 2026) would create the largest listed
      exchange; until then, exchange analysis in India is BSE and MCX — both smaller, more product-concentrated and
      hence more regulatorily sensitive.

!!! warning "Common mistakes"
    - Valuing a growing life insurer on statutory P/E (it looks absurdly expensive) or a shrinking one as cheap.
    - Treating VNB margin as fixed — it moves with product mix, and mix moves with regulation and rates.
    - Ignoring persistency: a VNB booked on a policy that lapses in year two was never real.
    - Valuing an AMC on total AUM without the equity/debt mix.
    - Extrapolating exchange volumes from a retail boom year.
    - Forgetting that other income (treasury) is a large share of AMC and exchange profits and deserves a lower multiple.

## Key terms

| Term | Meaning |
|:--|:--|
| **Embedded value (EV)** | Net worth + PV of future profits on in-force life policies |
| **Value of new business (VNB)** | PV of expected profits from policies sold in a period |
| **VNB margin** | VNB ÷ annualised premium equivalent (APE) |
| **APE** | Annualised premium equivalent: regular premium + 10% of single premium |
| **Persistency** | Share of policies still in force after a given period (13th, 25th, 37th, 61st month) |
| **Operating RoEV** | Operating growth in embedded value ÷ opening EV |
| **P/EV** | Market capitalisation ÷ embedded value |
| **Appraisal value** | EV + value of future new business |
| **Combined ratio** | Claims ratio + expense ratio for a general insurer; < 100% = underwriting profit |
| **Float** | Premiums held before claims are paid; invested for the insurer's account |
| **TER** | Total expense ratio charged to a mutual-fund scheme; capped by SEBI in slabs |
| **SIP** | Systematic investment plan; recurring retail mutual-fund inflows |
| **Take rate** | Fee as a share of transaction value or volume |
| **Weekly expiry** | Index option contracts expiring weekly; the focus of SEBI's 2024–25 curbs |
| **RTA** | Registrar and transfer agent; services mutual funds' investor records |

## Check your understanding

1. An insurer's statutory profit rises 20% while APE falls 10% and VNB falls 15%. Is the business improving?
<details><summary>Answer</summary>No. Statutory profit is rising because fewer new policies mean less first-year
strain, while the in-force book releases profit; VNB — the value created by selling — is shrinking. The franchise
is worth less; the accounting says the opposite.</details>

2. Recompute Vindhya Life's appraisal value if $k_e$ is 13% and VNB growth fades to 5% after five years instead of
   ten (5 years at 12%, then 5%).
<details><summary>Answer</summary>Run the loop with growth = [0.12]×5 then terminal at 5% from year 5: structural
value falls to ~₹27,900 Cr and appraisal to ~₹47,900 Cr, i.e. P/EV ≈ 2.4x — a 100-bp higher $k_e$ and a shorter
growth runway remove a third of the structural value; P/EV is very sensitive to both.</details>

3. An AMC has ₹3,00,000 Cr AUM, 55% equity at a 60-bp net yield and 45% debt/liquid at 12 bp; costs ₹700 Cr. What
   is operating profit, and what does a 10-bp cut in the equity TER do to it?
<details><summary>Answer</summary>Revenue = 1,65,000 × 0.0060 + 1,35,000 × 0.0012 = 990 + 162 = ₹1,152 Cr; operating
profit = 1,152 − 700 = ₹452 Cr. A 10-bp equity cut removes 1,65,000 × 0.0010 = ₹165 Cr of revenue → profit ₹287 Cr,
−37% from a 14% revenue cut. That is operating leverage in reverse.</details>

4. Why did SEBI's 2024 measures hurt some plumbing businesses more than others?
<details><summary>Answer</summary>Revenue concentration: exchanges and discount brokers whose growth had come from
retail index options lost the most; depositories (account-based fees) and RTAs (AUM-based) were largely unaffected;
BSE gained relative share as the surviving weekly expiry venue for Sensex. The lesson is to map revenue by product to
regulatory sensitivity.</details>

5. Why does a general insurer with a 102% combined ratio still earn a return for shareholders?
<details><summary>Answer</summary>It pays 2% of premium for the use of its float, which it invests. With float of 2x
equity earning 7%, investment income adds ~14% to RoE, more than covering the 2% underwriting loss on premium. The
business is an asset manager funded by policyholders — attractive while the combined ratio stays close to 100%.</details>

## Go deeper

- Listed Indian life insurers' annual embedded-value reports (with independent actuary certification) — read one
  cover to cover; they are the clearest financial documents in India.
- IRDAI annual report and AMFI monthly data — industry volumes, mix, SIP flows.
- SEBI's consultation papers and circulars on F&O (2024–25) and on mutual-fund expenses — primary sources for the
  regulatory scenarios.
- Warren Buffett's Berkshire letters on insurance float (esp. 1995–1999 and the "float" appendices).
- Sources used: [Zerodha on SEBI's index-derivative rules](https://zerodha.com/z-connect/business-updates/sebis-new-rules-for-index-derivatives-heres-whats-changing);
  [Jainam summary of SEBI F&O rules](https://www.jainam.in/blog/sebi-new-rules-for-fo-trading/);
  [NSE circular on lot sizes](https://nsearchives.nseindia.com/content/circulars/FAOP70616.pdf).

---
[← Previous: 07.1 Banks & NBFCs](01-banks-and-nbfcs.md) · [Module index](index.md) · [Next: 07.3 Cyclicals & commodities →](03-cyclicals-and-commodities.md)
