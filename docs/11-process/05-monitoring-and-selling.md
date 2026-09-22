# 11.5 · Monitoring & selling

> **Why this matters:** buying gets all the attention; selling makes most of the difference. The three ways to
> lose money after a good purchase are to hold through a broken thesis, to sell a winner because it went up, and
> to average into a loser because it went down. A monitoring routine tied to the memo's thesis-breakers, and
> pre-written sell rules, are the defence. This lesson also covers the Indian tax rules that shape when you
> sell — verified as of September 2026.

**Learning objectives** — after this lesson you can:

- Run a quarterly thesis review against the memo's KPIs and thesis-breakers in an hour.
- Apply the four sell reasons (thesis broken, valuation full, better opportunity, position too large) and
  distinguish them from noise.
- Decide between averaging down and catching a knife using the thesis, not the price.
- State the current Indian tax treatment of equity gains (STCG, LTCG, STT), the ₹1.25 lakh exemption, and use
  tax-loss harvesting correctly.

**Prerequisites:** [11.3 Writing an investment memo](03-writing-an-investment-memo.md),
[06.8 Margin of safety](../06-valuation/08-margin-of-safety-and-expected-value.md)  ·  **Time:** ~60 min

---

## 1. The quarterly review

After each result (Kaveri: May, Aug, Nov, Feb), fill the update template (casebook `03-quarterly-update.md`):

| Section | Content | Time |
|:--|:--|:--|
| Results vs expectations | Revenue, margin, PAT, and the memo's 3–5 KPIs: expected vs actual, with the delta | 15 min |
| Concall | Guidance changes; say-do row added; questions dodged; new disclosures or withdrawals | 20 min |
| Thesis-breaker check | Each breaker: green / amber / red, with the evidence | 10 min |
| Valuation now | Price vs bear/base/weighted/bull; what the price now implies; whether scenario probabilities should move | 10 min |
| Action | Hold / add / trim / exit, with the reason in two lines; journal entry if not "hold" | 5 min |

Rules: review *every* holding every quarter, including the ones going well; update the say-do table before
reading the stock price reaction; change probabilities only for evidence, not for price moves; and record the
"no action" decisions — they are decisions.

Kaveri's monitoring list from the [memo](03-writing-an-investment-memo.md): segment revenue, EBITDA margin,
receivable days (half-yearly balance sheet; ask on the call if the KPI stays withdrawn), provisioning, Hosur
utilisation, pledge (SAST filings — continuous), RPT share (annual), auditor's report (annual).

## 2. When to sell

| Reason | Test | Typical error |
|:--|:--|:--|
| **1. Thesis broken** | A thesis-breaker fired, or the variant perception is refuted by evidence (not by price) | Waiting "for a bounce"; redefining the thesis to fit the new facts |
| **2. Valuation full** | Price at or above the bull case, or the price-implied expectations are ones you would not underwrite; the expected return from here is below your hurdle | Selling at the base-case value out of habit (leaving the bull case); or never selling because "it's a compounder" |
| **3. Better opportunity** | Another idea offers materially higher expected return per unit of risk, and capital is the constraint | Churning for small differences; ignoring taxes and impact costs |
| **4. Position too large** | The position has grown beyond the size the current risk justifies (a winner now 15% of the portfolio with a wider distribution than at entry) | Letting winners run without re-underwriting; trimming purely on a percentage rule |

Not reasons to sell: the price fell; the price rose; someone on television said so; a quarter missed with the
thesis intact; you are bored. Not reasons to hold: it is below your cost (cost is irrelevant to value); "it will
come back"; taxes (a reason to *time* a sale, rarely to avoid one).

Selling is re-underwriting: the question is always "would I buy this today at this price with what I now know?"
If no, and the answer is not "hold for a specific dated catalyst", sell.

## 3. Averaging down vs catching knives

The price fell 30%. Add, hold or sell? The price contains no information about which; the *reason* does.

| If the fall is because… | And your check shows… | Action |
|:--|:--|:--|
| Market/sector sell-off; thesis untouched | KPIs on track; no breaker fired | Add — the margin of safety just widened |
| A quarter missed on something the thesis anticipated (timing) | KPIs within the bear-case range but improving | Hold; add only if the price is below the bear-adjusted entry |
| A quarter missed on the *thesis variable* (Kaveri: receivable days up again) | Breaker amber; probabilities shift toward bear | Hold, do not add; re-run the weighted value; sell if the new weighted value is below price |
| A thesis-breaker fired (auditor qualification; pledge invocation; regulatory action) | Red | Sell — the distribution has changed, and averaging into a broken thesis is how small losses become total ones |
| You cannot tell why | — | Do the work before any action; if it cannot be done within the review, reduce |

