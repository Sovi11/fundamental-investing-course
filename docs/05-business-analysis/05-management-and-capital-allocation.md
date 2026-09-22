# 05.5 · Management & capital allocation

> **Why this matters:** over a decade, the people running a company decide where every rupee of profit goes —
> back into the business, into acquisitions, to shareholders, or to the bank. Those choices, made with your money,
> compound. Two companies with identical businesses and different capital allocators end up worth very different
> amounts. Judging management is not about liking them on a conference call; it is about auditing what they did
> with the cash.

**Learning objectives** — after this lesson you can:

- Describe the five uses of cash and the test each one must pass.
- Judge a management team's capital-allocation record from the numbers: incremental ROIC, acquisition outcomes,
  dilution history, buyback and dividend timing.
- Read incentive structures (remuneration, ESOPs, promoter pay) and infer what behaviour they reward.
- Build and interpret a say-do tracker for guidance versus delivery.
- Recognise behavioural red flags and the difference between a promoter's interests and a minority shareholder's.
- Apply the framework to Kaveri Pumps' management.

**Prerequisites:** [04.3 Returns on capital](../04-financial-analysis/03-returns-on-capital.md),
[05.3 Moats & competitive advantage](03-moats-and-competitive-advantage.md)  ·  **Time:** ~90 min

---

## 1. The five uses of cash

Every rupee of operating cash flow has exactly five destinations. A capital allocator's job is to rank them by
return, every year, and act accordingly.

| Use | Creates value when | Destroys value when | How to check |
|:--|:--|:--|:--|
| **1. Reinvest in the existing business** (capex, working capital, R&D) | Incremental ROIC > WACC | Capacity added into a glut; working capital funding bad customers | Incremental ROIC over 3-year windows; utilisation of new capacity; receivable/inventory days after growth |
| **2. Acquire** | Price paid < value received *to this buyer* (synergies real, integration executed) | Paying for growth the market already prices; "diworsification"; goodwill later impaired | Post-deal ROIC on total consideration incl. debt assumed; goodwill impairments; revenue/margin of acquired unit vs deal-model claims |
| **3. Pay dividends** | No better internal use; stable, affordable payout | Paid from borrowings; paid while ROIC on reinvestment is high (leaving value on the table) | Payout ratio vs FCF; dividends vs net debt trend; promoter's dependence on dividends |
| **4. Buy back shares** | Shares trade below intrinsic value and cash is surplus | Bought at peak valuations; used to offset ESOP dilution while calling it "returning capital" | Buyback price vs subsequent prices and vs your valuation; net share count trend (buybacks minus issuance) |
| **5. Repay debt** | Leverage is above the prudent level for the business; cost of debt > return on alternatives | Company is under-levered and cash idles (or sits in low-yield treasury) | Net debt/EBITDA trend; cash as % of assets; other income yield |

The ranking is not fixed. A 30%-ROIC business with room to grow should reinvest everything; the same business
without room should return everything. The failure modes are the mismatches: reinvesting when returns have fallen
(most conglomerate expansions), or hoarding when returns are high but management is timid (a common Indian
MNC-subsidiary and IT-services pattern, at least until buybacks became routine).

## 2. Auditing the record

### 2.1 Reinvestment: incremental ROIC

From [04.3](../04-financial-analysis/03-returns-on-capital.md): Kaveri's FY24→FY26 incremental ROIC was 4.6% against a
12.2% WACC. That single number is a capital-allocation verdict: ₹196 Cr of shareholders' money was deployed at a
return below what a bank deposit would have earned after tax. Management's *stated* rationale (solar is a
"multi-year opportunity") may be right in the long run; the *record* so far is poor. Both facts belong in your
assessment, and the second is the one that gets ignored.

### 2.2 Acquisitions: the post-deal audit

For every acquisition over ~5% of market cap, build a one-line audit two to three years later:

| Deal | Year | Consideration (incl. debt assumed) | Acquired EBIT at deal | EBIT 3 years later | ROIC on consideration | Goodwill impaired? | Verdict |
|:--|:--|:--|:--|:--|:--|:--|:--|

