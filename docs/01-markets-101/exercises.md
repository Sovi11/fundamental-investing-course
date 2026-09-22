# Module 01 · Exercises

> **How to use this page:** give each problem 15 honest minutes before you open the
> [solutions](solutions.md). Show your arithmetic. A spreadsheet or Python is fine for anything longer than two
> steps; the point is to know *what* to compute and *why*. Every miss goes in your error log
> ([00.2 §3.2](../00-orientation/02-how-to-use-this-course.md)).

**Conventions.** Amounts are in ₹ crore (Cr) unless stated; 1 crore = 100 lakh = 10 million. FY26 = 1-Apr-2025 to
31-Mar-2026. Kaveri Pumps & Motors and Nirmal Finance numbers come from the reference pages
([Kaveri](../appendix/running-example/kaveri-pumps.md), [Nirmal](../appendix/running-example/nirmal-finance.md),
[Kaveri valuation](../appendix/running-example/kaveri-valuation.md)). Use them exactly. Kaveri's tax rate is 25.17%,
its market price is ₹390 (18-Sep-2026), it has 6.00 Cr basic and 6.07 Cr diluted shares, and the house view values
its equity at ₹1,941.3 Cr (₹319.8 per diluted share, rounded to ₹320). Every other company on this page is fictional
and fully specified in its problem. Where a problem says "hypothetical", the event did not happen in the reference data.
Regulatory rules are as stated in the lessons, as of September 2026.

**Tiers.** Warm-up (E01.01–E01.08): recall and definitions. Core (E01.09–E01.30): calculation and interpretation.
Stretch (E01.31–E01.35): multi-step and judgement. Real-world tasks (E01.36–E01.39): on a real listed Indian company,
using primary documents.

| Lesson | Problems |
|:--|:--|
| [01.1 What a company is](01-what-is-a-company.md) | E01.01, E01.02, E01.03, E01.31, E01.32 |
| [01.2 Shares, market cap & EV](02-shares-market-cap-and-enterprise-value.md) | E01.04, E01.09–E01.15, E01.33, E01.36 |
| [01.3 Raising & returning capital](03-raising-and-returning-capital.md) | E01.03, E01.05, E01.16–E01.21, E01.34, E01.38 |
| [01.4 Indian market plumbing](04-indian-market-structure.md) | E01.06, E01.07, E01.22–E01.25, E01.37 |
| [01.5 Time value & returns math](05-time-value-and-returns-math.md) | E01.08, E01.26–E01.30, E01.35, E01.39 |

---

## Warm-up

### E01.01 · True or false? *(01.1, 01.3)*

Mark each statement true or false and justify it in one line.

1. If Kaveri defaults on its ₹92.0 Cr term loans and its assets fall short, the bank can recover the shortfall from
   Kaveri's shareholders personally.
2. Owning 1% of Kaveri's shares means you own 1% of its Hosur motors plant.
3. A special resolution needs votes in favour from shareholders holding at least 75% of all issued shares.
4. If company A holds 30% of company B's voting power and has no other control rights, B is presumed to be an
   associate of A.
5. Every listed company is a public company, but not every public company is listed.
6. Other things equal, a share with a ₹10 face value is worth more than a share with a ₹1 face value.
7. In an IBC liquidation, preference shareholders are paid before trade creditors.
8. The board declares an interim dividend; shareholders declare the final dividend at the AGM and can reduce, but
   not increase, the amount the board recommended.
9. "Perpetual succession" means the company continues to exist when its shareholders die or sell their shares.
10. When a listed company seeks shareholder approval for a material related-party transaction, the promoter group
    may not vote on it.

### E01.02 · The liquidation queue *(01.1)*

(a) Put these claims in the order an Indian liquidator pays them under IBC s.53. Mark any that rank equally.

- Government dues for the last two years
- Equity shareholders
- Unsecured financial creditors (e.g., unsecured NCD holders)
- Insolvency resolution process and liquidation costs
- Workmen's dues for the 24 months before liquidation
- Preference shareholders
- Wages of employees other than workmen, for 12 months
- Trade creditors (suppliers)
- Secured creditors who relinquish their security to the liquidation estate

(b) A secured lender instead enforces its own security and recovers ₹70 Cr of a ₹100 Cr claim. Where does the ₹30 Cr
shortfall rank?

(c) In one sentence: why is the equity holder's payoff in a liquidation $\max(0, A - D)$, and what are $A$ and $D$?

### E01.03 · Face value, share capital and "dividend of 350%" *(01.1, 01.3)*

*Sindhu Textiles Ltd* (fictional) has 25.00 Cr equity shares of ₹2 face value, "other equity" of ₹4,950 Cr and a
share price of ₹1,180. Its board recommends a "final dividend of 350%".

(a) Compute equity share capital, total equity and book value per share.
(b) Compute market capitalisation and price-to-book.
(c) How much is paid per share, what is the total cash outflow, and what is the dividend yield?
(d) Sindhu issues 1.00 Cr new shares at ₹1,100 in a QIP. How is the ₹1,100 Cr split between the equity share
    capital line and other equity, and what is the name of the second component?
(e) A year later Sindhu splits each ₹2 share into two ₹1 shares and again declares a "dividend of 350%". What is paid
    per share and in total? What does this tell you about quoting dividends as a percentage of face value?

### E01.04 · Which share count? Which denominator? *(01.2)*

(a) Match each share count to the task it is right for. Each count is used at least once.

| Count | Task |
|:--|:--|
| A. Period-end basic shares | 1. Basic EPS for a year in which the company did a QIP in December |
| B. Weighted-average basic shares | 2. Today's market capitalisation (with today's count) |
| C. Diluted shares under Ind AS 33 | 3. Value per share from your DCF |
| D. Fully diluted shares (valuation) | 4. The diluted EPS printed in the annual report |
| | 5. Book value per share at 31 March |

(b) For each multiple, say whether numerator and denominator are consistent. If not, say what is wrong.

1. EV / EBITDA
2. Market cap / EBITDA
3. EV / PAT
4. Price / EPS
5. EV / Sales
6. Market cap / book equity
7. EV *excluding* lease liabilities / EBITDA *before* lease costs (i.e., as reported under Ind AS 116)
8. EV / free cash flow to equity (FCFE)
9. Market cap / FCFE
10. EV / installed capacity in tonnes

