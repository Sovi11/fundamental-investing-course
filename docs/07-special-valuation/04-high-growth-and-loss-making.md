# 07.4 · High-growth & loss-making companies

> **Why this matters:** since 2021 India has listed food delivery, payments, insurance marketplaces, beauty
> e-commerce, quick commerce and a string of SaaS and fintech companies — most of them loss-making at IPO, some
> now profitable, some worth a fraction of their listing price. None can be valued on P/E, and an EV/Sales multiple
> without a margin argument is a guess. The method is to value the *business the company will become*, and to be
> explicit about the path, the dilution, and the probability of getting there.

**Learning objectives** — after this lesson you can:

- Analyse a loss-making company through unit economics, contribution margins and cohorts.
- Build a path-to-profitability model with explicit fixed-cost and contribution-per-unit drivers.
- Sanity-check EV/Sales multiples against the terminal margin they imply, and use the Rule of 40.
- Account for ESOP dilution and "adjusted EBITDA" definitions.
- Set a terminal state for a company that has not reached it, and recognise the patterns in India's 2021 IPO
  cohort.

**Prerequisites:** [05.1 Business models & unit economics](../05-business-analysis/01-business-models-and-unit-economics.md),
[06.3 DCF step by step](../06-valuation/03-dcf-step-by-step.md)  ·  **Time:** ~90 min

---

## 1. Three questions

1. **Is the business losing money by choice or by nature?** A company with positive contribution per unit that
   loses money because it is spending on growth (marketing, new cities, engineering) can stop and be profitable. A
   company whose *contribution* is negative — each order loses money before overheads — has no such switch. Find the
   contribution line first.
2. **What does the profitable end-state look like, and who already looks like it?** A food-delivery platform at
   scale in a mature market; a SaaS company at 25% operating margins; a lender at 3% RoA. If nobody anywhere has
   reached the end-state you are assuming, your terminal margin is a hypothesis with no base rate.
3. **How much dilution and how many years between here and there?** Losses are funded by equity; every round and
   every ESOP grant reduces your share of the end-state.

## 2. Unit economics and contribution margin

The core disclosure is **contribution margin**: revenue per unit minus all variable costs of serving the unit
(delivery cost, payment fees, discounts, customer support, sometimes marketing), before fixed overheads. Indian
new-age companies define it differently — some include marketing, some not; some report it as % of GMV/GOV, others
as % of revenue — so **rebuild it from the P&L** before comparing:

$$\text{Contribution} = \text{Revenue} − \text{Variable costs}; \qquad
\text{Contribution per order} = \frac{\text{Contribution}}{\text{Orders}}$$

**Cohorts** turn contribution into value: for each acquisition month, plot retained customers and their spend over
time. A cohort that flattens at 40% retention with rising order frequency is a business; one that decays to 10% is
a marketing expense with a logo ([05.1 §4.3](../05-business-analysis/01-business-models-and-unit-economics.md)).
Companies that stop disclosing cohorts after the DRHP have usually seen them worsen.

## 3. A path-to-profitability model

**Dhruv Delivery** (fictional quick-commerce platform), base year: GMV ₹12,000 Cr, take rate 18% (revenue ₹2,160 Cr),
average order value ₹450 (26.7 Cr orders a year), contribution per order −₹5 (it loses money on every order before
overheads), fixed costs ₹900 Cr (technology, corporate, dark-store leases treated as fixed), EBITDA −₹1,033 Cr.

