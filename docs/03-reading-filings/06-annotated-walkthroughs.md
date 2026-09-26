# 03.6 · Annotated walkthroughs: practise reading

> **Why this matters:** knowing what an MD&A, an auditor's report or a rating rationale *should* contain is not the same
> as noticing what a particular one is telling you. This lesson is practice. Five realistic excerpts — all fictional,
> all consistent with the course's running examples — each contain a mixture of green flags and red flags. You annotate
> first, then compare with the model annotations. By the end you should be reading filings the way a trader reads a
> tape: fast, and alert to the one line that does not fit.

**Learning objectives** — after this lesson you can:

- Annotate an MD&A excerpt, separating facts from framing and reconciling claims to the numbers.
- Read an auditor's report with a Key Audit Matter and an Emphasis of Matter, and say what each implies for your
  analysis.
- Spot the questions a related-party note raises and quantify the exposure.
- Decode management's answers on an earnings call and turn them into dated, checkable commitments.
- Summarise a lender's rating rationale in five lines, including its liquidity and sensitivities.

**Prerequisites:** [03.2 Anatomy of an annual report](02-anatomy-of-an-annual-report.md),
[03.3 Notes to accounts](03-notes-to-accounts.md), [03.4 Quarterly results & concalls](04-quarterly-results-and-concalls.md),
[03.5 Rating rationales & other documents](05-other-documents.md)  ·  **Time:** ~90 min

---

## How to use this lesson

For each excerpt:

1. **Read it once, fast**, as you would on the day it was published.
2. **Annotate** on paper or in a file: mark each claim **F** (fact you can verify), **J** (management judgement or
   framing), **G** (green flag) or **R** (red flag); write the number you would check and where you would check it.
3. **Reconcile** every figure you can against the running-example pages
   ([Kaveri](../appendix/running-example/kaveri-pumps.md), [Nirmal](../appendix/running-example/nirmal-finance.md)).
4. **Only then** open the model annotations. Score yourself: you are doing well if you found at least 80% of the red
   flags and did not invent any that are not there.

!!! warning "All excerpts are fictional"
    Kaveri Pumps & Motors and Nirmal Finance are invented companies. The excerpts below are written for this course
    and use the running examples' numbers exactly; new details (quotes, procedures, a confirmation response rate, an
    advance) are fictional additions that do not contradict the reference pages.

---

## Excerpt 1 — Kaveri Pumps, FY26 Management Discussion & Analysis

!!! quote "Kaveri Pumps & Motors Ltd — Annual Report FY26, MD&A (extract, fictional)"
    **Performance overview.** FY26 was another year of profitable growth for your Company. Revenue from operations rose
    **12.5% to ₹1,318.0 crore**, led by our **Solar Pumping Systems** business, which grew **38%** to ₹355.9 crore and now
    contributes 27% of revenue. Industrial Pumps & Motors grew 8.4% as the Hosur motor plant ramped up (utilisation
    57%, from 48%). Agricultural & Domestic Pumps grew 3.4% in a year of an uneven monsoon.

    EBITDA was **₹181.9 crore**, a margin of **13.8%**, as we absorbed higher commodity costs and invested in our
    solar channel. Profit after tax was ₹90.5 crore. The Board has recommended a dividend in line with our policy.

    **Working capital.** Trade receivables were elevated at year-end on account of **timing differences** in payments
    from certain State nodal agencies under the PM-KUSUM scheme. These dues are backed by Government programmes and
    are **fully recoverable**. We continue to manage working capital prudently.

    **Outlook.** With an unexecuted solar order book of ₹410 crore, a strong dealer network and new capacity in place,
    we are confident of **sustaining healthy growth**. Your Company remains focused on value creation for all
    stakeholders.

<details markdown="1"><summary>Model annotations — try your own first</summary>

