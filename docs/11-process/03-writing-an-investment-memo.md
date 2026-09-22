# 11.3 · Writing an investment thesis & memo

> **Why this matters:** an investment memo is where research becomes a decision. Writing it forces the
> variant perception into one sentence, the valuation into a range with named drivers, the risks into a
> pre-mortem, and the future into thesis-breakers with dates. A memo that cannot be written is a position that
> should not be taken. This lesson gives the structure and a complete sample memo on Kaveri Pumps — whose
> conclusion, consistent with the whole course, is "not at this price".

**Learning objectives** — after this lesson you can:

- Write a thesis in three bullets and a variant perception in one sentence.
- Structure a memo: key value drivers and KPIs, valuation summary, catalysts, risks and pre-mortem,
  thesis-breakers, monitoring plan, recommendation and size.
- Write the "I'm wrong if…" section so that it is falsifiable and dated.
- Produce a one-page version for decisions and a full version for the case file.

**Prerequisites:** [06.8 Margin of safety](../06-valuation/08-margin-of-safety-and-expected-value.md),
[09.7 The forensic checklist](../09-forensics/07-the-forensic-checklist.md), [11.2 The research process](02-the-research-process.md)  ·  **Time:** ~75 min

---

## 1. The structure

| Section | Length | Content | Test |
|:--|:--|:--|:--|
| **Header** | 3 lines | Company, ticker, date, price, market cap; recommendation (Buy / Watch / Avoid / Sell); target range; horizon; proposed size | Could a reader act on this line alone? |
| **What the market believes** | 2–3 sentences | The consensus narrative and the expectations implied by the price (from the reverse DCF) | Is it stated fairly — the strongest version, not a straw man? |
| **Variant perception** | 1 sentence | What you believe that differs, and the evidence class it rests on | Would a sceptic know exactly what you are claiming? |
| **Thesis** | 3 bullets | Each bullet: a claim + a number + the source | Is each bullet checkable? |
| **Key value drivers and KPIs** | Table | The 3–5 drivers that move value (from the tornado), current level, your forecast, consensus/implied, the KPI that tracks each | Does each driver have a monitoring KPI? |
| **Valuation** | Table + 3 sentences | Base/bull/bear with probabilities and weighted value; the key sensitivities; what the price implies; multiples cross-check | Is the range honest and the asymmetry stated? |
| **Catalysts** | List with dates | Events that would move the price toward value, and when | Are they specific and dated? |
| **Risks and pre-mortem** | List + paragraph | The bear case's mechanisms; "it is three years later and this lost 50% — why?" | Does the pre-mortem name things the thesis section did not? |
| **Thesis-breakers ("I'm wrong if…")** | 3–5 items | Observable, dated tests that would falsify the thesis | Would you actually sell if one fired? |
| **Monitoring plan** | Table | KPI, source, frequency, threshold | Can it be done in an hour a quarter? |
| **Forensic and governance summary** | 3 lines | RAG rating; top items; adjustments made to reported numbers | Is the discount applied somewhere specific? |
| **Recommendation and sizing** | 3 lines | Action, size logic (from [11.4](04-position-sizing-and-portfolio-construction.md)), entry plan | |
| **Appendices** (full version) | | Model summary, checklist scores, scuttlebutt log, sources | |

The one-page version is the header through thesis-breakers, compressed; the case file has everything.

## 2. Writing the variant perception

Bad: "Kaveri is a quality pump company that will benefit from solar." (Not variant; not testable.)
Better: "The market expects ~14% growth for ten years; I expect 9–11%." (Variant, testable — but why?)
Good: "The market prices Kaveri (₹390) for ~14% revenue growth over ten years with margins recovering to 15.5%;
I expect 9–11% because the solar segment that produced the FY23–26 surge is tender-driven, concentrated in two
slow-paying states and now 27% of sales, and because management has missed its receivables guidance four quarters
running — evidence the market is under-weighting because the headline growth still looks intact. I will know by
Q3 FY27 (Feb-2027)."

The form: *market expects X · I expect Y · because Z (evidence the market under-weights) · value if right · known
by when.* Every clause is necessary.

## 3. Sample memo — Kaveri Pumps & Motors (fictional), 22-Sep-2026

**Kaveri Pumps & Motors Ltd (KAVERIPMP, fictional) · Price ₹390 · Mcap ₹2,340 Cr · Recommendation: WATCH (do not
buy above ₹260; avoid at current price) · Value range ₹168–416, probability-weighted ₹306 · Horizon 2–3 years ·
Proposed size at ₹260: 4% of portfolio**

**What the market believes.** Kaveri is a well-run Coimbatore pump maker riding the PM-KUSUM solar-pump
opportunity, with FY23–26 revenue CAGR of 14.7%, a new motors plant, and a temporary working-capital bulge from
state agencies that will normalise. At ₹390 (25.9x trailing EPS, 13.7x EV/EBITDA) the price implies ~14.1% revenue
growth for ten years with EBITDA margins recovering to 15.5% and receivables normalising to ~80 days — essentially
a continuation of FY23–26.