### E01.05 · Where does the money go? *(01.3)*

For each event, say (i) whether cash flows into the company, out of the company, or neither, and (ii) whether the
company's number of equity shares rises, falls or stays the same.

1. The fresh-issue part of an IPO
2. The offer-for-sale part of an IPO, sold by a private-equity fund
3. A promoter sells 2% of the company through the exchange OFS mechanism
4. A QIP
5. A rights issue in which every entitlement is taken up
6. A block deal between a mutual fund and a foreign portfolio investor
7. A tender-offer buyback
8. A 1:1 bonus issue
9. A 5-for-1 stock split
10. A promoter exercises preferential warrants by paying the remaining 75% of the price
11. A final dividend
12. A private placement of NCDs
13. Compulsorily convertible debentures, issued two years ago, convert into shares
14. Employees exercise vested ESOPs

### E01.06 · The plumbing *(01.4)*

(a) Match each institution to its main job: SEBI; NSE; NSE Clearing Ltd; CDSL/NSDL; your depository participant;
the company's RTA; AMFI; NSE Indices Ltd.

Jobs: (i) runs the order book and lists companies; (ii) becomes the counterparty to both sides of every trade and
guarantees settlement; (iii) holds shares electronically and records pledges; (iv) the regulator of the securities
market; (v) maintains the register of members and handles corporate actions for the company; (vi) your account
gateway to the depository (usually your broker or bank); (vii) the mutual-fund industry body that publishes the
large/mid/small-cap list every six months; (viii) sets the Nifty methodology and runs the index reviews.

(b) A company fixes Wednesday 5-Aug-2026 as the record date for its dividend. Under T+1 settlement, do you receive the
dividend if you buy on (i) Monday 3 Aug, (ii) Tuesday 4 Aug, (iii) Wednesday 5 Aug? On which day does the stock
trade ex-dividend? Assume no exchange holidays.

### E01.07 · Deadlines and thresholds *(01.4)*

Fill in the blanks (rules as of September 2026, from 01.4).

| # | Item | Rule | Your answer |
|--:|:--|:--|:--|
| 1 | Quarterly results for Q1–Q3 | LODR Reg 33 | within ___ days of quarter-end |
| 2 | Audited Q4 and full-year results | LODR Reg 33 | within ___ days of year-end |
| 3 | Shareholding pattern | LODR Reg 31 | within ___ days of quarter-end |
| 4 | Outcome of a board meeting | LODR Reg 30 | within ___ of the meeting closing |
| 5 | Material event originating inside the company (not a board decision) | LODR Reg 30 | within ___ hours |
| 6 | Material event originating outside the company | LODR Reg 30 | within ___ hours |
| 7 | Earnings-call transcript | LODR Reg 46 | within ___ working days |
| 8 | First disclosure of a holding | SAST Reg 29(1) | on reaching ___% (with persons acting in concert) |
| 9 | Subsequent disclosures | SAST Reg 29(2) | on each change of ___% or more, within ___ working days |
| 10 | Mandatory open offer | SAST Reg 3(1) | on acquiring ___% or more of voting rights |
| 11 | Creeping acquisition without an open offer | SAST Reg 3(2) | up to ___% per financial year (for holders between 25% and 75%) |
| 12 | Creation or invocation of a pledge by a promoter | SAST Reg 31 | within ___ working days |
| 13 | Insider's continual disclosure | PIT Reg 7(2) | once trades in a calendar quarter exceed ₹___ |
| 14 | Bulk deal | exchange rules | one client's trades in a day above ___% of listed shares |
| 15 | Block deal | SEBI, from 7-Dec-2025 | minimum order ₹___ Cr, within ±___% of the reference price |

### E01.08 · Quick-fire time value *(01.5)*

Aim for under a minute each, then check with a calculator.

(a) Using the Rule of 72, how long does money take to double at 9% and at 18% a year? Give the exact answers too.
(b) How many compounding periods are there in a "FY19–FY26 CAGR"?
(c) A stock falls 60%. What gain does it need to get back to its starting price?
(d) A nominal return of 10% with 4% inflation: approximate and exact real returns?
(e) Value today of ₹100 a year forever, first payment in one year, at 8%? And if the payments grow at 3% a year?
(f) Log returns of +100% and of −50%?
(g) Effective annual rate of 12% a year compounded monthly?

---

## Core

### E01.09 · Kaveri's valuation snapshot at 31-Mar-2024 *(01.2)*

Use Kaveri's FY24 figures and its 31-Mar-2024 share price of ₹610.

(a) Market capitalisation.
(b) Basic EPS, book value per share, P/E, P/B and earnings yield.
(c) Net debt (course definition: all borrowings − cash − current investments) and EV including lease liabilities.
(d) EV/EBITDA, EV/EBIT and EV/Sales.
(e) Check your P/E, P/B and EV/EBITDA against the FY24 column of Kaveri's ratio table (§6 of the reference page).
(f) In two sentences: compare the FY24 EV/EBITDA with 13.7x at ₹390 in September 2026. What changed, the business or
    the price the market pays for it?

### E01.10 · Kaveri's EV at ₹390, with judgement *(01.2)*

(a) Compute Kaveri's EV at ₹390 on 6.00 Cr basic shares and its EV/EBITDA (FY26 EBITDA ₹181.9 Cr).
(b) Redo (a) using the 6.07 Cr diluted shares.
(c) Starting from (b), make three analyst adjustments. Ignore any tax effects.
    - The ₹38.0 Cr GST demand under appeal: you judge a 50% chance Kaveri pays it.
    - The ₹11.0 Cr of income-tax disputes: you judge a 30% chance.
    - Minimum operating cash of 2% of FY26 revenue is needed to run the business, so it is not surplus.

    Compute the adjusted EV, EV/EBITDA and EV/EBIT (FY26 EBIT ₹134.1 Cr).