If the company does not disclose the acquired unit's performance (most do not after year one), that silence is
itself data. Serial acquirers deserve particular scrutiny: the combination of rising goodwill, "adjusted" earnings
that exclude integration costs every year, and a rising share count is the Valeant pattern
([case G8](../13-case-studies/global/08-valeant-2015.md)). Tata Motors–JLR ([case I15](../13-case-studies/india/15-tata-motors-jlr.md))
shows the opposite: a deal that looked reckless in 2008 and earned extraordinary returns by 2014 — then gave much of
it back. Judge on the full cycle.

### 2.3 Dilution history

Pull the share count for ten years (Screener.in shows it; annual reports give the reconciliation). Growth in shares
outstanding is a cost to you exactly like a cash outflow:

$$\text{Per-share value growth} \approx \text{Value growth} − \text{Share-count growth}$$

Ask what each issuance bought. A QIP to fund a plant earning 20% is fine; a preferential allotment of warrants to
promoters at a discount ([05.6](06-corporate-governance-india.md)) or annual ESOP grants of 2–3% of shares to a
handful of executives is a transfer from you to them. Nirmal Finance's FY24 QIP (₹300 Cr, 10% dilution at ₹300 when
book value was ~₹85/share) was accretive — new money came in at 3.5x book to fund loans earning 15% on equity;
that is what good dilution looks like.

### 2.4 Buybacks and dividends: timing tells

List every buyback with its price, then overlay the subsequent price path. Managers who buy back at 40x earnings and
issue shares at 12x are transferring value the wrong way, whatever the press release says. Indian buybacks come in
two forms — **tender offer** (fixed price, often at a premium; small shareholders get a reserved 15% quota) and
**open market** — and since the 2024 tax change the proceeds are taxed as dividend income in the shareholder's hands
(verify the current rule in [11.5](../11-process/05-monitoring-and-selling.md)), which changed the calculus for
promoters and institutions.

Dividends: check they are paid from free cash flow, not from borrowings; watch for a payout that rises just as
the promoter's own leverage rises (pledges, group-company debt) — the dividend is then serving the promoter's
liquidity, not yours.

## 3. Incentives: what is management paid to do?

Charlie Munger's line — show me the incentive and I will show you the outcome — is the whole method. The
**remuneration section of the Board's report** and the **ESOP note** tell you what behaviour is rewarded.

| Incentive | Rewards | Typical distortion | What to look for |
|:--|:--|:--|:--|
| Salary + bonus on revenue/PAT growth | Size | Growth at any return; acquisitions; capex into gluts | Bonus metrics in the remuneration policy; whether ROCE or FCF appears at all |
| Bonus on EBITDA | Reported operating profit | Capitalising costs; lease accounting effects; ignoring capital | Whether "EBITDA" is defined and audited |
| ESOPs with low exercise prices, short vesting | Share-price rise over 1–3 years | Short-termism; timing of disclosures around vesting; "adjusted" metrics | Grant price vs market; vesting schedule; annual grant as % of shares; whether performance-linked |
| Performance shares on 3–5 year TSR/ROIC | Long-term value per share | Few; the best structure | Rare in India outside some MNC subsidiaries and new-age companies |
| Promoter remuneration as % of profit (Companies Act caps managerial pay at 11% of net profit for all directors, 5% for one MD, with shareholder approval for more) | — | Salary extracting value when dividends would be shared with minorities | Managerial remuneration ÷ PAT; median-employee ratio; increases vs performance |
| Related-party arrangements (royalties, rents, purchases) | The promoter's other entities | Value leakage | RPT note; [05.6](06-corporate-governance-india.md) |

**Skin in the game** cuts both ways. A promoter with 58% of a company (Kaveri) shares your economic outcome —
until their personal balance sheet (pledges for a real-estate venture) or their other businesses (Kaveri Castings)
give them interests you do not share. Professional CEOs with 0.01% holdings and large option grants have the
opposite profile: no downside, levered upside. Neither is automatically better; know which you own.

