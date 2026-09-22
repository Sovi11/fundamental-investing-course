# 05.7 · Scuttlebutt & primary research

> **Why this matters:** everything in the previous six lessons came from documents the company itself wrote.
> Scuttlebutt is the discipline of checking those documents against the world — dealers, customers, competitors,
> ex-employees, government data, the shelf in a shop. It is where an individual investor's edge usually lies: the
> filings are read by everyone; the pump dealer in Coimbatore is spoken to by almost no one. It is also where the
> legal line between research and insider trading runs, so you need to know exactly where that line is.

**Learning objectives** — after this lesson you can:

- Design a scuttlebutt plan: whom to talk to, what to ask, how to avoid leading questions and confirmation bias.
- Use alternative data (app downloads, web traffic, job postings, e-commerce listings, Google Trends) and Indian
  government datasets (GST, VAHAN, SIAM, CEA, RBI, DGCA, commodity prices) to test a thesis.
- State the SEBI PIT rules on UPSI and the legal limits on expert networks and channel checks.
- Record and weight what you learn without over-fitting to anecdotes.
- Build a scuttlebutt plan for Kaveri Pumps.

**Prerequisites:** [05.1 Business models & unit economics](01-business-models-and-unit-economics.md),
[05.6 Corporate governance](06-corporate-governance-india.md)  ·  **Time:** ~75 min

---

## 1. Fisher's scuttlebutt

Philip Fisher (*Common Stocks and Uncommon Profits*, 1958) described the method: go around the company — to its
customers, suppliers, competitors, former employees, trade associations, research scientists — and ask what they
think of it. Any single source is biased; a dozen sources triangulate. Fisher's insight was that most of what you
need to know about a business's quality is known to the people who deal with it and is not in the annual report.

The modern version has three channels:

| Channel | What it tells you | Cost | Reliability |
|:--|:--|:--|:--|
| **Conversations** (dealers, customers, suppliers, ex-employees, competitors, industry consultants) | Product quality, service, pricing behaviour, inventory in the channel, management reputation, competitor moves | Time; travel; some money for expert networks | High when triangulated; each source biased |
| **Alternative data** (digital exhaust) | Demand trends, hiring, pricing, reviews, traffic — in near-real time | Low to moderate | Good for direction and turning points; noisy for levels |
| **Government and industry statistics** | Industry volumes, registrations, credit growth, prices, traffic | Free | High for the aggregate; company inference requires care |

## 2. Conversations: whom, and what to ask

### 2.1 Whom