(d) Should the ₹96.0 Cr of bank guarantees be added to EV? Why or why not?
(e) Recompute the adjusted EV/EBITDA from (c) with leases treated as operating costs: take lease liabilities out of
    EV and deduct FY26 ROU amortisation (₹4.7 Cr) and lease interest (₹1.4 Cr) from EBITDA.

### E01.11 · Nirmal Finance at ₹402 *(01.2)*

Nirmal has 11.0 Cr shares and trades at ₹402 (18-Sep-2026). Use FY26 PAT and net worth.

(a) Market capitalisation.
(b) FY26 EPS and BVPS (on 11.0 Cr shares), P/E, P/B and earnings yield.
(c) Show numerically that P/B = P/E × RoE when RoE is measured on closing equity.
(d) A colleague computes Nirmal's "EV" as market cap + borrowings − cash & liquid investments, and then
    "EV/PPOP". Compute both numbers, then explain in three sentences why EV is the wrong frame for a lender, and which
    multiples you would use instead.

### E01.12 · Weighted-average shares: Nirmal's FY24 QIP *(01.2)*

The reference ratio table computes Nirmal's FY24 EPS on year-end shares: ₹169.0 Cr ÷ 11.0 Cr = ₹15.36. Assume
(hypothetically) that the 1.0 Cr QIP shares were allotted on **15-Dec-2023** and rank for the rest of the year from
that day.

(a) How many days are there in FY24? (Careful.) For how many days were the QIP shares outstanding, counting the
    allotment day?
(b) Compute the weighted-average share count and basic EPS under Ind AS 33.
(c) By what percentage does the year-end-share EPS understate it?
(d) FY23 EPS was ₹12.68 (10.0 Cr shares all year). Compute FY24 EPS growth on each basis.
(e) FY25 EPS is ₹208.4 Cr ÷ 11.0 Cr = ₹18.95. Compute FY25 EPS growth on each FY24 basis. Which basis flatters FY25?
(f) Suppose Nirmal had also made a 1:1 bonus issue in FY25. Restate FY24 (weighted, from (b)) and FY25 EPS as Ind AS
    33 requires.

### E01.13 · Options and warrants: the treasury-stock method *(01.2)*

*Vaigai Software Ltd* (fictional) has 20.0 Cr basic shares trading at ₹350 and FY26 PAT of ₹400 Cr. Outstanding
potential shares (each converts one-for-one on payment of the exercise price):

| Tranche | Instruments (Cr) | Exercise price (₹) |
|:--|--:|--:|
| ESOP A | 0.50 | 120 |
| ESOP B | 0.80 | 260 |
| ESOP C | 0.30 | 400 |
| Promoter warrants W | 0.40 | 300 |

(a) Use the treasury-stock method at the market price of ₹350 to compute the net new shares from each tranche and
    the total diluted share count.
(b) What is the total intrinsic value the TSM charges existing shareholders?
(c) Your DCF values Vaigai's equity at ₹8,000 Cr (before any exercise proceeds). Compute value per share (i) on basic
    shares, (ii) on the TSM count from (a), and (iii) self-consistently: holders exercise only if the exercise price is
    below the resulting value per share, and exercise cash is added to equity value. Which tranches are in the money
    at your value?
(d) The average share price during FY26 was ₹280. Compute the Ind AS 33 diluted share count (ignore vesting
    conditions) and diluted EPS. Which tranches are excluded, and why?
(e) Why does the TSM understate the economic cost of tranche C, even though it counts it as zero?

### E01.14 · A convertible: anti-dilution vs economic dilution *(01.2)*

*Sabari Chemicals Ltd* (fictional) has 12.0 Cr shares and PAT of ₹96 Cr (EPS ₹8.00). It has ₹240 Cr of
optionally convertible debentures, convertible at ₹200 a share; the tax rate is 25.17%.

(a) How many new shares would conversion create?
(b) If the coupon is 4%, compute if-converted EPS. Is the instrument dilutive for reported diluted EPS?
(c) Repeat for a coupon of 7%.
(d) At what coupon does the instrument switch from dilutive to anti-dilutive?
(e) Sabari's EV is ₹3,600 Cr and its other net debt is ₹300 Cr. Value the equity per share treating the debentures
    (i) as equity (they convert) and (ii) as debt (they are repaid at ₹240 Cr). Which treatment is self-consistent?
    Repeat for an EV of ₹2,600 Cr.
(f) At what EV are holders exactly indifferent between converting and being repaid?

### E01.15 · Same business, three capital structures *(01.2)*

Three companies run identical businesses: EBITDA ₹200 Cr, D&A ₹40 Cr, tax rate 25%. Each is worth 10x EBITDA, so EV =
₹2,000 Cr.

- *X* has net cash of ₹300 Cr earning 7% pre-tax.
- *Y* has no debt and no cash.
- *Z* has ₹800 Cr of debt at 9.5% and no cash.

(a) For each, compute equity value, PAT, P/E and EV/EBITDA.
(b) EBITDA falls 25% and the market still pays 10x. Compute each company's new equity value and its percentage change.
    Relate the change to EV/equity.
(c) An analyst screens on "market cap / EBITDA". Compute it for each. Which company looks cheapest, and why is the
    screen wrong?
(d) Which company looks cheapest on P/E? Why is that comparison also misleading?

### E01.16 · An IPO: fresh issue plus OFS *(01.3)*

*Periyar Retail Ltd* (fictional) has 40.0 Cr shares before its IPO: promoter 30.0 Cr, a PE fund 8.0 Cr, employees
2.0 Cr. The price band is ₹180–₹216 and the issue is priced at the top of the band. The IPO has a fresh issue of ₹540 Cr
and an OFS of 5.0 Cr shares by the PE fund and 1.0 Cr shares by the promoter. FY26 PAT is ₹300 Cr. The issuer
qualifies under ICDR Regulation 6(1); there is no employee reservation.

(a) Is the price band compliant with the 120% rule?
(b) Compute new shares, post-issue shares, total issue size, and how much cash Periyar itself receives (before fees).
(c) Compute the post-issue market capitalisation at the issue price. Which minimum-public-offer tier of the SCRR
    (as amended in March 2026) applies, what does it require, and does the issue comply? By when must public
    shareholding reach 25%?
