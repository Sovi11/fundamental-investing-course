# 03.5 · Rating rationales, offer documents, broker reports & US filings

> **Why this matters:** the annual report is written by the company for its shareholders. Four other documents are
> written for different readers — lenders, IPO investors, fund managers and US regulators — and each tells you
> something the annual report does not: how close the company is to a liquidity problem, what insiders paid for their
> shares before they sold them to you, what the market already expects, and (for global stocks) what the company is
> legally required to say about its risks. Knowing where each one lives and what to take from it saves hours and
> occasionally saves a portfolio.

**Learning objectives** — after this lesson you can:

- Read a credit-rating rationale and extract, in five lines, the liquidity position, the covenants and funding
  profile, the support assumptions and the rating sensitivities.
- Walk through a DRHP/RHP and compute, from its pages, the fresh issue vs offer for sale, the post-issue share count,
  the market value at the price band, the weighted average cost of acquisition of the sellers, and the lock-in
  schedule.
- Deconstruct a sell-side research report's target price into its assumptions and decide what, if anything, it adds
  to your own work.
- Find any item in a US company's filings (10-K, 10-Q, 8-K, proxy, S-1, 13F, Forms 3/4/5; 20-F and 6-K for foreign
  issuers) and know which item answers which question.

**Prerequisites:** [03.1 Where information lives](01-the-disclosure-universe.md),
[03.2 Anatomy of an annual report](02-anatomy-of-an-annual-report.md),
[03.3 Notes to accounts](03-notes-to-accounts.md)  ·  **Time:** ~75 min

---

## 1. Credit-rating rationales: the equity analyst's free liquidity report

### 1.1 What a rating is — and why equity investors should read one

A **credit rating** is an opinion on the probability that a borrower pays interest and principal on time. In India,
SEBI-registered **credit rating agencies** (CRAs) — CRISIL, ICRA, CARE Ratings, India Ratings & Research, Acuité,
Brickwork, Infomerics — rate bank loans, bonds (non-convertible debentures, NCDs), commercial paper (CP) and fixed
deposits. Every rating action comes with a public **press release** or **rationale** of three to eight pages.