The model has three drivers: order growth (density lowers delivery cost per order), contribution per order (AOV
up, delivery cost per order down, advertising income), and fixed-cost growth (8% a year).

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|:--|--:|--:|--:|--:|--:|
| Order growth | 40% | 32% | 25% | 20% | 15% |
| Orders (Cr) | 37.3 | 49.3 | 61.6 | 73.9 | 85.0 |
| Revenue (₹ Cr) | 3,024 | 3,992 | 4,990 | 5,988 | 6,886 |
| Contribution / order (₹) | −5 | +3 | +10 | +16 | +22 |
| Contribution (₹ Cr) | (187) | 148 | 616 | 1,183 | 1,870 |
| Fixed costs (₹ Cr) | 900 | 972 | 1,050 | 1,134 | 1,224 |
| **EBITDA (₹ Cr)** | **(1,087)** | **(824)** | **(434)** | **49** | **646** |
| EBITDA margin | −35.9% | −20.6% | −8.7% | +0.8% | +9.4% |
| Cumulative EBITDA burn | (1,087) | (1,911) | (2,345) | (2,295) | (1,649) |
| Rule of 40 (growth % + margin %) | 4 | 11 | 16 | 21 | 24 |

```python
g = [0.40, 0.32, 0.25, 0.20, 0.15]; cpo = [-5, 3, 10, 16, 22]
rev, orders, fixed = 2160.0, 26.67, 900.0
for t, (gg, c) in enumerate(zip(g, cpo), 1):
    rev *= 1 + gg; orders *= 1 + gg; fixed *= 1.08 if t > 1 else 1
    ebitda = c * orders - fixed
    print(t, round(rev), round(ebitda), f"{ebitda / rev:.1%}")
```

What the table says:

- **Break-even is in Y4** and depends entirely on contribution per order rising from −₹5 to +₹16: that is the
  thesis. Every quarter, the number to check is contribution per order, not GMV growth.
- **Cumulative burn is ~₹2,350 Cr** before the turn. The company needs that much capital (net of what it has) — which
  means equity raises and dilution, or debt it cannot service. If it has ₹1,500 Cr of cash, there is a funding round
  in Y2–Y3 at whatever price the market then offers.
- **The Rule of 40** (revenue growth % + EBITDA margin % ≥ 40 for a healthy software/platform company) is failed
  throughout: growth is high but margins are deeply negative. The rule is a heuristic from US SaaS; apply it as a
  screen, not a valuation.

### 3.1 The terminal state and what EV/Sales implies

Suppose Dhruv trades at **6x revenue** (EV ₹12,960 Cr). Is that expensive? Convert it into what it assumes:
continue the model to Y8 at ~10% growth with EBITDA margin reaching a **15% steady state** (a plausible mature
quick-commerce margin — nobody has demonstrated it in India yet; verify against the latest Eternal/Blinkit and
Swiggy Instamart disclosures): Y8 revenue ≈ ₹9,165 Cr, EBITDA ≈ ₹1,375 Cr. Today's EV is 9.4x that Y8 EBITDA —
but Y8 is eight years away; discounted at 14%, the PV factor is 0.35, so the EV is **~27x the present value of
year-8 EBITDA**, before the dilution needed to get there. That is the honest translation of "6x sales": a
growth-stock multiple on profits eight years out, in a business model whose steady-state margin is unproven.

The general recipe:

$$\text{Implied terminal EV/EBITDA} = \frac{\text{EV}_{today} \times (1 + k)^{N}}{\text{Revenue}_N \times \text{margin}_N}$$

If the implied multiple is far above what mature comparables trade at, the price needs either a higher terminal
margin, faster growth, or a lower cost of capital — and you should say which you believe.

## 4. Dilution: ESOPs and rounds

Loss-making companies pay in shares. Two channels:

- **ESOPs**: Ind AS 102 expenses the grant-date fair value; Indian new-age companies have run ESOP charges of 2–10%
  of revenue and present "adjusted EBITDA excluding ESOP cost". Treat the expense as real (it *is* the cost of the
  people) and count the shares: 2% annual dilution for five years is a 9.4% haircut to your per-share value
  ($1.02^5 = 1.104$).
- **Funding rounds**: model the cumulative burn, the cash on hand, and the price at which the gap is filled. A
  ₹1,000 Cr raise at half today's price dilutes existing shareholders far more than the same raise at today's
  price — the path matters, and a bear market during the burn phase is the main way these investments fail even
  when the business succeeds.