(d) Compute the post-issue shareholding of the promoter, the PE fund, employees and IPO investors.
(e) Split the issue into QIB, non-institutional and retail portions at the ICDR limits. What is the maximum anchor
    allocation, and how much of it is reserved for domestic mutual funds, life insurers and pension funds?
(f) Compute EPS and P/E at ₹216 before and after the issue.
(g) How much of the ₹1,836 Cr is growth capital and how much is an exit? Why does it matter?

### E01.17 · Nirmal's QIP: who gained? *(01.3)*

Nirmal issued 1.0 Cr shares at ₹300 in FY24. Before the issue it had 10.0 Cr shares and net worth of ₹853.4 Cr.
Ignore fees.

(a) Compute BVPS before and immediately after the QIP, and the percentage accretion.
(b) Suppose Nirmal's intrinsic equity value before the QIP was ₹3,500 Cr. Compute value per share before and after,
    and the rupee transfer between old and new shareholders (say which direction).
(c) Repeat (b) for an intrinsic value of ₹2,500 Cr.
(d) BVPS rose by the same percentage in (b) and (c). Why is BVPS accretion no guide to whether the QIP helped
    existing holders?
(e) The QIP floor price under ICDR Reg 176 (as described in 01.3) was, say, ₹310, and the company may offer a discount
    of up to 5% to the floor. What is the lowest price it could have issued at? Was ₹300 permitted?

### E01.18 · A Kaveri rights issue (hypothetical) *(01.3)*

Kaveri (₹390, 6.00 Cr shares) announces a **1-for-6** rights issue at **₹240**.

(a) Compute the number of new shares, the amount raised, the TERP and the value of one rights entitlement (RE).
(b) An investor holds 1,200 shares. Compute her wealth before the issue and after each of three choices: subscribe,
    sell the REs at their theoretical value, or ignore them.
(c) Suppose only the promoter group (58.4%) subscribes, taking up exactly its entitlement, and all other REs lapse
    (no renunciation, no underwriting). How much is raised and what is the promoter's new stake?
(d) Kaveri could instead raise the same amount with a **1-for-3** issue at **₹120**. Compute the TERP, the RE value,
    and the loss (₹ and %) for the 1,200-share investor if she ignores it.
(e) Given Kaveri's 6% promoter pledge (created to fund a promoter-group real-estate venture), what might the market
    read into the promoter's behaviour in the rights issue? Two or three sentences.

### E01.19 · Kaveri's dividend: payout, dates, tax *(01.3, 01.4)*

(a) In FY25 Kaveri paid ₹3.5 a share (₹21.0 Cr), and FY25 PAT of ₹97.4 Cr included a ₹14.0 Cr pre-tax exceptional gain
    on land. Compute the payout ratio on reported PAT and on PAT excluding the gain (post-tax), the dividend as a
    "percentage of face value", and the yield on the 31-Mar-2025 price of ₹780.
(b) Suppose (hypothetically) the board recommends a final dividend of ₹3.75 for FY26. Compute the payout ratio on FY26
    PAT, the "%" Kaveri would announce, the yield at ₹390, the theoretical ex-dividend price, and the post-tax
    dividend for an individual taxed at 31.2% (30% slab + 4% cess, no surcharge).
(c) The record date is Thursday 23-Jul-2026. What is the last day to buy and receive the dividend, and what is the
    ex-date? Assume no exchange holidays.
(d) Resident individual shareholders holding (i) 2,666, (ii) 2,667 and (iii) 3,000 shares receive the ₹3.75 dividend
    and no other Kaveri dividend that year. How much TDS does Kaveri deduct from each (rules as of Sep-2026: 10% if
    dividends from the company exceed ₹10,000 in the year; assume a valid PAN)?
(e) Why do the dividends *paid* in a financial year usually relate to the *previous* year's profits in India?

### E01.20 · A Kaveri buyback (hypothetical) *(01.3)*

Kaveri announces a **tender-offer buyback of ₹120 Cr at ₹450** a share (≈15% premium to ₹390), funded entirely with new
borrowing at 8.9% pre-tax. Assume all of "other equity" (₹676.1 Cr) is free reserves.

(a) How many shares are bought, and what percentage of the 6.00 Cr shares is that?
(b) Check the Companies Act s.68 limits from 01.3: the 25% cap, whether a board resolution suffices, and the
    post-buyback debt test.
(c) Using the house equity value (₹1,941.3 Cr on 6.07 Cr diluted shares), compute value per remaining share after the
    buyback. At what price would the buyback be value-neutral?
(d) Compute pro-forma FY26 basic EPS after the buyback (extra interest is post-tax). At what buyback price would EPS be
    unchanged? Is "EPS-accretive" the same test as "value-accretive"?
(e) 15% of the buyback is reserved for small shareholders (holdings worth up to ₹2 lakh on the record date). Suppose
    the record-date price is ₹390, small shareholders own 9% of the shares, everyone else 91%, and every eligible
    holder tenders everything. Compute the maximum holding that counts as "small", and the acceptance ratio for each
    category. How many shares of a 500-share small holder are accepted?
(f) A minority shareholder bought at ₹210 on 31-Mar-2021 and tenders in 2026. Compute tax per accepted share under the
    capital-gains regime in force from 1-Apr-2026 (long-term, 12.5% + 4% cess, ignore the annual exemption and
    surcharge). Compare with the deemed-dividend regime of 1-Oct-2024 to 31-Mar-2026 at a 31.2% slab rate.
(g) Event trade: a small holder buys 500 shares at ₹390 to tender. Unaccepted shares are expected to trade at ₹380
    after the buyback. Compute the expected gain per share bought at the acceptance ratio from (e), and the
    break-even acceptance ratio.

### E01.21 · Adjusting history for a bonus (hypothetical) *(01.3)*

Kaveri makes a **1:1 bonus** issue in FY27.

(a) Restate Kaveri's FY21–FY26 basic EPS, BVPS, 31-March share price and DPS on a bonus-adjusted basis.
(b) Show that the FY21–FY26 EPS CAGR and every year's P/E are unchanged.
(c) A data vendor adjusts EPS for the bonus but forgets to adjust historical prices. What FY26 P/E would it show? And
    if it adjusted prices but not EPS?