The long-term scale runs **AAA, AA, A, BBB** (investment grade), then **BB, B, C** and **D** (default); "+" and "−"
modifiers refine it (AA+, AA, AA−). Short-term instruments (CP, working-capital lines) use **A1+, A1, A2, A3, A4, D**.
Each rating carries an **outlook** (Stable, Positive, Negative) or, when an event is pending, a **rating watch** ("with
negative implications", "with developing implications").

Rating rationales are among the most underused documents in Indian equity research, for three reasons:

1. **They contain numbers the annual report does not.** Month-by-month debt repayment schedules, unutilised credit
   lines, cash-flow cover for the next year's maturities, related-party support and covenant terms often appear only
   here.
2. **They are updated between annual reports.** A rating action can come at any time; a rating agency that places a
   company on watch is telling you it has seen something.
3. **SEBI requires specific sections.** After IL&FS defaulted in 2018, SEBI told rating agencies to add a section on
   **Liquidity** to every press release — using standard descriptors (**Strong/Superior, Adequate, Stretched, Poor**) and
   covering cash and liquid investments, unutilised lines, and the adequacy of cash flows to service maturing debt —
   and later a section on **Rating sensitivities**: the specific factors that would lead to an upgrade or a downgrade
   [[1]](#sources) [[2]](#sources). The current rules sit in SEBI's Master Circular for credit rating agencies (as of
   September 2026, the version of July 2025) [[2]](#sources).

!!! info "India notes"
    - Rationales are free: search the agency's website by company name, or use the links in the company's exchange
      filings (LODR requires listed companies to disclose rating changes).
    - A company can have ratings from several agencies. Differences between them — or an agency that "withdraws" a
      rating at the company's request — are information in themselves.
    - **"Issuer not cooperating"** (INC) means the company stopped providing information to the agency; the rating is
      then based on public data and usually cut. It is a governance signal, not just a credit one.
    - Ratings of group companies often assume **parent or group support**. Read how much of the rating rests on that
      assumption, and whether the parent is itself stretched.

### 1.2 The five things to extract

| Section | What to take | Why an equity analyst cares |
|:--|:--|:--|
| **Rating action and outlook** | Upgrade, downgrade, reaffirm, watch; the instruments and amounts rated | The direction of travel; how much debt exists by instrument |
| **Key rating drivers — strengths and weaknesses** | The agency's view of market position, profitability, leverage, working capital, management | A second opinion on the business from someone paid to worry about the downside |
| **Liquidity** | Cash and liquid investments; unutilised limits; debt due in the next 12 months; cash flow cover | The single best short-form test of whether the company can survive a bad year |
| **Rating sensitivities** | The explicit triggers: e.g. "net debt/EBITDA above 3.0×", "receivables above 120 days", "reduction in parent support" | Ready-made thesis-breakers for your monitoring list |
| **Key financial indicators and annexures** | A small table of revenue, profit, debt, gearing, interest cover; group structure; instruments and ratings history | Quick consistency check against the accounts |

### Worked example 1 — reading a real rationale: DHFL, 3 February 2019

On 3 February 2019 ICRA placed the A1+ rating on **Dewan Housing Finance's ₹8,000 crore commercial-paper programme on
watch with negative implications** [[3]](#sources). The case study [I4](../13-case-studies/india/04-ilfs-dhfl-2018.md)
covers the company; here we read the document as an equity analyst would.

What the rationale said (paraphrased, figures as reported):

- **Material event.** Disbursements in the December 2018 quarter collapsed to **₹510 crore** from **₹9,950 crore** in the
  September quarter, "amid tightening liquidity". Between 24 September and 31 December 2018 DHFL repaid **₹17,876
  crore** of debt.
- **How it paid.** In the same period it raised **₹16,290 crore**: **₹11,873 crore by selling or securitising loans**,
  ₹2,750 crore of NCDs, and only ₹500 crore of bank loans and **₹575 crore of CP**. Fixed deposits saw a net outflow
  of ₹1,356 crore.
- **Liquidity.** A reserve of about ₹6,500 crore (including statutory liquid assets) was "sufficient to meet the
  scheduled repayments till March 2019" — but could be stretched by premature deposit withdrawals.
- **Weaknesses.** Rising non-housing loans; builder loans at **17% of AUM**, largely under construction or moratorium;
  gearing of **9.3×**; "reduced ability to refinance".

The five-line equity summary:

1. The company can no longer roll short-term market debt (CP was 3.5% of new money raised).
2. It is funding repayments by **shrinking**: 73% of new funding came from selling assets.
3. Loan growth has effectively stopped (disbursements −95% quarter on quarter), so earnings will fall even if credit
   costs do not rise.
4. The runway is roughly two months of scheduled repayments, conditional on depositors not running.
5. The riskiest assets (builder loans) are the least saleable, so the book being sold is the good one.

None of this was in DHFL's last annual report. The shares closed at ₹116.10 on 4 February 2019, the first trading day
after this rationale (and ₹610 in mid-September 2018); DHFL defaulted four months later.

!!! tip "Trader's lens"
    Read the liquidity section like a funding-desk report: sources and uses over the next twelve months, then stress
    it. If the company needs the market to be open to survive, the equity is short a put on market access. Rating
    agencies lag prices, but their rationales often contain the *data* that the price is reacting to.

### 1.3 Limits of ratings

Ratings are paid for by the issuer, rely on information the issuer provides, and change slowly. IL&FS was rated AAA
until August 2018 and D within six weeks; SEBI later penalised ICRA and CARE over their IL&FS ratings
([I4](../13-case-studies/india/04-ilfs-dhfl-2018.md)). Use rationales for their **data and triggers**, not their
conclusions. When the price of a company's bonds or equity diverges sharply from its rating, trust the price's
direction and the rationale's numbers.

---

## 2. Offer documents: DRHP and RHP

### 2.1 The documents and the timeline

An Indian IPO produces three offer documents under SEBI's **ICDR Regulations, 2018** (Issue of Capital and Disclosure
Requirements):

- **DRHP** (draft red herring prospectus): filed with SEBI and published for public comment, usually months before the
  issue. It has everything except the price.
- **RHP** (red herring prospectus): the final document, filed with the Registrar of Companies days before the issue
  opens; it adds the **price band** and issue dates.
- **Prospectus**: filed after pricing, with the final price.

Since **1 December 2023** listing must happen within **three working days of the issue closing (T+3)**
[[4]](#sources). **Anchor investors** — large institutions allotted shares the day before the issue opens — are locked
in for **30 days on 50% of their allotment and 90 days on the rest** [[5]](#sources). Promoters' minimum contribution is
locked in for 18 months (3 years in some cases) and other pre-IPO shareholders for 6 months. The dates on which lock-ins
expire are known in advance and often coincide with selling pressure.

### 2.2 What to read, in order

| DRHP/RHP section | What it contains | What to take |
|:--|:--|:--|
| **Cover page and "The Offer"** | Fresh issue (new shares, money to the company) vs **offer for sale** (OFS: existing holders selling, money to them), sizes, price band | Who gets the money. A large OFS means insiders are cashing out |
| **Objects of the Issue** | Uses of fresh-issue money: capex, debt repayment, acquisitions, "general corporate purposes" (capped at 25%) | Whether the company needs the money, and for what |
| **Capital structure** | Share history, pre-IPO placements, ESOPs, **weighted average cost of acquisition (WACA)** of each selling shareholder | What insiders paid, and the multiple they are selling at |
| **Basis for Issue Price** | KPIs, peer comparison, and (since November 2022) the price per share of recent primary and secondary transactions and the IPO price band as a multiple of WACA, with a justification by a committee of independent directors [[6]](#sources) | The bankers' valuation case — and its weakest assumptions |
| **Risk factors** | Company-specific risks first, then generic ones | The few specific risks are the useful ones; count litigation and regulatory matters |
| **Restated financial information** | Three years of audited accounts restated to current policies, with auditor's examination report | Build your model from here, not from marketing pages |
| **Management's discussion and analysis** | Drivers, segment performance, liquidity | Compare with KPIs; look for changes in accounting policy |
| **Outstanding litigation and material developments** | Cases against the company, promoters and directors, tax disputes | Size relative to net worth; criminal matters against promoters |
| **Group companies and related-party transactions** | Promoter-controlled entities and dealings | Leakage paths |

### Worked example 2 — the arithmetic of an IPO: Zomato, July 2021

Zomato's IPO (July 2021) offered **₹9,375 crore** of shares at a price band of **₹72–76**: a **fresh issue of ₹9,000
crore** and an **OFS of ₹375 crore** by Info Edge. At ₹76 the company had about **784.5 crore shares** after the issue,
a market value of about **₹59,623 crore** ([I8](../13-case-studies/india/08-zomato-paytm-ipos-2021.md)).

- **Who gets the money?** 96% of the issue was fresh capital — cash for the company, not for sellers. That is the
  opposite of an insider exit.
- **Dilution:** fresh shares = 9,000 ÷ 76 ≈ **118.4 crore**, about 15% of the post-issue count.
- **Post-money cash:** the fresh issue added ₹9,000 crore to the balance sheet, about 15% of the market value — so the
  market value net of the new cash was ≈ ₹50,600 crore.
- **What the price implies:** Zomato was loss-making, so the question is not P/E but how many years of growth at what
  eventual margin justify ₹50,600 crore for the operating business. That is the analysis the case study asks you to do.

The lesson generalises: **first identify who is selling and at what cost, then what the price implies.** An IPO where
private-equity holders sell most of the shares at ten times their WACA is a different proposition from one where the
company raises growth capital at a price close to its last private round.

!!! warning "Reading the Basis for Issue Price"
    The KPIs are chosen by the company and its bankers. Check that each KPI is defined, audited or certified, and
    shown for every period; that the "listed peers" are genuinely comparable; and that the multiple quoted uses the same
    basis for the company and its peers (pre- vs post-issue shares, trailing vs forward earnings).

---

## 3. Sell-side research reports

### 3.1 Structure

A broker's company report usually has: a rating (Buy/Add/Hold/Reduce/Sell) and a **target price (TP)** with a 12-month
horizon; a one-page investment thesis; earnings estimates for two or three years with changes from the last report;
the valuation method; key risks; and pages of financial tables. **Initiation reports** (the first on a company) are
long and useful for industry background; **results updates** are short and mostly re-state the quarter.

### 3.2 How target prices are built

Most target prices are **a multiple times a forward estimate**: TP = target P/E × EPS two years out (or EV/EBITDA,
P/B for lenders, sum-of-the-parts for conglomerates), sometimes cross-checked with a DCF. The two inputs are both
judgements, and small changes move the answer a lot:

$$
TP = m \times EPS_{t+2} \quad\Rightarrow\quad \frac{\Delta TP}{TP} \approx \frac{\Delta m}{m} + \frac{\Delta EPS}{EPS}
$$

### Worked example 3 — deconstructing a (fictional) broker note on Kaveri

*This note is fictional, written for this lesson; the Kaveri numbers are from the running example.*

> **Broker X, 25-Aug-2026 — Kaveri Pumps & Motors: BUY, TP ₹528.** "We value Kaveri at 24× FY28E EPS of ₹22.0. We
> expect revenue to grow 15% a year to FY28 on the solar-pump order book and industrial demand, with EBITDA margin
> recovering to 15.5% as Hosur ramps up. Q1 was a blip; receivables will normalise as state payments resume. Risks:
> delays in government payments, copper prices."

How to use it against your own work ([Kaveri valuation](../appendix/running-example/kaveri-valuation.md)):

1. **Rebuild the estimate.** FY26 revenue was ₹1,318 crore. Fifteen per cent a year gives FY28 revenue of about ₹1,743
   crore; at a 15.5% EBITDA margin, EBITDA ≈ ₹270 crore. EPS of ₹22 on 6.07 crore shares is PAT of ≈ ₹134 crore — a
   48% rise from FY26's ₹90.5 crore. The course's base case has FY28 revenue of ₹1,653 crore at a 14.2% margin.
2. **Find the swing assumptions.** The note differs from the base case mainly on growth (15% vs 10–14%) and margin
   (15.5% vs 14.2%). It does not model receivables or cash flow at all — the course's central concern.
3. **Price the multiple.** 24× is roughly the stock's current trailing multiple (25.9× FY26 EPS of ₹15.08). A buyer at
   ₹390 who accepts the note is betting on EPS growth, not re-rating.
4. **Take what is useful.** The note's value is as a record of the bullish expectation you must beat or reject — the
   "market view" in your variant-perception statement ([11.3](../11-process/03-writing-an-investment-memo.md)). The
   course's reverse DCF says ₹390 already implies ≈14% growth; the note needs more than that.

### 3.3 Incentives and how not to be used by them

Sell-side analysts are paid, directly or indirectly, by trading commissions, investment-banking relationships and
access to management. The consequences are well documented: ratings skew heavily towards Buy, targets cluster just
above the current price, estimates follow guidance, downgrades come late, and companies with investment-banking
business get kinder coverage. SEBI's **Research Analysts Regulations** (2014, amended since) require disclosure of
conflicts — whether the firm or analyst holds the stock, received compensation from the company, or managed an issue —
at the end of every report; read that section first [[7]](#sources).

Use sell-side research for: industry data and channel checks; the consensus estimate you must beat; management access
notes; and good initiation reports' history of a sector. Do not use it for: the rating, the target price, or any
statement about what "the market is missing".

---

## 4. US filings: a map for global stocks

Global companies you may analyse — and Indian companies with US listings, such as the former Tata Motors and Satyam
ADSs, or Infosys and Wipro today — file with the **US Securities and Exchange Commission (SEC)** on **EDGAR** (free,
searchable by company name or CIK number) [[8]](#sources).

| Form | What it is | When | What to read first |
|:--|:--|:--|:--|
| **10-K** | Annual report (US companies) | 60–90 days after year end, by filer size | **Item 1** Business; **Item 1A Risk Factors**; **Item 7 MD&A**; **Item 8** Financial statements and notes; Item 9A controls |
| **10-Q** | Quarterly report (first three quarters) | 40–45 days after quarter end | MD&A changes; new risk factors; subsequent events |
| **8-K** | Current report on a material event (results, acquisitions, CEO changes, auditor changes, defaults) | Within four business days | Item 4.01 (auditor change), Item 2.02 (results), Item 5.02 (officers) |
| **DEF 14A** | Proxy statement before the annual meeting | Before the AGM | Executive pay and its metrics; related-party transactions; board independence |
| **S-1 / F-1** | IPO registration (US / foreign issuer) | Before an IPO | The US equivalent of a DRHP: risk factors, use of proceeds, dilution |
| **13F** | Holdings of institutional managers with over $100m | 45 days after quarter end | What large investors own (with a lag) — e.g. Berkshire's Apple purchases in [G10](../13-case-studies/global/10-apple-2016.md) |
| **Forms 3, 4, 5** | Insider holdings and trades | Form 4 within two business days of a trade | Insider buying and selling |
| **Schedule 13D / 13G** | Holdings above 5% (13D if activist) | Within days of crossing 5% | Activists' stated intentions |
| **20-F / 6-K** | Annual report and interim reports of **foreign private issuers** | 20-F within four months of year end | The 20-F is the foreign issuer's 10-K; 6-Ks carry press releases (as used in [I15](../13-case-studies/india/15-tata-motors-jlr.md)) |

!!! info "India notes"
    Indian companies with US ADSs file 20-Fs under IFRS (or with a US GAAP reconciliation in older years), which can
    give a second, differently-audited view of the same company. Satyam's and Tata Motors' 20-Fs are used in the case
    studies ([I1](../13-case-studies/india/01-satyam-2009.md), [I15](../13-case-studies/india/15-tata-motors-jlr.md)).
    The Indian equivalents of the US forms are covered in [03.1](01-the-disclosure-universe.md): LODR Regulation 30
    disclosures ≈ 8-K; SAST disclosures ≈ 13D/13G; insider trading disclosures under the PIT Regulations ≈ Form 4.

!!! warning "Common mistakes"
    - Reading only a rating's *letter* and not its liquidity section and sensitivities.
    - Treating an AAA or a Big Four auditor as proof of safety (see I4, G4, G9).
    - Reading the DRHP's marketing chapters and skipping the capital-structure pages that show what insiders paid.
    - Confusing a large *fresh issue* (money to the company) with a large *OFS* (money to sellers).
    - Using a broker's target price as your valuation, or its "Buy" as a signal.
    - Forgetting lock-in expiry dates when buying a recent IPO.
    - For US companies, reading the press release instead of the 10-K/10-Q, where the risk factors and notes are.

---

## Key terms

| Term | Meaning |
|:--|:--|
| **Credit rating** | An agency's opinion on the probability of timely debt service, on a scale from AAA to D |
| **Rating outlook / watch** | Stable, Positive or Negative direction over 1–2 years / a flag that a pending event may change the rating soon |
| **Liquidity descriptor** | Strong/Superior, Adequate, Stretched or Poor — the rating agency's standardised view of near-term liquidity |
| **Rating sensitivities** | The specific factors that would trigger an upgrade or downgrade |
| **Issuer not cooperating (INC)** | A rating maintained on public information because the issuer stopped providing data |
| **DRHP / RHP** | Draft red herring prospectus (filed with SEBI, no price) / red herring prospectus (final, with price band) |
| **Fresh issue** | New shares issued; the money goes to the company |
| **Offer for sale (OFS)** | Existing shareholders sell; the money goes to them |
| **Anchor investor** | An institution allotted shares before the issue opens; locked in 30 days (50%) and 90 days (50%) |
| **WACA** | Weighted average cost of acquisition of shares by a selling shareholder, disclosed in the offer document |
| **Basis for Issue Price** | The offer-document section justifying the price with KPIs, peers and past transaction prices |
| **Target price** | A broker's 12-month price estimate, usually a multiple times forward earnings |
| **10-K / 10-Q / 8-K** | US annual report / quarterly report / current report on a material event |
| **DEF 14A** | US proxy statement: pay, board, related parties |
| **13F** | Quarterly holdings report of US institutional managers above $100m |
| **Form 4** | US report of an insider's trade, due within two business days |
| **20-F / 6-K** | Annual report / interim report of a foreign private issuer listed in the US |

## Check your understanding

1. A rating agency's liquidity section says a company has ₹800 crore of cash and ₹400 crore of unutilised lines against
   ₹1,500 crore of debt due in the next twelve months and ₹500 crore of expected operating cash flow. What descriptor
   would you expect, and what is your equity-analyst takeaway?

<details markdown="1"><summary>Answer</summary>

Sources ₹800 + ₹400 + ₹500 = ₹1,700 crore against uses of ₹1,500 crore: cover of about 1.13× — probably **Adequate**, at
the weaker end. The takeaway: the company depends on rolling some debt or on its operating cash flow arriving on time;
a bad quarter or a closed market makes it Stretched. Add "liquidity cover below 1.1×" to your thesis-breakers.

</details>

2. An IPO raises ₹2,000 crore: ₹300 crore fresh issue and ₹1,700 crore OFS by a private-equity fund whose WACA is ₹120
   against an issue price of ₹600. What should you conclude, and what would you check?

<details markdown="1"><summary>Answer</summary>

85% of the money goes to a seller exiting at 5× its cost; the company barely needs capital. That is not a red flag by
itself — funds must exit — but it removes the "growth capital" argument and means the price was set to suit a motivated
seller. Check the Basis for Issue Price (peer multiples, KPI definitions), the fund's remaining stake and lock-in, and
whether recent secondary transactions were at prices far below ₹600.

</details>

3. A broker values a company at 30× FY28E EPS of ₹40 (TP ₹1,200). If EPS comes in 10% lower and the market pays 25×,
   where is the stock?

<details markdown="1"><summary>Answer</summary>

25 × ₹36 = ₹900 — **25% below the target**. Both judgements (multiple and estimate) moved against the note, and the
effects compound: (1 − 0.1) × (25/30) = 0.75.

</details>

4. Where in a US company's filings would you find (a) a change of auditor, (b) the CEO's bonus metrics, (c) a
   director's share sale last week, (d) the risks the company itself lists?

<details markdown="1"><summary>Answer</summary>

(a) Form 8-K, Item 4.01; (b) DEF 14A (proxy statement), compensation discussion and analysis; (c) Form 4; (d) 10-K, Item
1A (updated in 10-Qs).

</details>

5. Why might a rating rationale be more useful to an equity analyst *after* a rating downgrade than before?

<details markdown="1"><summary>Answer</summary>

A downgrade rationale usually spells out, with numbers, what went wrong — the liquidity shortfall, the covenant or the
support assumption that failed — and the sensitivities for the next move. Before the downgrade the document tends to
emphasise strengths. The numbers in a downgrade rationale often reveal how far the problem has gone.

</details>

## Go deeper

- SEBI, *Master Circular for Credit Rating Agencies* (current version) — the required contents of rating press
  releases [[2]](#sources).
- SEBI, *ICDR Regulations, 2018* and the November 2022 amendments on KPIs and the Basis for Issue Price
  [[6]](#sources).
- Any recent CRISIL or ICRA rationale for a company you follow — read the liquidity section and sensitivities, and add
  the triggers to your monitoring list.
- US SEC, *How to Read a 10-K* (investor.gov) [[8]](#sources).
- Case studies that use these documents: [I4 IL&FS and DHFL](../13-case-studies/india/04-ilfs-dhfl-2018.md) (rating
  rationales), [I8 Zomato & Paytm](../13-case-studies/india/08-zomato-paytm-ipos-2021.md) (offer documents),
  [G3 Cisco](../13-case-studies/global/03-cisco-2000.md) and [G10 Apple](../13-case-studies/global/10-apple-2016.md) (US
  filings).

## Sources

[1]: https://www.business-standard.com/article/news-ians/sebi-tightens-disclosure-norms-for-rating-agencies-118111301537_1.html
[2]: https://www.indiaratings.co.in/data/Uploads/Others/Subs/SEBI%20Master%20Cirular%20for%20Credit%20Rating%20Agencies_%20May2024.pdf
[3]: https://www.icra.in/Rating/GetRationalReportFilePdf/77400~Dewan%20Housing%20Finance-R-03022019.pdf
[4]: https://www.business-standard.com/markets/news/sebi-reduces-timeline-for-listing-shares-to-t-3-from-t-6-from-december-1-123080900726_1.html
[5]: https://www.mondaq.com/india/shareholders/1786582/decoding-the-ipo-lock-in-framework-under-the-sebi-icdr-regulations
[6]: https://www.khaitanco.com/thought-leaderships/SEBI-ICDR-Regulations-amendment-of-November-2022-Part-II-SEBI-mandates-discloure-of-KPIs-and-filing-of-offer-documents-with-SEBI-Head-Office
[7]: https://www.sebi.gov.in/legal/regulations/
[8]: https://www.sec.gov/edgar/search/

All accessed 24-Sep-2026. Regulatory details are as of September 2026; verify the current versions before relying on
them.

---
[← Previous: 03.4 Quarterly results, earnings season & conference calls](04-quarterly-results-and-concalls.md) · [Module index](index.md) · [Next: 03.6 Annotated walkthroughs →](06-annotated-walkthroughs.md)