The asymmetry: a stock down 50% needs +100% to recover; the base rate for "broken thesis" stocks recovering is
poor; the base rate for "sector sell-off with thesis intact" recovering is good. Averaging down is only ever
justified by the second kind, and the way to know which kind you have is the memo.

## 4. Trimming and rebalancing

A winner that has doubled is a different position: larger weight, higher price, narrower margin, often a wider
distribution (more of the value is now in the bull case). Re-underwrite: compute the expected return and
asymmetry from the *current* price ([06.8 §3](../06-valuation/08-margin-of-safety-and-expected-value.md)) and size
to that — which usually means trimming to the position size the new asymmetry justifies, not selling out. Set the
rule in advance (e.g., re-size whenever a position exceeds 1.5× its target weight) so that the decision is not made
under the glow of a gain. Taxes and impact costs are inputs to the timing, not to the decision.

## 5. Indian taxation of equity gains (as of September 2026)

| Item | Rule | Notes |
|:--|:--|:--|
| **Short-term capital gains** (listed equity/equity MFs held ≤ 12 months, STT paid) | **20%** (plus surcharge and cess) | Raised from 15% in the July 2024 Budget ([Business Standard](https://www.business-standard.com/amp/budget/news/budget-2024-fm-hikes-taxes-on-equity-trading-stcg-ltcg-stt-raised-124072301237_1.html)) |
| **Long-term capital gains** (held > 12 months, STT paid) | **12.5%** on gains above **₹1.25 lakh** per financial year | Raised from 10% / ₹1 lakh in July 2024; no indexation for listed equity ([Income Tax Dept](https://www.incometaxindia.gov.in/w/capital-gain); [Bajaj Finserv summary](https://www.bajajfinserv.in/investments/understanding-long-term-capital-gains-tax)) |
| **Grandfathering** | For shares bought before 1-Feb-2018, cost is the higher of actual cost or the 31-Jan-2018 price | A legacy of the 2018 reintroduction of LTCG |
| **Securities transaction tax (STT)** | On delivery equity: 0.1% on both buy and sell; on F&O: rates raised in 2024 (verify current) | Not creditable against capital-gains tax; deductible for business income |
| **Dividends** | Taxed at slab rates in the shareholder's hands (since FY21); TDS at 10% above ₹10,000 (verify threshold) | Buyback proceeds also taxed as dividend income in the shareholder's hands since Oct-2024 (verify) |
| **Set-off and carry-forward** | Short-term losses set off against STCG and LTCG; long-term losses only against LTCG; unabsorbed losses carried forward 8 years (return filed on time) | The basis for tax-loss harvesting |
| **F&O income** | Non-speculative **business income**, taxed at slab rates; expenses deductible; audit thresholds apply | Separate from capital gains ([11.7](07-fundamentals-meets-derivatives.md)) |
| **Income-tax Act, 2025** | In force from 1-Apr-2026; replaces the 1961 Act with renumbered sections and "tax year" terminology; **rates unchanged** for FY27 ([Bajaj Finserv](https://www.bajajfinserv.in/investments/understanding-long-term-capital-gains-tax)) | Verify section references when reading tax material |

Verify all of the above against the Income Tax Department's site and the current Finance Act before acting;
rates changed in 2018, 2024 and could change again.

Practical consequences:

- **The 12-month line matters**: a sale at 11 months pays 20%; at 13 months, 12.5% — a 37.5% lower rate on the
  same gain. If a sell decision is made near the boundary and the thesis is not broken, waiting can be worth it;
  if the thesis is broken, the tax saving is rarely worth the risk.
- **Tax-loss harvesting**: realise losses to offset gains in the same year (short-term losses are the most
  flexible); the ₹1.25 lakh LTCG exemption can be "used" each year by realising gains up to it. Do not let
  harvesting drive the investment decision — buying back a stock you would not otherwise own is a cost, not a
  saving.
- **Trading vs investing**: frequent buying and selling can lead the tax authorities to treat gains as business
  income; a long-term investor with a documented process is on firm ground.

## 6. The exit journal and post-mortem

Every sell (and every decision not to sell after a breaker fires) gets a journal entry; every closed position gets
a post-mortem (casebook `05-post-mortem.md`): what was expected vs what happened; which scenario played out;
process vs luck; what was knowable; one process change. Post-mortems on *winners* are as important as on losers —
a winner for the wrong reason is a process failure that got paid.

!!! tip "Trader's lens"
    Thesis-breakers are stops on facts, not on price. A trader's stop is a price because the position's edge is
    priced; an investor's stop is an event because the edge is a belief about the business. The discipline is the
    same — set it before entry, honour it without renegotiation — and so is the failure mode: moving the stop to
    avoid taking the loss.

!!! info "India notes"
    - Half-yearly balance sheets (LODR Reg 33) mean receivable-days monitoring is semi-annual unless management
      discloses quarterly; ask on the call.
    - SAST pledge filings and PIT insider-trade disclosures are continuous — set exchange alerts for holdings.
    - Tax: capital gains are computed per transaction using FIFO within a demat account for identical shares;
      brokers' capital-gains statements are the practical record.

!!! warning "Common mistakes"
    - Selling on price moves rather than on the memo.
    - Holding a broken thesis because of cost basis or taxes.
    - Averaging down without re-running the valuation and the breakers.
    - Never trimming winners and letting one name become the portfolio.
    - Letting tax-loss harvesting drive stock selection.
    - No post-mortems on winners.

## Key terms

| Term | Meaning |
|:--|:--|
| **Quarterly review** | The structured update of the thesis after each result |
| **Say-do table** | Guidance vs delivery record |
| **Thesis-breaker** | Pre-set observable outcome that triggers exit |
| **Re-underwriting** | Deciding whether you would buy the position today at this price with current knowledge |
| **Averaging down** | Buying more after a fall — justified only with the thesis intact |
| **STCG / LTCG** | Short-/long-term capital gains: ≤ 12 / > 12 months for listed equity |
| **STT** | Securities transaction tax |
| **Grandfathering** | Cost step-up to the 31-Jan-2018 price for pre-2018 holdings |
| **Tax-loss harvesting** | Realising losses to offset taxable gains |
| **Post-mortem** | Structured review of a closed position: expectations, outcome, process, lessons |

## Check your understanding

1. Kaveri's Q2 FY27 results show revenue +9%, margin 13.2%, and the H1 balance sheet shows receivable days of 101.
   You hold a 4% position bought at ₹260. What is the review outcome?
<details><summary>Answer</summary>Breaker 1 (receivable days < 80) is red; growth below the base path; margin
below. Probabilities shift toward bear (say 40/45/15 → weighted ≈ ₹274). At a price near ₹260 the position is
around fair value with a worsening distribution: hold, do not add; if a further quarter confirms, exit. The
decision is on the KPI, not the price.</details>

2. A holding is up 120% in 14 months and is now 12% of the portfolio; your updated bull case is 10% above the
   price. Action?
<details><summary>Answer</summary>Re-underwrite from the current price: expected return is low and asymmetry poor;
the position has grown past its risk-justified size. Trim to the size the new distribution supports (likely 3–5%)
— the gain is long-term (12.5%), so tax is not a reason to delay.</details>

3. Compute the tax on a ₹4 lakh LTCG and a ₹2 lakh STCG in the same year (ignore surcharge/cess).
<details><summary>Answer</summary>LTCG: (4.00 − 1.25) × 12.5% = ₹34,375. STCG: 2.00 × 20% = ₹40,000. Total ₹74,375.
Short-term losses, if any, would offset the STCG first.</details>

4. Why is "it's below my cost" not a reason to hold?
<details><summary>Answer</summary>Cost is a sunk fact about the past; value and expected return depend only on
the future cash flows and the current price. The only question is whether the position would be bought today; the
cost basis matters solely for tax timing.</details>

## Go deeper

- Income Tax Department, *Capital Gains* and *Tax on short-term capital gains* pages
  ([incometaxindia.gov.in](https://www.incometaxindia.gov.in/w/capital-gain)) — the primary source; re-read each
  budget.
- Howard Marks, "Selling Out" (Oaktree memo, 2022) — the four reasons and the non-reasons.
- Daniel Kahneman, *Thinking, Fast and Slow* — the disposition effect and sunk costs ([11.6](06-behavioural-finance-and-decision-journals.md)).
- The casebook's `03-quarterly-update.md` and `05-post-mortem.md` templates.

---
[← Previous: 11.4 Position sizing & portfolio construction](04-position-sizing-and-portfolio-construction.md) · [Module index](index.md) · [Next: 11.6 Behavioural finance & decision journals →](06-behavioural-finance-and-decision-journals.md)
