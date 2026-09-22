# 04.2 · Margins & cost structure

> **Why this matters:** growth tells you how big the business is getting; margins tell you how much of each rupee of
> sales survives to shareholders — and, more importantly, *why*. A company whose gross margin is stable through a
> commodity spike has pricing power. A company whose EBITDA margin expands as it grows has operating leverage. Both
> are worth more than the same profit earned by luck.

**Learning objectives** — after this lesson you can:

- Build and read a common-size income statement and explain what each margin layer (gross, EBITDA, EBIT, PAT)
  is telling you.
- Split a cost base into fixed and variable components, compute contribution margin, break-even revenue and the
  degree of operating leverage, and forecast how profit responds to a revenue change.
- Explain raw-material pass-through, lags and mix effects, and separate them in a margin bridge.
- Judge whether a margin is sustainable using peer levels, history and the pricing-power evidence in the gross margin.
- Apply all of this to Kaveri Pumps FY21–FY26 and diagnose what drove its margin peak and decline.

**Prerequisites:** [02.3 The income statement](../02-accounting/03-the-income-statement.md),
[04.1 Growth analysis](01-growth-analysis.md)  ·  **Time:** ~90 min

---

## 1. The margin ladder and what each rung measures

A **margin** is a profit subtotal divided by revenue. The four that matter, and what each isolates:

| Margin | Formula | What it measures | Typical India ranges (indicative) |
|:--|:--|:--|:--|
| **Gross margin** | (Revenue − cost of goods) ÷ revenue | Pricing power over customers and suppliers; product economics before any overheads | Commodity processors 10–20%; auto components 25–40%; pumps/engineering 30–40%; FMCG 45–60%; software 65–80%; pharma formulations 60–70% |
| **EBITDA margin** | EBITDA ÷ revenue | Operating efficiency after overheads (people, power, freight, marketing) but before the cost of the asset base | Contract manufacturing 5–10%; engineering 12–18%; FMCG 20–25%; IT services 20–28%; cement 15–25% (cyclical) |
| **EBIT margin** | EBIT ÷ revenue | Operating profit after depreciation — the honest operating margin for asset-heavy businesses | — |
| **PAT margin** | PAT ÷ revenue | What is left after financing and tax; mixes operating performance with capital structure | — |

The ladder is read top-down. If **gross margin** moves, the cause lies in price, input cost or product mix. If gross
margin is stable but **EBITDA margin** moves, the cause is overheads — scale, marketing, one-off costs. If EBITDA
margin is stable but **EBIT margin** moves, it is depreciation (a new plant). If EBIT margin is stable but **PAT
margin** moves, it is interest, other income, exceptional items or tax. This diagnostic order is the whole skill.

!!! info "India notes"
    Indian P&Ls classify expenses by nature, so gross margin must be built: cost of goods = cost of materials
    consumed + purchases of stock-in-trade + change in inventories. Screener.in's "OPM" is EBITDA margin
    **excluding** other income; many broker reports quote EBITDA **including** other income. When two sources
    disagree by a percentage point, this is usually why.

## 2. Common-size statements: Kaveri FY21–FY26

Divide every line by revenue. Numbers are ₹ Cr from the [running example](../appendix/running-example/kaveri-pumps.md);
percentages are computed with `tools/fi/ratios.margins`.

| % of revenue | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| Revenue (₹ Cr) | 612.0 | 758.0 | 874.0 | 1,006.0 | 1,172.0 | 1,318.0 |
| Materials | 64.0 | 67.0 | 65.8 | 63.2 | 64.4 | 65.1 |
| **Gross margin** | **36.0** | **33.0** | **34.2** | **36.8** | **35.6** | **34.9** |
| Employees | 10.2 | 9.2 | 9.1 | 9.0 | 8.8 | 8.9 |
| Other expenses | 12.8 | 11.8 | 12.0 | 12.4 | 12.1 | 12.2 |
| **EBITDA margin** | **13.0** | **12.0** | **13.1** | **15.4** | **14.7** | **13.8** |
| Depreciation & amortisation | 4.3 | 3.7 | 3.4 | 3.3 | 3.8 | 3.6 |
| **EBIT margin** | **8.7** | **8.3** | **9.7** | **12.1** | **10.9** | **10.2** |
| Finance costs | 1.1 | 0.8 | 1.0 | 1.3 | 1.4 | 1.3 |
| Other income + exceptional | −0.4 | 0.8 | 0.8 | 0.7 | 1.6 | 0.3 |
| **PAT margin** | **5.4** | **6.2** | **7.2** | **8.6** | **8.3** | **6.9** |

