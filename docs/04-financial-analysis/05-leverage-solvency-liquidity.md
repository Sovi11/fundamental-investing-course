# 04.5 · Leverage, solvency & liquidity

> **Why this matters:** most companies that go to zero do not run out of profit; they run out of *cash at a moment
> when a lender wants it back*. Leverage analysis asks three questions in rising order of urgency: is the debt load
> sensible for this business (leverage), can earnings service it through a bad year (solvency), and can the company
> meet what falls due in the next twelve months (liquidity)? Equity is the residual claim — you get paid last, so
> you must understand everyone who gets paid first.

**Learning objectives** — after this lesson you can:

- Compute and interpret debt/equity, net debt/EBITDA, interest cover, DSCR, fixed-charge cover, current and quick
  ratios, and say what "normal" is by sector.
- Read a borrowings note: lenders, security, rates, maturity ladder, covenants, and estimate refinancing risk.
- Find the obligations that are *not* in the borrowings line — guarantees, supplier finance, bill discounting,
  channel financing, promoter-group guarantees, contingent liabilities — and add them back.
- Explain how credit ratings are built and how to use rating rationales as an equity analyst.
- Assess Kaveri Pumps' FY26 balance sheet and say precisely what would have to happen for it to become a problem.

**Prerequisites:** [02.4 The balance sheet](../02-accounting/04-the-balance-sheet.md),
[02.5 The cash-flow statement](../02-accounting/05-the-cash-flow-statement.md),
[04.4 Working capital & cash conversion](04-working-capital-and-cash-conversion.md)  ·  **Time:** ~90 min

---

## 1. Three layers: leverage, solvency, liquidity

| Layer | Question | Time horizon | Core ratios |
|:--|:--|:--|:--|
| **Leverage** (capital structure) | How much of the business is financed by debt rather than equity? | Structural | Debt/equity, net debt/EBITDA, debt/capital |
| **Solvency** (debt service) | Can operating profit and cash flow cover interest and principal through a cycle? | 1–5 years | Interest cover, DSCR, fixed-charge cover, CFO/debt |
| **Liquidity** (near-term cash) | Can the company pay what falls due in the next 12 months? | 0–12 months | Current ratio, quick ratio, cash + undrawn lines vs maturities, CP dependence |

A company can be highly levered but solvent and liquid (a regulated utility with 20-year debt), or modestly levered
but illiquid (a small manufacturer whose ₹50 Cr of working-capital lines are due for renewal next month and whose
bank is nervous). The layers must be read together.

## 2. Leverage ratios

**Debt/equity** = total borrowings ÷ shareholders' equity. Include lease liabilities (they are debt under Ind AS 116);
exclude trade payables (operating, not financing). Book equity can be distorted by past write-offs or revaluations,
so also look at debt ÷ (debt + equity) and, for listed companies, debt ÷ market capitalisation.

**Net debt** = borrowings + lease liabilities − cash − liquid investments. Net debt can be negative ("net cash").
Whether to net off cash depends on whether the cash is really available: cash in an overseas subsidiary with
repatriation tax, cash pledged as margin, or cash that exists only on the balance-sheet date (see
[09.4](../09-forensics/04-cash-flow-games.md)) should not be netted.

**Net debt/EBITDA** — the ratio lenders and rating agencies watch most. It answers "how many years of operating
cash profit would repay the debt?"

| Net debt / EBITDA | Reading (non-financial company) |
|:--|:--|
| < 1x | Conservative; balance sheet is not a constraint |
| 1–2x | Normal for stable industrials |
| 2–3x | Comfortable only for very stable cash flows (utilities, consumer staples, toll roads) |
| 3–4x | Stretched; typical of LBO-style or capex-heavy structures; rating pressure |
| > 4x | Distressed unless the business is exceptionally predictable |

