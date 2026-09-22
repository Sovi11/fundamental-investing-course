# 07.5 · Holding companies, conglomerates, PSUs & MNC subsidiaries

> **Why this matters:** a large share of Indian market capitalisation sits in companies whose value depends on
> *who controls them* as much as on what they do: holding companies that own stakes they will never sell,
> conglomerates that cross-subsidise, public-sector undertakings whose majority owner has social objectives, and
> subsidiaries of multinationals whose parent sets the royalty and decides the strategy. The valuation methods are
> the standard ones; the adjustments for control are where the analysis lives.

**Learning objectives** — after this lesson you can:

- Build a sum-of-the-parts for a holding company and argue a holdco discount from its causes.
- Explain the conglomerate discount and how demergers address it.
- Analyse a PSU: government ownership, dividend policy, OFS overhang, social objectives, and the re-rating cycles
  of 2020–25.
- Analyse an MNC subsidiary: royalties and fees, parent strategy, delisting/buy-out optionality, capital-allocation
  constraints.
- Recognise family business-group dynamics and where minority value leaks or accrues.

**Prerequisites:** [06.7 Other valuation methods](../06-valuation/07-other-valuation-methods.md),
[05.6 Corporate governance](../05-business-analysis/06-corporate-governance-india.md)  ·  **Time:** ~90 min

---

## 1. Holding companies

A **holding company** (holdco) exists to own stakes in other companies. Its cash flows are the dividends it
receives and whatever it earns on its own treasury; its value is the market value of what it holds, less the
frictions between that value and you.

### 1.1 SOTP for a holdco — Deccan Investments (fictional)

| Holding | Stake | Market value of the investee (₹ Cr) | Value of stake (₹ Cr) | Basis |
|:--|--:|--:|--:|:--|
| Listed operating company A | 35% | 18,000 | 6,300 | Market |
| Listed operating company B | 22% | 9,000 | 1,980 | Market |
| Unlisted NBFC | 100% | 1,200 | 1,200 | 1.2x book |
| **Gross asset value** | | | **9,480** | |
| Shares outstanding (Cr) | | | 5.0 | |
| **Gross NAV per share** | | | **₹1,896** | |

If Deccan's stock trades at ₹950, the **holdco discount** is 1 − 950/1,896 = **50%**. Is that right?

### 1.2 Sizing the discount from its causes

| Cause | Estimate for Deccan | Comment |
|:--|--:|:--|
| Tax on eventual sale of stakes (long-term capital gains at the current rate on the unrealised gain — verify the rate in [11.5](../11-process/05-monitoring-and-selling.md)) | ~8–10% of gross value if the cost basis is near zero | Only relevant if a sale is ever likely; if never, the leak is via dividends |
| Dividend leakage: investee dividends are taxed at the holdco (corporate rate, with a deduction for onward dividends under Sec. 80M — verify), then again in your hands | Reduces the cash yield reaching you by 25–35% | The perpetuity of this leak is the structural core of the discount |
| Holdco expenses | ₹8 Cr/yr ÷ 11% $k_e$ = ₹73 Cr ≈ 1% | Small |
| Control: the promoter will not sell, merge or distribute; minorities cannot force it | Judgement: 15–30% depending on history | The largest and least quantifiable component; read 20 years of the holdco's actions |
| Illiquidity of the holdco stock | 5–10% | Traded value vs the investees' |
| Restructuring optionality (the other way) | −5 to −15% | A history of buybacks, mergers into the operating company, or promoter reorganisations narrows the discount |

A build-up of 10% (tax) + 15% (dividend leakage in perpetuity) + 1% + 20% (control) + 5% (liquidity) − 5% (option)
≈ **46%** — close to the observed 50%. That does not make 50% "right"; it makes it *explained*, and it tells you
what would change it: a change in dividend taxation, a buyback programme, a promoter reorganisation, or evidence of
distributions. Indian holdco discounts have ranged from ~30% to ~70% across names and periods (verify current
levels for e.g. Bajaj Holdings, Tata Investment, Maharashtra Scooters, Bombay Burmah, Pilani Investment); trades
that "wait for the discount to close" have worked mainly when a corporate event was already in motion.