Reading it top-down:

- **FY22:** gross margin fell 300 bps (36.0 → 33.0) — the post-COVID copper and steel spike hit a company that
  prices its pumps to dealers once or twice a year. Overheads fell as a percentage because revenue grew 24% on a
  largely fixed base: EBITDA margin fell only 100 bps. *Operating leverage cushioned a pricing-power problem.*
- **FY23–FY24:** gross margin recovered to 36.8% as price increases caught up with costs and the industrial mix
  helped; employee costs kept shrinking as a share of sales. EBITDA margin peaked at 15.4%.
- **FY25–FY26:** gross margin slid 190 bps from the peak — solar pumping systems (bought-in panels, tender pricing)
  went from 14% to 27% of sales. Depreciation stepped up when the Hosur plant was capitalised. PAT margin in FY25
  was propped up by the ₹14 Cr land gain (1.2% of revenue); strip it and FY25 PAT margin is 7.4%, so the decline
  into FY26 is gentler than the reported 8.3 → 6.9.

The lesson: the *level* of Kaveri's margin is average for Indian engineering; the *direction* since FY24 is down and
the cause is **mix** (a lower-margin segment growing fastest), not costs running out of control. That distinction
decides whether you expect mean reversion.

## 3. Fixed and variable costs

Every cost line is somewhere between purely **variable** (moves one-for-one with volume: raw materials, freight,
sales commissions, payment-gateway fees) and purely **fixed** (does not move with volume in the short run: plant
depreciation, salaried staff, rent, software licences). Reality is a mix — "semi-variable" costs with a fixed
core and a variable top-up — and most costs are fixed over a quarter and variable over five years.

Why it matters: the split determines how profit responds to a change in revenue.

$$\text{Contribution} = \text{Revenue} − \text{Variable costs} \qquad
\text{Contribution margin (CM)} = \frac{\text{Contribution}}{\text{Revenue}}$$

$$\text{EBIT} = \text{Contribution} − \text{Fixed costs} \qquad
\text{Break-even revenue} = \frac{\text{Fixed costs}}{\text{CM}}$$

### 3.1 Estimating the split for Kaveri (FY26)

Annual reports do not label costs as fixed or variable; you estimate. A reasonable first cut for a pump maker:
materials 100% variable; employee costs and other expenses ~60% fixed (salaried staff, plant overheads, rent, IT)
and ~40% variable (contract labour, freight, power for production, dealer incentives); depreciation 100% fixed.

```python
rev, mat, emp, oth, da, ebit = 1318.0, 858.0, 117.3, 160.8, 47.8, 134.1
variable = mat + 0.4 * (emp + oth)          # 969.2
fixed = 0.6 * (emp + oth) + da              # 214.7
contribution = rev - variable               # 348.8
cm = contribution / rev                     # 26.5%
breakeven = fixed / cm                      # 811.2
dol = contribution / ebit                   # 2.60
print(round(contribution,1), round(cm,3), round(fixed,1), round(breakeven,1), round(dol,2))
# 348.8 0.265 214.7 811.2 2.6
```

So Kaveri earns about 26.5 paise of contribution on each extra rupee of sales, carries ~₹215 Cr of fixed costs,
breaks even at ~₹810 Cr of revenue (it did ₹1,318 Cr — a comfortable 38% cushion), and has a **degree of operating
leverage of 2.6**: a 10% change in revenue moves EBIT by roughly 26%, *if* margins per unit hold.

### 3.2 Degree of operating leverage (DOL)

$$\text{DOL} = \frac{\%\Delta \text{EBIT}}{\%\Delta \text{Revenue}} = \frac{\text{Contribution}}{\text{EBIT}} = 1 + \frac{\text{Fixed costs}}{\text{EBIT}}$$

You can measure it two ways: structurally (contribution ÷ EBIT, as above) or empirically from history. The
empirical version is noisy because price and mix move at the same time as volume:

| Period | Revenue growth | EBIT growth | Empirical DOL |
|:--|--:|--:|--:|
| FY23 → FY24 | +15.1% | +44.3% | 2.9 |
| FY24 → FY25 | +16.5% | +4.8% | 0.3 |
| FY25 → FY26 | +12.5% | +4.8% | 0.4 |

FY24 shows the structural leverage working (2.9 ≈ the 2.6 estimate). FY25 and FY26 show it being *overridden* by
gross-margin erosion from mix — which is the point: DOL tells you what happens to profit when volume changes with
everything else constant; the gross margin tells you whether everything else is constant.

!!! tip "Trader's lens"
    Operating leverage is the **gamma of a business**. A high-fixed-cost company (airline, hotel, steel mill,
    exchange) has convex profits: small revenue moves produce large profit moves, in both directions. A
    variable-cost business (distributor, contract manufacturer) is nearly linear. When you pay a high multiple
    for an operationally levered company near its break-even, you are long gamma at a bad strike — the payoff is
    explosive but the theta (fixed costs) bleeds every quarter that volume disappoints. Cyclical troughs are where
    that convexity is cheapest; [07.3](../07-special-valuation/03-cyclicals-and-commodities.md) builds on this.

### 3.3 A second worked example — a QSR chain

**Tandoor Express Ltd** (fictional) runs 200 restaurants. Per store per year (₹ lakh): revenue 240; food & packaging
cost 30% of revenue; delivery commissions 8% of revenue; staff 60 (mostly fixed); rent 36 (fixed, under Ind AS 116
this is D&A + interest, but treat as fixed cost here); utilities 12 (half fixed); depreciation 18.

```python
rev = 240.0
var = 0.30 * rev + 0.08 * rev + 6          # food, delivery, variable half of utilities = 97.2
fixed = 60 + 36 + 6 + 18                   # 120
contrib = rev - var                        # 142.8; CM 59.5%
ebit = contrib - fixed                     # 22.8; margin 9.5%
be = fixed / (contrib / rev)               # 201.7 lakh per store
dol = contrib / ebit                       # 6.3
for g in (-0.10, 0.10, 0.20):
    print(g, round((rev*(1+g) - var*(1+g) - fixed), 1))
# -0.1 → 8.5 ; +0.1 → 37.1 ; +0.2 → 51.4
```

Store-level EBIT is ₹22.8 lakh (9.5%) with a DOL of 6.3: a 10% fall in same-store sales cuts store profit by 63%;
a 20% rise more than doubles it. This is why QSR stocks trade on **same-store sales growth (SSSG)** prints and why
a chain that keeps adding stores while SSSG is negative can show revenue growth and collapsing profit at the same
time. [08.3](../08-sectors/03-consumer.md) uses these unit economics.

## 4. Raw-material pass-through, lags and the gross margin

For manufacturers, the gross margin is a tug-of-war between input costs and selling prices. Three questions:

1. **Can the company pass cost increases on?** Evidence: gross margin *percentage* stable while raw-material prices
   swing (paints, FMCG leaders, branded pumps). If gross margin *per unit* in rupees is stable but the percentage
   falls when inputs rise, the company passes through cost but not margin — common in auto components with
   contractual pass-through clauses.
2. **With what lag?** Contractual quarterly resets (auto ancillaries), annual price lists (pumps, appliances),
   tender-locked prices (solar, EPC, defence — no pass-through at all until the next tender). Lag creates a
   predictable margin squeeze and rebound: for Kaveri, copper spiked in FY22 and the margin recovered in FY23–24.
3. **What is mix doing?** A rising share of low-margin products lowers the blended gross margin even when every
   product's own margin is unchanged. This is Kaveri's FY25–26 story. You can separate it with a margin bridge.

### 4.1 A margin bridge (mix vs rate)

Suppose Kaveri's segment gross margins in FY24 were agri 40%, industrial 36%, solar 22% (fictional detail
consistent with the blended 36.8%), and in FY26 they were agri 40%, industrial 36%, solar 24%. Segment shares moved
from 57/29/14 to 46/27/27.