(d) When the bonus shares are allotted, what happens to equity share capital, other equity and total equity? Use
    the 31-Mar-2026 balances; face value stays ₹5. Is the FY26 balance sheet itself restated?
(e) An investor bought 100 shares at ₹390 before the bonus. What is her cost per share after it, for the original and
    the bonus shares? (01.3 gives the tax rule.) How would a 5-for-1 split differ?
(f) The fictional ESOP grant in 01.2 (10 lakh options at ₹200) is adjusted in the usual way. What are the new terms?

### E01.22 · Kaveri's shareholding pattern and free float *(01.4)*

Use Kaveri's March-2026 shareholding (promoters 58.4%, mutual funds 14.2%, insurance 2.1%, FPIs 7.9%, retail & others
17.4%) and ₹390.

(a) Compute shares (lakh) and value (₹ Cr) for each category.
(b) Give the maximum possible IWF and the corresponding free-float market cap. Why could the actual IWF be lower?
(c) A small-cap fund with ₹12,000 Cr of AUM wants a 1.5% position. What percentage of Kaveri's equity and of its free
    float is that? If the fund trades at most 20% of an assumed ₹6 Cr of average daily volume (the fictional figure
    from 01.4), how many trading days does it take to build?
(d) At what shareholding must the fund make its first SAST disclosure, how many shares and rupees is that at ₹390, and
    within how long?
(e) If the fund succeeds, what would total mutual-fund ownership become (assume the shares come from retail)? Give one
    risk this creates for all holders.

### E01.23 · When does the pledge bite? *(01.4)*

The reference data say 6% of Kaveri's promoter shares are pledged. The loan terms are not disclosed. Assume
(fictional) a loan of **₹35 Cr**, a top-up trigger at **1.75×** cover and invocation at **1.25×** cover.

(a) How many shares are pledged (lakh), and what percentage of Kaveri's equity is that?
(b) What is the cover ratio at ₹520 (31-Mar-2026) and at ₹390?
(c) Compute the top-up and invocation prices, and how far each is below ₹390.
(d) The price falls to ₹260. How many shares must the promoter pledge in total to restore 1.75× cover, how many
    additional shares is that, and what percentage of the promoter holding would then be pledged?
(e) Does the pledge (before or after (d)) trigger SAST's "detailed reasons" requirement?
(f) If the lender invokes at ₹208 and sells all the pledged shares at no more than 20% of daily volume, with daily
    turnover of ₹6 Cr, how many trading days does the selling take?

### E01.24 · Kaveri's disclosure calendar and the materiality test *(01.4)*

(a) Give the latest filing dates for Kaveri's Q2 FY27 results and shareholding pattern, Q3 FY27 results and FY27
    audited results. Note any deadline that falls on a weekend.
(b) Compute the three quantitative materiality thresholds of LODR Reg 30 from Kaveri's FY26 turnover, FY26 net worth
    and FY24–FY26 PAT. Which one binds?
(c) For each event, say whether it is material under the quantitative test (or deemed material), and give the
    disclosure deadline:
    1. The GST department serves a ₹3.9 Cr show-cause notice.
    2. The board approves ₹60 Cr of automation capex and a plan to raise funds.
    3. Management, without a board meeting, signs a ₹6 Cr settlement with a supplier.
    4. The rating agency downgrades Kaveri's bank facilities from "A / Stable" to "A– / Negative".
(d) Kaveri announced Q1 FY27 results on 8-Aug-2026. How many days after quarter-end was that? When did the trading
    window reopen for designated persons?

### E01.25 · Circuits, bans and index flows *(01.4)*

(a) Kaveri is in a 5% price band. Starting from ₹390, how many consecutive lower-circuit days take it below the ₹291.33
    top-up trigger from E01.23? Ignore tick-size rounding. Why does this matter for the promoter's lender?
(b) The Nifty 50 closed at 23,346.40 on 18-Sep-2026. Compute the index levels that would trigger the 10%, 15% and 20%
    market-wide circuit breakers the next day, in both directions.
(c) *Chambal Chemicals* (fictional, in F&O) has 60 Cr free-float shares and a three-month average daily delivery volume
    (ADDV) of 12 lakh shares. Compute its MWPL and the FutEq OI levels for entering and leaving the ban. Repeat with
    ADDV of 8 lakh shares.
(d) How much does an option position on 1.5 Cr shares with delta 0.40 count towards FutEq OI?
(e) *Pennar Logistics* (fictional) has a full market cap of ₹36,000 Cr, an IWF of 0.45 and average daily traded value
    of ₹90 Cr. It is added to an index whose total free-float market cap is ₹30,00,000 Cr, tracked by ₹45,000 Cr of
    passive funds (fictional). Compute its index weight, the forced passive buying and the number of days of volume.
    What price pattern would you expect around the effective date?

### E01.26 · Where Kaveri's growth came from *(01.5)*

Use Kaveri's segment revenue (§5 of the reference page).

(a) Compute the FY21→FY26 CAGR of each segment (agri & domestic, industrial & motors, solar) and of total revenue.
(b) For solar, compare the CAGR with the arithmetic average of its five annual growth rates. Why is the gap so much
    larger than for total revenue?
(c) What share of FY26 revenue is solar, and what share of the FY21→FY26 increase in revenue did solar provide? What is
    the CAGR of revenue excluding solar?
(d) Compute the FY23→FY26 revenue CAGR and compare it with the historical figure quoted in the reference valuation.
(e) Apply the Rule of 72 to solar's CAGR and compare with the exact doubling time. What does this tell you about the
    rule?

### E01.27 · Discounting and the Gordon model on Kaveri *(01.5)*

Use Kaveri's unrounded WACC of 12.186% and cost of equity of 12.8%.

(a) Compute the mid-year discount factor for FY29 (the third year) and check it against the reference table.
(b) What is ₹100 Cr received exactly five years from now worth today at WACC?
(c) A dividend discount model: next year's dividend ₹4.20, growth 7% forever, cost of equity 12.8%. Value per share?
(d) What perpetual dividend growth rate does ₹390 imply, if the current dividend is ₹4.00 (so $D_1 = 4.00(1+g)$)?
(e) Compare (d) with Kaveri's sustainable growth rate, ROE × (1 − payout), using FY26 ROE of 13.5% and the FY26 payout
    of ₹24.0 Cr ÷ ₹90.5 Cr. Why is a single-stage DDM a poor tool for Kaveri?

