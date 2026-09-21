# 03.2 · Anatomy of an Indian annual report

> **Why this matters:** the annual report is the only document in which a company's board, its auditor and its
> company secretary all sign off on the same year — numbers, narrative, governance and pay, in one place. A 300-page
> Indian annual report is 80% boilerplate and 20% signal; knowing which 20% (and reading it in the right order) is the
> difference between a two-hour read that finds the problem and a two-day read that finds the chairman's photograph.

**Learning objectives** — after this lesson you can:

- Name every major section of an Indian annual report, the law that requires it, what it is for, and how long to
  spend on it.
- Read an auditor's report: identify the opinion type, Key Audit Matters, Emphasis of Matter, going-concern language,
  the CARO 2020 annexure and the internal-financial-controls opinion — and judge how serious each is.
- Extract and test governance data: director pay versus the median employee, AOC-1 (subsidiaries), AOC-2 (related-party
  contracts), and the resolutions in the AGM notice.
- Run the **2-hour annual-report read** and produce a one-page note.
- Compare 3–5 years of reports systematically — auditors, policies, related parties, language — including with a
  few lines of Python.

**Prerequisites:** [03.1 Where information lives](01-the-disclosure-universe.md);
[02.3](../02-accounting/03-the-income-statement.md)–[02.5](../02-accounting/05-the-cash-flow-statement.md) (the three statements);
[02.8 Group accounts, provisions, related parties](../02-accounting/08-deeper-cuts-group-accounts-and-other.md) helps  ·  **Time:** ~120 min (+ a 2-hour practice read)

---

## 1. The legal skeleton

An Indian annual report is not a free-form marketing document with some accounts attached. Most of it is **mandated
content**, and knowing the mandate tells you what *must* be there — which makes omissions visible.

| Section | Required by | Written by | Signal-to-noise |
|:--|:--|:--|:--|
| Corporate overview, chairman's / MD's letter | Nothing (voluntary) | Management + IR agency | Low, but reveals priorities |
| Board's (Directors') report and annexures | Companies Act 2013, Sec 134 (+ rules) | Board / company secretary | Medium; annexures are high |
| Management Discussion & Analysis (MD&A) | LODR Reg 34(3), Schedule V Part B | Management | Medium |
| Corporate-governance report | LODR Schedule V Part C | Company secretary | Medium; a few items are gold |
| Business Responsibility & Sustainability Report (BRSR) | LODR Reg 34(2)(f) — top 1,000 listed companies | Sustainability team | Low–medium |
| Secretarial audit report (Form MR-3) | Companies Act Sec 204 | Practising company secretary | Low, unless it lists breaches |
| Standalone financial statements + auditor's report | Sec 129, Sec 143, Ind AS | Management; auditor opines | **High** |
| Consolidated financial statements + auditor's report | Sec 129(3), Ind AS 110 | Management; auditor opines | **Highest** |
| Form AOC-1 (subsidiaries, associates, JVs) | Sec 129(3) proviso | Company | High |
| Form AOC-2 (related-party contracts) | Sec 134(3)(h), Sec 188 | Company | High |
| Notice of the AGM with explanatory statement | Sec 101–102 | Company secretary | High for what shareholders are asked to approve |