| Line | Mark | Annotation |
|:--|:-:|:--|
| Revenue +12.5% to ₹1,318.0 Cr | F | Ties to the income statement. Note it is *below* the 15%+ the company had been delivering (FY25: +16.5%) |
| Solar +38% to ₹355.9 Cr, 27% of revenue | F / R | Ties to segment data. Solar supplied **67% of the year's revenue growth** (₹98.1 Cr of ₹146 Cr). Growth is increasingly concentrated in a single segment whose customers are state agencies |
| Industrial +8.4%, Hosur 57% utilisation | F / G | A genuine operating improvement; the motor plant built in FY24 is being absorbed |
| Agri +3.4%, "uneven monsoon" | F / J | The core business is barely growing; the monsoon explanation is plausible but unverified |
| EBITDA 13.8%, "absorbed commodity costs and invested in our solar channel" | F / J | Margin fell from 14.7% (FY25) and 15.4% (FY24). The explanation names two causes but quantifies neither |
| "Timing differences … fully recoverable" | **R** | The key sentence. Receivables rose from ₹269.7 to **₹346.7 Cr**; receivable days from 84 to **96**; overdue >6 months doubled to **₹62.4 Cr**. "Timing" is a claim, not a fact — the notes show the dues are getting *older*. "Fully recoverable" is contradicted by the need for an ECL allowance at all |
| "Manage working capital prudently" | **R** | CFO was ₹65.1 Cr against EBITDA of ₹181.9 Cr (**35.8%**). Working-capital borrowings rose ₹38 Cr. The sentence is contradicted by the cash-flow statement |
| Order book ₹410 Cr | F / R | Up from ₹290 Cr — a green flag for revenue, but more state orders mean more receivables and more bank guarantees (₹96 Cr, up from ₹58 Cr) |
| "Sustaining healthy growth" | J | No number. Contrast with the 15–18% guided on the Q4 call (Excerpt 4) — the written MD&A is more cautious than the spoken guidance |
| What is missing | **R** | No mention of the ₹38 Cr GST demand, the related-party purchases rising to 10.4% of material cost, or the promoter pledge created in November 2025 |

**Five-line summary:** growth is slowing and increasingly depends on solar sales to state agencies; margins are
falling; the cash conversion problem is real and getting worse; management's language ("timing", "fully
recoverable", "prudently") is contradicted by the notes and the cash-flow statement; material items are omitted.

</details>

---

## Excerpt 2 — Kaveri Pumps, Independent Auditor's Report (FY26)

!!! quote "Independent Auditor's Report to the Members of Kaveri Pumps & Motors Ltd (extract, fictional)"
    **Opinion.** We have audited the consolidated financial statements… In our opinion… the consolidated financial
    statements give a **true and fair view**… of the state of affairs of the Group as at 31 March 2026, of its profit…

    **Emphasis of Matter.** We draw attention to Note 38 to the financial statements, which describes a demand of
    **₹38.0 crore** raised by the GST authorities relating to the classification of solar pumping systems, against which
    the Company has filed an appeal. Based on legal advice, management believes the demand is not sustainable and has
    disclosed it as a contingent liability. **Our opinion is not modified in respect of this matter.**

    **Key Audit Matter — Recoverability of trade receivables from State Government agencies.** As at 31 March 2026,
    trade receivables include ₹185.4 crore due from State nodal agencies, of which **₹62.4 crore is overdue for more
    than six months**. Management's assessment of the expected credit loss (ECL) involves significant judgement about
    the timing of collection and the credit risk of Government counterparties.

    *How our audit addressed the matter:* we obtained an understanding of the controls over credit assessment; we sent
    balance confirmations to the agencies — **responses were received for 58% of the balance by value**; for the
    remainder we performed alternative procedures, including examination of subsequent receipts (₹21.6 crore received
    between 1 April and 20 May 2026) and correspondence with the agencies; we evaluated management's ECL model and the
    appropriateness of the disclosures.

    **Report on Other Legal and Regulatory Requirements (CARO 2020).** … (ii)(b) The Company has been sanctioned
    working-capital limits in excess of ₹5 crore on the basis of security of current assets; **the quarterly returns
    filed with the banks are in agreement with the books of account**, except for the quarter ended 31 December 2025,
    where receivables reported to the banks exceeded the books by ₹7.8 crore, which the Company has attributed to
    timing of credit notes.

<details markdown="1"><summary>Model annotations — try your own first</summary>