### E01.28 · A Nirmal tractor loan and the flat-rate trap *(01.5)*

(a) Nirmal lends ₹8,00,000 for 48 months at 16.9% a year on a reducing balance. Compute the EMI, total interest,
    month-1 interest and principal, and the balance outstanding after 12 EMIs.
(b) What "flat rate" would produce the same EMI?
(c) A rival lender advertises "10% flat" for 48 months on the same ₹8,00,000. Compute its EMI and the equivalent
    reducing-balance rate (nominal annual and effective annual). Which loan is cheaper?

### E01.29 · IRR, XIRR and the investor who kept adding *(01.5)*

Use Kaveri's 31-March prices (FY21 ₹210 … FY25 ₹780) and dividends per share paid in each year. Assume the dividend
paid in FY22 (₹1.5) arrived on 16-Aug-2021, FY23's (₹2.0) on 16-Aug-2022, FY24's (₹2.5) on 16-Aug-2023, FY25's (₹3.5)
on 16-Aug-2024 and FY26's (₹4.0) on 14-Aug-2025. Value every holding at ₹390 on 18-Sep-2026.

(a) Investor A bought one share at ₹780 on 31-Mar-2025. Compute the absolute return and the XIRR.
(b) Investor B bought one share at ₹210 on 31-Mar-2021 and held. Compute the XIRR and the MOIC.
(c) Investor C bought **100 shares on 31 March every year from 2021 to 2025** (500 shares in all) and received the
    dividends on the shares held. Compute the total invested, total received (including the ₹390 valuation), MOIC,
    average cost and XIRR.
(d) B and C held the same stock over overlapping periods. Explain the gap between their returns in two sentences,
    using the terms time-weighted and money-weighted.

### E01.30 · Nirmal's TSR, decomposed *(01.5)*

Use Nirmal's PAT, shares, 31-March share prices and dividends paid (₹ Cr) for FY21–FY26. Define EPS = PAT ÷ year-end
shares and DPS = dividends paid ÷ year-end shares.

(a) Compute EPS, P/E and DPS for each year.
(b) Compute the FY21→FY26 CAGRs of PAT, EPS, P/E and price. Verify that (1 + EPS CAGR)(1 + P/E CAGR) − 1 equals the
    price CAGR, and show the same decomposition in logs.
(c) Compute the TSR as an IRR (buy at FY21's price, receive DPS at each year-end, sell at FY26's price). How far off is
    the additive approximation EPS CAGR + P/E CAGR + average dividend yield, and why?
(d) The P/E fell by more than half, yet the P/B rose from 2.1x to 2.5x. Reconcile the two. (Hint: look at FY21 RoE.)
(e) For the five annual price returns, compute the arithmetic mean, the population standard deviation and
    $A - \sigma^2/2$, and compare with the CAGR. What is the real price CAGR at 4% inflation?

---

## Stretch

### E01.31 · Equity as a call: Tapti Textiles as a going concern *(01.1)*

Revisit *Tapti Textiles* from 01.1 (worked example 1). Treat all ₹311 Cr of claims ranking ahead of equity as a single
zero-coupon claim due in 2 years. Today the firm's assets are worth ₹340 Cr, with asset volatility of 25%. The
continuously compounded risk-free rate is 6.5%.

(a) Using Merton's model (Black–Scholes on the assets), value the equity and the senior claims. Compare the equity
    value with what equity would get in an immediate liquidation at ₹340 Cr.
(b) Compute the implied yield and credit spread on the senior claims, and the value of the put the creditors have
    written. What is the risk-neutral probability that equity finishes worthless?
(c) Management can take on a project that *lowers* asset value to ₹330 Cr but raises asset volatility to 45%. Value
    equity and debt afterwards. Who gains, who loses, and by how much? Which agency problem is this?
(d) Give two covenants creditors would write to prevent (c).

### E01.32 · Pyramid, tunnelling and votes *(01.1)*

The Krishna family (fictional) owns 45% of *Krishna Holdings Ltd* (listed). Holdings owns 55% of *Krishna Steel Ltd*
(listed; turnover ₹4,000 Cr). The family also owns 100% of *Krishna Logistics Pvt Ltd*, which sells Steel ₹600 Cr a
year of freight services at prices 4% above arm's length. Both companies pay tax at 25.17%.

(a) Compute the annual overcharge, the post-tax transfer, and the family's look-through economic interest in Steel.
(b) Compute the family's net annual gain and the losses of Steel's outside shareholders and Holdings' outside
    shareholders. Check that gains and losses sum to zero.
(c) Per ₹1 of post-tax overcharge, how much does the family keep? Why does the pyramid make tunnelling *more*
    attractive than a direct 55% stake would?
(d) Capitalised at 15x earnings, what is the transfer worth to Steel's shareholders?
(e) Assume, as in 01.1, that a related-party transaction is material above 10% of annual consolidated turnover (verify
    the current Reg 23 text before relying on it). Is the logistics contract material? Who votes on it?
(f) For an unrelated special resolution at Steel, what share of *total* shares voting against defeats it if Holdings
    votes its 55% in favour? What share of the public's shares is that?

### E01.33 · A full equity bridge, per share *(01.2)*

Your DCF values *Mahanadi Consumer Ltd* (fictional) at an EV of ₹12,000 Cr. The FCFF excludes the associate's income.
Balance-sheet and other data (₹ Cr):