Sources: [Sec 134 contents, CAIRR](https://ca2013.com/134-financial-statement-boards-report-etc/);
[LODR Reg 34 and Schedule V, CAIRR](https://ca2013.com/lodr-regulation-34/) and
[Schedule V](https://ca2013.com/lodr-schedule-v/) (checked 21-Sep-2026).

The physical order varies by company — some put the AGM notice first, some last; financials are usually in the back
half — but the content is recognisably the same across thousands of companies. That standardisation is your friend:
once you have read ten, you can find anything in the eleventh in under a minute.

!!! tip "Read in the reverse of the printed order"
    The printed order runs from glossy to technical. The analyst's order runs the other way: **auditor's report →
    numbers → notes → governance → narrative**. Read the narrative last, so management's framing cannot anchor your
    reading of the numbers.

---

## 2. The narrative front half

### 2.1 Chairman's / MD's letter (≈5 minutes)

**What it is:** a letter from the chairman or managing director, unaudited and unregulated beyond general
misstatement rules.

**What to look for:**

- **Candour.** Does it name a mistake, a missed target, a bad segment? The best letters (Buffett's are the global
  benchmark) spend as much time on what went wrong as on what went right. Most Indian letters mention neither.
- **Selection of metrics.** Which numbers does the letter celebrate? "Record revenue" with no mention of cash flow is a
  choice. Track which metrics appear and *disappear* over the years.
- **Consistency with the numbers.** Read the letter *after* the statements and tick each claim against them.

Kaveri's FY26 revenue of ₹1,318.0 Cr was indeed a record (up 12.5% from ₹1,172.0 Cr). A letter that leads with that
but does not mention that cash from operations covered only 71.9% of PAT, or that receivable days rose to 96, is
selecting.

### 2.2 Management Discussion & Analysis (≈15 minutes)

**What it is:** a required narrative (LODR Schedule V Part B) covering industry structure and developments,
opportunities and threats, segment performance, outlook, risks and concerns, internal controls, discussion of
financial performance, and human resources. It must also give **detailed explanations of any key financial
ratio that changed by 25% or more** versus the previous year (debtors turnover, inventory turnover, interest
coverage, current ratio, debt-equity, operating and net profit margins), plus the change in return on net worth.

**What to look for:** specific, falsifiable statements (capacity numbers, market shares, order-book figures) versus
adjectives; risks that are *specific* to the company rather than a macro checklist; and the ratio-explanation table.

#### Worked example 1 — the 25% rule and the frog in slowly warming water

Does Kaveri's FY26 MD&A have to explain its receivables? Compute the Schedule V ratios from the reference statements
(debtors turnover = revenue ÷ closing trade receivables; interest coverage = EBIT ÷ total finance costs; current
ratio = current assets ÷ current liabilities excluding lease liabilities; RoNW on average equity).

| Ratio | FY24 | FY25 | FY26 | Change FY25 | Change FY26 | Change over 2 yrs |
|:--|--:|--:|--:|--:|--:|--:|
| Debtors turnover (x) | 5.22 | 4.35 | 3.80 | (16.7%) | (12.5%) | **(27.1%)** |
| Inventory turnover on material cost (x) | 4.87 | 4.68 | 4.56 | (3.9%) | (2.5%) | (6.3%) |
| Interest coverage (x) | 9.04 | 7.85 | 7.89 | (13.2%) | 0.5% | (12.8%) |
| Current ratio (x) | 2.21 | 2.11 | 2.04 | (4.7%) | (3.3%) | (7.8%) |
| Debt / equity (x) | 0.29 | 0.27 | 0.27 | (8.0%) | (0.2%) | (8.2%) |
| EBITDA margin (%) | 15.4 | 14.7 | 13.8 | (4.6%) | (6.1%) | (10.4%) |
| Net profit margin (%) | 8.6 | 8.3 | 6.9 | (3.2%) | (17.4%) | (20.1%) |
| Return on net worth (%) | 16.5 | 16.3 | 13.5 | (1.5%) | (17.3%) | (18.5%) |

*Example arithmetic, FY26 debtors turnover:* 1,318.0 ÷ 346.7 = 3.80x; change vs FY25 (1,172.0 ÷ 269.7 = 4.35x) is
3.80/4.35 − 1 = −12.5%. The same deterioration expressed as receivable days: 70 → 84 → 96 days.

**No ratio crosses the 25% line in either year**, yet debtors turnover fell 27% over two years. Kaveri's MD&A can
legally stay silent on receivables. The rule catches cliffs, not slopes — which is precisely why you compute trends
yourself across 3–5 years rather than relying on the company's year-on-year explanations.

### 2.3 Board's (Directors') report (≈10 minutes, mostly on annexures)

**What it is:** the board's statutory report under Sec 134(3), a long checklist that includes: financial summary,
dividend, material changes between year-end and the report date, subsidiaries and associates (with Form **AOC-1**),
related-party contracts (Form **AOC-2**), loans, guarantees and investments made, **CSR** (corporate social
responsibility) report, conservation of energy/technology/foreign-exchange data, the risk-management policy,
internal financial controls, the **directors' responsibility statement**, board evaluation, and — two items to
always read —

- the board's **explanations of every qualification, reservation, adverse remark or disclaimer** by the auditor and
  the secretarial auditor (Sec 134(3)(f)); and
- details of **frauds reported by the auditors** under Sec 143(12) (other than those reportable only to the Central
  Government) (Sec 134(3)(ca)).

**What to look for:** material post-balance-sheet changes; significant orders passed by regulators or courts;
changes in the nature of business; loans and guarantees to group companies; the remuneration annexure (next); the
secretarial audit report (§2.7).

### 2.4 Remuneration disclosures (≈5 minutes)

Under Sec 197(12) and Rule 5(1) of the Companies (Appointment and Remuneration of Managerial Personnel) Rules, 2014,
every listed company's Board's report must disclose: the **ratio of each director's remuneration to the median
employee's remuneration**; the percentage increase in pay of each director, CEO, CFO and company secretary; the
percentage increase in the median employee's pay; the number of permanent employees; and a comparison of average
increases for non-managerial staff vs managerial pay with a justification. Rule 5(2) adds details of the highest-paid
employees. Source: [Rule 5, CAIRR](https://ca2013.com/rule-5-companies-appointment-and-remuneration-of-managerial-personnel-rules2014/).

Two limits frame the numbers:

- **Companies Act Sec 197(1):** total managerial remuneration ≤ 11% of net profits (computed under Sec 198); any one
  managing/whole-time director ≤ 5% (≤ 10% for all together); exceedable with shareholder approval by special
  resolution since the 2017 amendment effective 12-Sep-2018
  ([Sec 197, CAIRR](https://ca2013.com/197-overall-maximum-managerial-remuneration-and-managerial-remuneration-in-case-of-absence-or-inadequacy-of-profits/)).
- **LODR Reg 17(6)(e):** pay to an executive director who is a **promoter** needs a shareholders' special resolution
  if it exceeds the higher of ₹5 Cr or 2.5% of net profit (or, with more than one such director, if their aggregate
  exceeds 5% of net profit)
  ([Taxguru summary of the SEBI amendment](https://taxguru.in/sebi/pass-special-resolution-remuneration-payable-toexecutive-promoter-director-exceeds-5-percent-net-profit-sebi.html)).

#### Worked example 2 — reading Kaveri's remuneration annexure

*Fictional details added for this lesson (not on the reference page):* Kaveri's managing director, a promoter-family
member, was paid ₹4.2 Cr in FY25 and ₹4.6 Cr in FY26. Median employee remuneration was ₹3.68 lakh in FY25 and
₹3.90 lakh in FY26. Employees: 2,310 (FY25) and 2,480 (FY26) per the reference page.

| Metric | Arithmetic | Result |
|:--|:--|--:|
| MD pay / median employee, FY26 | ₹4.6 Cr ÷ ₹3.90 lakh = 460 ÷ 3.90 | **118x** (FY25: 114x) |
| Increase in MD pay | 4.6 / 4.2 − 1 | **+9.5%** |
| Increase in median pay | 3.90 / 3.68 − 1 | +6.0% |
| Change in PAT | 90.5 / 97.4 − 1 | **(7.1%)** |
| MD pay as % of PAT | 4.6 / 90.5 | 5.1% |
| Average cost per employee (all-in, from P&L) | ₹117.3 Cr ÷ 2,480 | ₹4.73 lakh |
| Sec 197 one-director limit (5% of net profit; Sec 198 profit proxied as PBT + MD pay = 121.0 + 4.6) | 0.05 × 125.6 | ₹6.28 Cr — within |
| Reg 17(6)(e) trigger: higher of ₹5 Cr or 2.5% of net profit | max(5.0, 0.025 × 125.6 = 3.14) | ₹5.0 Cr — within |

**Reading:** nothing illegal, nothing extreme — but in a year when profit fell 7.1% and the stock fell from its peak,
the promoter-MD's pay rose 9.5%, faster than the median employee's. On its own this is a footnote. Combined with a new
pledge and rising purchases from a promoter-owned supplier, it belongs in the "alignment" column of your governance
assessment ([05.5](../05-business-analysis/05-management-and-capital-allocation.md),
[05.6](../05-business-analysis/06-corporate-governance-india.md)). Note that the median (₹3.90 lakh) is below the
all-in average cost (₹4.73 lakh): the P&L line includes employer contributions, gratuity, share-based pay and senior
salaries, and a pay distribution is right-skewed.

### 2.5 Corporate-governance report (≈5 minutes)

**What it is:** LODR Schedule V Part C — board composition, directors' attendance and other directorships, committee
composition and meetings, directors' remuneration, general meetings and special resolutions passed, shareholder
information (share-price data, distribution of shareholding), and a set of specific disclosures.

**The gold items:**

- **Detailed reasons for resignation of an independent director** before the end of their term.
- **Total fees paid to the statutory auditor and all entities in its network** — look at non-audit fees relative to
  audit fees (independence), and at audit fees relative to company size (a tiny fee for a complex group is a smell).
- A **certificate from a practising company secretary that no director is debarred or disqualified.**
- **Credit ratings** obtained during the year.
- Attendance: independent directors who attend half the meetings are not overseeing anything.

### 2.6 BRSR (≈5 minutes)

**What it is:** the Business Responsibility and Sustainability Report, mandatory for the top 1,000 listed companies by
market cap (Reg 34(2)(f)), organised as Section A (general disclosures), B (management and process), C
(principle-wise performance against nine principles). A subset, **BRSR Core**, carries third-party
**assessment or assurance** on a glide path: top 150 from FY24, top 250 from FY25, top 500 from FY26, top 1,000 from
FY27; value-chain disclosures were made voluntary. Source: SEBI circular of 28-Mar-2025
([copy on BSE](https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250401-21&attachedId=f3dd98e4-0648-4009-bb66-31dd4abbf4bd));
[Reg 34, CAIRR](https://ca2013.com/lodr-regulation-34/) (checked 21-Sep-2026).

**What to look for as a fundamental analyst:** employee headcount and **attrition** (cross-check against the
employee-cost line), permanent vs contract workers, safety statistics (fatalities, lost-time injuries — operational
discipline shows up here), customer complaints, energy and water intensity per rupee of revenue (a cost line in
disguise for energy-intensive businesses), and the share of inputs bought from MSMEs.

### 2.7 Secretarial audit report — Form MR-3 (≈2 minutes)

**What it is:** a practising company secretary's report (Sec 204) on compliance with the Companies Act, SEBI
regulations, FEMA and sector laws. Separately, LODR Reg 24A requires an annual secretarial compliance report. Since
1-Apr-2025, a listed company's secretarial auditor must be appointed by shareholders at the AGM, for at most one
five-year term (individual) or two five-year terms (firm), with a five-year cooling-off
([Taxguru FAQs on the Dec-2024 LODR amendment](https://taxguru.in/sebi/faqs-sebi-lodr-third-amendment-regulations-2024.html)).

**What to look for:** the "observations" paragraph. Most reports say "no observations". Anything else — delayed
filings, board-composition breaches, fines imposed by exchanges, non-compliance with related-party approvals — is a
cheap, reliable signal about how seriously the company takes rules.

---

## 3. The auditor's report: the most important five pages

Read this first. The auditor has spent months inside the company with access you will never have; the report is
their (heavily constrained) way of telling you where they looked hardest and whether they are comfortable.

### 3.1 Structure

Under the Standards on Auditing (SAs) issued by ICAI (the Institute of Chartered Accountants of India) — SA 700
(Revised) for the report format, SA 701 for Key Audit Matters, SA 705 for modified opinions, SA 706 for Emphasis of
Matter, SA 570 for going concern — an Indian auditor's report on a listed company runs:

1. **Opinion** — the verdict.
2. **Basis for opinion** — including, for a modified opinion, *why*.
3. **Material uncertainty related to going concern** — only if there is one.
4. **Key Audit Matters (KAMs)** — mandatory for listed entities for periods beginning on or after 1-Apr-2018
   ([Taxguru on SA 701](https://taxguru.in/chartered-accountant/sa-701-key-audit-matters.html)).
5. **Emphasis of Matter / Other Matter** paragraphs — if any.
6. Other information; responsibilities of management and of the auditor (boilerplate — skip).
7. **Report on other legal and regulatory requirements** — including the **CARO 2020** annexure (standalone
   report only), the opinion on **internal financial controls** under Sec 143(3)(i), and statements under Rule 11 of
   the Companies (Audit and Auditors) Rules, including — for years beginning on or after 1-Apr-2023 — whether the
   accounting software kept an **audit trail (edit log)** of every change that could not be disabled (Rule 11(g))
   ([Taxguru practitioner's guide](https://taxguru.in/company-law/audit-trail-compliance-rule-3-1-rule-11-practitioners-guide.html)).

There are **two** auditor's reports — one on the standalone statements, one on the consolidated. Read both; they can
differ (a KAM or qualification may relate to a subsidiary).

### 3.2 The four opinions — and what each should do to you

| Opinion | Wording cue | What it means | Your response |
|:--|:--|:--|:--|
| **Unmodified** ("clean") | "give a true and fair view" | Auditor obtained sufficient evidence; no material misstatement found | Normal. A clean opinion is necessary, not sufficient |
| **Qualified** | "**except for** the effects of the matter described…" | A material misstatement or scope limitation, but **not pervasive** | Quantify the matter; ask why management won't fix it. Frequently a first step toward worse |
| **Adverse** | "do **not** give a true and fair view" | Misstatements both material **and pervasive** | The statements are unreliable. Rare; usually uninvestable |
| **Disclaimer** | "we **do not express** an opinion" | Auditor could not obtain enough evidence; possible effects pervasive | Treat as a red alert — the auditor could not verify the accounts |

Two things that are **not** modifications but still matter:

- **Material uncertainty related to going concern** (SA 570): the auditor agrees the accounts are properly prepared
  on a going-concern basis but flags significant doubt about the company's ability to continue — typically when debt
  is due and refinancing is uncertain. This is the auditor telling you the equity may be an option on survival.
- **Emphasis of Matter** (SA 706): the auditor draws attention to something already disclosed in the notes — an
  ongoing regulatory investigation, a large disputed claim, a scheme of arrangement — *without* modifying the opinion.
  Read the note it points to; the auditor thought you might miss it. An **Other Matter** paragraph often discloses that
  other auditors audited some subsidiaries (note what share of group assets and revenue they cover).

A useful companion: every listed company must file a *statement on the impact of audit qualifications* with its
annual results under Reg 33, which quantifies the effect of any qualification.

### 3.3 Key Audit Matters — the auditor's heat map

KAMs are the matters that, in the auditor's judgement, were **of most significance** in the audit — selected from
the matters discussed with the audit committee. Each KAM says why it mattered and how it was addressed. KAMs are not
findings of error; they tell you where judgement and estimation were concentrated.

**How to read them:**

- **Specific vs generic.** "Revenue recognition" with a paragraph that could apply to any company is noise. A KAM that
  names a customer class, a contract type, an amount or an ageing bucket is signal.
- **Changes year to year.** A new KAM means something new required heavy audit work. A KAM that *vanishes* while the
  underlying issue has grown deserves a question.
- **Match KAMs to the notes.** Every KAM should point to a note; read that note next ([03.3](03-notes-to-accounts.md)).

!!! tip "Trader's lens"
    Think of the KAM section as the auditor's **implied-volatility surface**: it shows where the auditor sees the
    widest distribution of possible values for a balance (receivables recoverability, inventory valuation, goodwill,
    revenue cut-off). A clean opinion is the at-the-money quote — "the mid is fair". The KAMs are the wings — "but
    here, the error bars are wide". Like skew, the *changes* are more informative than the levels.

#### Worked example 3 — sizing Kaveri's receivables KAM

Suppose Kaveri's FY26 auditor's report includes a KAM on the **recoverability of trade receivables from state
government agencies** (the full, annotated fictional text is in [03.6](06-annotated-walkthroughs.md)). The note it
points to shows (reference page §8): receivables overdue more than 6 months ₹62.4 Cr (FY25: ₹31.0 Cr), expected
credit loss (ECL) allowance ₹4.0 Cr (FY25: ₹3.1 Cr). An **ECL allowance** is the provision a company makes, under
Ind AS 109, for receivables it expects not to collect in full.

| Step | Arithmetic | Result |
|:--|:--|--:|
| Allowance cover on >6-month bucket, FY25 | 3.1 ÷ 31.0 | 10.0% |
| Allowance cover on >6-month bucket, FY26 | 4.0 ÷ 62.4 | **6.4%** |
| Stress: provide 50% of the >6-month bucket | 0.5 × 62.4 − 4.0 | ₹27.2 Cr extra pre-tax |
| Post-tax at 25.17% | 27.2 × (1 − 0.2517) | ₹20.35 Cr |
| As % of FY26 PAT (₹90.5 Cr) | 20.35 ÷ 90.5 | **22.5%** |
| Per share (6.00 Cr shares) | 20.35 ÷ 6.00 | ₹3.39 |
| As % of net worth (₹706.1 Cr) | 20.35 ÷ 706.1 | 2.9% |

**Reading:** the overdue bucket doubled while the allowance cover fell from 10% to 6.4%. A hypothetical 50% provision
would remove a fifth of the year's profit but under 3% of net worth. So the balance-sheet risk is moderate; the
**earnings-quality** risk is significant — FY26 profit may be overstated by the amount of under-provision, and the
cash was never received (hence CFO/PAT of 71.9%). The KAM tells you the auditor looked hard at this; it does not tell
you they are comfortable with 6.4% cover. That judgement is yours.

### 3.4 CARO 2020 — the auditor's checklist annexure

The **Companies (Auditor's Report) Order, 2020** (CARO) applies from FY22 and requires the auditor to report on 21
specific matters (clauses 3(i)–3(xxi)); it does not apply to banks, insurers, small companies and certain private
companies, and applies to consolidated statements only through clause (xxi) (qualifications in group companies'
CARO reports). Sources: [Cleartax clause list](https://cleartax.in/s/caro-companies-auditors-report-order-2020);
[CAG guidance note on CARO 2020](https://cag.gov.in/uploads/media/Guidance-note-on-CARO-2020-064e84867178ba9-47322653.pdf).

The clauses worth reading every year:

| Clause | Subject | Why an analyst cares |
|:--|:--|:--|
| (i) | Property records, physical verification, **title deeds** not in the company's name | Assets that may not really be the company's |
| (ii) | Inventory verification; **quarterly statements filed with banks** for working-capital limits agree with books? | Differences between stock/debtor statements given to banks and the books are a classic early warning |
| (iii) | Loans, advances, guarantees, investments given | Money flowing to group companies; loans overdue |
| (vii) | Undisputed statutory dues outstanding; **disputed dues** by forum | A mini contingent-liability table with the forum and year |
| (ix) | **Defaults** on loans; wilful-defaulter status; short-term funds used for long-term purposes; borrowing to fund subsidiaries | Liquidity mismatches in plain words |
| (x) | Use of IPO/QIP/preferential-issue money | Did the money go where promised? |
| (xi) | **Fraud** noticed; whistle-blower complaints | Self-explanatory |
| (xiv) | Internal-audit system commensurate with size? | Governance hygiene |
| (xvii) | Cash losses in the year and previous year | Distress indicator |
| (xviii) | Resignation of statutory auditors — issues raised by the outgoing auditor considered? | Why did the last auditor leave? |
| (xix) | **Material uncertainty** about meeting liabilities falling due within a year | Going-concern-type warning in CARO form |
| (xx) | Unspent CSR | Minor, but a compliance signal |

### 3.5 Internal financial controls (IFC) opinion

Under Sec 143(3)(i) the auditor also opines on whether the company has **adequate internal financial controls over
financial reporting** and whether they **operate effectively**. It is India's analogue of the US SOX 404(b) audit.
A modified IFC opinion (a "material weakness") means the processes that produce the numbers are unreliable even if
this year's numbers were corrected — watch for it in fast-growing small caps.

### 3.6 The auditor as a person

- **Who and how long.** Listed companies must rotate an individual auditor after one five-year term and a firm after
  two five-year terms, with a five-year cooling-off (Sec 139(2);
  [CAIRR](https://ca2013.com/appointment-of-auditors/)). Kaveri's rotation in FY25 was mandatory — a new auditor
  reading old judgements with fresh eyes, which sometimes produces new KAMs or provisions in the first two years.
- **Resignations.** An auditor resigning mid-term is a major event. Since SEBI's circular of 18-Oct-2019, an auditor
  resigning within 45 days of a quarter-end must first complete that quarter's review/audit report, and the reasons
  must be disclosed ([Vinod Kothari summary](https://vinodkothari.com/2019/11/sebi-on-resignation-of-auditors/)).
  Read the reasons; then read CARO clause (xviii) in the successor's first report.
- **Fees.** From the governance report; compare with peers and with the complexity of the group.
- **Regulatory history.** The National Financial Reporting Authority (NFRA) publishes orders against auditors of
  listed companies.

---

## 4. The financial statements — standalone and consolidated

Each set contains a balance sheet, a statement of profit and loss (including other comprehensive income), a
statement of changes in equity, a cash-flow statement and **notes**. You learned to read the statements in
[Module 02](../02-accounting/06-linking-the-three-statements.md); the notes are the next lesson.

**Which set to read?** Consolidated first — it is the economic entity you are valuing. Then the standalone set for
three things the consolidated set hides: **(1) where the cash sits** (can the parent pay dividends and service its
debt, or is cash trapped in subsidiaries?), **(2) loans, guarantees and investments from the parent into
subsidiaries** (eliminated on consolidation), and **(3) subsidiaries' losses funded by the parent**.

#### Worked example 4 — what AOC-1 and the standalone statements reveal together

Kaveri's reference statements are presented only on a consolidated basis, so we use a small **fictional** company,
**Tungabhadra Foods Ltd**. Its standalone PAT is ₹120.0 Cr. Its AOC-1 (Part A, subsidiaries; ₹ Cr) shows:

| Subsidiary | Holding | Share capital | Reserves | Total assets | Total liabilities | Turnover | PBT | Tax | PAT |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tungabhadra Dairy Pvt Ltd | 51% | 20.0 | 64.0 | 210.0 | 126.0 | 390.0 | 20.0 | 5.0 | 15.0 |
| TF Retail Pvt Ltd | 100% | 50.0 | (90.0) | 230.0 | 270.0 | 160.0 | (22.0) | 0.0 | (22.0) |
| TF Exports FZE (UAE) | 100% | 25.0 | 8.0 | 60.0 | 27.0 | 140.0 | 3.3 | 0.3 | 3.0 |

(Check: for each row, total assets − total liabilities = share capital + reserves: 84.0, (40.0), 33.0.)

The standalone balance sheet shows a **₹180.0 Cr loan to TF Retail** at 9% interest, plus the ₹50.0 Cr equity
investment at cost.

| Step | Arithmetic | ₹ Cr |
|:--|:--|--:|
| Consolidated PAT (ignoring intra-group items, which cancel) | 120.0 + 15.0 − 22.0 + 3.0 | 116.0 |
| Non-controlling interest (49% of Dairy) | 0.49 × 15.0 | 7.35 |
| **PAT attributable to owners** | 116.0 − 7.35 | **108.65** |
| Interest the parent books from TF Retail | 0.09 × 180.0 | 16.2 |
| …post-tax at 25.17% | 16.2 × 0.7483 | 12.12 |
| Standalone PAT excluding that interest | 120.0 − 12.12 | 107.88 |

**Readings:** (1) The headline standalone PAT of ₹120.0 Cr is ~10% above what owners actually earn from the group
(₹108.65 Cr). (2) Part of standalone profit is interest "earned" from a subsidiary with **negative net worth**
(₹(40.0) Cr) that is itself losing money — the parent is, economically, lending money to itself and booking the
interest as income. (3) The ₹180.0 Cr loan and ₹50.0 Cr investment are carried at cost in the standalone balance
sheet; whether they need impairment (Ind AS 36/109) is exactly the sort of judgement that should appear as a KAM in the
standalone auditor's report. None of this is visible on an aggregator that shows only consolidated numbers.

Also scan AOC-1 for subsidiaries with **large assets and tiny turnover** (cash or land parked there), **overseas
entities in low-tax jurisdictions** with unclear purpose, and entities that appear or disappear from one year to the
next. Part B of AOC-1 does the same for associates and joint ventures (equity-accounted, so their debt never appears
in consolidated borrowings).

---

## 5. AOC-2: related-party contracts

Form AOC-2 (Sec 134(3)(h) with Sec 188) lists (1) contracts with related parties **not at arm's length**, and (2)
**material** contracts at arm's length. Almost every company reports "Nil" in part (1) — every related-party
transaction is asserted to be at arm's length. So AOC-2 is mainly a pointer: the full numbers are in the Ind AS 24
related-party note ([03.3](03-notes-to-accounts.md)); the approval trail is in the audit-committee and AGM
documents.

**The LODR approval thresholds changed recently.** Under Reg 23, a **material** related-party transaction needs
shareholder approval (related parties may not vote in favour). Until late 2025 "material" meant above the lower of
₹1,000 Cr or 10% of consolidated turnover. SEBI's LODR (Fifth Amendment) Regulations, notified 19-Nov-2025, replaced
this with a **turnover-based scale**: 10% of turnover for companies with turnover up to ₹20,000 Cr; ₹2,000 Cr + 5% of
turnover above ₹20,000 Cr up to ₹40,000 Cr; ₹3,000 Cr + 2.5% of turnover above ₹40,000 Cr, capped at ₹5,000 Cr
([Maheshwari & Co note](https://www.maheshwariandco.com/press-releases/sebi-fifth-amendment-lodr-new-rpt-materiality-rules/);
[Fox Mandal note](https://foxmandal.in/sebis-fifth-lodr-amendment-2025/); checked 21-Sep-2026).

#### Worked example 5 — when would Kaveri's shareholders get a vote on Kaveri Castings?

Kaveri's purchases from promoter-owned Kaveri Castings Pvt Ltd were ₹89.2 Cr in FY26, having grown from ₹25.5 Cr in
FY21 — a compound annual growth rate (CAGR) of $(89.2/25.5)^{1/5}-1 = 28.5\%$, against 17.0% for total material
cost. Kaveri's turnover is below ₹20,000 Cr, so the materiality threshold is 10% of the last audited turnover.

| Year | Projected RPT at 28.5% CAGR (₹ Cr) | Threshold: 10% of prior-year turnover (₹ Cr) | Shareholder vote? |
|:--|--:|--:|:--|
| FY27 | 89.2 × 1.285 = 114.6 | 0.10 × 1,318.0 = 131.8 | No |
| FY28 | 89.2 × 1.285² = 147.2 | 0.10 × 1,449.8 = 145.0 | **Yes, just** |
| FY29 | 89.2 × 1.285³ = 189.1 | 0.10 × 1,652.8 = 165.3 | Yes |

(FY27–FY28 turnover from the base-case projection in the [reference valuation](../appendix/running-example/kaveri-valuation.md).)

If instead Kaveri Castings' share of material cost stayed at 10.4%, purchases would track material cost (≈65.1% of
revenue) and stay below the threshold (≈₹98 Cr in FY27, ≈₹112 Cr in FY28). **Reading:** the AGM notice is where you
would first see this — a resolution seeking approval for purchases from Kaveri Castings "up to ₹X Cr". Minority
shareholders would then vote without the promoters, and the explanatory statement must justify pricing. A company that
structures contracts to stay just under a threshold is also telling you something.

---

## 6. The AGM notice: what shareholders are asked to decide

The notice of the annual general meeting, with its **explanatory statement** (Sec 102), is short and underrated. It
lists every resolution, and the explanatory statement must disclose the material facts, including directors'
interests.

- **Ordinary resolutions** pass with a simple majority of votes cast; **special resolutions** need at least 75%.
- Typical items: adopting the accounts; declaring dividend; re-appointing directors who retire by rotation;
  appointing or re-appointing the statutory auditor (and, since 2025, the secretarial auditor); ratifying the cost
  auditor's fee; **directors' remuneration** (special resolutions where Sec 197 or Reg 17(6)(e) limits are crossed);
  **material related-party transactions** (Reg 23); **borrowing limits** and creation of charges (Sec 180 — special
  resolutions); loans and investments above the Sec 186 limits; **preferential issues and warrants**; ESOP schemes;
  changes to the articles.

**What to look for:** raised borrowing limits (a leading indicator of debt-funded plans); preferential allotments or
warrants to promoters (price, lock-in, dilution — see [01.3](../01-markets-101/03-raising-and-returning-capital.md));
large RPT omnibus approvals; re-appointment of independent directors whose tenure is getting long; pay resolutions.

**After the meeting**, the company files **voting results** and the **scrutiniser's report** with the exchanges (Reg
44(3); two working days at the time of writing — confirm on the [CAIRR Reg 44 page](https://ca2013.com/lodr-regulation-44/)).
Look at how *institutions* voted: public institutions voting substantially against a related-party or pay resolution
often means proxy advisers (IiAS, InGovern, SES) recommended against — their reports explain why.

---

## 7. The 2-hour annual-report read

A protocol for a first serious read of a company you are researching. It assumes you have the current and previous
annual reports open and have already skimmed the latest results. Times are budgets, not targets.

| # | Step | Minutes | What you produce |
|:--|:--|--:|:--|
| 0 | Set-up: download this year's and last year's reports; open a one-page template | 5 | Blank note |
| 1 | **Auditor's reports** (standalone and consolidated): opinion, going concern, KAMs, EoM/Other matter, CARO (i), (ii), (iii), (vii), (ix), (xi), (xvii)–(xix), IFC, audit trail | 15 | List of "look here" notes |
| 2 | **Consolidated statements**: tie revenue, PAT, equity to results; compute 6 numbers — revenue growth, EBITDA margin, CFO/PAT, receivable days, net debt, ROCE | 25 | Six-number strip vs last year |
| 3 | **The critical notes** (policies and changes, segments, receivables ageing, borrowings, contingent liabilities, related parties, tax reconciliation, exceptional items) — see [03.3](03-notes-to-accounts.md) | 25 | Flags with note references |
| 4 | **Standalone vs consolidated** + AOC-1 | 10 | Where cash sits; loss-making subsidiaries |
| 5 | **MD&A and chairman's letter** — tick each claim against the numbers | 15 | Claims that do / don't match |
| 6 | **Board's report**: remuneration annexure, AOC-2, loans/guarantees, material changes after year-end | 10 | Governance data points |
| 7 | **Governance report + secretarial audit**: attendance, ID resignations, auditor fees, observations | 5 | Governance flags |
| 8 | **AGM notice**: resolutions and explanatory statements | 5 | What shareholders are asked to approve |
| 9 | **BRSR skim**: employees, attrition, safety, complaints | 5 | Operational sanity checks |
| | **Total** | **120** | |

**The one-page output** has five boxes: (a) five facts I did not know; (b) the three numbers that changed most, and
the company's explanation; (c) red and yellow flags, each with a note or page reference; (d) questions for the next
earnings call or for primary research; (e) what to model or check next. A read that does not produce questions was
not a read.

Why this order? The auditor tells you where to look; the numbers and notes tell you what happened; the governance
sections tell you who decided it; and only then does management get to tell you what it means.

For Kaveri FY26, a disciplined read produces the flags that the course's forensic checklist later formalises
([09.7](../09-forensics/07-the-forensic-checklist.md)): receivables and solar concentration (KAM + ageing note), CFO/PAT
below 75%, rising related-party purchases (AOC-2 + RPT note), a new promoter pledge (governance report / exchange
filings), and a new ₹38.0 Cr GST contingent liability.

---

## 8. Comparing 3–5 years of reports

One annual report is a photograph; five are a film. The most valuable information is in what **changed**.

**What to diff, year over year:**

- **Auditor**: name, tenure, fees, opinion; KAMs added, removed or reworded; new Emphasis of Matter.
- **Accounting policies**: revenue-recognition wording, depreciation lives, capitalisation policies, consolidation
  scope. A policy paragraph that silently changes is a lever being pulled ([02.7](../02-accounting/07-deeper-cuts-assets-and-expenses.md)).
- **Related parties**: new names in the list; rising amounts; new *types* of transaction (loans, guarantees, rent).
- **Subsidiaries**: entities created, merged, sold (to whom?) or struck off.
- **Contingent liabilities and guarantees**: trend vs net worth.
- **Segments and KPIs**: a re-segmentation can bury a weak business; a KPI that disappears from the chairman's letter
  usually stopped looking good.
- **People**: CFO, company secretary, independent directors, auditor.
- **Language**: new risks; promises that quietly vanish; the adjectives.

#### Worked example 6 — a five-year change log for Kaveri

Built only from facts on the reference page:

| Year | What changed | Where you would see it |
|:--|:--|:--|
| FY22 | Solar revenue ₹30.3 Cr (4.0% of revenue); purchases from Kaveri Castings 7.0% of material cost | Segment note; RPT note |
| FY23 | CWIP jumps to ₹68.0 Cr (Hosur plant); term loans up; FCF negative | Balance sheet; CWIP ageing; borrowings note |
| FY24 | Hosur commissioned (gross block +₹216 Cr); first ESOP grant; receivable days 70 | PP&E note; share-based-payment note |
| FY25 | **Auditor rotated**; ₹14.0 Cr exceptional land gain; receivables >6 months ₹31.0 Cr | Auditor's report; exceptional-items note; ageing |
| FY26 | Receivables >6 months ₹62.4 Cr; new ₹38.0 Cr GST contingent liability; guarantees ₹96.0 Cr; RPT share 10.4%; promoter pledge 6% | Ageing; contingent-liabilities note; SAST filings |

And a language diff. With the text of two MD&As extracted (e.g., with `pdfplumber`), Python's standard library does
the rest. The two excerpts below are **fictional** Kaveri MD&A sentences:

```python
import difflib

fy24 = """Solar pumping systems grew strongly on the back of PM-KUSUM tenders.
Receivables from state nodal agencies are collected within contractual timelines.
We target receivable days of 65 to 70 by FY26.
Related party purchases are at arm's length and approved by the Audit Committee."""
fy26 = """Solar pumping systems grew strongly on the back of PM-KUSUM tenders.
Receivables from state nodal agencies remain elevated but are fully recoverable.
We are being selective on states with good payment track records.
Related party purchases are at arm's length and approved by the Audit Committee."""

def sents(t):
    return [s.strip() for s in t.splitlines() if s.strip()]

for line in difflib.unified_diff(sents(fy24), sents(fy26), "MD&A FY24", "MD&A FY26", lineterm="", n=0):
    print(line)
print("similarity", round(difflib.SequenceMatcher(None, fy24, fy26).ratio(), 3))
```

Output:

```text
--- MD&A FY24
+++ MD&A FY26
@@ -2,2 +2,2 @@
-Receivables from state nodal agencies are collected within contractual timelines.
-We target receivable days of 65 to 70 by FY26.
+Receivables from state nodal agencies remain elevated but are fully recoverable.
+We are being selective on states with good payment track records.
similarity 0.676
```

The diff surfaces exactly the two sentences that matter: collection "within contractual timelines" became "elevated
but fully recoverable", and a numeric target (65–70 days by FY26) vanished — the actual FY26 figure was 96 days. The
unchanged boilerplate on related parties is also informative: the language stayed identical while the amount grew
from 8.2% to 10.4% of material cost. Scale this to whole reports (split by section headings, compare paragraph by
paragraph) and you have a cheap early-warning system.

!!! tip "Trader's lens"
    You rarely trade the level of implied vol; you trade its *changes* relative to what realised vol tells you. Annual
    reports work the same way: the level of disclosure is mostly boilerplate, but the **first derivative** — a new KAM,
    a softened sentence, a vanished target — is where the information is. Diff, don't just read.

---

!!! info "India notes"
    - **Two auditor's reports, two sets of statements.** Unlike a US 10-K (essentially consolidated only), Indian reports carry
      standalone and consolidated statements. Parent-level cash, loans to subsidiaries and guarantees live in the
      standalone set.
    - **Government companies** (PSUs) carry comments of the Comptroller and Auditor General (CAG) alongside the
      statutory auditor's report.
    - **Banks and NBFCs** add regulator-mandated disclosures (for banks, Basel III Pillar 3; for NBFCs such as Nirmal
      Finance, RBI-prescribed schedules on asset classification, liquidity and exposures). CARO does not apply to
      banks and insurers.
    - **MNC subsidiaries** (e.g., listed Indian arms of foreign groups) disclose royalty and technology fees to the
      parent in the related-party note — often the most important RPT.
    - **Subsidiary accounts on the website.** Reg 46 requires separate audited financial statements of each
      subsidiary on the company's website before the AGM ([03.1](01-the-disclosure-universe.md)).
    - **Timing.** Annual reports for March year-ends usually appear between June and early September, ahead of AGMs
      that must be held by 30-Sep (five months for the top 100).

!!! warning "Common mistakes"
    - Reading the report front to back and letting the chairman's letter frame everything that follows.
    - Treating an unmodified opinion as a certificate of quality. It is a certificate of *no material misstatement
      found* — the KAMs, EoM and CARO remarks still need reading.
    - Reading only the consolidated statements and missing loans to, and losses of, subsidiaries.
    - Skipping the AGM notice — where borrowing limits, related-party approvals, preferential issues and pay are
      decided.
    - Trusting the MD&A's ratio explanations to catch slow deterioration; the 25% trigger misses slopes.
    - Reading one year in isolation. Most red flags are *changes*.

## Key terms

| Term | Meaning |
|:--|:--|
| **Board's (Directors') report** | Statutory report of the board under Sec 134(3), with annexures (AOC-1, AOC-2, CSR, remuneration, MR-3) |
| **MD&A** | Management Discussion & Analysis (LODR Schedule V Part B), including explanations of ratios that moved ≥25% |
| **Corporate-governance report** | LODR Schedule V Part C disclosure on board, committees, auditor fees, director resignations |
| **BRSR / BRSR Core** | Sustainability report for the top 1,000 listed companies; the Core subset gets third-party assessment or assurance on a glide path |
| **Form MR-3** | Secretarial audit report by a practising company secretary (Sec 204) |
| **Unmodified / qualified / adverse / disclaimer** | The four audit opinions, in rising order of severity |
| **Key Audit Matter (KAM)** | A matter of most significance in the audit (SA 701), mandatory for listed companies |
| **Emphasis of Matter** | Auditor's pointer to a disclosed matter, without modifying the opinion (SA 706) |
| **Material uncertainty related to going concern** | Auditor's flag (SA 570) of significant doubt about the company's ability to continue |
| **CARO 2020** | Companies (Auditor's Report) Order: 21 clause checklist reported by the auditor on standalone statements |
| **IFC opinion** | Auditor's opinion on internal financial controls over financial reporting (Sec 143(3)(i)) |
| **Audit trail (Rule 11(g))** | Auditor's report on whether the accounting software kept a non-disableable edit log (from FY24) |
| **AOC-1** | Form summarising each subsidiary's, associate's and JV's key financials |
| **AOC-2** | Form listing related-party contracts (not at arm's length; material at arm's length) |
| **Median-employee ratio** | Ratio of each director's pay to the median employee's pay (Sec 197(12), Rule 5(1)) |
| **Ordinary / special resolution** | Shareholder resolutions passed by simple majority / at least 75% of votes cast |
| **Explanatory statement** | The Sec 102 statement accompanying AGM resolutions, disclosing material facts and interests |

## Check your understanding

**1.** An auditor's report says the financial statements "give a true and fair view", includes a Key Audit Matter on
inventory valuation, and an Emphasis of Matter paragraph pointing to a note on a tax search at the company's
premises. Is the opinion modified? What do you read next?

<details markdown="1"><summary>Answer</summary>

No — it is an **unmodified** opinion. KAMs and Emphasis of Matter paragraphs do not modify the opinion. Next, read the
inventory note (ageing, write-downs, valuation policy) and the note on the tax search (what was found, any demand
raised, how the company assessed it), then check Reg 30 announcements around the search date and CARO clause (vii)
for disputed dues.

</details>

**2.** Rank from least to most severe: disclaimer of opinion; qualified opinion; unmodified opinion with a material
uncertainty related to going concern; adverse opinion. Justify the position of the going-concern case.

<details markdown="1"><summary>Answer</summary>

Unmodified with going-concern uncertainty < qualified < adverse ≈ disclaimer (many analysts treat a disclaimer as
worse, since the auditor could not verify the accounts at all). The going-concern case is not a modification — the
accounts are fairly presented — but it flags survival risk: the statements are reliable, the *business* may not be.
Depending on the situation it can matter more to an equity holder than a narrow qualification.

</details>

**3.** A company's MD&A says "no key financial ratio changed by 25% or more". Receivable days went 60 → 72 → 86 over two
years. Show that each year's change in debtors turnover is below 25% while the two-year change is not.

<details markdown="1"><summary>Answer</summary>

Debtors turnover ≈ 365 ÷ receivable days: 6.08x → 5.07x → 4.24x. Year 1: 5.07/6.08 − 1 = −16.7%; year 2: 4.24/5.07 −
1 = −16.3%; two years: 4.24/6.08 − 1 = −30.2%. Each annual change is under 25%; the cumulative change is over 25%. The
MD&A rule is satisfied while the business deteriorates.

</details>

**4.** Using the Tungabhadra Foods example, suppose TF Retail's loss widens to ₹(40.0) Cr and nothing else changes.
What happens to consolidated PAT attributable to owners? Does the standalone PAT change?

<details markdown="1"><summary>Answer</summary>

Consolidated PAT = 120.0 + 15.0 − 40.0 + 3.0 = ₹98.0 Cr; less NCI 7.35 → **₹90.65 Cr** attributable to owners (down
₹18.0 Cr). Standalone PAT is **unchanged at ₹120.0 Cr** (it still books interest on the loan) unless the parent
impairs its loan or investment — which is exactly the judgement to look for in the standalone auditor's report and the
notes.

</details>

**5.** Kaveri's MD asks for a raise to ₹6.0 Cr. Using the FY26 numbers (PBT ₹121.0 Cr; proxy Sec 198 profit = PBT +
MD pay), does it need a special resolution under LODR Reg 17(6)(e)? Under Sec 197's 5% individual limit?

<details markdown="1"><summary>Answer</summary>

Proxy net profit = 121.0 + 6.0 = ₹127.0 Cr. Reg 17(6)(e) trigger = higher of ₹5 Cr or 2.5% × 127.0 = ₹3.18 Cr → ₹5 Cr;
₹6.0 Cr exceeds it → **special resolution needed** (the MD is a promoter). Sec 197 individual limit = 5% × 127.0 =
₹6.35 Cr; ₹6.0 Cr is within it. (The Sec 198 computation has specific adjustments; the proxy is for illustration.)

</details>

**6.** Name three CARO 2020 clauses you would read first for a working-capital-heavy small cap, and what each could
reveal.

<details markdown="1"><summary>Answer</summary>

(ii) — whether quarterly stock and debtor statements filed with banks agree with the books (differences suggest
inflated collateral or window-dressing); (ix) — loan defaults and use of short-term funds for long-term purposes
(liquidity mismatch); (vii) — undisputed statutory dues outstanding (cash stress) and disputed dues by forum. Also
acceptable: (iii) loans to group companies, (xvii) cash losses, (xix) material uncertainty about meeting liabilities.

</details>

**7.** Why does the diff approach in §8 flag "we target receivable days of 65 to 70 by FY26" disappearing, and why is
the *unchanged* sentence on related-party purchases also informative?

<details markdown="1"><summary>Answer</summary>

A specific, falsifiable target that disappears without comment usually means it was missed (FY26 actual: 96 days) —
management stopped committing to the number. The unchanged related-party sentence is informative because the
underlying amount grew (8.2% → 10.4% of material cost) while the disclosure stayed boilerplate: identical language
over a changing fact is a sign that the disclosure is not doing any work.

</details>

## Go deeper

- [Berkshire Hathaway shareholder letters](https://www.berkshirehathaway.com/letters/letters.html) — the benchmark for
  what a candid chairman's letter looks like; read two, then read an Indian letter.
- ICAI, *Implementation Guide to SA 701, Communicating Key Audit Matters* (2018) — how auditors choose and write KAMs;
  useful for reading between the lines.
- [CAG guidance note on CARO 2020](https://cag.gov.in/uploads/media/Guidance-note-on-CARO-2020-064e84867178ba9-47322653.pdf)
  — what each clause asks the auditor to check.
- [National Financial Reporting Authority (NFRA)](https://nfra.gov.in) — audit-quality inspection reports and orders
  against auditors of listed companies.
- Howard Schilit, Jeremy Perler & Yoni Engelhart, *Financial Shenanigans* (4th ed.) — which disclosures to read when
  something smells wrong.

---
[← Previous: 03.1 Where information lives](01-the-disclosure-universe.md) · [Module index](index.md) · [Next: 03.3 Notes to accounts →](03-notes-to-accounts.md)