For **Kaveri FY26**: borrowings 92.0 + 96.0 = ₹188.0 Cr; plus leases 18.2; less cash 32.5 and current investments
15.0 → net debt ₹158.7 Cr including leases (the running-example ratio table shows ₹140.5 Cr *excluding* leases; both
conventions exist — state which you use). Net debt/EBITDA = 158.7 / 181.9 = **0.87x** (0.77x ex-leases). Debt/equity
= 188.0 / 706.1 = **0.27x**. By any standard, lightly levered.

The trend matters more than the level:

| ₹ Cr | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| Borrowings (ex-leases) | 64.0 | 62.0 | 108.0 | 162.0 | 170.0 | 188.0 |
| of which current | 36.0 | 42.0 | 38.0 | 30.0 | 58.0 | 96.0 |
| Cash + current investments | 91.8 | 109.0 | 102.1 | 66.1 | 58.0 | 47.5 |
| Net debt (ex-leases) | (27.8) | (47.0) | 5.9 | 95.9 | 112.0 | 140.5 |
| Net debt / EBITDA | −0.3x | −0.5x | 0.0x | 0.6x | 0.7x | 0.8x |
| Debt / equity | 0.16x | 0.14x | 0.22x | 0.29x | 0.27x | 0.27x |

Kaveri went from ₹47 Cr net cash to ₹140 Cr net debt in four years. The FY23–24 step was the Hosur plant (term
loans — sensible, matched to a long-lived asset). The FY25–26 step is different: term loans are being *repaid*
(132 → 92) while **working-capital borrowings have tripled** (30 → 96) to fund receivables. Short-term debt funding
a receivables pile from state agencies is a classic mismatch and is the one leverage fact about Kaveri worth
remembering.

## 3. Solvency ratios

**Interest cover** = EBIT ÷ finance costs. Kaveri FY26: 134.1 / 17.0 = **7.9x**. Rules of thumb: > 5x comfortable;
3–5x adequate; < 3x lenders get involved in decisions; < 1.5x distress. Use EBIT, not EBITDA, for asset-heavy
companies (depreciation is a real future cash need); EBITDA/interest (10.7x) is what covenants usually specify.

**Debt service coverage ratio (DSCR)** — the lender's ratio. Cash available for debt service ÷ (interest + scheduled
principal repayments):

$$\text{DSCR} = \frac{\text{EBITDA} − \text{cash taxes}}{\text{Interest} + \text{principal due in the year}}$$

Kaveri FY26: (181.9 − 29.5) / (17.0 + 20.0 term-loan repayment) = 152.4 / 37.0 = **4.1x**. Project lenders want
≥ 1.2–1.5x; a corporate at 4x has ample headroom. If you include the ₹96 Cr of working-capital debt as "due"
(it is technically repayable on demand), DSCR falls to 152.4 / 133.0 = 1.15x — which is why working-capital lines
are excluded from DSCR by convention *as long as the bank keeps renewing them*.

**Fixed-charge coverage** extends DSCR to leases and other fixed commitments:
(EBITDA − taxes) ÷ (interest + principal + lease payments) = 152.4 / (37.0 + 5.9) = **3.6x**.

**CFO/total debt** = 65.1 / 188.0 = **35%** — the company could repay its debt from operating cash flow in about
three years. Rating agencies like this ratio because it uses real cash rather than EBITDA.

### 3.1 Stress test: what would make Kaveri's debt a problem?

Take FY26 and shock it: revenue −15%, EBITDA margin 10% (from 13.8%), and the two state agencies delay payment
another year so working-capital debt rises by ₹60 Cr.

```python
rev = 1318.0 * 0.85                    # 1120.3
ebitda = rev * 0.10                    # 112.0
debt = 188.0 + 60.0                    # 248.0
interest = 15.6 * (248.0 / 188.0) + 1.4   # scale interest with debt: 22.0
ebit = ebitda - 47.8                   # 64.2
print(round(ebitda,1), round(ebit / interest, 1), round((debt - 47.5) / ebitda, 2))
# 112.0  2.9x interest cover  1.79x net debt/EBITDA
```