**Variant perception.** The FY23–26 growth was a mix shift into a segment with structurally worse economics —
tender pricing, concentrated slow-paying state buyers, bank-guarantee intensity — and the market is capitalising
that growth at a franchise multiple. I expect 9–11% growth with margins plateauing near 14%, receivables
normalising only partly, and a ₹10–15 Cr provisioning catch-up; management's four consecutive misses on receivable
guidance and the withdrawal of the KPI in Q1 FY27 are the evidence the market under-weights.

**Thesis (why I am right).**
1. *The growth engine is the weak segment.* Solar went from 7% to 27% of revenue (FY23–26) while agri grew ~5% a
   year; solar carries ~22–24% gross margins vs ~40% agri, and 6–12-month payment cycles vs ~60 days (segment note;
   running-example §5, §8).
2. *The cash has not followed the profit.* CFO/PAT fell from 100% (FY24) to 63–72% (FY25–26); receivable days rose
   61 → 96; > 6-month overdues doubled to ₹62 Cr with 6.4% coverage; FCF was ₹13 Cr on ₹90 Cr of PAT (§4, §6, §8).
3. *Returns on new capital are below cost.* Incremental ROIC FY24–26 was 4.6% vs a 12.2% WACC; ROIC fell from 15.1%
   to 12.0%; the reference DCF's ₹320 already assumes a recovery to 15.5% margins and 18% terminal RONIC.

**Key value drivers and KPIs.**

| Driver | FY26 | My base FY27–29 | Price-implied | KPI / source |
|:--|--:|--:|--:|:--|
| Revenue growth | 12.5% | 9–11% | ~14% | Quarterly results; segment revenue |
| EBITDA margin | 13.8% | 13.5–14.5% | 15.5% | Results; gross margin vs copper |
| Receivable days | 96 | 85–90 | ~76–80 | Half-yearly BS; ageing note; management disclosure (withdrawn in Q1) |
| ECL coverage of > 6m overdues | 6.4% | 25% (my adjustment) | — | Annual report note |
| Hosur motors utilisation | 57% | 65–70% | 75%+ | Annual report; concall |
| RPT purchases (% of materials) | 10.4% | stable | — | RPT note |

**Valuation.**

| | Bear | Base | Bull | Weighted | Price |
|:--|--:|--:|--:|--:|--:|
| Value / share | ₹168 | ₹320 | ₹416 | ₹306 (25/50/25) or ₹286 (35/45/20) | ₹390 |
| Return from ₹390 | −57% | −18% | +7% | −22% | |

Most sensitive to terminal margin and RONIC (±₹40/share each), then WACC (±₹27 per 50 bps); the working-capital
normalisation is worth ₹23/share and is the near-term test. The whole WACC × g grid (11–13%, 4–6%) sits below
₹390. Peers trade at 30–40x (median 35x) on higher ROCE; Kaveri's ~26x is roughly fair *within* the group after
adjusting for returns and receivables risk — the group itself is priced for growth the value-driver formula
cannot support at a 12% cost of capital. Reverse DCF: ₹390 requires 14.1% growth for ten years (holding base
margins), or a 17.4% flat margin, or an 11.1% WACC.

**Catalysts (toward value, i.e. downward from here).** Q2 FY27 results (Nov-2026): receivable days and any
provision; Q3 FY27 (Feb-2027): confirmation or refutation of the 15–18% guidance; FY27 annual report (Jul-2027):
ageing schedule and ECL; any SAST filing on the pledge. Upward catalysts (bull case): a state clearing dues; an
industrial-motor contract win; a copper price fall.

**Risks and pre-mortem.** Bear mechanisms: state dues stuck → provisions and working-capital debt → growth cut →
de-rating to 15–18x on lower EPS (₹13 × 16 = ~₹210). Pre-mortem: *"It is September 2029 and Kaveri is at ₹180. The
two state agencies disputed ₹40 Cr of claims in FY27; the auditor qualified; the promoter's real-estate venture
needed cash and the pledge rose to 25%; a rival won the FY28 tenders at lower prices; Hosur never passed 65%
utilisation; the stock de-rated to 14x."* Risks to a *short* or to staying out: a large state pays in full (stock
+15% in a day); management is right about 15–18% growth; the Indian small-cap multiple regime stays elevated.

**I'm wrong if… (thesis-breakers).**
1. Receivable days at 30-Sep-2026 (H1 balance sheet, due Nov-2026) are below 80 with > 6-month overdues falling.
2. Q2–Q3 FY27 revenue growth is above 14% YoY with EBITDA margin above 14.5%.
3. Provisioning is raised to ≥ 20% of overdues *and* the stock does not fall (the market already priced it).
4. Hosur utilisation is disclosed above 70% by FY27 year-end.
Any two of these by Feb-2027 and the bear probability drops to 15%; the weighted value rises to ~₹330 and the
verdict becomes "fair, not cheap".