!!! tip "Trader's lens"
    A holdco is a basket trade with a negative carry (the leakages) and an embedded call on restructuring. The
    discount is the price of the carry and the illiquidity; it is *not* free money. The relative-value trade —
    long holdco, short the underlying stakes in proportion — isolates the discount's *changes*, which move with
    sentiment (discounts widen in bear markets when nobody wants illiquid structures) and with event probability.
    That trade has negative carry and a fat right tail; size it accordingly.

## 2. Conglomerates and the conglomerate discount

An operating company running several unrelated businesses (chemicals + hotels + textiles + finance) tends to trade
below the sum of its parts valued separately, for reasons that are partly analytical (opacity of segment
economics, capital allocation across segments that no one can audit, the market applying the *worst* segment's
multiple to the whole) and partly structural (investors cannot choose the exposure they want).

Analysis: value each segment on its own method and peers (segment disclosures under Ind AS 108 give revenue and
results; capital employed by segment is usually disclosed), subtract unallocated corporate costs capitalised,
subtract net debt, and compare. A discount of 10–25% is typical; the analysis then asks whether a catalyst exists:

- **Demergers**: splitting the businesses into separately listed companies has been the standard cure and, in
  India, a reliable source of returns — spun-off entities get their own investor base and multiples
  ([12.3](../12-macro-special-sits/03-special-situations.md); [case I12 ITC](../13-case-studies/india/12-itc-value-trap-or-not.md);
  the Reliance, Aditya Birla, Tata Motors and Vedanta demergers of 2023–25 — verify each).
- **Portfolio simplification**: sale of non-core units; the discount narrows as the story simplifies.
- **Group restructuring**: cross-holdings unwound, which also cuts the holdco layer.

Beware the opposite: a "conglomerate premium" in bull markets for groups with a strong narrative and rising
cross-holding values (the Adani group in 2021–22 — [case I9](../13-case-studies/india/09-adani-hindenburg-2023.md))
tends to reverse when leverage or governance comes into question.

## 3. Public-sector undertakings (PSUs)

The Government of India (or a state) holds a majority — often 51–90% — in listed PSUs across banking, oil & gas,
power, mining, defence, railways and engineering. The owner's objectives differ from a private promoter's:

| Feature | Effect on analysis | Example / where to see it |
|:--|:--|:--|
| **Government as majority owner with policy objectives** | Pricing, capex and investment decisions may serve policy (fuel under-recoveries at OMCs; Coal India's notified prices; PSU banks' priority lending and rescues) rather than returns | Annual reports; ministry directives; budget documents |
| **Dividend policy** | DIPAM guidelines require CPSEs to pay the higher of 30% of PAT or 4–5% of net worth (verify current guidelines); dividends are a fiscal revenue source → high, reliable payouts | High dividend yields, especially at cycle peaks; the yield is not a valuation anchor for cyclicals |
| **OFS overhang** | Government divestment through offers for sale, ETFs (Bharat 22, CPSE ETF) and strategic sales adds supply; minimum public shareholding rules force sales | Disinvestment targets in the Union Budget; SEBI MPS rules (25% public float, with exemptions for PSUs — verify) |
| **Capital allocation constraints** | Cross-subsidies within the group (a profitable PSU asked to buy a weak one — e.g., ONGC–HPCL 2018; LIC–IDBI); mandated capex | Announcements; parliamentary questions |
| **Governance** | Board appointments by ministries; CMD tenure; vigilance culture that slows decisions but also constrains fraud | — |
| **Re-rating cycles** | PSUs traded at deep discounts to private peers for a decade (2013–20), then re-rated sharply in 2022–24 on capex, defence, power and rail themes and on "policy support"; parts of that re-rating reversed in 2024–25 (verify magnitudes) | Screener PSU index vs Nifty; sector P/B histories |

Valuation approach: the standard method for the sector (P/B for banks, EV/EBITDA and normalised earnings for
commodities, order-book DCF for defence), then explicit adjustments for (i) the policy risk to cash flows (a
scenario, not a discount rate fudge), (ii) the dividend floor (a real support for value in cash-rich PSUs), and
(iii) supply overhang and float. The cheapness of PSUs is often real *and* often permanent: a 6x P/E on a PSU whose
owner will never let it price rationally is not 6x on the same earnings power as a private peer.

