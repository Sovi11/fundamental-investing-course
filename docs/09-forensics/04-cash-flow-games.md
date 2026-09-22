# 09.4 · Cash-flow games

> **Why this matters:** "profit is an opinion, cash is a fact" is the analyst's comfort — and it is only mostly
> true. The cash-flow statement can be arranged: financing dressed as operations, operating outflows parked in
> investing, timing pulled across a year-end, and, in the worst cases, cash that simply is not there. The tests in
> this lesson — including the single most powerful one in Indian forensic history, the interest-income-on-cash
> check that would have caught Satyam — are how you make cash a fact again.

**Learning objectives** — after this lesson you can:

- Recognise the ways CFO is flattered: reclassification between CFO/CFI/CFF, supplier finance and receivables
  factoring, capitalisation, working-capital timing and one-offs.
- Apply the "cash-rich but borrowing" and implied-yield-on-cash tests.
- Check loans and advances, investments in obscure entities and capital advances for cash that has left.
- Compare standalone and consolidated cash and explain what a gap means.
- Run all of it on Kaveri and know what "clean" looks like.

**Prerequisites:** [02.5 The cash-flow statement](../02-accounting/05-the-cash-flow-statement.md),
[04.4 Working capital & cash conversion](../04-financial-analysis/04-working-capital-and-cash-conversion.md)  ·  **Time:** ~75 min

---

## 1. Moving flows between sections

CFO is the number investors treat as clean, so the games move outflows *out* of it and inflows *into* it.

| Game | Mechanism | Test |
|:--|:--|:--|
| **Capitalising operating costs** | Costs go to CFI (capex) instead of CFO | [09.3](03-expense-and-asset-red-flags.md); CFO − capex (FCF) is immune — always look at FCF, not CFO |
| **Interest classification** | Ind AS 7 allows interest paid in CFO *or* CFF; a company that switches from CFO to CFF lifts CFO | Read the policy; restate to one convention across companies and years (Kaveri: interest paid in CFF, interest received in CFI — disclosed) |
| **Tax classification** | Taxes on asset-sale gains put in CFI | Minor; check |
| **Customer advances and deposits** | Financing in substance (deposits from dealers) presented as operating | Look for "security deposits received" growing |
| **Sale-and-leaseback** | Sell an asset (CFI inflow), lease it back (lease payments in CFF under Ind AS 116) — EBITDA and CFO both improve | Note on leases; growth in ROU assets without new locations |
| **Discontinued operations** | Cash flows of a divested loss-maker excluded from "continuing" CFO | Reconcile total CFO |

## 2. Financing dressed as operating cash

| Game | Mechanism | Mark | Test |
|:--|:--|:--|:--|
| **Supplier finance / reverse factoring** | A bank pays suppliers early; the company pays the bank later; the obligation stays in *trade payables* and the extra credit period shows up as CFO | Payable days jump; "other financial liabilities" or a note on supply-chain finance | Payable days vs industry; auditor's report; ask on calls; since 2024, IAS 7/IFRS 7 amendments require disclosure abroad — Ind AS is following (verify) |
| **Receivables factoring with recourse** | Receivables sold to a bank for cash (CFO up); risk retained | DSO falls suddenly; "bills discounted" in contingent liabilities or borrowings | Check the borrowings note for discounted bills; contingent-liabilities note |
| **Securitisation (NBFCs)** | Loans sold; upfront gains booked; off-book AUM | Assignment income; AUM > loans on balance sheet | Separate on-book and off-book; who holds the credit risk |
| **Channel financing** | Bank lends to dealers; dealers pay the company promptly; the company guarantees | Low receivables; guarantees in contingent liabilities | Read guarantees given |
| **Stretching payables before year-end** | Delay supplier payments in the last week of March | Payables spike at year-end; CFO strong in Q4, weak in Q1 | Quarterly balance sheets (where available); payable days vs mid-year |

## 3. Cash that isn't there — the Satyam test

Satyam's balance sheet at 30-Sep-2008 showed ₹5,361 Cr of cash and bank balances; ₹5,040 Cr of it did not exist.
Nothing in the audit caught it (the bank confirmations were forged). One ratio would have: **interest income on
cash**. A company holding ₹5,000 Cr of deposits should earn ₹300–400 Cr a year at Indian rates; Satyam reported far
less. The test:

$$\text{Implied yield on cash} = \frac{\text{Interest / treasury income}}{\text{Average cash + bank balances + liquid investments}}$$

| Result | Reading |
|:--|:--|
| Within 1–2 pp of prevailing deposit/liquid-fund yields (5–7% in India, varying with the rate cycle) | Cash is real and invested |
| Far below (< 3% when rates are 6–7%) | Cash arrived only at year-end (window dressing), is trapped/restricted, is in non-interest accounts — or does not exist |
| Far above | Interest from something other than cash (loans to related parties booked as "interest income"; hidden lending) |

