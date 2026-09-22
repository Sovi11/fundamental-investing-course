# Module 01 · Solutions

> **Use these after you have tried the problems.** Every numerical answer on this page was recomputed in Python.
> Intermediate figures are shown rounded but were carried unrounded, so the last digit can differ from a
> hand calculation that rounds at every step.

**Rules and market facts** are as of September 2026. They are stated in the lessons and were re-checked on
21-Sep-2026 against the sources linked where they are used: [block-deal framework](https://www.taxmann.com/post/blog/sebi-revises-block-deal-framework-minimum-order-size-rs-25-crore),
[SCRR minimum-public-offer tiers](https://www.taxmann.com/post/blog/scrr-amendment-new-ipo-public-offer-norms),
[buyback taxation from 1-Apr-2026](https://taxguru.in/income-tax/buyback-taxation-shifted-dividend-capital-gains-1st-april-2026.html),
[dividend TDS under s.393 of the Income-tax Act, 2025](https://blog.tdsman.com/2026/05/tds-on-dividend-section-3931-section-194/),
[the buyback small-shareholder reservation](https://investor.sebi.gov.in/buy_back_of_shares.html),
[the Reg 30 materiality test](https://vinodkothari.com/wp-content/uploads/2023/05/Renewed-Continuing-Disclosure-Regime_-Regulation-30-of-SEBI-LODR.pdf),
[the MWPL formula](https://www.nseclearing.in/sites/default/files/2025-10/Recent%20changes%20in%20Equity%20Derivative%20segment%20focusing%20on%20position%20limits,%20Limit%20Monitoring,%20and%20Securities%20in%20Ban%20Period.pdf)
and [the AMFI July-2026 cutoffs](https://matasec.com/wp-content/uploads/2026/07/AMFI-Latest-Stocks-Categorisation-July-2026.pdf).
The Nifty 50 close of 23,346.40 on 18-Sep-2026 was checked against Yahoo Finance (`^NSEI`). Re-verify any rule
before you rely on it for a real decision.

---

## Warm-up

### E01.01 · True or false?

1. **False.** Limited liability: the bank's claim is on Kaveri, a separate legal person. Shareholders lose at most what
   they paid for their shares.
2. **False.** Kaveri owns the plant. You own 1% of the shares, which is a residual claim on the company.
3. **False.** A special resolution needs votes *for* at least three times the votes *against*, i.e. 75% of the votes
   **cast** (Companies Act s.114), not 75% of all shares.
4. **True.** Significant influence is presumed at 20% or more of voting power without control, and such an investee is
   an associate (equity-accounted).
5. **True.** A listed company has securities on a recognised exchange, and only public companies may offer securities
   to the public. Many public companies are unlisted.
6. **False.** Face value is a legal artefact. It sets how equity is split between share capital and securities premium,
   nothing more.
7. **False.** Under IBC s.53, trade creditors sit in class (f), "remaining debts". Preference shareholders are class
   (g), below them, and equity is class (h).
8. **True.** The board declares interim dividends. It recommends the final dividend and shareholders declare it at the
   AGM, where they can reduce it but not increase it.
9. **True.** A company does not die with its owners. This is why a share can be valued on cash flows decades ahead.
10. **True.** Under LODR Reg 23, no related party may vote to approve a material RPT. The decision belongs to the
    minority, a "majority of the minority" test.

### E01.02 · The liquidation queue

(a) Order under IBC s.53(1):

| Rank | Claim |
|:--|:--|
| (a) | Insolvency resolution process and liquidation costs |
| (b) | Workmen's dues (24 months) **and** secured creditors who relinquished their security, ranking equally |
| (c) | Wages of other employees (12 months) |
| (d) | Unsecured financial creditors |
| (e) | Government dues (2 years) |
| (f) | Trade creditors, i.e. remaining debts |
| (g) | Preference shareholders |
| (h) | Equity shareholders |

(b) A secured creditor that enforces its own security ranks at **(e)** for the ₹30 Cr shortfall, equally with government
dues.

(c) Equity receives whatever is left after every prior claim, but never less than zero because of limited liability.
$A$ is the value realised from the assets and $D$ is the total of all claims ranking ahead of equity (₹311 Cr for Tapti
Textiles). That is a call on the assets struck at $D$.

### E01.03 · Face value, share capital and "dividend of 350%"

(a) Share capital $= 25.00 \times ₹2 = ₹50$ Cr. Total equity $= 50 + 4{,}950 = ₹5{,}000$ Cr. BVPS $= 5{,}000 / 25 = ₹200$.

(b) Market cap $= 25 \times 1{,}180 = ₹29{,}500$ Cr. P/B $= 29{,}500 / 5{,}000 = 5.9$x (equivalently $1{,}180 / 200$).

(c) 350% of the ₹2 face value is **₹7.00 per share**. Total outflow $= 25 \times 7 = ₹175$ Cr. Yield $= 7 / 1{,}180 =
0.59\%$. "350%" sounds huge but is under a 0.6% yield.

(d) Share capital rises by $1.00 \times ₹2 = ₹2$ Cr. The remaining $1.00 \times (1{,}100 - 2) = ₹1{,}098$ Cr goes to
**securities premium**, part of other equity. Total equity rises by ₹1,100 Cr either way.

(e) After the split there are twice as many shares with a ₹1 face value. "350%" now means $3.5 \times ₹1 = ₹3.50$ per
share. Ignoring the QIP shares, the total is $50 \times 3.50 = ₹175$ Cr, the same as before. The percentage-of-face-value
convention changes meaning with every split, which is why analysts quote dividends per share, payout ratios and yields
instead.

### E01.04 · Which share count? Which denominator?

(a) Task 1 → **B** (weighted-average basic). Task 2 → **A** (today's period-end basic). Task 3 → **D** (fully diluted
for valuation). Task 4 → **C** (Ind AS 33 diluted). Task 5 → **A** (period-end basic).

(b)

| # | Multiple | Consistent? | Why |
|--:|:--|:--|:--|
| 1 | EV / EBITDA | Yes | Both belong to all capital providers |
| 2 | Market cap / EBITDA | **No** | Equity numerator, pre-interest denominator. It flatters levered companies |
| 3 | EV / PAT | **No** | Debt is in the numerator but interest has already been deducted from the denominator |
| 4 | Price / EPS | Yes | Both are equity, per share |
| 5 | EV / Sales | Yes | Sales are pre-interest |
| 6 | Market cap / book equity | Yes | This is P/B |
| 7 | EV ex-leases / EBITDA before lease costs | **No** | Lease costs sit below EBITDA under Ind AS 116, so the lease liability must be in EV. The mix flatters the multiple |
| 8 | EV / FCFE | **No** | FCFE is after interest and debt flows, so it belongs to equity only |
| 9 | Market cap / FCFE | Yes | Both are equity |
| 10 | EV / installed capacity | Yes | Capacity is an operating measure, owned by the whole enterprise |

### E01.05 · Where does the money go?

| # | Event | Cash | Share count |
|--:|:--|:--|:--|
| 1 | IPO fresh issue | Into the company | ↑ |
| 2 | IPO OFS by PE fund | Neither: the money goes to the seller | = |
| 3 | Promoter's exchange OFS | Neither | = |
| 4 | QIP | Into | ↑ |
| 5 | Rights issue, fully subscribed | Into | ↑ |
| 6 | Block deal | Neither (a secondary trade) | = |
| 7 | Tender buyback | Out of | ↓ (shares extinguished) |
| 8 | 1:1 bonus | Neither | ↑ (doubles) |
| 9 | 5-for-1 split | Neither | ↑ (×5) |
| 10 | Warrant exercise (75% balance) | Into (the 25% came in at allotment) | ↑ |
| 11 | Final dividend | Out of | = |
| 12 | NCD private placement | Into, with a matching debt claim | = |
| 13 | CCD conversion | Neither now (the cash came in at issue) | ↑ |
| 14 | ESOP exercise | Into (the exercise price) | ↑ |

Rows 2, 3 and 6 are the ones people get wrong. Secondary transactions move ownership between investors and give the
company nothing.

### E01.06 · The plumbing

(a) SEBI → (iv). NSE → (i). NSE Clearing Ltd → (ii). CDSL/NSDL → (iii). Depository participant → (vi). RTA → (v).
AMFI → (vii). NSE Indices Ltd → (viii).

(b) Under T+1 you must be on the register at the end of the record date, so your trade must settle by then.

- (i) Buy Monday 3 Aug → settles Tuesday 4 Aug → **receives** the dividend.
- (ii) Buy Tuesday 4 Aug → settles Wednesday 5 Aug, the record date → **receives** it.
- (iii) Buy Wednesday 5 Aug → settles Thursday 6 Aug → **does not**.

The stock trades **ex-dividend on Wednesday 5 Aug**: under T+1 the ex-date equals the record date.

### E01.07 · Deadlines and thresholds

| # | Answer |
|--:|:--|
| 1 | 45 days |
| 2 | 60 days |
| 3 | 21 days |
| 4 | 30 minutes |
| 5 | 12 hours |
| 6 | 24 hours |
| 7 | 5 working days |
| 8 | 5% |
| 9 | 2%; within 2 working days |
| 10 | 25% |
| 11 | 5% |
| 12 | 7 working days |
| 13 | ₹10 lakh |
| 14 | 0.5% |
| 15 | ₹25 Cr; ±3% (since 7-Dec-2025; previously ₹10 Cr and ±1%. [Taxmann summary](https://www.taxmann.com/post/blog/sebi-revises-block-deal-framework-minimum-order-size-rs-25-crore)) |

### E01.08 · Quick-fire time value

(a) 9% → 72/9 = **8.0** years (exact $\ln 2/\ln 1.09 = 8.04$). 18% → **4.0** years (exact 4.19). The rule is good at 9%
and already about 5% short at 18%.

(b) **Seven** (FY19→FY20→…→FY26).

(c) $0.60/0.40 = 150\%$.

(d) Approximately $10 - 4 = 6\%$. Exactly $1.10/1.04 - 1 = 5.77\%$.

(e) $100/0.08 = ₹1{,}250$. With 3% growth: $100/(0.08 - 0.03) = ₹2{,}000$.

(f) $\ln 2 = +0.693$ and $\ln 0.5 = -0.693$. Symmetric in logs, not in simple returns.

(g) $(1 + 0.12/12)^{12} - 1 = 12.68\%$.

---

## Core

### E01.09 · Kaveri's valuation snapshot at 31-Mar-2024

(a) Market cap $= 6.00 \times 610 = ₹3{,}660.0$ Cr.

(b)

| Metric | Computation | Value |
|:--|:--|--:|
| Basic EPS | 86.4 ÷ 6.00 | ₹14.40 |
| BVPS | 558.8 ÷ 6.00 | ₹93.13 |
| P/E | 3,660.0 ÷ 86.4 | 42.4x |
| P/B | 3,660.0 ÷ 558.8 | 6.55x |
| Earnings yield | 86.4 ÷ 3,660.0 | 2.36% |

(c) Net debt $= (132.0 + 30.0) - 46.1 - 20.0 = ₹95.9$ Cr. EV $= 3{,}660.0 + 95.9 + 15.9 \text{ (leases)} = ₹3{,}771.8$ Cr.

(d) EV/EBITDA $= 3{,}771.8/155.0 = 24.3$x. EV/EBIT $= 3{,}771.8/122.1 = 30.9$x. EV/Sales $= 3{,}771.8/1{,}006.0 = 3.75$x.

(e) The §6 table shows FY24 P/E 42.4x, P/B 6.5x and EV/EBITDA 24.3x. All three match.

(f) FY26 EBITDA (₹181.9 Cr) is higher than FY24's (₹155.0 Cr), yet the multiple fell from 24.3x to 13.7x. Almost all of
the change is in what the market pays per rupee of EBITDA, not in the business. Having priced FY24 as a solar growth
story, the market in September 2026 is pricing receivables risk, the pledge and a guidance miss.

### E01.10 · Kaveri's EV at ₹390, with judgement

(a) EV $= 6.00 \times 390 + (92.0 + 96.0) + 18.2 - 32.5 - 15.0 = 2{,}340.0 + 140.5 + 18.2 = ₹2{,}498.7$ Cr.
EV/EBITDA $= 2{,}498.7 / 181.9 = 13.74$x.

(b) Market cap on diluted shares $= 6.07 \times 390 = ₹2{,}367.3$ Cr, so EV $= 2{,}367.3 + 140.5 + 18.2 = ₹2{,}526.0$ Cr.
EV/EBITDA $= 13.89$x.

(c)

| Adjustment | ₹ Cr |
|:--|--:|
| EV from (b) | 2,526.0 |
| + Expected GST payment: 50% × 38.0 | 19.0 |
| + Expected income-tax payment: 30% × 11.0 | 3.3 |
| + Operating cash not surplus: 2% × 1,318.0 | 26.4 |
| **Adjusted EV** | **2,574.7** |
| EV/EBITDA (÷ 181.9) | 14.15x |
| EV/EBIT (÷ 134.1) | 19.20x |

The operating-cash line adds back cash that the basic build subtracted as if it were surplus. Kaveri holds ₹47.5 Cr of
cash and liquid funds, and you have judged ₹26.4 Cr of it to be working capital.

(d) **No**, not as a base case. A performance or tender guarantee becomes a liability only if a customer invokes it,
which requires Kaveri to fail to perform. Add a probability-weighted amount only if invocation looks likely. The
guarantees are still worth tracking, because they grow with the solar business and sit behind the same state
counterparties as the overdue receivables.

(e) EV without leases $= 2{,}574.66 - 18.2 = ₹2{,}556.5$ Cr. EBITDA after lease costs $= 181.9 - 4.7 - 1.4 = ₹175.8$ Cr.
EV/EBITDA $= 14.54$x. Either consistent convention is fine. The mixed one is not.

**Takeaway.** Three defensible adjustments take the "screen" multiple from 13.7x to about 14.2x. The adjustments are
small for Kaveri, but each would be large for a company with big contingent liabilities or trapped cash.

### E01.11 · Nirmal Finance at ₹402

(a) Market cap $= 11.0 \times 402 = ₹4{,}422$ Cr.

(b) EPS $= 239.5/11.0 = ₹21.77$. BVPS $= 1{,}695.3/11.0 = ₹154.12$. P/E $= 402/21.77 = 18.46$x. P/B $= 402/154.12 = 2.61$x.
Earnings yield $= 5.42\%$.

(c) RoE on closing equity $= 239.5/1{,}695.3 = 14.13\%$. P/E × RoE $= 18.46 \times 0.1413 = 2.61$x, which equals P/B,
because $\frac{P}{E}\times\frac{E}{B} = \frac{P}{B}$. (The reference table's 15.1% RoE uses *average* equity, so it does
not satisfy the identity exactly.)

(d) "EV" $= 4{,}422 + 5{,}565.4 - 560.0 = ₹9{,}427.4$ Cr, and "EV/PPOP" $= 9{,}427.4/440.6 = 21.4$x. The number is
meaningless for three reasons:

- A lender's borrowings are its **raw material**, not its financing choice. Borrowed money is lent on at a spread, and
  interest expense is an operating cost, deducted above PPOP.
- There is no operating business separate from the balance sheet for EV to price. The loans *are* the business.
- The borrowing mix is set by regulation (capital adequacy) and ALM, so "EV" moves mechanically with the loan book.

Value lenders on equity measures: P/B (against RoE and cost of equity), P/E, and later P/ABV (book adjusted for NPAs)
and residual-income models ([07.1](../07-special-valuation/01-banks-and-nbfcs.md)).

### E01.12 · Weighted-average shares: Nirmal's FY24 QIP

(a) FY24 runs from 1-Apr-2023 to 31-Mar-2024 and includes 29-Feb-2024, so it has **366 days**. From 15-Dec-2023 to
31-Mar-2024 inclusive is **108 days** (17 + 31 + 29 + 31).

(b) Weighted average $= 10.0 + 1.0 \times 108/366 = 10.2951$ Cr. Basic EPS $= 169.0/10.2951 = ₹16.42$.

(c) The year-end-share EPS of ₹15.36 is **6.4% lower** ($15.36/16.42 - 1$). Put the other way, the Ind AS figure is
6.8% higher.

(d) FY24 EPS growth: weighted $16.42/12.68 - 1 = 29.5\%$; year-end $15.36/12.68 - 1 = 21.2\%$.

(e) FY25 growth: on the weighted FY24 base $18.95/16.42 - 1 = 15.4\%$; on the year-end base $18.95/15.36 - 1 = 23.3\%$.
The year-end basis **flatters FY25** because it understates the FY24 base. Always check which denominator a
data source uses before computing growth.

(f) A bonus is adjusted retrospectively for every period presented, as if it had happened at the start of the
earliest period. Restated FY24 EPS $= 169.0/(2 \times 10.2951) = ₹8.21$. FY25 EPS $= 208.4/22.0 = ₹9.47$. Growth is
unchanged at 15.4%.

### E01.13 · Options and warrants: the treasury-stock method

(a) $\Delta N = n(1 - K/P)$ for $P > K$, with $P = ₹350$:

| Tranche | $n$ (Cr) | $K$ | $\Delta N$ (Cr) |
|:--|--:|--:|--:|
| A | 0.50 | 120 | $0.50 \times (1 - 120/350) = 0.3286$ |
| B | 0.80 | 260 | $0.80 \times (1 - 260/350) = 0.2057$ |
| C | 0.30 | 400 | 0 (out of the money) |
| W | 0.40 | 300 | $0.40 \times (1 - 300/350) = 0.0571$ |
| **Total** | | | **0.5914** |

Diluted count $= 20.0 + 0.5914 = 20.591$ Cr.

(b) Intrinsic value $= 0.50 \times 230 + 0.80 \times 90 + 0.40 \times 50 = 115 + 72 + 20 = ₹207$ Cr. Check: $\Delta N
\times P = 0.5914 \times 350 = ₹207$ Cr.

(c) (i) Basic: $8{,}000/20.0 = ₹400.0$. (ii) TSM at market price: $8{,}000/20.591 = ₹388.5$.
(iii) Self-consistent: guess that A, B and W exercise and C does not. Then

$$v = \frac{8{,}000 + 0.5 \times 120 + 0.8 \times 260 + 0.4 \times 300}{20.0 + 0.5 + 0.8 + 0.4} = \frac{8{,}388}{21.7} = ₹386.5$$

Check the guess: ₹386.5 is above 120, 260 and 300, so A, B and W do exercise. It is below 400, so C does not. If you
included C you would get $8{,}508/22.0 = ₹386.7$, still below 400, which contradicts the assumption. **Value per share
≈ ₹386.5.** (Running the TSM at your own value of ₹386.5 instead of the market price gives the same answer.)

(d) At an average price of ₹280, only A and B are in the money: $\Delta N = 0.5 \times (1 - 120/280) + 0.8 \times (1 -
260/280) = 0.2857 + 0.0571 = 0.3429$ Cr. Diluted count 20.343 Cr, diluted EPS $= 400/20.343 = ₹19.66$ (basic ₹20.00).
C (₹400) and W (₹300) are excluded because their exercise prices exceed the average price, so including them would
*raise* EPS. They are anti-dilutive.

(e) C has zero intrinsic value, but three years of a 40%-volatility call struck near the money is worth a lot (01.2's
lens: an at-the-money option on ₹390 was worth about ₹145). The TSM prices options at expiry value, so it ignores
time value. Deducting the Black–Scholes value of the options from equity value is more rigorous.

### E01.14 · A convertible: anti-dilution vs economic dilution

(a) $240/200 = 1.2$ Cr new shares.

(b) Coupon 4%: interest $= 240 \times 4\% = ₹9.6$ Cr, post-tax $9.6 \times 0.7483 = ₹7.18$ Cr. If-converted EPS $= (96 +
7.18)/(12.0 + 1.2) = ₹7.82$. That is below ₹8.00, so the instrument is **dilutive** and reported diluted EPS is ₹7.82.

(c) Coupon 7%: post-tax interest $= 16.8 \times 0.7483 = ₹12.57$ Cr. EPS $= 108.57/13.2 = ₹8.23 > ₹8.00$, so it is
**anti-dilutive**. It is excluded and reported diluted EPS stays at ₹8.00.

(d) Each new share must bring in exactly ₹8.00 of post-tax interest saved: $8.00 \times 1.2 = ₹9.6$ Cr post-tax, i.e.
$9.6/0.7483 = ₹12.83$ Cr pre-tax, i.e. a coupon of $12.83/240 = $ **5.35%**. Above it the bond is anti-dilutive.

(e)

| EV | As equity: (EV − 300) ÷ 13.2 | As debt: (EV − 300 − 240) ÷ 12.0 | Self-consistent answer |
|--:|--:|--:|:--|
| 3,600 | ₹250.0 (> ₹200, so holders convert ✓) | ₹255.0 (> ₹200, so holders would *not* take repayment ✗) | **₹250.0**, as equity |
| 2,600 | ₹174.2 (< ₹200, so holders would not convert ✗) | ₹171.7 (< ₹200, so repayment is rational ✓) | **₹171.7**, as debt |

With a 7% coupon, reported diluted EPS shows *no* dilution, yet at an EV of ₹3,600 Cr the conversion right costs
existing holders ₹5 a share ($255 - 250$).

(f) Both treatments give ₹200 when $(EV - 540)/12 = 200$, i.e. **EV = ₹2,940 Cr** (check: $(2{,}940 - 300)/13.2 = 200$).

### E01.15 · Same business, three capital structures

EBIT $= 200 - 40 = ₹160$ Cr for all three. Tax 25%.

(a)

| ₹ Cr | X (net cash 300) | Y (no debt) | Z (debt 800) |
|:--|--:|--:|--:|
| EV | 2,000 | 2,000 | 2,000 |
| Equity value = EV − net debt | 2,300 | 2,000 | 1,200 |
| Interest (income) / expense | (21.0) | 0.0 | 76.0 |
| PBT | 181.0 | 160.0 | 84.0 |
| PAT | 135.75 | 120.0 | 63.0 |
| P/E | 16.9x | 16.7x | 19.0x |
| EV/EBITDA | 10.0x | 10.0x | 10.0x |

(b) EBITDA falls to ₹150 Cr, so EV $= ₹1{,}500$ Cr for all three.

| | X | Y | Z |
|:--|--:|--:|--:|
| New equity value | 1,800 | 1,500 | 700 |
| % change | −21.7% | −25.0% | **−41.7%** |
| EV / equity before | 0.87 | 1.00 | 1.67 |

The change in equity is (−25%) × EV/equity: $-25\% \times 0.87 = -21.7\%$ and $-25\% \times 1.67 = -41.7\%$. Leverage is a
delta multiplier, and net cash is a damper.

(c) Market cap/EBITDA: X $2{,}300/200 = 11.5$x, Y 10.0x, Z **6.0x**. Z "looks" cheapest only because ₹800 Cr of debt is
left out of the numerator. Every business costs the same 10x.

(d) On P/E, Y (16.7x) and X (16.9x) look cheaper than Z (19.0x). But all three businesses are priced identically.
Z's P/E is higher because interest takes out a bigger share of profit than debt takes out of value, and X's P/E
includes treasury income on cash valued at 1x. P/E mixes the business with its financing.

### E01.16 · An IPO: fresh issue plus OFS

(a) $216/180 = 1.20$. The cap is exactly 120% of the floor, so the band is **compliant**.

(b) New shares $= 540/216 = 2.5$ Cr. Post-issue shares $= 42.5$ Cr. OFS $= 6.0 \text{ Cr} \times 216 = ₹1{,}296$ Cr.
Issue size $= 540 + 1{,}296 = ₹1{,}836$ Cr. Periyar receives **₹540 Cr**. The PE fund receives ₹1,080 Cr and the promoter
₹216 Cr.

(c) Post-issue market cap $= 42.5 \times 216 = ₹9{,}180$ Cr, which falls in the **₹4,000–50,000 Cr** tier. That tier
requires an offer of at least 10% of post-issue capital, i.e. ₹918 Cr. The issue offers $8.5/42.5 = 20\%$ (₹1,836 Cr),
so it complies. Public shareholding must reach 25% within **three years** of listing
([Taxmann on the SCRR Amendment Rules, 2026](https://www.taxmann.com/post/blog/scrr-amendment-new-ipo-public-offer-norms)).
In fact everyone except the promoter counts as public, including the PE fund and employees, so public shareholding is
already $100 - 68.2 = 31.8\%$.

(d)

| Holder | Shares after (Cr) | % |
|:--|--:|--:|
| Promoter | 30.0 − 1.0 = 29.0 | 68.2% |
| PE fund | 8.0 − 5.0 = 3.0 | 7.1% |
| Employees | 2.0 | 4.7% |
| IPO investors | 2.5 + 6.0 = 8.5 | 20.0% |
| **Total** | **42.5** | **100.0%** |

(e) Under ICDR Reg 6(1): QIBs up to 50% = ₹918.0 Cr; non-institutional at least 15% = ₹275.4 Cr; retail at least 35% =
₹642.6 Cr. Anchors can take up to 60% of the QIB portion, i.e. ₹550.8 Cr. Since 30-Nov-2025, 40% of the anchor portion
(₹220.3 Cr) is reserved for domestic mutual funds, life insurers and pension funds (01.3).

(f) Pre-issue EPS $= 300/40.0 = ₹7.50$, P/E $= 216/7.50 = 28.8$x. Post-issue EPS $= 300/42.5 = ₹7.06$ (−5.9%), P/E
$= 30.6$x. IPO investors pay 30.6x trailing earnings, before the ₹540 Cr earns anything.

(g) Only the **₹540 Cr fresh issue (29%)** funds the company. The **₹1,296 Cr OFS (71%)** is an exit, mostly for the PE
fund. That is not wrong, but it changes the question. You are buying from informed sellers, and the "objects of the
issue" section tells you the company needs only ₹540 Cr. The promoter's ₹8.5 Cr-share minimum lock-in (20% of
post-issue capital) is easily covered by its 29.0 Cr shares.

### E01.17 · Nirmal's QIP: who gained?

(a) BVPS before $= 853.4/10.0 = ₹85.34$. After $= (853.4 + 300)/11.0 = ₹104.85$. Accretion **+22.9%**.

(b) $V = ₹3{,}500$ Cr: $v_{\text{pre}} = ₹350.00$ and $v_{\text{post}} = (3{,}500 + 300)/11 = ₹345.45$. Old holders lose
$10.0 \times 4.55 = ₹45.5$ Cr. New investors pay ₹300 Cr for $1.0 \times 345.45 = ₹345.5$ Cr of value, a **₹45.5 Cr
transfer from old to new**. Issuing at ₹300 is below ₹350 intrinsic.

(c) $V = ₹2{,}500$ Cr: $v_{\text{pre}} = ₹250.00$ and $v_{\text{post}} = 2{,}800/11 = ₹254.55$. Old holders gain ₹45.5 Cr,
a **transfer from new to old**.

(d) BVPS is an accounting number. It rises whenever shares are issued above book (₹300 against ₹85 book), whatever the
shares are worth. The wealth test compares the issue price with **intrinsic** value per share, $P$ vs $V/N$. For a
lender there is a second-order effect: the new capital lets it grow the loan book, which creates value only if RoE
exceeds the cost of equity.

(e) $310 \times 0.95 = ₹294.50$. ₹300 is above that, so it was **permitted**.

### E01.18 · A Kaveri rights issue (hypothetical)

(a) New shares $= 6.00/6 = 1.00$ Cr. Raised $= 1.00 \times 240 = ₹240$ Cr.
TERP $= (6 \times 390 + 240)/7 = 2{,}580/7 = ₹368.57$. RE value $= 368.57 - 240 = ₹128.57$.

(b) Before: $1{,}200 \times 390 = ₹4{,}68{,}000$. She receives 200 REs.

| Choice | Computation | Wealth |
|:--|:--|--:|
| Subscribe | $1{,}400 \times 368.57 - 200 \times 240 = 5{,}16{,}000 - 48{,}000$ | ₹4,68,000 |
| Sell REs | $1{,}200 \times 368.57 + 200 \times 128.57 = 4{,}42{,}286 + 25{,}714$ | ₹4,68,000 |
| Ignore | $1{,}200 \times 368.57$ | ₹4,42,286 (−₹25,714, −5.5%) |

(c) Promoter entitlement $= 0.584 \times 6.00/6 = 0.584$ Cr shares, costing $0.584 \times 240 = ₹140.2$ Cr. New stake
$= (3.504 + 0.584)/(6.00 + 0.584) = 4.088/6.584 = $ **62.1%**, up 3.7 points. The issue raises only ₹140.2 Cr of the
₹240 Cr target.

(d) 1-for-3 at ₹120 gives 2.00 Cr new shares and ₹240 Cr. TERP $= (3 \times 390 + 120)/4 = ₹322.50$. RE value $= ₹202.50$.
The 1,200-share holder gets 400 REs. Ignoring them costs $400 \times 202.50 = ₹81{,}000$, which is **17.3%** of
₹4,68,000. The same money is raised, but the deeper discount makes inaction far more expensive.

(e) Model answer: if the promoter takes up its rights, it has to find about ₹140 Cr in cash while already borrowing
against its shares for a real-estate venture. That would raise questions about where the money comes from, possibly
more pledging. If it renounces, its stake falls and the market reads it as a lack of capacity or confidence. A deep
discount combined with a promoter who plans to subscribe can also be a cheap way to creep up in ownership when
others don't participate, as (c) shows. Either way the pledge makes the promoter's choice informative.

### E01.19 · Kaveri's dividend: payout, dates, tax

(a) Reported payout $= 21.0/97.4 = 21.6\%$. PAT excluding the gain $= 97.4 - 14.0 \times (1 - 0.2517) = 97.4 - 10.48 =
₹86.92$ Cr, so the adjusted payout is **24.2%**. "Dividend %" $= 3.5/5 = 70\%$. Yield at ₹780 $= 0.45\%$.

(b) Total $= 3.75 \times 6.00 = ₹22.5$ Cr, so the payout is $22.5/90.5 = 24.9\%$, in line with the "~25%" guidance.
Announced as **75%** ($3.75/5$). Yield at ₹390 $= 0.96\%$. Theoretical ex-dividend price $= 390 - 3.75 = ₹386.25$.
Post-tax at 31.2% $= 3.75 \times 0.688 = ₹2.58$.

(c) The ex-date equals the record date under T+1: **Thursday 23-Jul-2026**. The last day to buy with the dividend is
**Wednesday 22-Jul-2026**.

(d) TDS applies only if dividends from the company exceed ₹10,000 in the year (rate 10%, s.393 of the Income-tax Act,
2025; [TDSMAN](https://blog.tdsman.com/2026/05/tds-on-dividend-section-3931-section-194/)):

| Shares | Dividend | TDS |
|--:|--:|--:|
| 2,666 | ₹9,997.50 | nil |
| 2,667 | ₹10,001.25 | ₹1,000.13 (10% of the whole amount) |
| 3,000 | ₹11,250.00 | ₹1,125.00 |

TDS is a prepayment, not the final tax. Dividends are taxed at the holder's slab rate.

(e) The **final** dividend for FY *t* is recommended with the results and declared at the AGM, which is usually held
July–September, so it is paid in FY *t+1*. Only interim dividends are paid in the year they relate to. "Dividends paid
in FY26" therefore mostly reflect FY25 profits, which matters when you compute payout ratios.

### E01.20 · A Kaveri buyback (hypothetical)

(a) Shares bought $= 120/450 = 0.2667$ Cr (26.67 lakh) $= 4.44\%$ of 6.00 Cr.

(b) Paid-up capital + free reserves $= 30.0 + 676.1 = ₹706.1$ Cr.

- 25% cap: $0.25 \times 706.1 = ₹176.5$ Cr, and ₹120 Cr is within it ✓.
- 10% of capital + free reserves $= ₹70.6$ Cr, and ₹120 Cr exceeds it, so a **special resolution** is needed, not just a
  board resolution.
- Post-buyback debt $= 188.0 + 120.0 = ₹308$ Cr, against $2 \times (706.1 - 120) = ₹1{,}172$ Cr ✓.

(c) Value per remaining share $= (1{,}941.3 - 120)/(6.07 - 0.2667) = 1{,}821.3/5.8033 = ₹313.8$, **−1.9%** against ₹319.8.
Buying back at ₹450, above intrinsic value, transfers value to the sellers. The buyback is value-neutral at the
intrinsic value of **₹319.8**.

(d) Extra post-tax interest $= 120 \times 8.9\% \times (1 - 0.2517) = ₹7.99$ Cr. Pro-forma EPS $= (90.5 - 7.99)/(6.00 -
0.2667) = 82.51/5.7333 = ₹14.39$, against ₹15.08 (**−4.6%**). EPS is unchanged when the earnings yield at the buyback
price equals the post-tax cost of debt: $15.08/P = 6.66\%$ gives $P = ₹226.5$. Below ₹226.5 the buyback is
EPS-accretive, and below ₹319.8 it is value-accretive. **They are different tests.** At ₹300, for example, value per
share rises (₹321.2) while EPS falls (₹14.73).

(e) Small-shareholder cap at ₹390: $2{,}00{,}000/390 = 512.8$, so **512 shares** (₹1,99,680). Reserved $= 15\% \times 26.67
= 4.00$ lakh shares, against small holdings of $9\% \times 600 = 54.0$ lakh: acceptance **7.41%**. General $= 22.67$ lakh
against 546.0 lakh: **4.15%**. A 500-share small holder gets $500 \times 7.41\% = 37.04$, so **37 shares** accepted
(entitlements round down; more can be accepted if some eligible holders don't tender).

(f) From 1-Apr-2026 the buyback is taxed as a capital gain: $(450 - 210) \times 13\% = ₹31.20$ per share
([TaxGuru summary](https://taxguru.in/income-tax/buyback-taxation-shifted-dividend-capital-gains-1st-april-2026.html)).
Under the deemed-dividend regime the whole ₹450 was taxed at 31.2% = **₹140.40** per share, with the ₹210 cost left as
a capital loss to set off elsewhere. Promoters now pay extra tax (an effective 22% or 30%, 01.3), which is worth checking
when a promoter says it will tender.

(g) Expected gain per share $= a(450 - 390) + (1 - a)(380 - 390)$. At $a = 7.41\%$: $4.44 - 9.26 = $ **−₹4.81 per
share**. Break-even: $60a = 10(1 - a)$ gives $a = 10/70 = $ **14.3%**. The trade needs actual acceptance of about double
the entitlement ratio, i.e. many eligible holders not tendering.

### E01.21 · Adjusting history for a bonus (hypothetical)

(a) Divide every per-share figure by 2:

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| EPS (₹), adjusted | 2.73 | 3.93 | 5.22 | 7.20 | 8.12 | 7.54 |
| BVPS (₹), adjusted | 33.15 | 36.33 | 40.55 | 46.57 | 53.10 | 58.84 |
| Price (₹), adjusted | 105 | 160 | 180 | 305 | 390 | 260 |
| DPS paid (₹), adjusted | 0.75 | 0.75 | 1.00 | 1.25 | 1.75 | 2.00 |

(b) EPS CAGR $= (7.54/2.73)^{1/5} - 1 = 22.5\%$, identical because both endpoints are halved. P/E by year: 38.4x, 40.7x,
34.5x, 42.4x, 48.0x, 34.5x, identical to the unadjusted series.

(c) Adjusted EPS with unadjusted price: $520/7.54 = $ **69.0x**. Adjusted price with unadjusted EPS: $260/15.08 = $
**17.2x**. Both are nonsense. A sudden jump or halving of a historical multiple on a data site usually means a bonus or
split was adjusted on one side only.

(d) On allotment, ₹30.0 Cr moves from other equity to share capital: share capital becomes $12.00 \times ₹5 = ₹60.0$ Cr,
other equity $676.1 - 30.0 = ₹646.1$ Cr, and **total equity stays ₹706.1 Cr**. The FY26 balance sheet is not restated.
The capitalisation happens when the shares are allotted in FY27. Only per-share figures (EPS, DPS) are restated for
comparability.

(e) After a bonus, the original 100 shares keep their ₹390 cost and the 100 bonus shares have a **zero** cost of
acquisition. The average is ₹195, but for tax each lot is separate. After a 5-for-1 split she would hold 500 shares with
the original cost **apportioned**, ₹78 each.

(f) The usual adjustment preserves the option holders' economics: **20 lakh options at ₹100**. The number of options
doubles and the exercise price halves.

### E01.22 · Kaveri's shareholding pattern and free float

(a)

| Category | % | Shares (lakh) | Value at ₹390 (₹ Cr) |
|:--|--:|--:|--:|
| Promoter & group | 58.4 | 350.40 | 1,366.6 |
| Mutual funds | 14.2 | 85.20 | 332.3 |
| Insurance | 2.1 | 12.60 | 49.1 |
| FPIs | 7.9 | 47.40 | 184.9 |
| Retail & others | 17.4 | 104.40 | 407.2 |
| **Total** | **100.0** | **600.00** | **2,340.0** |

(b) IWF at most $1 - 0.584 = 0.416$, giving free-float market cap at most $0.416 \times 2{,}340 = ₹973.4$ Cr. The real IWF
could be lower because NSE also excludes shares held by directors and KMP outside the promoter group, employee welfare
trusts, strategic or FDI holders, locked-in shares and the IEPF (01.2).

(c) Position $= 1.5\% \times 12{,}000 = ₹180$ Cr $= 46.15$ lakh shares. That is **7.7% of the equity** and **18.5% of
the free float**. Days to build $= 180/(0.20 \times 6) = $ **150 trading days**, about seven months, with price impact
all the way.

(d) At **5%** of the shares (30.00 lakh shares, ₹117.0 Cr at ₹390) the fund must disclose under SAST Reg 29(1) within
**two working days**, and again for every further 2% change.

(e) MF ownership would rise to $14.2 + 7.7 = $ **21.9%**. The risk is crowding. If small-cap redemptions or a governance
scare force several funds to sell at once, a stock trading ₹6 Cr a day cannot absorb it, and the price gaps down far
more than any change in the business.

### E01.23 · When does the pledge bite?

(a) Pledged $= 6.00 \times 0.584 \times 0.06 = 0.21024$ Cr $= 21.02$ lakh shares $= 3.50\%$ of equity.

(b) At ₹520: collateral ₹109.3 Cr, so cover $= 109.3/35 = 3.12$×. At ₹390: ₹82.0 Cr, cover $= 2.34$×.

(c) $P = \text{cover} \times \text{loan} / \text{pledged shares}$. Top-up $= 1.75 \times 35/0.21024 = $ **₹291.33**,
25.3% below ₹390. Invocation $= 1.25 \times 35/0.21024 = $ **₹208.10**, 46.6% below.

(d) Required collateral $= 1.75 \times 35 = ₹61.25$ Cr. At ₹260 that is $61.25/260 = 23.56$ lakh shares, **2.53 lakh**
more. Pledged share of the promoter holding $= 23.56/350.40 = $ **6.7%**.

(e) **No.** Detailed reasons are required once encumbrance reaches 50% of the promoter holding or 20% of share capital.
Before: 6% and 3.5%. After (d): 6.7% and $23.56/600 = 3.9\%$. Both are far below.

(f) At ₹208, ₹6 Cr of daily turnover is $6/208 = 2.88$ lakh shares a day, and 20% of that is 0.577 lakh. Selling 21.02
lakh shares takes $21.02/0.577 = 36.4$, i.e. **about 37 trading days**. The lender needs almost two months, and that
supply overhang is why invocations cause cascades in small caps.

### E01.24 · Kaveri's disclosure calendar and the materiality test

(a)

| Filing | Deadline | Day |
|:--|:--|:--|
| Q2 FY27 shareholding pattern (quarter ended 30-Sep-2026) | 21-Oct-2026 | Wed |
| Q2 FY27 results | 14-Nov-2026 | **Sat** |
| Q3 FY27 results | 14-Feb-2027 | **Sun** |
| FY27 audited results | 30-May-2027 | **Sun** |

The three results deadlines fall on weekends. The rule counts calendar days, so don't assume a weekend extends it. In
practice boards meet on or before the last working day.

(b) Thresholds: 2% of turnover $= 0.02 \times 1{,}318 = ₹26.36$ Cr; 2% of net worth $= 0.02 \times 706.1 = ₹14.12$ Cr;
5% of average PAT $= 0.05 \times (86.4 + 97.4 + 90.5)/3 = 0.05 \times 91.43 = ₹4.57$ Cr. The **lowest, ₹4.57 Cr, binds**.

(c)

| Event | Material? | Deadline |
|:--|:--|:--|
| 1. ₹3.9 Cr GST show-cause notice | Below ₹4.57 Cr, so **not material on the quantitative test**. The company's policy and the qualitative price-sensitivity test still apply | If disclosed: 24 hours (originates outside) |
| 2. Board approves ₹60 Cr capex and a fund-raise | Fund-raising decisions are deemed material (Para A); ₹60 Cr also exceeds ₹4.57 Cr | **30 minutes** after the board meeting closes |
| 3. ₹6 Cr supplier settlement, no board meeting | ₹6 Cr > ₹4.57 Cr: **material** | **12 hours** (originates inside) |
| 4. Rating downgrade | Rating revisions are **deemed material** | **24 hours** (originates outside) |

(d) 30-Jun-2026 to 8-Aug-2026 is **39 days**, inside the 45-day limit. The trading window, closed since the quarter-end,
reopens 48 hours after the results are published: **Monday 10-Aug-2026**, at the same time of day as the Saturday
announcement.

### E01.25 · Circuits, bans and index flows

(a) Successive 5% lower circuits: ₹370.50, ₹351.98, ₹334.38, ₹317.66, ₹301.77, ₹286.69. The top-up trigger (₹291.33) is
breached on **day 6**. In a locked lower circuit the lender cannot sell either. The cover can fall straight through the
invocation level before any shares change hands, which is why lenders demand high cover on illiquid small caps.

(b)

| Trigger | Down | Up |
|:--|--:|--:|
| 10% | 21,011.76 | 25,681.04 |
| 15% | 19,844.44 | 26,848.36 |
| 20% | 18,677.12 | 28,015.68 |

(c) 15% of free float $= 9.0$ Cr. $65 \times$ ADDV $= 65 \times 0.12 = 7.8$ Cr. Floor $= 6.0$ Cr. MWPL $= \max(\min(9.0,
7.8), 6.0) = $ **7.8 Cr** shares. Ban entry when FutEq OI exceeds **7.41 Cr** ($0.95 \times 7.8$). Exit when it falls to
**6.24 Cr** or below ($0.80 \times 7.8$). With ADDV of 8 lakh: $65 \times 0.08 = 5.2$ Cr is below the 6.0 Cr floor, so
MWPL $= $ **6.0 Cr**, ban above 5.7 Cr, exit at 4.8 Cr. Weaker delivery volume lowers the limit until the floor binds.

(d) $1.5 \times 0.40 = $ **0.6 Cr** FutEq shares.

(e) Free-float market cap $= 0.45 \times 36{,}000 = ₹16{,}200$ Cr. Weight $= 16{,}200/30{,}00{,}000 = 0.54\%$. Forced buying
$= 45{,}000 \times 0.0054 = ₹243$ Cr, which is $243/90 = $ **2.7 days** of volume. Expect a run-up between the announcement
and the effective date as arbitrageurs pre-buy, very heavy volume at the effective-date close, and often some give-back
afterwards.

### E01.26 · Where Kaveri's growth came from

(a)

| Segment | FY21 | FY26 | CAGR |
|:--|--:|--:|--:|
| Agri & domestic | 403.9 | 606.2 | 8.5% |
| Industrial & motors | 189.7 | 355.9 | 13.4% |
| Solar | 18.4 | 355.9 | **80.8%** |
| Total | 612.0 | 1,318.0 | 16.6% |

(b) Solar's annual growth rates were 64.7%, 102.0%, 130.1%, 83.1% and 38.1%, averaging **83.6%** against a CAGR of 80.8%.
Total revenue averages 16.64% against 16.58%. The arithmetic mean exceeds the geometric mean by roughly half the
variance of the growth rates, and solar's growth rates are far more dispersed. That is volatility drag again.

(c) Solar is $355.9/1{,}318.0 = $ **27.0%** of FY26 revenue (3.0% in FY21). It supplied $(355.9 - 18.4)/(1{,}318.0 -
612.0) = 337.5/706.0 = $ **47.8%** of the increase. Revenue excluding solar grew from ₹593.6 Cr to ₹962.1 Cr, a CAGR of
**10.1%**. Without solar, Kaveri is a 10% grower, and solar is exactly where the receivables problem sits.

(d) $(1{,}318/874)^{1/3} - 1 = $ **14.7%**, matching the reference valuation's historical FY23–FY26 CAGR.

(e) Rule of 72: $72/80.8 = 0.89$ years. Exact: $\ln 2/\ln 1.808 = 1.17$ years. The rule is 24% short at 80%, because its
approximation $\ln(1+r) \approx r$ fails for large $r$. Don't use it for hyper-growth.

### E01.27 · Discounting and the Gordon model on Kaveri

(a) $DF_{FY29} = 1/1.12186^{2.5} = $ **0.7502**, matching the reference table.

(b) $100/1.12186^5 = $ **₹56.3 Cr**.

(c) $P = 4.20/(0.128 - 0.07) = $ **₹72.41**.

(d) Solve $390 = 4.00(1+g)/(0.128 - g)$: $49.92 - 390g = 4 + 4g$, so $g = 45.92/394 = $ **11.65%** a year, forever.

(e) Sustainable growth $= 13.5\% \times (1 - 24.0/90.5) = 13.5\% \times 0.735 = $ **9.9%**. The DDM result fails on several
counts:

- ₹390 implies 11.65% *perpetual* dividend growth, far above long-run nominal GDP (01.5 says perpetual $g$ should sit at
  or below it) and above what the company's own reinvestment supports.
- With a ~25% payout, dividends are a small, policy-driven slice of the cash the business generates. The 75% it retains
  is reinvested, and its value shows up in growth, which a single-stage model can't phase properly.
- $r - g$ is tiny, so the output is hypersensitive.

Value Kaveri on FCFF (the reference DCF) and use the DDM only as a cross-check. The course tools reproduce (c) and (d):

```python
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, "tools")                      # run from the repo root
from fi.valuation import gordon_value, reverse_dcf

print(f"DDM value: ₹{gordon_value(4.20, 0.128, 0.07):.2f}")                     # ₹72.41
g = reverse_dcf(390, lambda g: gordon_value(4.00 * (1 + g), 0.128, g), lo=0.0, hi=0.127)
print(f"growth implied by ₹390: {g:.2%}")                                        # 11.65%
try:
    gordon_value(4.00 * 1.13, 0.128, 0.13)
except ValueError as e:
    print("refused:", e)                         # g >= r: the perpetuity does not converge
```

### E01.28 · A Nirmal tractor loan and the flat-rate trap

(a) $i = 16.9\%/12 = 1.4083\%$. EMI $= 8{,}00{,}000 \times 0.014083/(1 - 1.014083^{-48}) = $ **₹23,043**. Total paid
$= 48 \times 23{,}042.67 = ₹11{,}06{,}048$, so total interest is **₹3,06,048**. Month 1: interest $= 8{,}00{,}000 \times
1.4083\% = ₹11{,}267$, principal $= ₹11{,}776$. Balance after 12 EMIs: **₹6,47,212**.

(b) Flat rate $= 3{,}06{,}048/(8{,}00{,}000 \times 4) = $ **9.56%** a year.

(c) "10% flat": interest $= 8{,}00{,}000 \times 10\% \times 4 = ₹3{,}20{,}000$, so EMI $= 11{,}20{,}000/48 = $ **₹23,333**.
Solving the annuity for the rate gives 1.4667% a month: **17.6% nominal, 19.1% effective**. The 16.9% reducing-balance
loan is **cheaper** (EMI ₹23,043 against ₹23,333), even though "10%" sounds lower than "16.9%".

### E01.29 · IRR, XIRR and the investor who kept adding

(a) Investor A: absolute return $= (390 + 4)/780 - 1 = $ **−49.5%** over 1.47 years. XIRR $= $ **−37.4%** a year.

(b) Investor B: XIRR $= $ **12.9%**. MOIC $= (390 + 13.5)/210 = $ **1.92×**.

(c) Investor C:

| | ₹ |
|:--|--:|
| Invested: 100 × (210 + 320 + 360 + 610 + 780) | 2,28,000 |
| Dividends: 150 + 400 + 750 + 1,400 + 2,000 | 4,700 |
| Value of 500 shares at ₹390 | 1,95,000 |
| Total received | 1,99,700 |
| MOIC | 0.88× |
| Average cost (2,28,000 ÷ 500) | ₹456 |
| **XIRR** | **−4.7%** |

```python
from datetime import date

def xirr(flows, lo=-0.99, hi=10.0, tol=1e-10):
    """flows: list of (date, amount); negative = money in. Bisection on XNPV (the 01.5 function)."""
    d0 = min(d for d, _ in flows)
    f = lambda r: sum(a / (1 + r) ** ((d - d0).days / 365) for d, a in flows)
    for _ in range(300):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
        if hi - lo < tol:
            break
    return (lo + hi) / 2

buys = {2021: 210, 2022: 320, 2023: 360, 2024: 610, 2025: 780}          # 31-March prices
dps = {2021: 1.5, 2022: 2.0, 2023: 2.5, 2024: 3.5, 2025: 4.0}            # paid in August of that year
pay = {2021: date(2021, 8, 16), 2022: date(2022, 8, 16), 2023: date(2023, 8, 16),
       2024: date(2024, 8, 16), 2025: date(2025, 8, 14)}
flows = [(date(y, 3, 31), -100 * p) for y, p in buys.items()]
flows += [(pay[y], 100 * (k + 1) * dps[y]) for k, y in enumerate(dps)]   # holding grows 100 a year
flows += [(date(2026, 9, 18), 500 * 390)]
print(f"adder's XIRR {xirr(flows):.1%}")                                   # -4.7%
hold = [(date(2021, 3, 31), -210)] + [(pay[y], dps[y]) for y in dps] + [(date(2026, 9, 18), 390)]
print(f"buy-and-hold XIRR {xirr(hold):.1%}")                               # 12.9%
```

(d) B's return is close to the stock's **time-weighted** return: one rupee invested at the start. C's XIRR is
**money-weighted**, and C put most of the money in near the top (₹1.39 lakh of the ₹2.28 lakh in 2024–25 at ₹610 and
₹780). Same stock, opposite outcomes. The investor's timing, not the business, made the difference.

### E01.30 · Nirmal's TSR, decomposed

(a)

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| EPS (₹) | 4.15 | 9.01 | 12.68 | 15.36 | 18.95 | 21.77 |
| P/E | 33.7x | 21.1x | 17.0x | 21.5x | 22.2x | 17.7x |
| DPS (₹) | 0.00 | 1.00 | 1.50 | 1.82 | 2.27 | 2.73 |

(b) PAT CAGR $= (239.5/41.5)^{1/5} - 1 = 42.0\%$. EPS CAGR $= (21.77/4.15)^{1/5} - 1 = 39.3\%$. P/E CAGR $= (17.68/33.73)^{1/5}
- 1 = -12.1\%$. Price CAGR $= (385/140)^{1/5} - 1 = 22.4\%$. Check: $1.3931 \times 0.8788 = 1.2242$ ✓. In logs: $\ln(21.77/4.15)
= 1.658$, $\ln(17.68/33.73) = -0.646$, sum $1.012 = \ln(385/140)$ ✓. PAT grew faster than EPS because of the FY24 QIP
(10 → 11 Cr shares).

(c) TSR (IRR) $= $ **23.3%**. The additive approximation gives $39.3 - 12.1 + 0.7 = 27.9\%$, **4.7 points too high**. The
missing cross-term is $0.393 \times (-0.121) = -4.8\%$. With components this large, use the multiplicative form or logs.

(d) FY21 EPS was depressed by COVID-era credit costs (3.6% of loans, RoE 6.5%), so the P/E of 33.7x was a multiple of
abnormally low earnings. It was not a high price for the franchise. $P/B = P/E \times RoE$: as RoE normalised to about
15%, the P/E could fall by half while P/B rose (2.1x → 2.5x). BVPS compounded at 18.4% and P/B at 3.4% a year. For
lenders, and for any company coming off a trough, P/B is the steadier anchor. This is a **base effect**.

(e) Annual price returns: +35.7%, +13.2%, +53.5%, +27.3%, −8.3%. Arithmetic mean $A = 24.3\%$, population s.d. $\sigma
= 20.9\%$, $A - \sigma^2/2 = 22.1\%$, against the actual CAGR of 22.4%. Real price CAGR at 4% inflation $= 1.2242/1.04 - 1 =
$ **17.7%**.

---

## Stretch

### E01.31 · Equity as a call: Tapti Textiles as a going concern

(a) With $A = 340$, $D = 311$, $r = 6.5\%$, $T = 2$, $\sigma = 25\%$:
$d_1 = [\ln(340/311) + (0.065 + 0.03125) \times 2]/(0.25\sqrt{2}) = 0.797$, $d_2 = 0.443$.
Equity $= A N(d_1) - D e^{-rT} N(d_2) = $ **₹84.4 Cr**. Senior claims $= 340 - 84.4 = $ **₹255.6 Cr**. An immediate
liquidation gives equity $\max(0, 340 - 311) = ₹29$ Cr. The extra ₹55.4 Cr is time value: two years of optionality on
volatile assets.

(b) Yield $= \ln(311/255.6)/2 = 9.80\%$, a **spread of 3.30%** over 6.5%. Riskless PV of the claims $= 311e^{-0.13} =
₹273.1$ Cr, so the creditors' written put is worth $273.1 - 255.6 = $ **₹17.4 Cr**. Risk-neutral probability that equity
finishes worthless $= N(-d_2) = $ **32.9%**.

(c) After the project ($A = 330$, $\sigma = 45\%$): equity $= $ **₹106.9 Cr (+₹22.6 Cr)** and debt $= $ **₹223.1 Cr
(−₹32.6 Cr)**. Firm value falls by ₹10 Cr, yet shareholders gain, because they are long vega and the creditors are short
the put. This is **Type III agency** (risk-shifting, shareholders vs creditors).

(d) Any two of: limits on new debt and leverage (e.g., net debt/EBITDA caps); restrictions on asset sales and on changing
the business; limits on dividends and buybacks; security over specific assets; approval rights over large capex or
acquisitions; cross-default and information covenants.

### E01.32 · Pyramid, tunnelling and votes

(a) Overcharge $= 600 \times 0.04/1.04 = ₹23.08$ Cr. Post-tax transfer $= 23.08 \times (1 - 0.2517) = ₹17.27$ Cr a year.
Family look-through interest in Steel $= 0.45 \times 0.55 = $ **24.75%**.

(b)

| Party | Computation | ₹ Cr a year |
|:--|:--|--:|
| Family | $+17.27 - 0.2475 \times 17.27$ | **+13.00** |
| Steel's outside shareholders (45%) | $-0.45 \times 17.27$ | −7.77 |
| Holdings' outside shareholders (55% of Holdings) | $-0.55 \times 0.55 \times 17.27$ | −5.22 |
| **Sum** | | **0.00** |

(c) The family keeps **75.25 paise** per ₹1. With a direct 55% stake in Steel it would keep only 45 paise. The pyramid
gives control of Steel (through Holdings' 55%) with a cash-flow stake of only 24.75%. The wider the gap between control
and cash-flow rights, the more tunnelling pays.

(d) $17.27 \times 15 = $ **₹259 Cr** of Steel's equity value.

(e) 10% of ₹4,000 Cr = ₹400 Cr, and ₹600 Cr exceeds it, so the contract is **material**. It needs prior shareholder
approval, and **no related party may vote**: Holdings and the family are excluded. The decision rests with Steel's 45%
public shareholders (and any other non-related holders).

(f) The resolution fails if votes against exceed $55/3 = $ **18.33% of total shares**, which is **40.7% of the public's
45%**. Turnout decides it: if institutions holding 18.34% or more of Steel vote no, they block it.

### E01.33 · A full equity bridge, per share

(a)

| Step | ₹ Cr | Why |
|:--|--:|:--|
| Enterprise value (DCF) | 12,000.0 | |
| − Borrowings | (1,500.0) | Lenders' claim |
| − Lease liabilities | (400.0) | Debt-like; lease costs sit below EBITDA in the FCFF |
| − Preference shares | (250.0) | Senior to equity |
| − NCI at market: $0.26 \times 60 \times 20$ | (312.0) | FCFF includes 100% of the subsidiary |
| + Usable cash: $900 - 150 - 200 + 0.75 \times 200$ | 700.0 | Excludes operating float; trapped cash at a 25% haircut |
| + Liquid mutual funds | 300.0 | Surplus liquidity |
| + Associate at market less 20%: $0.8 \times 800$ | 640.0 | Income not in FCFF, so add separately |
| − Expected tax demand: $0.4 \times 180$ | (72.0) | Probability-weighted, not deductible |
| − Gratuity after tax: $50 \times (1 - 0.2517)$ | (37.4) | Unfunded obligation, tax-deductible when paid |
| **Equity value** | **11,068.6** | CCDs *not* deducted: they convert into shares |

(b) Shares: 40.0 basic + 0.8 from the CCDs ($200/250$) = 40.8 Cr. At about ₹268 a share the ₹150 options are in the money
and the ₹320 options are not:

$$v = \frac{11{,}068.6 + 1.2 \times 150}{40.8 + 1.2} = \frac{11{,}248.6}{42.0} = ₹267.8$$

Check: ₹267.8 > ₹150 ✓ and < ₹320 ✓.

(c) Naive: $(12{,}000 - 1{,}500 + 900 + 300)/40 = 11{,}700/40 = ₹292.5$. The gap of ₹24.7 a share (8.4%) is mostly leases
(₹400 Cr), NCI (₹312 Cr), preference (₹250 Cr) and the cash haircuts (₹200 Cr), partly offset by the associate (+₹640 Cr),
plus 2.0 Cr of extra shares from CCDs and options.

### E01.34 · Kaveri needs ₹150 Cr: equity or debt?

(a)

| | QIP at ₹370 | Rights 1-for-10 at ₹250 | Debt at 9.5% |
|:--|--:|--:|--:|
| New shares (Cr) | 0.405 | 0.600 | 0 |
| Value per share: (1,941.3 + 150) ÷ diluted shares | ₹323.0 (+1.0%) | ₹313.5 (subscribers' wealth unchanged, see (b)) | ₹319.8 (unchanged in the DCF) |
| Pro-forma FY26 basic EPS | 90.5 ÷ 6.405 = ₹14.13 | 90.5 ÷ 6.60 = ₹13.71 | (90.5 − 10.66) ÷ 6.00 = ₹13.31 |
| Net debt / EBITDA | 140.5 ÷ 181.9 = 0.77x | 0.77x | 290.5 ÷ 181.9 = 1.60x |
| EBIT / finance costs | 134.1 ÷ 17.0 = 7.9x | 7.9x | 134.1 ÷ (17.0 + 14.25) = 4.3x |
| Promoter stake | 58.4 × 6.00 ÷ 6.405 = 54.7% | 58.4% (if it subscribes) | 58.4% |

Debt interest after tax $= 150 \times 9.5\% \times 0.7483 = ₹10.66$ Cr. The QIP adds value for existing holders (₹19 Cr in
total) because ₹370 is above the ₹319.8 house value: new investors overpay relative to the house view.

(b) Wealth per original share for a subscriber $= 1.1 \times 313.54 - 0.1 \times 250 = ₹319.89$, against ₹319.82 before.
The ₹0.07 gain arises because the 0.07 Cr ESOP-equivalent shares in the diluted count receive no rights: the issue's
discount moves a sliver of value from option holders to shareholders. TERP $= (10 \times 390 + 250)/11 = ₹377.27$, RE
value ₹127.27.

(c) Promoter entitlement $= 0.584 \times 0.60 = 0.3504$ Cr shares × ₹250 $= $ **₹87.6 Cr**. A promoter that is already
borrowing against its shares for an outside venture would probably have to borrow more, perhaps against more shares.
If instead it renounces and others subscribe, its stake falls to $3.504/6.60 = 53.1\%$, a visible signal.

(d) **Rubric (10 marks):**

- **3 marks.** Frames the real problem: the need is caused by receivables from two state agencies. The first question
  is whether those receivables are collectible and whether solar growth should be slowed, not how to fund them.
- **2 marks.** Uses the numbers: debt raises net debt/EBITDA to 1.6x and cuts interest cover to 4.3x on a business whose
  cash conversion is already weak (CFO/PAT 72%). Equity avoids that, at a cost of 6–9% EPS dilution.
- **2 marks.** Understands pricing. A QIP at ₹370 is accretive *if* you believe the house value of ₹320, and wealth-neutral
  for subscribers in a rights issue at any price. The rights issue is fairest to minorities; the QIP is fastest.
- **2 marks.** Governance: the pledge and the promoter's ability to fund its rights (₹87.6 Cr). A QIP dilutes the promoter
  to 54.7%. Any preferential or warrant route to the promoter would need scrutiny.
- **1 mark.** A clear recommendation with a trigger to revisit (e.g., "fund with debt up to X only if receivable days fall
  below Y by Q4").

Model answer (one of several acceptable): *"Kaveri should first cap solar exposure to states with good payment records
and push collection of the ₹62.4 Cr overdue for more than six months. For the residual need, a QIP is preferable to more
bank debt: at ₹370 it is accretive to intrinsic value, keeps net debt/EBITDA below 1x and protects interest cover while
cash conversion is weak. A rights issue is fairer to minorities but asks a pledged promoter for ₹88 Cr, which could turn
into more pledging or a damaging renunciation. Debt should fund only seasonal working capital, with a board-level limit
tied to receivable days."*

### E01.35 · What does ₹390 need?

(a) Required price in Sep-2031 $= 390 \times 1.118^5 = $ **₹681**.

| Exit P/E | Required FY31 EPS | EPS CAGR FY26→FY31 |
|--:|--:|--:|
| 20x | ₹34.06 | **17.7%** |
| 25.9x | ₹26.30 | 11.8% |
| 30x | ₹22.71 | 8.5% |

At an unchanged 25.9x, EPS needs to compound at 11.8%, broadly in line with the reverse DCF's message that ₹390 prices
healthy growth. If the multiple de-rates to 20x, EPS must compound at about 18% for five years, which is more than Kaveri
delivered even in its solar-boom years once FY26 is included.

(b) With the gap growing at $1.25/1.10$ a year:
years to the mid-cap cutoff $= \ln(33{,}500/2{,}340)/\ln(1.25/1.10) = $ **20.8 years**; to rank 500 (₹12,093 Cr) $= $
**12.8 years**. At 11.8% growth the relative gain is only $1.118/1.10$ a year: about **164 years** and **101 years**.
"Small cap becomes mid cap" stories need decades of outperformance, not a good year.

(c) $\mu = \ln 1.14 - 0.40^2/2 = 0.131 - 0.080 = 0.051$. Median five-year multiple $= e^{5 \times 0.051} = $ **1.29×**. Mean
multiple $= 1.14^5 = $ **1.93×**. $P(\text{loss}) = \Phi(-0.051\sqrt{5}/0.40) = \Phi(-0.285) = $ **38.8%**. The "expected"
return is carried by a right tail. The typical outcome is far lower, and a loss over five years is almost a coin flip.
Position sizing should respect the median, not the mean ([11.4](../11-process/04-position-sizing-and-portfolio-construction.md)).

---

## Real-world tasks (rubrics)

These have no single right answer. Grade yourself against the rubric, and if possible have someone else check one
number end to end against the primary source.

### E01.36 · Build a real company's EV — rubric (20 marks)

| Criterion | Marks | What good looks like |
|:--|--:|:--|
| Sourcing | 4 | Every input cites the document, page or note and a date. Share count from the latest SHP; price with a date; consolidated statements used |
| Debt and leases | 4 | Current maturities included in borrowings; lease liabilities in EV *and* a matching EBITDA (post-Ind AS 116 EBITDA is before lease costs) |
| Cash judgement | 3 | Other bank balances checked in the note (lien or margin money excluded); liquid funds included; any cash held abroad or restricted flagged |
| NCI, preference, associates | 3 | NCI added (book, noting that market is better); equity-method investments subtracted at market if listed, otherwise book, with the choice stated |
| EBITDA definition | 3 | Other income and exceptional items stripped out; the company's own "EBITDA" reconciled to yours |
| Reconciliation | 3 | Differences from Screener and Yahoo attributed to specific causes (Yahoo's `total_debt` includes leases; Screener uses its own debt and cash definitions; timing of share count and price; consolidated vs standalone) |

**Typical pitfalls:** using standalone statements for a group; forgetting current maturities (often in "other financial
liabilities" in older reports); subtracting fixed deposits held as margin money; double-counting leases (in both Yahoo's
debt and your lease line).

### E01.37 · Ownership and disclosure audit — rubric (20 marks)

| Criterion | Marks | What good looks like |
|:--|--:|:--|
| Eight-quarter SHP table | 5 | Correct categories; pledged/encumbered shown as % of promoter holding *and* % of equity; changes computed quarter on quarter |
| Pledge and insider data | 4 | Every Reg 31 and PIT disclosure listed with date, quantity and price; promoter creeping acquisitions noted against the 5%-a-year limit |
| Bulk/block deals | 3 | Buyer, seller, price vs close; a view on whether each was an exit, a rotation or a new holder |
| Timeliness | 3 | Days to file vs the 45/60/21-day limits; any late filing noted |
| Size bucket and free float | 2 | AMFI rank and bucket; free float computed and compared with NSE's figure; the definitional difference explained |
| Note | 3 | Separates observation from inference ("promoter pledge rose from 0% to 8% in two quarters" is an observation; "the promoter is in financial stress" is a hypothesis to test). No buy/sell language |

### E01.38 · A capital-action history — rubric (20 marks)

| Criterion | Marks | What good looks like |
|:--|--:|:--|
| Share-count bridge | 6 | Every year-end count reconciled to the share-capital note; bonus/split years restated; ESOP allotments included |
| Primary document | 4 | The right document found (placement document, letter of offer, EGM notice, post-offer announcement) and cited |
| Arithmetic | 6 | For issues: $v_{\text{post}}$ at a stated range of intrinsic values and who gained. For rights: TERP and RE value. For warrants: a Black–Scholes value with a justified volatility, compared with the upfront 25%. For buybacks: entitlement vs actual acceptance, with the reason for any gap |
| Judgement | 4 | A clear view on the direction and rough size of any value transfer, and on what the event says about management's capital allocation |

### E01.39 · Where did your company's return come from? — rubric (20 marks)

| Criterion | Marks | What good looks like |
|:--|--:|:--|
| Clean inputs | 5 | EPS restated for bonus/split; prices verified against NSE; dividends verified against announcements; window stated exactly |
| Decomposition | 6 | Multiplicative identity checks to the rounding; log version adds up; both reported and adjusted EPS |
| Dividends | 2 | Dividend yield estimated sensibly, noting that the yfinance price series is split-adjusted but not dividend-adjusted |
| Benchmark | 3 | Compared with the Nifty 50 over the same dates; explains that `^NSEI` is a price index, so the TRI (dividends reinvested) is the fair comparison |
| Story | 4 | Says clearly what share of the return came from the business (EPS, dividends) and what from the multiple, and whether the starting multiple was depressed or elevated (base effects, as in E01.30(d)) |

**Self-check:** if your EPS CAGR times your P/E CAGR does not reproduce the price CAGR, one of the inputs is on a
different share basis. Usually a bonus or split has been adjusted in the price but not in the EPS.

---
[← Exercises](exercises.md) · [Module index](index.md)