## 4. MNC subsidiaries

Listed Indian arms of multinationals (consumer goods, pharma, engineering, autos, IT hardware) share a pattern:
strong franchises, high returns, conservative balance sheets, premium multiples — and a parent whose interests sit
above the minorities'.

| Issue | What to check | Where |
|:--|:--|:--|
| **Royalty and technical fees** | % of sales; trend; what is received for it; whether increases track any new technology; shareholder approval status (LODR Reg 23(1A): related-party royalty/brand payments above 5% of turnover need minority approval) | RPT note; AGM notices; SEBI's 2023 consultation on royalties |
| **Parent strategy** | Does the parent route new products, exports and adjacent categories through the listed entity or through a 100%-owned Indian company? | Parent's annual report; announcements of new unlisted Indian subsidiaries |
| **Transfer pricing** | Imports from the parent at group prices | RPT note; gross margin vs local peers |
| **Capital allocation** | Cash accumulates (the parent does not want debt); buybacks and special dividends at the parent's convenience | Cash as % of assets; other income share |
| **Delisting / buy-out optionality** | Parents have delisted (or attempted to) at premiums when the Indian arm is strategic and the price is right; the reverse book-building mechanism sets the price | History of delisting attempts; parent's holding (above 75% forces a sale or a delisting) |
| **Open offers and stake increases** | Parent raising its stake via open offer or creeping acquisition | SAST filings |

Valuation: the operating business on its merits (often deserving a premium for franchise and governance
*controls*), minus the capitalised royalty leak beyond what a third party would pay, plus an explicit probability
× premium for a delisting or buy-out, minus a discount for strategic side-lining. The royalty adjustment can be
large: a subsidiary paying 4.5% of ₹5,000 Cr sales (₹225 Cr) against PAT of ₹600 Cr is sending 27% of pre-royalty
profit to the parent; if a fair royalty were 2%, ₹125 Cr a year (≈ 20% of PAT) is the leak — capitalised at a
30x multiple, ₹3,750 Cr of value.

## 5. Family business groups

Most Indian conglomerates are family groups: several listed companies with cross-holdings, a family holdco or
trust at the top, and shared brands, treasury and management. The analytical questions:

- **Where does the group's value accrue?** The company the family owns most of tends to get the best assets and
  the best terms.
- **Cross-holdings and inter-corporate deposits**: map them from the investments notes and SEBI SAST filings;
  a group with circular holdings has less real equity than the sum of the listed market caps suggests.
- **Group support and contagion**: a weak group company's rescue (guarantees, ICDs, mergers) is paid for by the
  strong one's minorities; a group-level debt problem hits every listed entity's multiple at once.
- **Succession and splits**: family divisions have created value (Reliance 2005) and destroyed it (protracted
  disputes); read the succession plan and the shareholder agreement disclosures.

!!! info "India notes"
    - Minimum public shareholding (25%) and the promoter cap (75%) shape both PSU divestment and MNC delisting
      decisions; SEBI's delisting regulations (2021, amended 2024 to add a fixed-price route — verify) set the
      price mechanics.
    - Section 80M of the Income-tax Act allows a deduction for dividends received and redistributed within
      timelines, which mitigates but does not remove holdco dividend leakage — verify treatment under the
      Income-tax Act, 2025.
    - DIPAM's capital-restructuring guidelines for CPSEs (dividends, buybacks, bonus, splits) are public; read the
      latest version before modelling PSU payouts.

!!! warning "Common mistakes"
    - Buying a holdco because the discount is "historically wide" with no catalyst.
    - Applying private-peer multiples to a PSU without adjusting for policy risk and overhang.
    - Ignoring royalty trends at MNC subsidiaries because the franchise is strong.
    - Summing group market caps as if cross-holdings were not double-counted.
    - Treating a demerger announcement as a guaranteed value unlock (the parts must be worth more apart).

## Key terms