| Item | Mark | Annotation |
|:--|:-:|:--|
| Unmodified ("true and fair") opinion | G | No qualification. But an unmodified opinion is the default; the information is in the rest of the report |
| Emphasis of Matter on the ₹38 Cr GST demand | R | An EoM draws attention to something already disclosed; it is not a qualification. ₹38 Cr is **42% of FY26 PAT** and 5.4% of net worth. The dispute (5% vs 12–18% GST on solar systems) also bears on future solar margins if lost |
| KAM on receivables | R | A KAM means the auditor considered this among the most significant matters. It is not a red flag *by itself* (revenue and receivables are common KAMs) — but here it coincides with rising days and weak cash conversion |
| ₹185.4 Cr due from state agencies; ₹62.4 Cr > 6 months | F | State-agency dues are **53% of receivables**; a third of them are more than six months overdue |
| ECL judgement | R | The reference notes show an ECL allowance of only **₹4.0 Cr — 6.4% of the >6-month bucket** and 1.2% of receivables. The auditor accepted it, but you do not have to |
| Confirmations received for 58% by value | **R** | 42% of the balance was *not* confirmed by the counterparty. Alternative procedures (subsequent receipts) covered ₹21.6 Cr. Ask: how much of the unconfirmed balance is the >6-month bucket? |
| Subsequent receipts ₹21.6 Cr in seven weeks | G / J | Some cash is coming in — but ₹21.6 Cr against ₹185.4 Cr of state dues is slow |
| CARO (ii)(b): stock statements vs books mismatch of ₹7.8 Cr | **R** | Receivables reported to banks (for drawing-power) exceeded the books. "Timing of credit notes" may be innocent, but overstated drawing-power statements are a classic early warning in Indian small caps. Check whether the difference recurs |
| Auditor rotated in FY25 | J | A new auditor's second year. New auditors sometimes take a harder line; here the report is careful but not qualified |

**What changes in your analysis:** haircut receivables (e.g. provide 25–50% on the >6-month bucket: ₹15–31 Cr, i.e.
17–35% of FY26 PAT); treat the GST demand as a probability-weighted liability; add "confirmation coverage" and "CARO
drawing-power remarks" to your monitoring list; re-read the MD&A's "fully recoverable" in this light.

</details>

---

## Excerpt 3 — Kaveri Pumps, related-party note (FY26)

!!! quote "Note 41 — Related Party Disclosures (extract, fictional)"
    **(a) Names of related parties.** Promoter group: Mr R. Raghunathan (Chairman & Managing Director), Mrs L.
    Raghunathan (Non-executive Director), Mr A. Raghunathan (Whole-time Director). Entities controlled by the promoter
    group: **Kaveri Castings Pvt Ltd**; Raghunathan Realty LLP.

    **(b) Transactions during the year (₹ crore)**

    | Nature | FY25 | FY26 |
    |:--|--:|--:|
    | Purchase of castings — Kaveri Castings Pvt Ltd | 68.7 | 89.2 |
    | Advance paid for castings — Kaveri Castings Pvt Ltd | — | 6.0 |
    | Rent for corporate office — Raghunathan Realty LLP | 1.1 | 1.2 |
    | Remuneration — CMD and whole-time director | 4.6 | 5.4 |

    **(c) Balances outstanding at year-end:** payable to Kaveri Castings ₹9.8 crore; advance to Kaveri Castings **₹6.0
    crore** (included in other current assets).

    All transactions were **at arm's length and in the ordinary course of business**, and were approved by the Audit
    Committee. The Company has obtained **omnibus approval** for transactions with Kaveri Castings up to ₹120 crore for
    FY27.

<details markdown="1"><summary>Model annotations — try your own first</summary>

| Item | Mark | Annotation |
|:--|:-:|:--|
| Purchases from Kaveri Castings ₹68.7 → ₹89.2 Cr | **R** | **+29.8%**, against a 13.7% rise in total material cost; now **10.4%** of material cost (6.5% in FY21). A promoter-owned supplier taking a growing share of purchases is the most common leakage channel in Indian mid-caps |
| Advance of ₹6.0 Cr to Kaveri Castings | **R** | New this year. The company is financing its promoter's company while itself borrowing more for working capital. Ask why an advance was needed and on what terms |
| Omnibus approval up to ₹120 Cr for FY27 | R | Implies another ~35% increase is contemplated. Under SEBI's LODR, material RPTs above the threshold need shareholder approval — check whether this one will be put to a vote and how minority holders vote |
| "Arm's length", approved by the audit committee | J | Standard wording. Look for evidence: benchmark prices, share of Kaveri Castings' output sold to Kaveri, its margins (from its MCA filings) |
| Rent to Raghunathan Realty LLP ₹1.2 Cr | G / J | Small; typical; check it against local rents once |
| Remuneration ₹5.4 Cr (+17%) | J | 6% of PAT, rising faster than profit (PAT fell 7%). Check the remuneration policy and the median-employee ratio |
| Link to the pledge | R | Promoter shares were pledged in November 2025 "for a promoter-group real-estate venture" — possibly Raghunathan Realty. A promoter who needs cash, a growing RPT and an advance are three facts that together deserve a question at the next AGM |