Per-share value = (terminal equity value) ÷ (today's shares × cumulative dilution factor), discounted. Always.

## 5. Patterns from India's 2021–24 cohort

Facts to verify before citing; the *patterns* are the lesson:

| Pattern | Examples (verify specifics) | Lesson |
|:--|:--|:--|
| Contribution turned positive, then EBITDA, then the multiple re-rated | Zomato (now Eternal): food delivery reached adjusted-EBITDA break-even in FY23–24; the stock re-rated strongly, then Blinkit's quick-commerce losses reopened the burn debate | The market pays for the *turn* in contribution; it then re-prices when a new burn segment is added |
| Regulatory jump risk | Paytm: RBI's Jan-2024 restrictions on Paytm Payments Bank removed a core business overnight | Regulated platforms carry a discrete, unhedgeable risk — scenario it explicitly ([case I8](../13-case-studies/india/08-zomato-paytm-ipos-2021.md)) |
| Marketplace with take-rate pressure | Nykaa (beauty e-commerce), PB Fintech (insurance/loan marketplace) | Take rates compress as competition and regulation act; model take rate as a driver, not a constant |
| Duopoly capital war | Swiggy vs Zomato/Eternal in quick commerce (2024–26) | Both burn until one blinks; the capital cycle ([05.4](../05-business-analysis/04-capital-cycle-and-competition.md)) applies to dark stores as it does to steel mills |
| Profitable at IPO, still de-rated | Several 2024–25 listings priced for growth that slowed | Profitability is necessary, not sufficient; the growth-multiple compression of [06.5](../06-valuation/05-relative-valuation-and-multiples.md) applies |

!!! info "India notes"
    - SEBI's ICDR rules require new-age issuers to disclose **Key Performance Indicators** (GMV, contribution
      margin, cohorts, CAC) in the DRHP with auditor certification, and to explain the basis of the issue price
      against them (the 2022 "BIP" rules) — save the DRHP; later disclosures are thinner.
    - Indian new-age companies typically report **adjusted EBITDA** excluding ESOP cost and sometimes excluding
      "one-time" items every quarter; rebuild reported EBITDA and free cash flow yourself.
    - Ind AS 116 makes dark-store and warehouse leases part of D&A and interest — EBITDA flatters lease-heavy
      quick-commerce models; look at EBIT or pre-Ind AS 116 EBITDA and free cash flow after lease payments.