## 4. The say-do tracker

Nothing reveals management like comparing what they said with what happened. Build the table from concall
transcripts and investor presentations ([03.4](../03-reading-filings/04-quarterly-results-and-concalls.md)) — Kaveri,
from the running example:

| Date | What management said | What happened | Score |
|:--|:--|:--|:--|
| May-2025 (Q4 FY25 call) | "FY26 revenue growth 15–18%; EBITDA margin 15%+" | FY26: +12.5%; 13.8% | Miss on both |
| May-2025 | "Receivable days to normalise to 70–75 by FY26 end" | 96 days at Mar-26 | Miss, and worsening |
| May-2025 | "Capex ₹40–45 Cr" | ₹52 Cr (incl. intangibles) | Slight miss |
| Nov-2025 (Q2 FY26 call) | "Solar receivables fully recoverable; two states clearing dues in Q4" | >6-month overdue rose to ₹62 Cr at Mar-26 | Miss |
| May-2026 (Q4 FY26 call) | "FY27 growth 15–18%; margin 14–15%; receivables 75–80 days by FY27 end" | Q1 FY27: +3.5%, 12.6% margin; days not disclosed | Early miss; disclosure withdrawn |
| May-2026 | "Dividend payout ~25%; no large capex; open to motors acquisitions" | — | Watch |

Four consecutive misses on the same theme (receivables), a guidance range repeated unchanged after a miss, and a
KPI that stopped being disclosed when it worsened. Any one is noise; the pattern is a **credibility discount**: model
the low end of guidance or below, and weight the bear case more. Contrast a management that guided conservatively
and beat for eight quarters — the say-do ratio is a legitimate input to the probabilities you assign to scenarios.

!!! tip "Trader's lens"
    Guidance is a quote; delivery is the fill. A counterparty whose fills are consistently worse than their quotes
    gets a wider spread from you — so should a management team. Track the say-do ratio like slippage: per quarter,
    per metric, with a rolling average, and widen your valuation haircut when it deteriorates.

## 5. Reading management: tone, disclosure and behaviour

Beyond the numbers, the *quality of disclosure* is the most reliable soft signal:

| Good sign | Bad sign |
|:--|:--|
| Discusses mistakes and what changed (Buffett's letters as the standard) | Every miss has an external cause; every beat is execution |
| KPIs disclosed consistently, including when they worsen | KPIs redefined or dropped when inconvenient (Kaveri's receivable days) |
| Capital-allocation framework stated (hurdle rates, payout policy) and followed | "Opportunistic" acquisitions; payout policy silent |
| Answers the analyst's question, including "we don't know" | Long non-answers; "we don't give that number"; hostility to short sellers or critics |
| Management sells shares rarely and discloses why; buys in downturns | Promoter selling into strength ("for personal reasons"); pledging rising |
| Succession planned and visible | Founder in 70s, no CEO, children in unrelated roles |
| Related-party dealings shrinking as the company matures | RPTs growing faster than revenue (Kaveri Castings: 6.5% → 10.4% of materials in five years) |
| Auditor is a large firm, unchanged except by rotation | Small auditor for a large company; resignations; qualified opinions |

None of these is proof. Together they form a prior. The formal governance checklist is in
[05.6](06-corporate-governance-india.md).

## 6. Worked example — two allocators, same business

**Company A** and **Company B** (fictional) both start FY17 with ₹1,000 Cr of invested capital earning 20% ROIC
(NOPAT ₹200 Cr), no debt, 10 Cr shares, WACC 12%. Over ten years:

- **A** reinvests 50% of NOPAT in the core at 20%, pays the rest as dividends, never acquires, never issues shares.
- **B** reinvests 50% in the core at 20%, and *also* borrows to make one acquisition every two years at 25x EBIT
  (4% pre-tax yield), funding half with new shares at 20x earnings.

```python
def run_A(years=10):
    ic, shares, divs = 1000.0, 10.0, 0.0
    for _ in range(years):
        nopat = ic * 0.20; reinvest = 0.5 * nopat; divs += nopat - reinvest; ic += reinvest
    return ic, ic * 0.20, shares, divs
ic, nopat, sh, divs = run_A()
print(round(ic), round(nopat), round(nopat / sh, 1), round(divs))
# 2594  519  NOPAT/share 51.9  cumulative dividends 1594
```

A ends FY26 with NOPAT of ₹519 Cr (10% CAGR from ₹200 Cr — exactly reinvestment 50% × ROIC 20%) on 10 Cr shares,
having paid ₹1,594 Cr in dividends. B's acquisitions at a 3% after-tax yield with a 12% WACC each destroy value on
day one; its reported NOPAT grows *faster* than A's (it is buying earnings), its share count rises ~25%, and its
NOPAT per share ends up lower than A's while its balance sheet carries goodwill and debt. Every conference call
B's management will talk about "scale" and "platform"; A's will talk about return on capital. The market may
even reward B for a few years. Over ten, it never does.

## 7. Kaveri's management: the assessment

| Dimension | Evidence | Assessment |
|:--|:--|:--|
| Reinvestment returns | Incremental ROIC 4.6% (FY24–26); Hosur plant at 57% utilisation | Weak recent record; plant may yet pay off |
| Acquisitions | None; "open to motors acquisitions" | Unproven; the statement plus a pledge and weak FCF is a caution |
| Dilution | ESOPs 6.00 → 6.07 Cr diluted (1.2% over 3 years) | Modest |
| Dividends | Payout ~25%, rising DPS, paid from CFO | Sensible |
| Debt | Term loans being repaid; WC lines rising | Mixed — the WC funding of receivables is the issue |
| Incentives | Promoter family runs it; ESOPs granted FY24; remuneration not in the running example — read the Board's report | — |
| Say-do | Four misses on receivables; guidance unchanged; KPI withdrawn | Credibility discount warranted |
| Behaviour | New pledge; RPT purchases rising | Two yellow flags |

Conclusion for the memo: competent operators of a decent business whose capital allocation has deteriorated as they
chased solar growth, and whose disclosure quality declined when the numbers did. Not disqualifying; not a management
to pay a premium for.

!!! info "India notes"
    - Managerial remuneration limits: Sections 197–198 of the Companies Act, 2013 cap total pay to directors at 11%
      of net profit (5% for a single managing director; 10% for all executive directors) unless shareholders approve
      more by special resolution; loss-making companies are limited to Schedule V slabs. The Board's report must
      disclose each director's pay, the ratio to the median employee's, and percentage increases.
    - ESOP disclosures under SEBI's SBEB Regulations, 2021 give grant prices, vesting, and dilution — read the note.
    - Dividend-distribution policies are mandatory for the top 1,000 listed companies (LODR Reg 43A; verify the
      current threshold) — compare the policy with the practice.

!!! warning "Common mistakes"
    - Judging management on charisma, education or the smoothness of the call.
    - Crediting management for industry tailwinds (cement in an up-cycle) or blaming them for headwinds.
    - Ignoring dilution because it does not appear as an expense.
    - Treating buybacks as automatically shareholder-friendly regardless of price.
    - Forgetting that a promoter's interests diverge from yours precisely when their other businesses need money.
    - Not tracking guidance — the single cheapest, most predictive discipline in this module.

## Key terms

| Term | Meaning |
|:--|:--|
| **Capital allocation** | The deployment of a company's cash among reinvestment, acquisitions, dividends, buybacks and debt repayment |
| **Incremental ROIC** | Return earned on new capital deployed over a period |
| **Goodwill** | Excess of acquisition price over the fair value of net assets acquired; impaired when the deal disappoints |
| **Dilution** | Increase in shares outstanding, reducing each share's claim |
| **QIP / preferential allotment / warrants** | Equity issuance to institutions / to chosen investors (often promoters) / rights to buy shares later at a fixed price |
| **Tender-offer buyback** | Buyback at a fixed price with proportional acceptance; 15% reserved for small shareholders |
| **Payout ratio** | Dividends ÷ PAT (or ÷ FCF) |
| **Say-do ratio** | Frequency with which management's stated guidance is delivered |
| **Skin in the game** | Management's own economic exposure to the company's outcome |
| **ESOP** | Employee stock option plan; a call option granted to employees, expensed under Ind AS 102 |
| **Managerial remuneration cap** | Companies Act limits on directors' pay as a percentage of net profit |
| **Credibility discount** | A valuation haircut applied when management's guidance has been unreliable |

## Check your understanding

1. A company with ROIC of 25% and ample reinvestment opportunities pays out 60% of profit as dividends. Is this
   good capital allocation?
<details><summary>Answer</summary>Probably not: each rupee reinvested at 25% is worth more than a rupee paid out
(shareholders cannot reinvest at 25% after tax). Unless the "opportunities" are illusory or the company is
constrained, a high payout at high ROIC leaves value on the table — though it may signal a promoter's own need for
cash.</details>

2. Compute Company A's NOPAT per share after ten years if it had instead issued 2 Cr shares in year 1 to make an
   acquisition earning ₹40 Cr of NOPAT on ₹1,000 Cr of consideration, with no other change.
<details><summary>Answer</summary>Core NOPAT still ₹519 Cr; acquired NOPAT ₹40 Cr (no growth assumed); total ₹559 Cr
on 12 Cr shares = ₹46.6/share vs ₹51.9 without the deal — a 10% worse outcome despite higher total profit, because
the acquisition earned 4% on capital costing 12%.</details>

3. Management's bonus is 100% linked to revenue growth. Name three decisions this incentive predicts.
<details><summary>Answer</summary>Expansion into low-margin segments or geographies; acquisitions regardless of
price; loosening credit terms (receivables growth) or channel stuffing to pull sales forward. Kaveri's solar push,
with its tender pricing and long receivables, is exactly what a growth-linked incentive would produce.</details>

4. What does it tell you when a company stops disclosing a KPI it previously reported every quarter?
<details><summary>Answer</summary>Almost always that the KPI has deteriorated; withdrawal of disclosure is itself
information (Kaveri's receivable days in Q1 FY27). Model the KPI at the bad end and ask on the call.</details>

5. Why might a promoter with 58% ownership still make decisions against minority shareholders' interests?
<details><summary>Answer</summary>Because the promoter has other economic interests the minorities do not: a
supplier company they own 100% of (Kaveri Castings — every rupee of margin there is theirs alone vs 58% at Kaveri),
personal borrowings secured by pledged shares that create pressure for dividends or a supported share price, and
family employment. Alignment on the listed company's equity is partial, not total.</details>

6. A company announces a ₹500 Cr buyback at ₹1,200 when your DCF says the shares are worth ₹800. What is the
   effect on remaining shareholders?
<details><summary>Answer</summary>Value is transferred *to* the tendering shareholders *from* those who remain:
paying ₹1,200 for something worth ₹800 destroys ₹400 per share bought — roughly ₹167 Cr of value on 41.7 lakh shares.
Buybacks create value only below intrinsic value.</details>

## Go deeper

- William Thorndike, *The Outsiders* (2012) — eight CEOs judged purely on capital allocation; the book that made
  the topic mainstream.
- Warren Buffett, Berkshire Hathaway letters — 1984 (dividends), 1999 and 2011 (buybacks), any year's discussion of
  acquisitions; the *Owner's Manual* on the "one-dollar test" (each rupee retained should create at least a rupee
  of market value).
- Michael Mauboussin & Dan Callahan, *Capital Allocation: Evidence, Analytical Methods, and Assessment Guidance*
  (Credit Suisse, 2014) — the analytical framework behind Section 2.
- Any ten years of a company's concall transcripts read in one sitting — the fastest way to build a say-do table.

---
[← Previous: 05.4 The capital cycle](04-capital-cycle-and-competition.md) · [Module index](index.md) · [Next: 05.6 Corporate governance — the India edition →](06-corporate-governance-india.md)