**Quantify the exposure:** if Kaveri Castings charged 5% above market, the leakage on ₹89.2 Cr of purchases is ≈ ₹4.5
Cr a year pre-tax — about 5% of PAT. Small, but the direction and the advance matter more than the amount.

</details>

---

## Excerpt 4 — Kaveri Pumps, Q4 FY26 earnings call (May 2026)

!!! quote "Kaveri Pumps & Motors Ltd — Q4 FY26 earnings conference call (extract, fictional)"
    **Analyst (domestic fund):** Receivable days have gone from 84 to 96. What is the plan, and what is the ageing of the
    solar dues?

    **CFO:** We are in constant engagement with the agencies. These are sovereign-backed programmes and there is no
    question of recoverability. Two States account for the bulk of the overdue amount; we expect both to clear during
    the year, and **we expect receivable days to normalise towards 75–80 by the end of FY27**.

    **Analyst:** Could you share the ageing buckets?

    **CFO:** We do not give that granularity, but the auditors have gone through it in detail.

    **Analyst (PMS):** On guidance — you did 12.5% this year. What gives you confidence in 15–18% for FY27?

    **CMD:** The order book is at a record ₹410 crore, the Hosur plant is ramping up and agri demand should recover with a
    normal monsoon. **We are comfortable with 15–18% revenue growth and a 14–15% EBITDA margin.** Capex will be ₹45–50
    crore, mostly maintenance and automation.

    **Analyst (PMS):** There is a promoter pledge disclosed in the shareholding. Can you explain?

    **CMD:** That is a personal matter of the family, relating to a real-estate project. It has nothing to do with the
    Company, and I would request we keep the discussion to the business.

    **Analyst (sell-side):** Any plans for acquisitions?

    **CMD:** We are open to acquisitions in the motors space if valuations are sensible. Nothing specific right now.

<details markdown="1"><summary>Model annotations — try your own first</summary>

| Statement | Mark | Annotation |
|:--|:-:|:--|
| "No question of recoverability" | R | Absolute language about an uncertain matter; the auditor's KAM and the low ECL say otherwise |
| "Two States account for the bulk" | F / R | Concentration confirmed. Record it: **two counterparties** drive the receivables risk |
| **Receivable days 75–80 by end-FY27** | G (commitment) | A dated, checkable promise. Add it to the say-do ledger ([03.4](04-quarterly-results-and-concalls.md)): check at Q2 and Q4 FY27 |
| Refuses ageing buckets | **R** | The single most useful number is withheld, and responsibility is deflected to the auditors. Q1 FY27's presentation then showed receivables as "a bar chart without numbers" — a pattern, not an accident |
| Guidance 15–18% revenue, 14–15% EBITDA margin | J | Both above FY26's actual (12.5%, 13.8%). The reasons (order book, Hosur, monsoon) are plausible but the first depends on the state agencies that are paying late. (Q1 FY27 delivered +3.5% and 12.6%) |
| Capex ₹45–50 Cr | G | Disciplined; matches FY26's ₹48 Cr |
| Pledge: "a personal matter" | **R** | A pledge of a promoter's shares is not a personal matter for minority shareholders: forced selling hits the share price and control. The refusal to explain is the red flag, more than the 6% pledge itself |
| "Open to acquisitions" | J / R | With cash conversion at 36% and net debt rising, an acquisition would be funded by debt. Note it as a risk to capital allocation |

**Say-do ledger entries:** (1) receivable days 75–80 by March 2027; (2) FY27 revenue growth 15–18%; (3) FY27 EBITDA
margin 14–15%; (4) capex ₹45–50 Cr; (5) no specific acquisition. Two of the first three were already off track after Q1.

</details>

---

## Excerpt 5 — Nirmal Finance, rating rationale (FY26)