`fi.forensics.cash_yield_check(cash_and_investments_avg, other_income)`. **Kaveri FY26**: 3.9 ÷ ((58.0 + 47.5)/2)
= **7.4%** — consistent with liquid-fund returns. FY24: 8.2%; FY25: 7.3%. Clean.

The companion test — **cash-rich but borrowing**: a company with large cash *and* large debt *and* low interest
income is paying interest on money it claims not to need. Ask why. Legitimate answers exist (cash in a subsidiary
or overseas; debt at a subsidiary; a regulatory requirement; timing) and must be specific. "Treasury policy" is
not an answer. Kaveri holds ₹47 Cr of cash against ₹188 Cr of debt — small, and explained by working-capital lines
funding receivables while a liquidity buffer is kept. Reasonable.

## 4. Cash that left through the side door

| Channel | Where to look | Warning |
|:--|:--|:--|
| **Loans and advances to related parties / group entities** | Loans note; RPT note; CARO clause on loans to parties covered by s.185/186 | Any material amount; rolling over; interest below the company's cost of funds |
| **Inter-corporate deposits** | Investments/loans note | ICDs to unlisted entities |
| **Investments in obscure entities** | Investments note: unlisted equity, preference shares, debentures of private companies, "AIF units" | Growing; entities with no discernible business; valued at cost |
| **Capital advances** | Other non-current assets | Large, to unnamed vendors; not converting to assets |
| **Advances to suppliers** | Other current assets | Growing faster than purchases; related suppliers |
| **Security deposits given** | | Rent deposits to promoter-owned premises at above-market levels |
| **Subsidiary funding** | Standalone RPT note: loans, guarantees, investments in subsidiaries | Money flowing to loss-making subsidiaries year after year |

These are the channels through which Indian promoters have historically extracted cash while the consolidated
P&L looked healthy. The DHFL forensic audits and several 2019–24 SEBI orders describe the mechanics: loans to
shell companies that on-lend to promoter entities; investments in group vehicles written off years later.

## 5. Standalone vs consolidated cash

Read both. If consolidated cash is ₹500 Cr but standalone is ₹30 Cr, the cash is in subsidiaries — which may be
fine (an overseas arm) or not (a subsidiary the parent cannot access, or a subsidiary that is itself borrowing).
If standalone shows large loans to subsidiaries and consolidated shows those subsidiaries losing money, the
"consolidated cash" is being generated by the parent and consumed downstream. The standalone cash-flow statement
plus the RPT note answer the question the consolidated statement hides. Kaveri is a single entity in the running
example; for a real group this comparison is mandatory.

## 6. Working-capital timing and one-offs

CFO can be *legitimately* lumpy: a large collection on 1 April instead of 31 March moves ₹50 Cr of CFO across years.
Tests: three-year cumulative CFO vs three-year PAT + D&A; payable and receivable days at each quarter-end (where
disclosed); CFO before working-capital changes vs after. One-offs inside CFO: tax refunds, insurance receipts,
litigation settlements, government grants, advances received on a large order — read the operating section line
by line and remove them from the run-rate.

## 7. Kaveri — the cash-flow audit in one table

| Test | Result | Verdict |
|:--|:--|:--|
| Interest classification | Interest paid in CFF, received in CFI — disclosed and consistent | Restate to compare with peers that put both in CFO: Kaveri's "CFO" would be 65.1 + 3.9 − 17.0 = ₹52.0 Cr on that basis |
| CFO/EBITDA 3-year | (86.6 + 60.9 + 65.1)/(155.0 + 172.3 + 181.9) = 42% | Low; explained by receivables ([04.4](../04-financial-analysis/04-working-capital-and-cash-conversion.md)) |
| FCF (CFO − capex) 3-year | 212.6 − 261.0 = −₹48 Cr | Negative over the cycle that included the plant; ₹13 Cr in FY26 |
| Implied yield on cash | 7.4% | Clean |
| Cash-rich but borrowing | ₹47 Cr cash vs ₹188 Cr debt; WC lines fund receivables | Explained |
| Supplier finance / factoring | Payable days steady (61–66); no discounted bills disclosed | Clean |
| Loans/advances/investments to related parties | None | Clean |
| Capital advances / obscure investments | None (₹15 Cr liquid funds only) | Clean |
| Standalone vs consolidated | Single entity | n/a |
| One-offs in CFO | None; land sale correctly in CFI | Clean |

Kaveri's cash-flow statement is honest; its problem is *what the honest statement shows* — profit that is not
becoming cash because customers are not paying. That is a business problem, not an accounting one, and it is
the distinction this module exists to make.

!!! tip "Trader's lens"
    Cash is settlement. Every game in this lesson delays or fakes settlement while showing P&L. The
    interest-on-cash test is a margin-account check: a balance that earns nothing is a balance you should doubt.
    And the standalone-vs-consolidated comparison is a check on where the collateral actually sits — if the cash
    is in an entity you have no claim on, it is not your cash.

