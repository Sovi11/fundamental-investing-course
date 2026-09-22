# 12.3 · Special situations

> **Why this matters:** most mispricing comes from disagreement about a company's future. Special situations
> are different: the mispricing comes from *structure* — a spin-off nobody wanted, a buyback with an acceptance
> ratio, an open offer with a floor price, an index change that forces flows. The outcomes depend less on
> forecasting and more on reading documents carefully, doing the arithmetic, and understanding who is forced to
> act. India's 2025–26 demerger wave (ITC Hotels, Tata Motors, HUL's ice-cream unit, Vedanta) makes this the
> most active corner of the market for a document-literate investor.

**Learning objectives** — after this lesson you can:

- Analyse demergers/spin-offs: why they tend to outperform, the mechanics (record dates, ratios, listing), and
  the traps.
- Do the arithmetic of tender-offer buybacks (acceptance ratios, the small-shareholder quota, tax) and open
  offers under SAST.
- Explain delisting (reverse book building, the 2024 fixed-price route), mergers and swap-ratio arbitrage,
  rights issues and renunciation, IPO analysis and grey-market caution, index inclusion/exclusion, and holdco
  discount-closure events.

**Prerequisites:** [07.5 Holdcos, conglomerates, PSUs & MNCs](../07-special-valuation/05-holdcos-conglomerates-psus-mncs.md),
[01.3 Raising and returning capital](../01-markets-101/03-raising-and-returning-capital.md)  ·  **Time:** ~80 min

---

## 1. Demergers and spin-offs