!!! quote "Rating rationale — Nirmal Finance Ltd (extract, fictional agency, June 2026)"
    **Rating action.** Long-term bank facilities and NCDs aggregating ₹4,200 crore: **AA− / Stable (reaffirmed)**.
    Commercial paper ₹400 crore: A1+ (reaffirmed).

    **Key rating strengths.** *Healthy capitalisation:* CRAR of **27.6%** (Tier-1 25.5%) at 31 March 2026 and gearing of
    3.3×, supported by the ₹300 crore QIP in FY24. *Established franchise:* over two decades in used commercial-vehicle
    and tractor finance across four States through 410 branches; AUM of **₹6,920 crore**, up 20%. *Matched ALM:* average
    tenor of assets ~34 months vs liabilities ~30 months; CP below 5% of borrowings; no negative cumulative mismatch in
    the up-to-one-year buckets.

    **Key rating weaknesses.** *Moderating asset quality:* GNPA rose to **2.9%** (2.6% a year earlier) and credit cost
    to 1.9% of average loans, driven by the used-CV book. *Concentration:* used CVs are 55% of AUM, and the four States
    account for all of it. *Borrower profile:* first-time and small-fleet operators, sensitive to freight rates and
    diesel prices.

    **Liquidity: Strong.** Cash and liquid investments of **₹560 crore** and unutilised sanctioned bank lines of ₹450
    crore at 31 May 2026, against debt repayments of ₹1,120 crore over June–November 2026; expected collections over the
    same period of about ₹1,300 crore.

    **Rating sensitivities.** *Upward:* significant scale-up (AUM above ₹10,000 crore) with diversification and GNPA
    sustained below 2.5%. *Downward:* GNPA above **4%** on a sustained basis; CRAR below **20%**; gearing above **5×**;
    or a material change in the funding profile, including CP above 10% of borrowings.

    **Key financial indicators (₹ crore):** FY25 — total income 943.2, PAT 208.4, GNPA 2.6%, CRAR 28.7%. FY26 — total
    income 1,124.0, PAT 239.5, GNPA 2.9%, CRAR 27.6%.

<details markdown="1"><summary>Model annotations — try your own first</summary>

| Item | Mark | Annotation |
|:--|:-:|:--|
| AA−/Stable reaffirmed; CP A1+ | G | Stable, investment grade with room; no watch |
| CRAR 27.6%, gearing 3.3× | F / G | Ties to the reference page (borrowings ₹5,565.4 Cr ÷ net worth ₹1,695.3 Cr = 3.28×). Ample capital: RBI's minimum for NBFCs is 15% |
| AUM ₹6,920 Cr, +20% | F | Ties (5,780 → 6,920, +19.7%) |
| Matched ALM; CP < 5% | **G** | The single most important strength after 2018 ([I4](../13-case-studies/india/04-ilfs-dhfl-2018.md)): no reliance on rolling short-term paper |
| GNPA 2.9% (2.6%); credit cost 1.9% | **R** | Stage-3 loans rose **34%** (₹150.3 → ₹200.7 Cr) while AUM grew 20%. The trend matters more than the level |
| Used CV 55% of AUM; four States | R | Concentrated by product and geography; a freight or diesel shock hits the whole book |
| Liquidity: ₹560 Cr + ₹450 Cr lines vs ₹1,120 Cr of repayments in six months, with ₹1,300 Cr of collections | F / G | Sources ₹2,310 Cr vs uses ₹1,120 Cr: **2.1× cover** even before new borrowing. "Strong" is justified |
| Sensitivities: GNPA > 4%, CRAR < 20%, gearing > 5×, CP > 10% | **G (for you)** | Ready-made thesis-breakers. GNPA is 1.1 points from the trigger; the others are far away |
| Total income in the indicators | F | 943.2 = interest income 901.3 + fees 41.9 (FY25); 1,124.0 = 1,073.2 + 50.8 (FY26). Ties |

**Five-line summary:** well-capitalised, conservatively funded lender with a matched ALM and strong liquidity; the
risk is on the asset side — stage-3 loans are growing faster than the book in a concentrated used-CV portfolio; the
downgrade trigger to watch is GNPA above 4%; the equity case depends on credit cost staying near 2%
([07.1](../07-special-valuation/01-banks-and-nbfcs.md)); add quarterly GNPA and credit cost to the monitoring list.

</details>

---

!!! tip "Trader's lens"
    Reading filings is pattern-matching under time pressure, like reading order flow: most lines are noise, a few are
    signal, and the signal is usually a *change* — a number that moved, a word that appeared, an answer that was
    refused. Train on these excerpts until you can find the red flags in under ten minutes each; then do the same on a
    real annual report.