!!! info "India notes"
    - Indian companies must present the cash-flow statement under Ind AS 7 (indirect method almost universal);
      interest and dividend classification choices should be stated in the policies note — check they are
      consistent year to year.
    - CARO 2020 clauses iii (loans/advances/guarantees to parties), iv (compliance with s.185/186), and ix (use of
      funds; short-term funds used for long-term purposes) are the auditor's own cash-flow forensics — read them.
    - Bank confirmations in India are now largely electronic (the ICAI's standards were tightened after Satyam),
      but the interest-income test remains the outsider's check.

!!! warning "Common mistakes"
    - Comparing CFO across companies with different interest-classification policies.
    - Reading CFO without capex (FCF is the number capitalisation cannot flatter).
    - Ignoring a low yield on cash because "the cash is there on the balance sheet".
    - Accepting "group treasury" explanations for loans to related parties.
    - Reading only the consolidated statements for a group.

## Key terms

| Term | Meaning |
|:--|:--|
| **CFO / CFI / CFF** | Cash flow from operating / investing / financing activities |
| **Supplier finance (reverse factoring)** | Bank pays suppliers; the company repays the bank later; presented as payables |
| **Factoring with recourse** | Selling receivables for cash while retaining the credit risk |
| **Bills discounted** | Receivables (bills) financed by a bank; contingent liability if with recourse |
| **Channel financing** | Bank lending to dealers to buy the company's goods, often guaranteed by the company |
| **Sale-and-leaseback** | Selling an asset and leasing it back; converts an asset into lease cash flows |
| **Implied yield on cash** | Interest/treasury income ÷ average cash and liquid investments |
| **Window dressing** | Arranging year-end balances (cash, payables) to look better than the year's average |
| **Inter-corporate deposit (ICD)** | Loan between companies, often within a group |
| **Capital advance** | Payment to a vendor for a fixed asset not yet received |
| **Standalone vs consolidated** | Parent-only vs group statements; compare cash and related-party flows |

## Check your understanding

1. A company reports cash of ₹2,000 Cr, debt of ₹1,500 Cr, and other income of ₹40 Cr. Compute the implied yield
   and interpret.
<details><summary>Answer</summary>40 / ~2,000 = 2% (using closing; use average if available) vs 6–7% market
yields. Either the cash arrived at year-end, is restricted, or isn't real — and the company is paying interest on
₹1,500 Cr while "holding" cash earning 2%. Demand a specific explanation; treat as a red flag until given.</details>

2. Restate Kaveri's FY26 CFO to a convention where interest paid and received are both in CFO.
<details><summary>Answer</summary>65.1 + 3.9 (interest received, currently in CFI) − 17.0 (finance costs paid,
currently in CFF; lease interest 1.4 + debt interest 15.6) = ₹52.0 Cr.</details>

3. A retailer's payable days jump from 45 to 95 in one year while CFO doubles; the notes mention a "supply-chain
   financing programme". What is the economic reality?
<details><summary>Answer</summary>The company has borrowed from a bank (which paid its suppliers) and presented the
borrowing as trade credit; CFO's improvement is financing. Reclassify the extra ~50 days of payables to debt;
net debt/EBITDA rises accordingly (the Carillion lesson).</details>

4. Standalone cash ₹20 Cr; consolidated cash ₹600 Cr; standalone loans to subsidiaries ₹400 Cr; subsidiaries
   loss-making. What is happening?
<details><summary>Answer</summary>The parent generates cash and lends it to subsidiaries that burn it; the
consolidated cash may be in a subsidiary the parent cannot upstream, or may be transient. Value the group on the
subsidiaries' actual economics and treat the parent's loans as at risk.</details>

5. Which single line item would have exposed Satyam, and what did it show?
<details><summary>Answer</summary>Interest income relative to reported cash: ₹5,000+ Cr of bank balances should have
produced ₹300–400 Cr of interest a year; the reported figure was a small fraction, implying the cash did not exist
([case I1](../13-case-studies/india/01-satyam-2009.md) gives the actual numbers).</details>

## Go deeper

- Schilit, *Financial Shenanigans* — Part Three, "Cash Flow Shenanigans" (four techniques).
- Ind AS 7 *Statement of Cash Flows* — classification options; the 2024 IFRS amendments on supplier-finance
  disclosures (IAS 7/IFRS 7) and their Ind AS adoption status.
- SFIO/SEBI orders on DHFL and related NBFC cases (public) — the fund-diversion mechanics in India.
- [Case G9 Wirecard](../13-case-studies/global/09-wirecard-2020.md) — €1.9 bn of cash "in escrow" that did not exist.

---
[← Previous: 09.3 Expense & asset red flags](03-expense-and-asset-red-flags.md) · [Module index](index.md) · [Next: 09.5 Governance red flags in India →](05-governance-red-flags-india.md)