!!! tip "Trader's lens"
    A loss-making growth stock is a long-dated call with a *funding-dependent* path: the strike is the cumulative
    burn, the expiry is the runway, and the vol is enormous. Two things a vol trader will recognise: theta is real
    (every quarter of burn moves value to the next funding round's investors), and the position's delta is not to
    revenue but to *contribution per unit* — the variable that decides whether the option finishes in the money.
    Trade the contribution line; the GMV line is noise with a marketing budget.

!!! warning "Common mistakes"
    - Valuing on EV/Sales without translating it into an implied terminal margin and multiple.
    - Accepting management's contribution-margin definition.
    - Ignoring cumulative burn and the funding path (and the price at which it will be funded).
    - Treating ESOP cost as non-cash and therefore ignorable — then also ignoring the share count.
    - Assuming a terminal margin no company in the model has ever achieved.
    - Extrapolating GMV growth when the drivers are discounting and marketing spend.
    - Ignoring regulatory jump risk for platforms in payments, lending, insurance distribution or gaming.

## Key terms

| Term | Meaning |
|:--|:--|
| **Contribution margin** | Revenue minus variable costs of serving a unit, before fixed overheads |
| **Contribution per order / unit** | Contribution ÷ units; the variable that decides break-even |
| **GMV / GOV** | Gross merchandise / order value flowing through a platform |
| **Take rate** | Platform revenue ÷ GMV |
| **Cohort analysis** | Retention and spend of customers grouped by acquisition period |
| **CAC / LTV** | Customer acquisition cost / lifetime value |
| **Path to profitability** | A driver-based forecast of when and how contribution overtakes fixed costs |
| **Burn / runway** | Cash consumed per period / periods of cash remaining |
| **Rule of 40** | Growth % + margin % ≥ 40 as a health screen for software/platform businesses |
| **Adjusted EBITDA** | Company-defined EBITDA excluding ESOP and "one-time" costs; rebuild before use |
| **ESOP dilution** | Increase in share count from employee options; a real cost to per-share value |
| **Terminal state** | The mature economics (growth, margin, capital intensity) the valuation assumes the company reaches |
| **Implied terminal multiple** | Today's EV grown at the discount rate ÷ terminal-year EBITDA |

## Check your understanding

1. Dhruv's contribution per order stalls at +₹10 from Y3 onward. When does it break even, if ever?
<details><summary>Answer</summary>Contribution at ₹10 × orders: Y4 = 739 vs fixed 1,134; Y5 = 850 vs 1,224 — the gap
narrows only if orders keep growing faster than fixed costs (8%); at 15% order growth it is still −₹89 Cr in
Y10, with cumulative burn above ₹4,200 Cr. The investment fails on time and dilution even if "it eventually
works".</details>

2. Rebuild the implied terminal multiple if Dhruv's terminal margin is 10% instead of 15%.
<details><summary>Answer</summary>Y8 EBITDA = 9,165 × 10% = ₹917 Cr; EV 12,960 / 917 = 14.1x nominal; ÷ 0.351
PV factor = ~40x the present value of year-8 EBITDA — before dilution. A 5-pp change in an unproven terminal
margin moves the implied multiple by 50%.</details>

3. A company reports "adjusted EBITDA margin of +3%" with an ESOP charge of 6% of revenue. What is the reported
   EBITDA margin, and how should you treat the difference?
<details><summary>Answer</summary>−3%. The 6 pp is compensation paid in shares: real cost, recurring while the
company pays people that way. Use the −3% for profitability, and add the share issuance to the dilution schedule.</details>

4. Why is contribution per order a better leading indicator than GMV growth for a quick-commerce company?
<details><summary>Answer</summary>GMV can be bought with discounts and marketing (which sit in variable or fixed
costs); contribution per order captures whether each incremental order adds or destroys money after those costs.
Break-even is contribution × orders − fixed costs; only the first term's sign tells you if growth helps.</details>

5. List three ways an Indian platform's take rate could fall.
<details><summary>Answer</summary>Competition (a rival subsidises merchants/customers); regulation (caps on
commissions, e.g. proposals on food-delivery or app-store fees; RBI rules on payment charges); mix shift toward
lower-commission categories or larger merchants with negotiating power.</details>

## Go deeper

- Aswath Damodaran, *The Dark Side of Valuation* — young and growth companies; and his periodic blog valuations of
  Zomato, Paytm and Swiggy at IPO (useful models of method, whatever one thinks of the numbers).
- Bill Gurley, "All Revenue Is Not Created Equal: The Keys to the 10X Revenue Club" (2011) — what a high EV/Sales
  multiple requires.
- Any 2021–24 Indian new-age DRHP, "Key Performance Indicators" and "Basis for Offer Price" sections — SEBI-mandated
  unit-economics disclosures.
- [Case I8 Zomato & Paytm IPOs](../13-case-studies/india/08-zomato-paytm-ipos-2021.md) and [case G5 Amazon](../13-case-studies/global/05-amazon-1997-2015.md) —
  the divergent outcomes and the one that worked.

---
[← Previous: 07.3 Cyclicals & commodities](03-cyclicals-and-commodities.md) · [Module index](index.md) · [Next: 07.5 Holdcos, conglomerates, PSUs & MNC subsidiaries →](05-holdcos-conglomerates-psus-mncs.md)