```python
fy24 = {'agri': (0.57, 0.40), 'ind': (0.29, 0.36), 'solar': (0.14, 0.22)}
fy26 = {'agri': (0.46, 0.40), 'ind': (0.27, 0.36), 'solar': (0.27, 0.24)}
gm24 = sum(w*m for w, m in fy24.values())                    # 36.32%
gm26 = sum(w*m for w, m in fy26.values())                    # 34.60%
mix_effect  = sum(fy26[s][0]*fy24[s][1] for s in fy24) - gm24   # new weights, old margins: −2.26 pp
rate_effect = gm26 - (gm24 + mix_effect)                        # +0.54 pp
print(round(gm24*100,2), round(gm26*100,2), round(mix_effect*100,2), round(rate_effect*100,2))
# 36.32 34.6 -2.26 0.54
```

The bridge says the ~170 bps decline is entirely **mix** (−226 bps) partly offset by **rate** (+54 bps: solar
margins actually improved). That is a different — and less alarming — conclusion than "Kaveri is losing pricing
power". It also tells you what to model: if solar keeps growing faster than the rest, the blended margin keeps
falling even if nothing goes wrong.

## 5. Are margins sustainable? Mean reversion and the evidence for pricing power

Margins mean-revert. Above-average margins attract competition and capacity (the capital cycle,
[05.4](../05-business-analysis/04-capital-cycle-and-competition.md)); below-average margins drive exits and price
discipline. The exceptions — companies that hold 20–25% EBITDA margins for decades — are the ones with a moat
([05.3](../05-business-analysis/03-moats-and-competitive-advantage.md)). Before extrapolating a margin, check:

| Test | What to look at | Kaveri |
|:--|:--|:--|
| History | 10-year range and where the current margin sits in it | EBITDA 12.0–15.4% over six years; FY26 at 13.8% is mid-range |
| Peers | Same-segment peers' margins (the running example's fictional peer set: 11.5–16.8%) | Mid-pack; Nilgiri Pumps at 16.8% shows what a stronger brand/mix earns |
| Gross-margin stability through input cycles | Std. dev. of gross margin vs std. dev. of key input prices | ±1.5 pp swings vs copper ±30%: decent but lagged pass-through |
| Mix trajectory | Which segments are growing and at what margin | Lower-margin solar growing fastest → structural pressure |
| Scale economies | Fixed costs as % of sales falling with growth | Employees 10.2% → 8.9%: yes |
| One-offs inside opex | Exceptional items, provisions, ESOP charges | FY25 land gain (below EBITDA); ECL provision arguably too low (flatters other expenses) |

A last, quantitative sanity check: **what is one percentage point of gross margin worth?** For Kaveri, 1% of
revenue is ₹13.2 Cr, which is 9.8% of FY26 EBIT. A 2-pp mix-driven slide — the FY24→FY26 experience — is a fifth of
operating profit. Small margin numbers, big profit numbers: that asymmetry is why margin analysis comes before
growth analysis in most analysts' heads, even though this course teaches them the other way round.

!!! warning "Common mistakes"
    - Comparing EBITDA margins across companies with different lease intensity: since Ind AS 116 (FY20), rent
      sits in depreciation and interest, so retailers' and airlines' EBITDA margins jumped without any economic
      change. Use EBIT or pre-Ind AS 116 EBITDA for cross-period comparisons.
    - Treating a mix-driven margin decline as a pricing-power problem (or the reverse). Do the bridge.
    - Applying DOL to a period where gross margin also moved — it only isolates volume.
    - Ignoring other income when comparing "EBITDA" from different sources.
    - Extrapolating peak margins from the top of a commodity cycle (chemicals FY22, steel FY22).
    - Forgetting that a percentage margin can rise while rupee profit falls (shrinking revenue with fixed costs cut).

## Key terms

| Term | Meaning |
|:--|:--|
| **Common-size statement** | Each P&L line expressed as a percentage of revenue |
| **Gross margin** | (Revenue − cost of goods) ÷ revenue; the pricing-power layer |
| **EBITDA / EBIT / PAT margin** | Successive profit subtotals ÷ revenue |
| **Variable cost** | Cost that moves proportionally with volume (materials, freight, commissions) |
| **Fixed cost** | Cost that does not change with volume in the short run (depreciation, salaried staff, rent) |
| **Contribution margin** | (Revenue − variable costs) ÷ revenue; the profit on each incremental unit before fixed costs |
| **Break-even revenue** | Fixed costs ÷ contribution margin |
| **Degree of operating leverage (DOL)** | %ΔEBIT ÷ %Δrevenue = contribution ÷ EBIT; profit's sensitivity to volume |
| **Pass-through** | The ability and speed with which input-cost changes are reflected in selling prices |
| **Mix effect** | Change in a blended margin caused by the weights of segments/products shifting |
| **Rate effect** | Change in a blended margin caused by segments' own margins changing |
| **Margin bridge** | Decomposition of a margin change into mix, rate (price/cost) and volume/scale components |
| **Mean reversion** | The tendency of abnormal margins to move back toward industry norms as competition responds |
| **SSSG** | Same-store sales growth — revenue growth from stores open more than a year |