| Item | Amount |
|:--|--:|
| Borrowings (excluding the CCDs below) | 1,500 |
| Lease liabilities | 400 |
| Redeemable preference shares held by an outside investor | 250 |
| Cash and bank balances | 900 |
| &nbsp;&nbsp;of which minimum operating cash | 150 |
| &nbsp;&nbsp;of which held in an overseas subsidiary (25% haircut to repatriate) | 200 |
| Liquid mutual funds | 300 |
| Book NCI (outsiders own 26% of a subsidiary earning PAT of ₹60 Cr; peers trade at 20x earnings) | 350 |
| 30% stake in a listed associate, market value (apply a 20% holding/tax discount) | 800 |
| Tax demand under appeal (40% probability of paying; not tax-deductible) | 180 |
| Unfunded gratuity obligation (pre-tax; tax rate 25.17%) | 50 |
| Compulsorily convertible debentures (CCDs), converting at ₹250 a share | 200 |

Mahanadi has 40.0 Cr basic shares and two ESOP tranches: 1.2 Cr options at ₹150 and 0.8 Cr at ₹320.

(a) Build the bridge from EV to equity value, justifying each line. Value NCI at market.
(b) Compute value per share self-consistently, including the CCD shares and only the options in the money at your
    value per share.
(c) Compare with a naive "EV − debt + cash + liquid funds, divided by basic shares". Which items explain most of the
    gap?

### E01.34 · Kaveri needs ₹150 Cr: equity or debt? *(01.3, 01.2)*

Kaveri's receivables keep rising, and the board wants ₹150 Cr of new funding for working capital. Three options:

1. **QIP** at ₹370 (≈5% below ₹390).
2. **Rights issue**, 1-for-10 at ₹250, fully subscribed.
3. **Working-capital borrowing** at 9.5% pre-tax.

Use the house equity value (₹1,941.3 Cr, 6.07 Cr diluted shares) and treat new cash as worth its face value (net debt
falls by the amount raised). Rights are offered on the 6.00 Cr basic shares.

(a) For each option compute value per share after the transaction, pro-forma FY26 basic EPS, net debt/EBITDA and
    EBIT/finance costs (FY26 finance costs ₹17.0 Cr), and the promoter's stake (assume the promoter subscribes in full
    to the rights).
(b) For the rights issue, show that a shareholder who subscribes ends up with the same wealth per original share,
    and explain the ₹0.07 difference you find.
(c) How much cash does the promoter need to take up its rights? Why is that awkward given the pledge?
(d) Write a 150-word recommendation to Kaveri's board. You are graded on reasoning, not on which option you pick.

### E01.35 · What does ₹390 need? *(01.5, 01.4)*

(a) An investor buying Kaveri at ₹390 on 18-Sep-2026 wants a 12.8% annual TSR (the house cost of equity) over five
    years. Assume dividends contribute about 1% a year, so the price must compound at about 11.8%. What price is needed
    in September 2031? What FY31 EPS does that require at exit P/Es of 20x, 25.9x and 30x, and what EPS CAGR from FY26's
    ₹15.08?
(b) Kaveri's market cap is ₹2,340 Cr. The AMFI mid-cap cutoff was about ₹33,500 Cr in July 2026, and the 500th company
    was about ₹12,093 Cr in the Dec-2025 ranking. If the cutoffs grow at 10% a year, how many years would Kaveri take to
    reach each if its market cap compounded at 25% a year? At 11.8%?
(c) Suppose Kaveri's annual log returns are normal with 40% volatility and an arithmetic mean simple return of 14%.
    Compute the median five-year wealth multiple, the mean multiple and the probability of a loss over five years.
    What does this say about "expected return"?

---

## Real-world tasks

!!! warning "Method, not recommendations"
    These tasks use real, listed companies to practise reading primary documents. Nothing you conclude is, or should
    be treated as, a recommendation to buy or sell a security. Record the date and source of every number you use.

### E01.36 · Build a real company's EV from its annual report *(01.2)*

Pick any **non-financial Nifty 500 company with an identifiable promoter** (a manufacturer is ideal).

1. **Share count.** Open the latest quarterly shareholding pattern: nseindia.com → search the company → *Corporate
   Filings* / *Shareholding Pattern* (or bseindia.com → company page → *Corporate Filings → Shareholding Pattern*).
   Record total shares, promoter %, pledged/encumbered promoter shares and the date.
2. **Price.** Take the NSE closing price on a date you state.
3. **Balance sheet.** From the latest **consolidated** balance sheet in the annual report (company IR site, or the
   exchange's *Annual Reports* section), record: non-current and current borrowings (current borrowings include
   current maturities of long-term debt), lease liabilities (both), non-controlling interests (inside total equity),
   preference capital if any, cash and cash equivalents, other bank balances (read the note: fixed deposits under lien
   or margin money are not free cash), current investments, and investments accounted for using the equity method.
4. **Operating profit.** From the P&L compute EBITDA as the course does: PBT + finance costs + depreciation &
   amortisation − other income, adding back exceptional losses or deducting exceptional gains. Note whether the company
   reports any "EBITDA" of its own and how it differs.
5. **Build EV** line by line, compute EV/EBITDA, P/E and P/B, and write one line per judgement call (other bank
   balances, associates, leases, contingent liabilities in the notes).
6. **Cross-check** against Screener.in's market cap and EV, and against Yahoo's figures with the course tools. Run from
   the repository root with your VPN off:

```python
# needs network
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")   # lets Windows print ₹
sys.path.insert(0, "tools")                                           # run from the repo root

from fi.data import fetch_price_info, fetch_statements

TICKER = "ASIANPAINT.NS"                     # <- your company: NSE symbol + ".NS"
info = fetch_price_info(TICKER)
st = fetch_statements(TICKER, period="annual", in_crore=True)
bs, inc = st["balance"], st["income"]
last = bs.columns[-1]                        # latest fiscal year-end (columns run oldest -> newest)
get = lambda df, r: float(df.at[r, last]) if r in df.index else 0.0

mcap = info["market_cap"] / 1e7              # Yahoo reports rupees; 1 crore = 1e7
debt = get(bs, "total_debt")                 # Yahoo's total debt usually includes lease liabilities
cash = get(bs, "cash_cash_equivalents_and_short_term_investments")
nci  = get(bs, "minority_interest")
ev   = mcap + debt + nci - cash
print(f"{info['name']} | balance sheet {last} | source: {bs.attrs.get('source')}")
print(f"mcap ₹{mcap:,.0f} Cr + debt ₹{debt:,.0f} + NCI ₹{nci:,.0f} - cash ₹{cash:,.0f} = EV ₹{ev:,.0f} Cr")
print(f"Yahoo's own EV: ₹{info['enterprise_value']/1e7:,.0f} Cr | EV/EBITDA {ev/get(inc, 'ebitda'):.1f}x")
```