Even in that scenario interest cover is ~2.9x and net debt/EBITDA under 2x — uncomfortable, covenant-testing, but
not distress. The balance sheet is not where Kaveri's risk lies; the *quality of the receivables* is. That is the
kind of conclusion leverage analysis should produce: not "safe/unsafe" but "here is the scenario that breaks it".

## 4. Liquidity ratios and the maturity ladder

**Current ratio** = current assets ÷ current liabilities. Kaveri FY26: (188.1 + 346.7 + 39.5 + 15.0 + 32.5) /
(96.0 + 143.4 + 65.9) = 621.8 / 305.3 = **2.04x**. **Quick ratio** removes inventory: 433.7 / 305.3 = **1.42x**.

Both look healthy — and both are almost useless on their own. Kaveri's current assets are 56% receivables, of which
₹62 Cr is more than six months overdue. A current ratio counts a doubtful state-government receivable at 100 paise.
Better liquidity questions:

1. **What falls due in the next 12 months, and what will pay for it?** From the borrowings note: current maturities
   of term loans (₹20 Cr), working-capital lines (₹96 Cr, renewable annually), lease payments (₹6 Cr). Against:
   cash 32.5, liquid funds 15.0, undrawn sanctioned limits (disclosed in the note — say ₹40 Cr), and expected CFO.
2. **Dependence on short-term markets.** Commercial paper (CP) and short-term loans must be rolled. In September
   2018, IL&FS's default froze the CP market and NBFCs that funded long loans with 90-day paper could not roll
   ([case I4](../13-case-studies/india/04-ilfs-dhfl-2018.md)). For non-financial companies the analogue is
   working-capital lines that a nervous bank can cut.
3. **Cash that is really there.** Compare average cash with interest income ([09.4](../09-forensics/04-cash-flow-games.md)):
   Kaveri's other income of ₹3.9 Cr on average cash + investments of ₹52.8 Cr is a 7.4% yield — consistent with
   liquid-fund returns. Good.

## 5. Reading the borrowings note

Every Indian annual report has a borrowings note with more information than most analysts use. Extract:

| Item | Where | Why it matters |
|:--|:--|:--|
| **Lender names and types** | Note; rating rationale | A syndicate of large banks is stable; reliance on a single NBFC or on unlisted NCDs placed with promoter-friendly funds is fragile |
| **Security** | Note ("secured by first charge on…") | What lenders take first in default; whether promoters have given personal guarantees (a sign lenders doubt the company's standalone credit) |
| **Interest rates** | Note (often a range) | Compare with the rating; a 12% rate on an "A"-rated company means the rating is stale or the disclosure incomplete |
| **Maturity ladder** | Note / Ind AS 107 liquidity table | The year-by-year repayment schedule; bunching in one year is refinancing risk |
| **Covenants** | Sometimes disclosed; often only "the company has complied with all covenants" | Typical: net debt/EBITDA < 3x, DSCR > 1.25x, D/E < 1.5x, minimum net worth. A breach lets lenders accelerate |
| **Foreign-currency debt** | Note | Unhedged USD debt on an INR-earning company adds an FX short; ask about hedges |
| **Default / delays** | Note; CARO annexure clause on repayment of dues | Any delay in repaying dues is a red flag lenders see before you do |

!!! info "India notes"
    - Schedule III requires disclosure of **current maturities of long-term debt** within current borrowings, so you
      can build the ladder.
    - The CARO 2020 auditor's annexure (see [03.2](../03-reading-filings/02-anatomy-of-an-annual-report.md)) asks the
      auditor to report whether short-term funds were used for long-term purposes and whether the company defaulted
      on any lender — read it every year.
    - Since FY22, companies must disclose whether **quarterly stock statements** filed with banks against
      working-capital limits agree with the books (Schedule III amendment). A mismatch means the company told its
      bank one inventory number and its shareholders another. Manpasand-style cases turned on this
      ([case I14](../13-case-studies/india/14-manpasand-vakrangee-small-cap-flags.md)).
    - **Promoter share pledges** are not company debt but are a leverage signal on the *owner*: a margin call forces
      selling. Kaveri's promoters pledged 6% of their holding in Nov-2025 for a real-estate venture — small, but new,
      and it is why the borrowings note and the SAST disclosures should be read together.

## 6. Off-balance-sheet and hidden obligations

Ind AS pulled leases onto the balance sheet, but plenty still lives outside the borrowings line:

| Obligation | Where to find it | How to treat it |
|:--|:--|:--|
| **Guarantees given** (bank guarantees for tenders/performance; corporate guarantees for subsidiaries or group companies) | Contingent-liabilities note; related-party note | Performance BGs are normal for tender businesses (Kaveri: ₹96 Cr, rising with solar); corporate guarantees for *group* companies are debt in disguise — add to net debt |
| **Contingent liabilities** (tax disputes, litigation) | Contingent-liabilities note | Probability-weight; a ₹38 Cr GST demand (Kaveri) against ₹90 Cr PAT is material — check the basis and precedent |
| **Supplier finance / reverse factoring** | Payables note (if disclosed); auditor's report; sudden rise in payable days | Bank pays suppliers early and the company pays the bank later: economically debt, presented as payables. Reclassify to debt if material (the Carillion lesson) |
| **Bill discounting / receivables factoring with recourse** | Borrowings note; receivables note | With recourse, the risk stays with the company — treat as debt |
| **Channel financing** (banks lend to dealers to buy the company's goods) | Rarely disclosed; ask on calls | Boosts sales and shrinks receivables; if the company guarantees dealer loans, it is debt |
| **Capital commitments** | Commitments note | Contracted capex not yet spent — future cash outflow |
| **Put options / earn-outs on acquisitions** | Business-combination notes | Future payments; often at fair value as a liability |
| **Group-level leverage** | Promoter-entity filings; rating rationales for group companies | Promoter debt serviced by dividends from the listed company pushes for payouts or related-party support |

The adjusted net debt for Kaveri, being conservative: 158.7 (incl. leases) + 0 (no group guarantees) + a
probability-weighted 50% of the GST dispute (19.0) = ~₹178 Cr → adjusted net debt/EBITDA ≈ 1.0x. Still fine —
but now you have a number you can defend.

## 7. Credit ratings and how to use rating rationales

Indian companies with bank loans above a threshold or listed debt must be rated by a SEBI-registered agency
(CRISIL, ICRA, CARE, India Ratings, Acuité, Brickwork, Infomerics). The rating scale for long-term instruments:

| Rating | Meaning | Typical net debt/EBITDA (indicative, sector-dependent) |
|:--|:--|:--|
| AAA | Highest safety | < 1x, or government-linked |
| AA | High safety | 1–2x |
| A | Adequate safety | 2–3x |
| BBB | Moderate safety — lowest investment grade | 3–4x |
| BB and below | Speculative | > 4x or weak liquidity |
| D | Default | — |

Rating **rationales** are free on the agencies' websites and are among the best documents an equity analyst can
read: they summarise the business, the debt structure, the liquidity position (cash, undrawn lines, upcoming
maturities), group linkages and — crucially — "**key rating sensitivities**": the numbers at which the agency would
upgrade or downgrade. Kaveri is "A / Stable"; a typical sensitivity would be "net debt/EBITDA sustained above 2.5x
or a further stretch in receivable days beyond 100". That is a lender's thesis-breaker, handed to you.

Two cautions. Ratings lag: IL&FS was AAA weeks before default, and DHFL was AAA in early 2019 and D by June.
And agencies are paid by issuers. Treat a rating as a summary of the *past* balance sheet and the rationale as a
list of things to monitor, never as a forecast.

!!! tip "Trader's lens"
    Equity in a levered company is a call option on the enterprise value with strike equal to the debt (Merton;
    [06.7](../06-valuation/07-other-valuation-methods.md)). Leverage ratios tell you the moneyness; the maturity
    ladder tells you the expiry. A company with net debt/EBITDA of 4x and a bullet maturity next year is a
    short-dated, near-the-money option — vega heaven if the cycle turns, zero if it doesn't. Vodafone Idea
    ([case I10](../13-case-studies/india/10-vodafone-idea-telecom-war.md)) is the extreme example: the equity
    traded like a long-dated OTM call on tariff hikes and government forbearance.

## 8. What "normal" looks like by sector

| Sector | Typical net debt/EBITDA | Why |
|:--|:--|:--|
| IT services, FMCG, consumer durables | Net cash | Asset-light, negative or low working capital |
| Pharma (domestic) | 0–1x | Cash generative; acquisitions push it up temporarily |
| Auto OEMs | 0–1x (industrial ops), ex-finance subsidiary | Finance arms carry 6–8x and must be looked at separately |
| Engineering / capital goods | 0–1.5x | Working-capital driven; BGs matter more than debt |
| Cement, steel, metals | 1–3x at mid-cycle; can spike to 5x+ at troughs | Capital-intensive, cyclical EBITDA |
| Real estate | 1–3x on EBITDA, but judge on debt/pre-sales and cash flows | Project-level, lumpy |
| Utilities, roads, airports | 3–6x | Regulated or contracted cash flows; long-dated debt |
| Telecom | 2–4x (AGR and spectrum dues make Vodafone Idea an outlier) | Capex heavy |
| Banks & NBFCs | Not applicable — use leverage (assets/equity), CRAR, ALM | Debt *is* the raw material ([07.1](../07-special-valuation/01-banks-and-nbfcs.md)) |

!!! warning "Common mistakes"
    - Reading a current ratio without looking at what the current assets are.
    - Netting off cash that is not really available (trapped, pledged, window-dressed).
    - Ignoring lease liabilities in one company and including them in another.
    - Treating working-capital lines as permanent (they are renewed annually at the bank's discretion).
    - Missing corporate guarantees to group companies — the classic Indian promoter-group leverage leak.
    - Using EBITDA/interest when EBIT/interest is the honest test for a capital-intensive company.
    - Taking a rating as forward-looking. Read the rationale's sensitivities and monitor them yourself.

## Key terms

| Term | Meaning |
|:--|:--|
| **Leverage** | The extent to which assets are financed by debt; debt/equity, net debt/EBITDA |
| **Solvency** | The ability to service debt (interest and principal) from earnings and cash flow over time |
| **Liquidity** | The ability to meet obligations falling due in the next 12 months |
| **Net debt** | Borrowings (+ leases) − cash − liquid investments |
| **Interest cover** | EBIT ÷ finance costs |
| **DSCR** | (EBITDA − cash taxes) ÷ (interest + scheduled principal); the lender's coverage ratio |
| **Fixed-charge cover** | Coverage extended to lease payments and other fixed commitments |
| **Current / quick ratio** | Current assets ÷ current liabilities; (current assets − inventory) ÷ current liabilities |
| **Maturity ladder** | Schedule of debt repayments by year; bunching = refinancing risk |
| **Covenant** | A contractual financial test in a loan agreement; breach allows lenders to demand repayment |
| **Commercial paper (CP)** | Unsecured short-term (up to one year) debt instrument that must be rolled over |
| **Supplier finance / reverse factoring** | Bank pays suppliers early on the company's behalf; debt presented as payables |
| **Contingent liability** | A possible obligation (tax dispute, litigation, guarantee) disclosed but not recorded |
| **Corporate guarantee** | The company's promise to pay another entity's debt if it defaults |
| **Credit rating / rationale** | An agency's opinion on default risk, and the document explaining it and its sensitivities |
| **Promoter pledge** | Promoter shares given as collateral for loans; a margin-call risk for the stock |

## Check your understanding

1. Compute Kaveri's FY26 net debt/EBITDA including leases and excluding leases, and explain why both appear in
   published sources.
<details><summary>Answer</summary>Including leases: (188.0 + 18.2 − 47.5) / 181.9 = 0.87x. Excluding: (188.0 − 47.5)
/ 181.9 = 0.77x. Pre-Ind AS 116 data and many screeners exclude leases; rating agencies and careful analysts include
them. State your convention and apply it to every company you compare.</details>

2. Why is Kaveri's shift from term loans to working-capital borrowings a bigger concern than the level of debt?
<details><summary>Answer</summary>Working-capital lines are short-term and renewable at the bank's discretion; they
are funding receivables from state agencies that are increasingly overdue. If the bank cuts limits (or if the
Schedule III stock-statement check shows disagreement), the mismatch surfaces as a liquidity crunch even though
leverage ratios look fine. Term loans funding a plant are matched in tenor.</details>

3. A company reports current ratio 2.5x and quick ratio 0.6x. What is its balance sheet made of, and is it liquid?
<details><summary>Answer</summary>Inventory is ~76% of current assets (quick removes it). Liquidity depends entirely
on how fast that inventory turns — fine for a jeweller with gold, dangerous for a fashion retailer with last
season's stock. Look at inventory days and ageing.</details>

4. Recompute Kaveri's DSCR if the working-capital lines are treated as due within the year. What does the result
   tell you?
<details><summary>Answer</summary>152.4 / (17.0 + 20.0 + 96.0) = 1.15x. It says Kaveri cannot repay its working-capital
lines from one year's cash flow — nobody can; the ratio shows how dependent the company is on the bank's willingness
to renew, which is the real liquidity risk.</details>

5. Where would you find, and how would you treat, a ₹200 Cr corporate guarantee given by a listed company for a
   promoter-group entity's loan?
<details><summary>Answer</summary>Contingent-liabilities note and related-party note (Ind AS 24). Treat as debt of the
listed company for leverage purposes (add to net debt) and as a governance red flag — shareholders' balance sheet
is being used to support the promoters' other businesses ([05.6](../05-business-analysis/06-corporate-governance-india.md)).</details>

6. A rating rationale says liquidity is "adequate: cash ₹80 Cr, undrawn lines ₹120 Cr, against repayments of ₹150 Cr
   in the next 12 months and expected CFO of ₹100 Cr". Is it?
<details><summary>Answer</summary>Sources 80 + 120 + 100 = 300 vs uses 150: yes, ~2x cover — but undrawn lines can
be withdrawn and CFO is a forecast. Check what CFO was last year and whether the undrawn lines are committed.
"Adequate" is the agency's lowest comfortable grade; "strong" would show cash alone covering maturities.</details>

## Go deeper

- CRISIL and ICRA rating rationales for any two companies in the same sector — compare the "key rating
  sensitivities" sections; this is the fastest way to learn what lenders watch.
- Ind AS 107 *Financial Instruments: Disclosures* — the liquidity-risk maturity table every company must publish.
- Frank Fabozzi (ed.), *The Handbook of Fixed Income Securities* — chapters on credit analysis, for the lender's
  viewpoint on the same statements.
- Case studies [G6 Lehman](../13-case-studies/global/06-lehman-2008.md), [I4 IL&FS/DHFL](../13-case-studies/india/04-ilfs-dhfl-2018.md)
  and [I11 Kingfisher & Jet](../13-case-studies/india/11-jet-kingfisher-airlines.md) — three ways leverage kills.

---
[← Previous: 04.4 Working capital & cash conversion](04-working-capital-and-cash-conversion.md) · [Module index](index.md) · [Next: 04.6 Per-share metrics & ratio dashboard →](06-per-share-metrics-and-ratio-dashboard.md)