!!! warning "Common mistakes"
    - Accepting management's adjectives ("fully recoverable", "prudent", "arm's length") without finding the number
      behind them.
    - Treating an unmodified audit opinion as a clean bill of health and skipping the KAMs, EoMs and CARO remarks.
    - Reading related-party notes for their *existence* rather than their *trend*.
    - Recording guidance without a date and a measurable target, so it cannot be checked later.
    - Reading a rating's letter and outlook without its liquidity section and sensitivities.
    - Inventing red flags that are not there: a KAM on revenue, a small office rent to a promoter, or a higher GNPA in a
      cyclical downturn are not, alone, evidence of wrongdoing.

## Key terms

| Term | Meaning |
|:--|:--|
| **Annotation (F/J/G/R)** | Marking each claim as a verifiable Fact, management Judgement, Green flag or Red flag |
| **Emphasis of Matter (EoM)** | Auditor's paragraph drawing attention to a disclosed matter; the opinion is not modified |
| **Key Audit Matter (KAM)** | A matter the auditor judged most significant in the audit, with the procedures performed |
| **Balance confirmation** | A request to a counterparty to confirm the balance owed; response rates are a quality signal |
| **CARO (ii)(b) remark** | Auditor's statement on whether quarterly stock/receivable returns filed with banks agree with the books |
| **Omnibus approval** | Audit-committee approval of expected related-party transactions up to a limit for the year |
| **Say-do ledger** | A record of management's dated, measurable commitments and whether they were met |
| **Liquidity cover** | (Cash + unutilised lines + expected collections) ÷ debt repayments over a period |

## Check your understanding

1. In Excerpt 1, which single sentence would you most want to test, and with which two numbers from the accounts?

<details markdown="1"><summary>Answer</summary>

"Timing differences … fully recoverable". Test it with the **receivables ageing** (overdue >6 months doubling from
₹31.0 Cr to ₹62.4 Cr) and **cash conversion** (CFO/EBITDA of 35.8%). If the differences were only timing, the ageing
would not lengthen year after year.

</details>

2. The auditor received confirmations for 58% of state-agency receivables by value. Why does this matter, and what
would reassure you?

<details markdown="1"><summary>Answer</summary>

Confirmations are the strongest independent evidence that a receivable exists and is acknowledged. For 42% of the
balance the auditor relied on alternative procedures. Reassurance would come from (a) subsequent receipts covering a
large part of the unconfirmed balance, (b) confirmation coverage rising next year, and (c) the >6-month bucket falling.

</details>

3. Why is the ₹6.0 crore advance to Kaveri Castings more concerning than the ₹89.2 crore of purchases?

<details markdown="1"><summary>Answer</summary>

Purchases have a commercial rationale (Kaveri needs castings) and a price you can benchmark. An advance is a transfer of
cash to a promoter-owned company before goods are delivered — effectively a loan — made in a year when Kaveri itself was
borrowing more for working capital and the promoters had pledged shares.

</details>

4. From Excerpt 5, compute Nirmal's liquidity cover over June–November 2026, and say which rating sensitivity is closest
to being triggered.

<details markdown="1"><summary>Answer</summary>

(₹560 + ₹450 + ₹1,300) ÷ ₹1,120 = **2.06×**. The closest trigger is **GNPA above 4%** (currently 2.9%, and stage-3 loans
grew 34% in FY26). CRAR (27.6% vs 20%) and gearing (3.3× vs 5×) are far from their triggers.

</details>

## Go deeper

- Take the latest annual report of any mid-cap you own and annotate its MD&A, auditor's report and related-party note
  with the F/J/G/R method. Time yourself.
- Find one real CARO (ii)(b) remark about differences between bank returns and books; read the company's explanation
  and the next year's report.
- Case studies that turn on these documents: [I1 Satyam](../13-case-studies/india/01-satyam-2009.md) (related-party
  deal), [I14 Manpasand & Vakrangee](../13-case-studies/india/14-manpasand-vakrangee-small-cap-flags.md) (auditor
  resignations), [I4 IL&FS & DHFL](../13-case-studies/india/04-ilfs-dhfl-2018.md) (rating rationales).

---
[← Previous: 03.5 Rating rationales, offer documents, broker reports & US filings](05-other-documents.md) · [Module index](index.md) · [Next: Module 03 exercises →](exercises.md)