**Deliverable:** a one-page table (your EV, Screener's, Yahoo's) and a reconciliation of the differences, each
attributed to a specific line (definition of debt, treatment of leases or other bank balances, stale share count,
standalone vs consolidated, price date).

### E01.37 · Ownership and disclosure audit *(01.4)*

For the same company (or another Nifty 500 name):

1. **Eight quarters of shareholding patterns.** From NSE/BSE, tabulate promoter %, promoter shares pledged or
   encumbered (% of promoter holding and % of equity), MFs, insurers, FPIs, and resident individuals. Flag any
   "bodies corporate" holder above 1% in the public category.
2. **Pledges and insider trades.** On NSE, find the SAST (Reg 29 and Reg 31) and insider-trading (PIT) disclosures for
   the last 12 months. (The NSE site has sections for insider trading, SAST and pledged data under corporate filings;
   menu names change, so use the site search if needed.) List promoter and director trades with dates and prices.
3. **Bulk and block deals.** From NSE's historical bulk and block deal data, list the deals of the last 12 months: who
   sold, who bought, at what price relative to that day's close.
4. **Timeliness.** For the last four quarters, compute the days from quarter-end to the results filing and to the
   shareholding-pattern filing, and compare with the Reg 33 and Reg 31 deadlines.
5. **Size bucket and index.** Find the company's rank and bucket in AMFI's latest categorisation list (amfiindia.com)
   and its index memberships (niftyindices.com). Compute its free-float market cap using the promoter holding as a
   first approximation, and compare with the free-float figure NSE shows on the stock's page (if shown).

**Deliverable:** the tables plus a 300-word note: what the ownership trends suggest, any pledge or insider-trading
signals, and whether the company's disclosure is timely. Frame findings as observations, not verdicts.

### E01.38 · A capital-action history *(01.3)*

1. From the share-capital note in the last five annual reports (or Screener's share-count history, verified against
   the reports), reconstruct the number of shares at each year-end and explain every change: bonus, split, QIP,
   rights, preferential allotment, warrant conversion, ESOP allotment, buyback.
2. Pick **one** event from the last five years and find its primary document: the QIP placement document, the rights
   letter of offer, the EGM notice for a preferential issue or warrants, or the buyback letter of offer and post-offer
   public announcement (SEBI → *Filings*, or the company's announcements on NSE/BSE).
3. Do the arithmetic for that event, as appropriate: dilution and $v_{\text{post}} = (V + nP)/(N + n)$ for a stated
   range of intrinsic values; the TERP and RE value; a Black–Scholes value for warrants (state and justify your
   volatility); or the buyback entitlement ratios versus the acceptance ratios actually achieved.
4. Judge whether the event moved value between shareholder groups, and in which direction.

**Deliverable:** a share-count bridge table and a one-page analysis of the chosen event.

### E01.39 · Where did your company's return come from? *(01.5)*

1. For the same company, take diluted EPS from the annual reports for FY21 and FY26 (or any five-year window). Restate
   the earlier figure for any bonus or split since. Note any large exceptional items and also compute EPS excluding them.
2. Get prices and dividends. The snippet below pulls split-adjusted closes and dividend ex-dates from Yahoo. Replace
   the placeholder EPS values with your annual-report figures.

```python
# needs network
import io, sys, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import yfinance as yf

TICKER, START, END = "ASIANPAINT.NS", "2021-03-31", "2026-03-31"   # <- your company and window
EPS_START, EPS_END = 10.0, 20.0     # <- placeholders: type in diluted EPS from the two annual reports,
                                    #    restated for any later bonus/split (the EPS note shows it)

h = yf.Ticker(TICKER).history(start="2021-03-01", end="2026-04-15", auto_adjust=False)
h.index = h.index.tz_localize(None)
p0 = float(h.loc[:START, "Close"].iloc[-1])      # last close on or before START (split-adjusted, not dividend-adjusted)
p1 = float(h.loc[:END, "Close"].iloc[-1])
divs = h.loc[START:END, "Dividends"]
divs = divs[divs > 0]
yrs = (h.loc[:END].index[-1] - h.loc[:START].index[-1]).days / 365.25

price_cagr = (p1 / p0) ** (1 / yrs) - 1
eps_cagr = (EPS_END / EPS_START) ** (1 / yrs) - 1
pe0, pe1 = p0 / EPS_START, p1 / EPS_END
pe_cagr = (pe1 / pe0) ** (1 / yrs) - 1
avg_yield = divs.sum() / p0 / yrs                # crude: dividends per year / starting price
print(f"{TICKER}: ₹{p0:,.1f} -> ₹{p1:,.1f} over {yrs:.2f} y; {len(divs)} dividends totalling ₹{divs.sum():,.2f}")
print(f"price CAGR {price_cagr:.1%} = EPS CAGR {eps_cagr:.1%} x P/E CAGR {pe_cagr:.1%} (P/E {pe0:.1f}x -> {pe1:.1f}x)")
print(f"check: {(1 + eps_cagr) * (1 + pe_cagr) - 1:.1%};  + avg dividend yield ≈ {avg_yield:.1%}")
print(f"logs: ln(P1/P0) {math.log(p1/p0):.3f} = ln EPS {math.log(EPS_END/EPS_START):.3f} + ln P/E {math.log(pe1/pe0):.3f}")
```

3. Verify the two prices against NSE's historical data, and the dividends against the company's announcements.
4. Decompose the TSR into EPS growth, P/E change and dividend yield, multiplicatively and in logs, on reported and on
   adjusted EPS.
5. Compare the stock's price CAGR with the Nifty 50's over the same window (`^NSEI` in yfinance, a price index) and say
   why comparing with the Nifty 50 TRI would be fairer.

**Deliverable:** the decomposition table and a 200-word "story of the return": business delivery vs change in the
market's mood.

---
[Module index](index.md) · [Solutions →](solutions.md)