| Source | Access | Best for | Bias to correct for |
|:--|:--|:--|:--|
| Dealers / distributors | Walk in; trade fairs; dealer lists on company websites | Sell-through vs sell-in, inventory in the channel, competitor schemes, credit terms, service quality | Talk their book; recent experience dominates |
| End customers (farmers, factories, doctors, contractors) | Field visits; forums; trade bodies | Why they buy; switching; price sensitivity | Small samples |
| Suppliers | Trade fairs; supplier lists in filings; industry contacts | Payment discipline, volumes, cost pressures | Fear of losing the customer |
| Former employees | LinkedIn; personal networks; expert networks | Culture, controls, real capacity utilisation, how numbers are made | Grievances; stale information; **confidentiality obligations** |
| Competitors | Their concalls (the best free source on any company is its competitor's call); trade fairs | Pricing behaviour, share, capacity plans | Self-serving |
| Industry consultants, trade associations, journalists | Reports; conferences | Structure, regulation, history | Generalists |
| Sell-side analysts | Reports; calls | Consensus view and what is priced in | Incentives ([03.5](../03-reading-filings/05-other-documents.md)) |

### 2.2 What to ask — and how

The craft is in the question. Leading questions ("Is Kaveri's service good?") get polite agreement. Open, comparative
and behavioural questions get information:

| Instead of | Ask |
|:--|:--|
| "Is Kaveri's service good?" | "When a pump fails in peak season, walk me through what happens — who comes, how fast, who pays?" |
| "Are sales growing?" | "How many units did you sell last summer vs this summer? What is sitting in your godown right now, and how old is it?" |
| "Is the brand strong?" | "If a farmer walks in and asks for a 1 HP submersible, what do you show him first, and why? What if brand X gives you ₹300 more margin?" |
| "Do state agencies pay?" | "Which tenders have you supplied against, and how many months did each take to pay? Which state is worst?" |
| "Is management good?" | "Who at the company do you deal with? Has that changed? What happened the last time you had a dispute?" |

Rules: ask for **numbers and stories**, not opinions; ask the same question of several sources in the same week;
ask each source who else you should talk to; write everything down immediately, including what surprised you; keep
a log of what you *expected* to hear so you can measure your own bias.

### 2.3 Weighting anecdotes

Five dealer conversations are not a survey. Treat them as *hypothesis generators* and *contradiction detectors*:

- If four of five dealers say channel inventory is 3–4 months (normal is 1–2), that is not proof — but it is a
  question for the next concall and a reason to look at the company's inventory days and receivable days again.
- If every source praises the product and the numbers show share loss, believe the numbers and ask what else is
  happening (pricing, distribution, a competitor's scheme).
- Record the date. Scuttlebutt decays fast.

## 3. Alternative data

| Data | Source (free unless noted) | What it proxies | Caveats |
|:--|:--|:--|:--|
| App downloads and ratings | Google Play / App Store pages; third-party trackers (paid) | Consumer-app demand, engagement | Installs ≠ active users; India skews Android |
| Web traffic | Similarweb (limited free tier) | E-commerce/D2C traffic trend | Sampled; shifts to apps |
| Job postings | Company careers pages; LinkedIn; Naukri | Expansion, new locations, hiring freezes; which skills (AI, EV) | Postings are cheap; look at *filled* roles via headcount disclosures |
| E-commerce listings, prices, reviews | Amazon/Flipkart/Blinkit pages | Pricing, discounting, review velocity, stock-outs, private-label competition | Manual; snapshot noise |
| Google Trends | trends.google.com | Brand search interest, category seasonality, regional demand | Relative index, not volume |
| Satellite / footfall | Paid | Parking lots, plant activity, port traffic | Expensive; mostly institutional |
| Tender portals | GeM, state e-procurement portals, CPPP | Government orders won/lost, prices bid (for Kaveri's solar segment: which states, what price per HP, who else bid) | Manual; formats vary |
| Patent and regulatory filings | Indian Patent Office; CDSCO; USFDA (for pharma: inspections, 483s, warning letters) | Pipeline, compliance | — |

The most useful of these for a small-cap Indian industrial is often the least glamorous: tender portals. For
Kaveri, every PM-KUSUM tender is public — winner, price, quantity, state — and so is each state agency's record of
paying (from other suppliers' filings and rating rationales).

## 4. Indian government and industry data

| Dataset | Publisher | Frequency | Use |
|:--|:--|:--|:--|
| GST collections | Ministry of Finance / GSTN press releases | Monthly | Aggregate demand; state-level activity |
| E-way bills | GSTN | Monthly | Goods movement |
| VAHAN vehicle registrations | Ministry of Road Transport (vahan.parivahan.gov.in dashboard) | Daily/monthly | Retail auto sales by segment, maker, state — the best real-time demand series for autos, CV finance (Nirmal) and tractor demand |
| SIAM / FADA | Industry bodies | Monthly | Wholesale (SIAM) vs retail (FADA) auto volumes |
| CEA power data | Central Electricity Authority | Monthly | Generation, PLF, demand by state — utilities, and rural electrification for pumps |
| RBI sectoral credit, ECB, banking statistics | RBI DBIE | Monthly/quarterly | Credit growth by sector, NBFC funding conditions, deposit rates |
| DGCA traffic | DGCA | Monthly | Airline passengers, load factors, market share |
| Commodity prices | MCX, LME (copper), SteelMint (paid), Ministry of Mines | Daily | Input costs (Kaveri: copper, steel); realisations (metals) |
| IMD monsoon data | India Meteorological Department | Daily in season | Rural demand (pumps, tractors, two-wheelers, FMCG) |
| Agricultural data | Agmarknet (mandi prices), Ministry of Agriculture | Daily/seasonal | Farm incomes → rural demand |
| Telecom subscribers | TRAI | Monthly/quarterly | ARPU, subscriber share |
| MOSPI (IIP, CPI, GDP) | Ministry of Statistics | Monthly/quarterly | Macro |
| Real-estate registrations | State registration departments; PropEquity/Anarock (paid) | Monthly | Housing demand by city |

Inference from aggregate data to a company requires the company's share and mix: strong VAHAN tractor registrations
help Nirmal's tractor book; a weak monsoon in Tamil Nadu and Karnataka matters more to Kaveri than the all-India
figure.

## 5. The legal line: UPSI, PIT and what you may not do

India's SEBI (Prohibition of Insider Trading) Regulations, 2015 prohibit trading while in possession of
**unpublished price-sensitive information (UPSI)** — information about a company or its securities, not generally
available, which would materially affect the price if published: financial results, dividends, capital changes,
M&A, changes in KMP, and (after the 2025 amendments) a broader list of events such as fund-raising, agreements
affecting control, fraud or defaults, regulatory actions and rating changes ([SEBI PIT Regulations as amended to
March 2025](https://www.sebi.gov.in/legal/regulations/mar-2025/securities-and-exchange-board-of-india-prohibition-of-insider-trading-regulations-2015-last-amended-on-march-12-2025-_92672.html);
[Taxmann summary](https://www.taxmann.com/post/blog/sebi-amends-pit-regulations-expands-scope-of-unpublished-price-sensitive-information)).
"Insider" includes anyone who has received UPSI, however obtained. Penalties under the SEBI Act run up to ₹25 Cr or
three times the profit, whichever is higher, plus possible prosecution and market bans.

The practical boundaries for a researcher:

| Allowed (generally) | Not allowed |
|:--|:--|
| Asking a dealer how *his* sales are going, what stock he holds, what competitors offer | Asking (or accepting from) a company employee the company's unpublished quarterly numbers, order wins, deal talks |
| Talking to former employees about how the business works, culture, processes — *provided they do not breach their confidentiality obligations and do not disclose UPSI* | Receiving from a current or former employee non-public material information (e.g., "the state has told us they won't pay") and trading on it |
| Reading public tender results, regulatory filings, government data | Obtaining unpublished tender outcomes from officials |
| Attending public concalls, AGMs, investor days; asking management questions in those forums | Private, selective disclosure by management of UPSI to you (also a violation *by them* — LODR Reg 30 requires prompt public disclosure of material events) |
| Using expert networks whose experts are screened and instructed not to share confidential information about current/former employers | Using expert networks to obtain confidential or price-sensitive information; note the "mosaic theory" is a US concept and SEBI's regime is stricter in practice |
| Aggregating many non-material public and private data points into a view | Trading on a single non-public material fact, however obtained |

If a conversation strays into something that sounds like UPSI — a specific unpublished number, a deal, a regulatory
action — stop the conversation, do not trade the stock until the information is public, and write down what
happened. SEBI has pursued cases built on WhatsApp forwards of results and on "pre-positioning" ahead of
televised tips ([Multibagg summary of recent cases](https://www.multibagg.ai/market-pulse/articles/insider-trading-sebi-latest-cases-cmroluwyhf81ws60j2ffkd4mx));
the standard is possession, not source.

!!! warning "This is not legal advice"
    The table summarises the regulations as of September 2026 for an individual investor. Regulations, SEBI's
    interpretation and case law change. If you run money for others or use expert networks systematically, get
    compliance advice and keep a research log that shows what you knew and when.

## 6. A scuttlebutt plan for Kaveri Pumps

The thesis question after Modules 04–05: *are the solar receivables collectible and is the agri franchise intact?*
Design the work around it.

| # | Question | Source | Method | What would change my view |
|:--|:--|:--|:--|:--|
| 1 | How do dealers in Kaveri's top three states rate service and pricing vs the two biggest rivals? | 8–10 dealers (Coimbatore, Salem, Hubballi, Rajkot) — dealer locator on company website | Visits/calls; the "walk me through a failure" question; ask what scheme each brand is running this season | Consistent reports of share loss or channel stuffing (3+ months inventory) |
| 2 | What is in the channel right now? | Same dealers | "How many units in stock; when bought" | Dealer inventory > 2 months in September (off-peak) |
| 3 | Which states' solar tenders has Kaveri won, at what price, and how do those states pay? | State e-procurement portals; MNRE PM-KUSUM dashboards; rating rationales of *other* solar-pump suppliers naming state delays | Build a table: state, tender, price/HP, quantity, Kaveri's share, average days to payment reported by peers | Evidence that the two overdue states have paid other suppliers (Kaveri-specific problem) or have paid nobody (systemic) |
| 4 | Is Kaveri Castings' pricing fair? | Two independent foundries in the Coimbatore cluster | "What would you charge per kg for these castings at this volume?" | Kaveri Castings' implied price per kg > 10% above market |
| 5 | How is the Hosur motors plant doing? | Job postings (Hosur roles), LinkedIn headcount trend, one or two ex-employees on process (not numbers) | Track postings monthly | Hiring freeze or senior operations exits |
| 6 | What is the monsoon and irrigation outlook in Kaveri's states? | IMD, state agriculture departments, CEA rural feeder data | Monthly check | Deficient monsoon in TN/KA/AP → weak Q3–Q4 agri demand |
| 7 | What do competitors say about tender pricing and receivables? | Concall transcripts of listed pump peers | Read the last four calls for "solar", "receivable", "state" | Peers reporting the same delays (systemic, likelier to resolve) vs peers collecting (Kaveri-specific) |
| 8 | Copper and steel cost trajectory vs Kaveri's price list | LME/MCX copper; dealer price lists | Compare price-list changes with input moves | Price-list cuts under competitive pressure while copper is flat |

Budget: three weeks of evenings and two field days. Output: a two-page note with the table above filled in, each
row tagged with confidence and date, feeding the memo in [11.3](../11-process/03-writing-an-investment-memo.md).

!!! tip "Trader's lens"
    Scuttlebutt is how a fundamental investor gets the order-flow information a market-maker gets for free.
    A dealer telling you inventory is piling up is the equivalent of seeing the offer stack build. Treat it the same
    way: it is a signal about the direction of the next print, not its size, and it is worthless if everyone else
    already has it — which is why calling ten dealers beats reading one broker's channel check.

!!! warning "Common mistakes"
    - Asking leading questions and hearing what you hoped.
    - Stopping after the first two conversations because they agreed with the thesis.
    - Treating a former employee's confidential information as a research coup rather than a legal problem.
    - Inferring company performance from industry data without the company's share and mix.
    - Not writing it down — three weeks later you remember the anecdote, not the date or the caveat.
    - Letting scuttlebutt override the numbers instead of interrogating them.

## Key terms

| Term | Meaning |
|:--|:--|
| **Scuttlebutt** | Fisher's term for gathering information about a company from the people who deal with it |
| **Channel check** | Asking dealers/distributors about sell-through, inventory and competition |
| **Sell-in vs sell-through** | Company's sales to the channel vs the channel's sales to end customers |
| **Channel inventory** | Stock held by dealers/distributors; a leading indicator of future sell-in |
| **Alternative data** | Non-traditional data (web, app, satellite, job postings) used to infer business activity |
| **Expert network** | A paid service connecting investors with industry experts, subject to compliance rules |
| **UPSI** | Unpublished price-sensitive information as defined by SEBI's PIT Regulations |
| **Insider (PIT)** | Anyone connected to the company or in possession of UPSI |
| **Mosaic theory** | The (US) idea that assembling non-material pieces into a material conclusion is legitimate; treat with caution in India |
| **VAHAN / SIAM / FADA** | Vehicle registration database / manufacturers' wholesale data / dealers' retail data |
| **CEA / TRAI / DGCA** | Central Electricity Authority / telecom regulator / aviation regulator — sources of sector data |
| **Research log** | Dated record of what you learned, from whom, and what you expected — for bias control and compliance |

## Check your understanding

1. Rewrite "Do customers like the product?" as three scuttlebutt questions for a two-wheeler dealer.
<details><summary>Answer</summary>"Which two models did you sell most last month, and what did buyers say when they
chose between them?" "When a customer comes back with a complaint in the first year, what is it usually about?"
"If the rival brand's finance partner offers a lower EMI this month, how many of your walk-ins switch?"</details>

2. A dealer tells you that Kaveri's regional manager mentioned "the Q2 numbers will be bad". Can you trade on that?
<details><summary>Answer</summary>No. Unpublished quarterly results are UPSI; you are now an insider in possession
of it regardless of how it reached you. Do not trade until results are public; note the incident in your log. The
regional manager (and the company) may also have breached PIT rules.</details>

3. VAHAN shows tractor registrations up 18% YoY in Maharashtra and MP. How does that bear on Nirmal Finance, and
   what could still go wrong?
<details><summary>Answer</summary>Nirmal's tractor book (20% of AUM) is in those states, so disbursement demand is
likely strong. It says nothing about credit quality: a registration surge on easy credit can precede higher
delinquencies; and Nirmal's *share* of financing may fall if banks are aggressive. Check disbursement mix and
early-bucket delinquencies in the next results.</details>

4. Why is a competitor's concall often the best free source about a company?
<details><summary>Answer</summary>Competitors describe the same market — pricing, tender behaviour, state payment
delays, input costs — without the incentive to flatter the company you are studying, and analysts ask them about
it directly. Discrepancies between two companies' descriptions of the same market are where the research starts.</details>

5. Design one alternative-data check for the claim "our new Hosur plant is ramping well".
<details><summary>Answer</summary>Track job postings and LinkedIn headcount tagged to Hosur monthly (operators,
quality, maintenance roles); compare with disclosed capacity utilisation each quarter; a plant ramping from 57%
should show steady hiring, not a freeze. Cross-check with CEA/state discom industrial power-consumption data for
the Hosur feeder if available.</details>

## Go deeper

- Philip Fisher, *Common Stocks and Uncommon Profits* (1958), chapter 2, "What 'Scuttlebutt' Can Do".
- SEBI (Prohibition of Insider Trading) Regulations, 2015 (as amended) — Regulations 2(1)(n) (UPSI), 3 and 4;
  read them once in full.
- The VAHAN dashboard (vahan.parivahan.gov.in) and the CEA monthly reports — spend an hour learning to pull the
  series you will use repeatedly.
- Sources for this lesson: [SEBI PIT Regulations (Mar-2025 consolidated)](https://www.sebi.gov.in/legal/regulations/mar-2025/securities-and-exchange-board-of-india-prohibition-of-insider-trading-regulations-2015-last-amended-on-march-12-2025-_92672.html);
  [Taxmann on the expanded UPSI definition](https://www.taxmann.com/post/blog/sebi-amends-pit-regulations-expands-scope-of-unpublished-price-sensitive-information).

---
[← Previous: 05.6 Corporate governance — the India edition](06-corporate-governance-india.md) · [Module index](index.md) · [Next: 06.1 What value is →](../06-valuation/01-what-is-value.md)