**Monitoring plan.** Quarterly: revenue by segment, EBITDA margin, receivables (half-yearly BS), provisioning
commentary, Hosur utilisation, guidance vs delivery (say-do table), pledge (SAST filings, continuous), RPT share
(annual), auditor's report (annual). One hour per quarter; template in the casebook.

**Forensic and governance.** Checklist Amber (18 points, six 2s, no 3s): revenue/receivables cluster; RPT trend;
new pledge. Adjustments: EPS ₹15.1 → ₹13.6 for provisioning; bear probability 25% → 35% for governance; WACC
unchanged. No evidence of fabrication.

**Recommendation and sizing.** Watch. Entry trigger ₹260 (expected return +18%, upside/downside 3.0 on the
reference scenarios) *with* receivable days < 85; at that price and evidence, size 4% (half-Kelly ≈ 6–7%, capped by
a 3% max-loss on a −35% bear at ~8.5%, then halved for governance Amber). Kill: pledge > 15%; auditor qualification;
CFO exit.

That is the whole memo. Note what it does *not* contain: a target price to the rupee, a paragraph about India's
irrigation potential, or a recommendation the numbers do not support.

## 4. Writing well

- **Lead with the conclusion.** Header first; the reader may stop there.
- **Numbers with sources** in every claim; no adjectives doing the work of evidence.
- **The strongest opposing case**, stated fairly, in "what the market believes" and in "risks".
- **Falsifiable, dated thesis-breakers.** "If execution disappoints" is not one; "receivable days > 90 at Sep-2026"
  is.
- **One page for the decision, the rest for the file.** A memo nobody finishes is not a memo.
- **Date and freeze it.** Later updates are new documents that reference the original; the original is the record
  of what you believed and why.

!!! tip "Trader's lens"
    The memo is a trade ticket with a thesis attached: instrument, direction, size, entry, stop (thesis-breakers),
    target (value range), and the reason. Traders who write the ticket before the trade fill fewer bad ones; the
    memo is the same pre-commitment, with the added discipline that the "stop" is a fact about the company, not a
    price.

!!! warning "Common mistakes"
    - A thesis that is a description of the company.
    - No variant perception (the memo agrees with the price and recommends buying anyway).
    - Risks listed as boilerplate ("execution risk, competition, macro").
    - Thesis-breakers that are unobservable or undated.
    - A target price with no distribution.
    - Writing the memo to justify a position already taken.

## Key terms

| Term | Meaning |
|:--|:--|
| **Investment memo** | The written case for a decision: thesis, drivers, valuation, catalysts, risks, breakers, sizing |
| **Variant perception** | The specific belief that differs from price-implied expectations, with evidence and a test |
| **Thesis** | The three claims, each with a number and a source, on which the case rests |
| **Catalyst** | A dated event expected to move price toward value |
| **Pre-mortem** | A narrative of how the position failed, written before it is taken |
| **Thesis-breaker** | An observable, dated outcome that would falsify the thesis and trigger exit |
| **Monitoring plan** | The KPIs, sources, frequency and thresholds used to track the thesis |
| **One-pager** | The compressed decision version of the memo |

## Check your understanding

1. Rewrite "Kaveri has strong growth prospects in solar pumps" as a thesis bullet.
<details><summary>Answer</summary>"Solar pumping systems grew from ₹61 Cr (7% of revenue) in FY23 to ₹356 Cr (27%)
in FY26 on state PM-KUSUM tenders; the unexecuted solar order book is ₹410 Cr (FY26 annual report, notes) —
which supports ~₹400–450 Cr of FY27 solar revenue if execution and payments hold." Claim, number, source, and
the condition.</details>

2. Why does the sample memo put "what the market believes" before the thesis?
<details><summary>Answer</summary>Because the thesis is only valuable relative to the price; stating the market's
view (and the implied expectations from the reverse DCF) first defines what the memo must disagree with, and
forces the author to represent the opposing case fairly.</details>

3. Write one more thesis-breaker for the Kaveri memo.
<details><summary>Answer</summary>"The FY27 annual report shows RPT purchases from Kaveri Castings falling below 9%
of materials with disclosed supplier margins in line with third-party foundries, removing the margin-migration
concern" — observable, dated (Jul-2027), and it would raise the base probability.</details>

4. What distinguishes a pre-mortem from a risk list?
<details><summary>Answer</summary>A pre-mortem is a specific causal story told from the failed future, which
surfaces interactions (state dispute → provisions → pledge rises → auditor) that a list of independent risks
misses; it also produces the thesis-breakers directly.</details>

## Go deeper

- Michael Steinhardt, *No Bull* — the origin of "variant perception".
- Gary Klein, "Performing a Project Premortem", *Harvard Business Review* (2007).
- Howard Marks, memos (Oaktree) — models of writing that leads with the conclusion and states the opposing case.
- The casebook's `templates/02-one-page-thesis.md` and `01-full-case-study.md` — the memo as a form.

---
[← Previous: 11.2 The research process](02-the-research-process.md) · [Module index](index.md) · [Next: 11.4 Position sizing & portfolio construction →](04-position-sizing-and-portfolio-construction.md)