**Mechanics.** A scheme of arrangement (Companies Act ss.230–232; NCLT approval; SEBI/exchange no-objection)
transfers a business to a new company whose shares are issued to the parent's shareholders in a ratio on a
record date; the new company lists a few weeks to months later. Recent Indian examples (verify details):
ITC Hotels (effective 1-Jan-2025; 1 ITC Hotels share per 10 ITC shares; listed 29-Jan-2025; ITC retained 40%);
Tata Motors' commercial-vehicle business (effective 1-Oct-2025; record date 14-Oct-2025; 1:1; listed 12-Nov-2025);
Hindustan Unilever's ice-cream business (effective 1-Dec-2025; 1:1); Vedanta's multi-way split (2026)
([Business Standard](https://www.business-standard.com/industry/news/tata-motors-itc-raymond-aditya-birla-demergers-markey-value-india-inc-125110601408_1.html);
[BusinessToday](https://www.businesstoday.in/markets/stocks/story/vedanta-demerger-listing-timeline-cues-from-tata-motors-itc-hotels-jio-financial-526794-2026-04-22)).

**Why they tend to outperform** (the Greenblatt argument; supported by US studies and, anecdotally, Indian
experience): the spun entity is sold by index funds and by holders who bought the parent for a different
business; it has no analyst coverage and no trading history; management incentives are reset to the smaller
entity; the conglomerate discount is removed; and the parent's remaining business gets a cleaner multiple.

**Analysis**: read the scheme document (appointed date, effective date, ratio, which liabilities move, any
cash payments, the promoter's post-scheme holdings, and tax treatment — demergers under s.2(19AA) are tax-neutral
to shareholders, with cost split by a notified ratio); value both entities separately ([07.5 SOTP](../07-special-valuation/05-holdcos-conglomerates-psus-mncs.md));
identify who must sell (index rules, mandates); and decide whether to hold the spin, buy more after the forced
selling, or sell the parent.

**Arithmetic**: an ITC holder with 10 shares at ~₹480 pre-demerger (₹4,800) received 1 ITC Hotels share; if
ITC then traded at ₹450 and ITC Hotels at ₹180, the position was ₹4,500 + ₹180 = ₹4,680 — the "loss" on ITC is
the value that moved, not value destroyed (illustrative numbers; verify actual prices).

**Traps**: debt allocated to the weaker entity; a spin so small it is uninvestable; the promoter using the
scheme to raise their stake or extract a business; and the delay between record date and listing (weeks in which
you hold an unlisted, unpriced security).

## 2. Buybacks

**Tender offer** (the common Indian form): the company offers to buy a fixed number of shares at a fixed price
(usually a premium) from all shareholders in proportion to holdings, with **15% of the offer reserved for small
shareholders** (holdings ≤ ₹2 lakh at the record date). Because small shareholders as a group often tender less
than their reservation, their **acceptance ratio** can be far above the general ratio — the arbitrage.

**Arithmetic**: shares at ₹1,000; buyback of 5% of equity at ₹1,200; expected small-shareholder acceptance 30%.
Holding 100 shares (₹1 lakh, under the ₹2 lakh cap): 30 accepted at ₹1,200 = ₹6,000 gain; 70 remain and, if the
stock drifts down 2% ex-buyback, lose ₹1,400 → net ₹4,600 (4.6%) in a few weeks. The risks: the acceptance ratio
(estimated from past buybacks and the small-shareholder base), the post-buyback price, and — since October 2024 —
**tax**: buyback proceeds are taxed as **dividend income** in the shareholder's hands at slab rates, with the cost
of the tendered shares becoming a capital loss (verify the current treatment and its interaction with the ₹2
lakh threshold). At a 30% slab the arithmetic above roughly halves.

**Open-market buybacks** (via the exchange, up to a maximum price, over months) have no acceptance-ratio
arbitrage; they are a capital-allocation signal to be judged on price vs value ([05.5](../05-business-analysis/05-management-and-capital-allocation.md)).

## 3. Open offers and delisting

**Open offers (SAST)**: an acquirer crossing 25% (or acquiring control) must offer to buy at least 26% of the
public's shares at a price set by SAST's formula (the higher of negotiated price, 60-day VWAP, etc.). The offer
price is a floor for the offer period; the arbitrage is the spread between market price and offer price against
the acceptance probability and timeline. Watch: whether the acquirer intends to delist; competing offers; and the
post-offer float (a stock at 80% promoter holding must return to 75% within a year — supply).

**Delisting**: promoters holding ≥ 90% after the offer can delist; the price is set by **reverse book building**
(shareholders tender at prices; the discovered price is the one at which the 90% threshold is reached; the
promoter can accept or reject) — or, under SEBI's 2024 amendments, a **fixed-price route** at a premium to the
floor (verify the current rules). Delisting arbitrage: buy below the expected discovered price; risk that the
promoter rejects a high discovered price (many delistings fail) or that the stock falls back after a failed
attempt.

## 4. Mergers and swap-ratio arbitrage

In a share-swap merger, target shareholders receive a fixed number of acquirer shares; the target should trade at
(swap ratio × acquirer price) minus a spread for time and completion risk. The spread widens when approvals
(CCI, NCLT, SEBI, sector regulators) are uncertain or when a competing bid or shareholder opposition is
possible. Analysis: the ratio and its fairness opinions; the approval calendar; what would break the deal;
the acquirer's valuation (you are becoming its shareholder). The HDFC–HDFC Bank merger (2023 — [case I7](../13-case-studies/india/07-hdfc-bank-consistency.md))
is the reference for scale and index effects; the Zee–Sony collapse (2024) for completion risk.

## 5. Rights issues

A rights issue offers existing shareholders new shares at a discount in a ratio; the **rights entitlements
(REs)** trade separately for a period, and their price should equal (market price − issue price) less a spread.
Renouncing (selling the RE) vs subscribing is a valuation decision on the company; the mispricing comes from
holders who do nothing (the RE lapses) and from retail confusion — REs have traded far from theoretical value
in several Indian issues. Also read *why* the money is being raised (deleveraging a stressed balance sheet —
Vodafone Idea 2024 — vs funding growth).

## 6. IPOs

The base rate for buying IPOs at listing is poor — the seller chose the timing and the price, and the pop, if any,
goes to allottees. The analyst's route: read the DRHP ([03.5](../03-reading-filings/05-other-documents.md)) —
objects of the issue, OFS share, pre-IPO placement prices, KPIs, litigation, related parties; value it as any
other company; ignore the grey-market premium (unofficial, manipulable, and irrelevant to value); and consider
that the best entry point for a good IPO is often 6–18 months later, after lock-in expiries and the first
disappointing quarter. NSE's September 2026 IPO is the current test of all of this.

## 7. Index inclusion and exclusion

Inclusion in a major index (Nifty 50/Next 50, MSCI India, FTSE) forces passive buying on the effective date and
often front-running before it; exclusion forces selling. The index providers publish methodologies and
announcement calendars; the arbitrage is small, crowded and short-lived, but the *exclusion* side creates
genuine buying opportunities in good companies dropped for technical reasons (free-float, liquidity). Watch also
the SEBI/AMFI large/mid/small-cap re-categorisation (half-yearly), which forces mutual-fund rebalancing.

## 8. Holdco discount-closure events

A holdco's discount ([07.5](../07-special-valuation/05-holdcos-conglomerates-psus-mncs.md)) closes on events:
merger of the holdco into the operating company; a buyback; a sale of the stake with distribution; a promoter
reorganisation; a change in dividend taxation. The trade is event-driven: probability × discount closure vs the
carry of holding an illiquid, negatively-yielding structure. Without an identifiable event, a wide discount is a
description, not an opportunity.

## 9. A checklist for any special situation

1. Read the primary document (scheme, offer letter, DRHP, index methodology) — not the press summary.
2. Do the arithmetic: ratios, prices, acceptance, tax, timeline.
3. Identify the forced actors (index funds, mandates, lock-ins, promoters) and their dates.
4. Value the securities independently of the event.
5. Name what breaks it (regulator, court, competing bid, promoter rejection) and the loss if it does.
6. Size it as an event position with a dated exit ([11.4](../11-process/04-position-sizing-and-portfolio-construction.md)).

!!! tip "Trader's lens"
    Special situations are the closest thing in equities to your home turf: defined payoffs, dated events,
    forced flows, and arbitrage bounded by identifiable risks. Treat them as event trades — expected value from
    the arithmetic, a hard exit date, and a loss limit if the event fails — and resist turning a failed arbitrage
    into a long-term holding.

!!! info "India notes"
    - Scheme documents and NCLT orders are on the exchanges and the company's site; SEBI's SAST and delisting
      regulations (as amended) are the primary sources for offer mechanics.
    - Buyback tax: the October 2024 change (proceeds as dividend income) removed much of the retail tender
      arbitrage; recompute post-tax before every tender.
    - Demerger cost-basis splits are notified by the company (for capital-gains purposes); keep the notice.

!!! warning "Common mistakes"
    - Trading a demerger on the announcement without reading which liabilities move.
    - Ignoring tax in buyback arithmetic.
    - Assuming a delisting succeeds.
    - Buying IPOs on grey-market premia.
    - Holding a failed event trade "because the company is good" without re-underwriting it as an investment.

## Key terms

| Term | Meaning |
|:--|:--|
| **Demerger / spin-off** | Separation of a business into a new listed company via a scheme of arrangement |
| **Record date / appointed date / effective date** | Dates fixing entitlement / accounting transfer / legal effect |
| **Tender-offer buyback** | Fixed-price, proportional buyback with a 15% small-shareholder reservation |
| **Acceptance ratio** | Shares accepted ÷ shares tendered |
| **Open offer (SAST)** | Mandatory offer to public shareholders on a change of control or crossing 25% |
| **Reverse book building** | Delisting price discovery by shareholder tenders |
| **Swap ratio** | Acquirer shares received per target share in a merger |
| **Rights entitlement (RE)** | Tradable right to subscribe to a rights issue |
| **Grey-market premium** | Unofficial pre-listing IPO premium |
| **Index rebalancing** | Scheduled changes to index constituents forcing passive flows |
| **Discount-closure event** | A corporate action that narrows a holdco/conglomerate discount |

## Check your understanding

1. Recompute the buyback example at a 30% tax slab on the buyback proceeds treated as dividend income (ignore the
   capital-loss offset).
<details><summary>Answer</summary>Tax on proceeds: 30 × 1,200 × 30% = ₹10,800 — larger than the ₹6,000 pre-tax gain;
the tender is loss-making unless the capital loss (30 × 1,000 = ₹30,000, offsettable against other gains) is
valuable to you. Post-Oct-2024, tender arbitrage depends on the investor's tax position.</details>

2. A demerger allocates 80% of group debt to the spun-off manufacturing business and none to the retained
   brand business. What is the likely outcome and the trade?
<details><summary>Answer</summary>The spin is levered and will be sold hard on listing; the parent re-rates.
The trade may be long the parent into the scheme and, if the spin's business can service the debt, buy the spin
after forced selling — but only after valuing it with the debt ([04.5](../04-financial-analysis/05-leverage-solvency-liquidity.md)).</details>

3. Why do index exclusions produce better opportunities than inclusions?
<details><summary>Answer</summary>Exclusions force selling of a stock regardless of its fundamentals, often for
technical reasons, and the selling is concentrated and time-bound; inclusions attract front-running that
removes most of the premium before the effective date.</details>

4. State the six-step checklist in one line each for the NSE IPO.
<details><summary>Answer</summary>Read the RHP; compute valuation per share vs exchange peers and DCF; note
lock-in expiry dates and anchor allocations (forced/likely sellers); value NSE as an exchange
([07.2](../07-special-valuation/02-insurers-amcs-exchanges.md)); name the breakers (regulatory fee action,
volume collapse, governance legacy); size as an event if trading the listing, or as an investment only at a price
the valuation supports.</details>

## Go deeper

- Joel Greenblatt, *You Can Be a Stock Market Genius* (1997) — spin-offs, rights, restructurings; dated but
  foundational.
- SEBI (SAST) Regulations, 2011; SEBI (Delisting of Equity Shares) Regulations, 2021 as amended 2024; SEBI
  (Buy-back of Securities) Regulations, 2018 — the mechanics.
- Company scheme documents for ITC Hotels and Tata Motors CV — read one end to end.
- [Case I12 ITC](../13-case-studies/india/12-itc-value-trap-or-not.md) and [case I15 Tata Motors](../13-case-studies/india/15-tata-motors-jlr.md).

---
[← Previous: 12.2 Market cycles & sentiment](02-market-cycles-and-sentiment.md) · [Module index](index.md) · [Next: 13 Case studies →](../13-case-studies/index.md)