## Check your understanding

1. Kaveri's employee costs fell from 10.2% to 8.9% of revenue between FY21 and FY26 while revenue more than doubled.
   Is this cost cutting or operating leverage? How would you tell?
<details><summary>Answer</summary>Almost certainly operating leverage: absolute employee cost rose 88% (62.4 →
117.3) while revenue rose 115%, so the base is growing but slower than sales, as a partly fixed cost should. Cost
cutting would show absolute costs flat or falling, headcount down, or a VRS (Kaveri did have one in FY21). Check
headcount (2,310 → 2,480) and revenue per employee.</details>

2. Using the FY26 fixed/variable split above, estimate Kaveri's EBIT if FY27 revenue falls 8% with unchanged
   contribution margin.
<details><summary>Answer</summary>Contribution = 348.8 × 0.92 = 320.9; EBIT = 320.9 − 214.7 = ₹106.2 Cr, a 20.8%
decline (≈ 2.6 × 8%). Reported Q1 FY27 already showed EBITDA margin down to 12.6% on +3.5% revenue — margin
slippage is compounding the leverage.</details>

3. Company A: gross margin 55%, EBITDA margin 12%. Company B: gross margin 25%, EBITDA margin 12%. Which likely has
   pricing power, and which has the higher operating leverage?
<details><summary>Answer</summary>A has pricing power (high gross margin) but spends 43% of revenue on overheads
(marketing, staff) — typical of a consumer brand or software firm; its DOL is high because so much cost is fixed.
B is a lean processor/distributor with little pricing power and mostly variable costs; low DOL. Same EBITDA margin,
very different businesses and risk.</details>

4. Redo the margin bridge if solar's FY26 margin had stayed at 22%. What would the blended margin be?
<details><summary>Answer</summary>0.46×0.40 + 0.27×0.36 + 0.27×0.22 = 0.184 + 0.0972 + 0.0594 = 34.06%; the
whole decline (−2.26 pp) would be mix, with zero rate effect.</details>

5. A retailer's EBITDA margin rose from 8% in FY19 to 13% in FY20 with no change in sales or gross margin. What
   happened?
<details><summary>Answer</summary>Ind AS 116 took effect for FY20: store rents moved out of other expenses into
depreciation (ROU assets) and finance costs (lease liabilities). EBITDA rose mechanically; EBIT and PAT barely
moved. Compare EBIT margins, or add lease payments back to get a pre-116 EBITDA.</details>

6. Why can a company report a rising EBITDA margin and falling EBITDA in the same year?
<details><summary>Answer</summary>Revenue fell and management cut variable and some fixed costs faster than revenue
fell (or mix shifted toward higher-margin products as volume shrank). Margin percentages are ratios; rupee profit is
what pays dividends. Always look at both.</details>

## Go deeper

- Michael Mauboussin & Dan Callahan, *Operating Leverage* (Credit Suisse/Morgan Stanley research note, 2016) — the
  clearest practitioner treatment of DOL and why it is hard to measure.
- Any Indian auto-component company's investor presentation — look for the raw-material pass-through clause
  language and lag.
- Asian Paints and Pidilite annual reports across the FY21–FY23 crude-derivative spike — a live study of pricing
  power in the gross margin (see [case I2](../13-case-studies/india/02-asian-paints-compounder.md)).
- Screener.in "Profit & Loss" tab for any company — the OPM row is the EBITDA margin excluding other income; check
  it against your own common-size table.

---
[← Previous: 04.1 Growth analysis](01-growth-analysis.md) · [Module index](index.md) · [Next: 04.3 Returns on capital →](03-returns-on-capital.md)