| Term | Meaning |
|:--|:--|
| **Holding company (holdco)** | A company whose principal assets are stakes in other companies |
| **Gross NAV** | Market/appraised value of holdings before discounts |
| **Holdco discount** | Gap between a holdco's market value and its gross NAV |
| **Conglomerate discount** | Below-SOTP valuation of a multi-business operating company |
| **Demerger / spin-off** | Separation of a business into a separately listed company |
| **PSU / CPSE** | Public-sector undertaking / central public-sector enterprise |
| **DIPAM** | Department of Investment and Public Asset Management; sets CPSE payout and disinvestment policy |
| **OFS** | Offer for sale by a promoter (often the government) through the exchange mechanism |
| **Minimum public shareholding** | SEBI requirement of ≥ 25% public float |
| **Royalty / technical fee** | Payment by a subsidiary to its parent for brands, technology or services |
| **Delisting / reverse book building** | Promoter buy-out of public shareholders; the price-discovery mechanism |
| **Cross-holding** | Group companies owning shares in each other |
| **Inter-corporate deposit (ICD)** | A loan between group companies |

## Check your understanding

1. Recompute Deccan's NAV per share and discount if company A's market value falls 30% and the stock falls to ₹700.
<details><summary>Answer</summary>A's stake = 0.35 × 12,600 = 4,410; gross = 4,410 + 1,980 + 1,200 = 7,590; NAV/share
= ₹1,518; discount = 1 − 700/1,518 = 54%. Discounts typically *widen* in drawdowns, so the holdco falls more than
its holdings.</details>

2. A PSU miner trades at 7x earnings and a 9% dividend yield at the top of a commodity cycle. Why is neither number
   a reason to buy?
<details><summary>Answer</summary>Both are on peak earnings (the P/E paradox of [07.3](03-cyclicals-and-commodities.md));
the dividend is DIPAM-driven and will fall with profit; and government pricing/OFS overhang cap the re-rating.
Value on normalised earnings and check the dividend at mid-cycle profit.</details>

3. An MNC subsidiary's royalty rises from 2.5% to 4.5% of sales over five years with no new products. What is the
   annual value transfer on ₹5,000 Cr of sales, and what governance mechanism now applies?
<details><summary>Answer</summary>2 pp × ₹5,000 Cr = ₹100 Cr a year of pre-tax profit moved to the parent
(~₹75 Cr post-tax). Since royalty payments to a related party above 5% of turnover require minority approval under
LODR Reg 23(1A), the 4.5% sits just below the threshold — itself a tell; any further increase would face a vote.</details>

4. Why might a conglomerate's demerger fail to unlock value?
<details><summary>Answer</summary>If the parts are individually sub-scale, if debt is allocated to a part that cannot
service it, if the market already valued the parts fairly (no discount to unlock), or if the promoter's control
structure and related-party arrangements survive the split. The unlock requires an actual discount and a clean
separation.</details>

5. What determines whether a holdco discount should be 30% or 60%?
<details><summary>Answer</summary>Mainly the promoter's demonstrated willingness to distribute or restructure
(control), the tax leakage on dividends and sales, and the liquidity of the holdco stock. A holdco with regular
buybacks and past mergers into the operating company deserves the low end; one that has never distributed and has no
reason to deserves the high end.</details>

## Go deeper

- IiAS, "Holding Company Discounts" reports (periodic) and broker holdco-discount trackers — base rates.
- DIPAM guidelines on capital restructuring of CPSEs and the annual disinvestment section of the Union Budget.
- SEBI consultation paper on royalty payments by listed companies to related parties (2023) and the resulting
  LODR amendments.
- Aswath Damodaran, notes on valuing holding companies and the "conglomerate discount".
- [Case I12 ITC](../13-case-studies/india/12-itc-value-trap-or-not.md) and [case I15 Tata Motors](../13-case-studies/india/15-tata-motors-jlr.md)
  — conglomerate discount and demerger in practice.

---
[← Previous: 07.4 High-growth & loss-making companies](04-high-growth-and-loss-making.md) · [Module index](index.md) · [Next: 07.6 Real estate, infra, utilities & telecom →](06-real-estate-infra-utilities-telecom.md)
