# 04.3 · Returns on capital: ROE, ROCE, ROIC

> **Why this matters:** a business is a machine that turns capital into profit. Growth and margins describe the
> output; return on capital describes the *efficiency of the machine* — how much profit each rupee tied up in it
> produces. It is the single number that most separates businesses worth paying up for from businesses that merely
> get bigger, because growth only creates value when the return on the new capital exceeds its cost.

**Learning objectives** — after this lesson you can:

- Define and compute ROE, ROCE and ROIC correctly, including what goes in the denominator, why averages are used,
  and how cash, goodwill, leases and CWIP are treated.
- Decompose ROE with the 3-step and 5-step DuPont identities and say which lever moved.
- Explain why a high ROE can be a leverage artefact, and why ROIC vs WACC is the value-creation test.
- Compute incremental ROIC and the reinvestment identity (growth = reinvestment rate × ROIC).
- Apply all of this to Kaveri FY21–FY26 and explain the rise to FY24 and the decline since.

**Prerequisites:** [02.4 The balance sheet](../02-accounting/04-the-balance-sheet.md),
[04.2 Margins & cost structure](02-margins-and-cost-structure.md)  ·  **Time:** ~100 min

---

## 1. Three ratios, three questions

All return ratios have the same shape — a profit measure over the capital that generated it — and the art is
matching numerator to denominator. Each answers a different question:

| Ratio | Numerator | Denominator | Question it answers | Who uses it |
|:--|:--|:--|:--|:--|
| **ROE** — return on equity | PAT (attributable to owners) | Average shareholders' equity | What do *shareholders* earn on the book value they have in the business, after everyone else is paid? | Equity investors, bank analysts (it is *the* bank metric) |
| **ROCE** — return on capital employed | EBIT (usually + other income; pre-tax) | Average capital employed = equity + all borrowings (+ lease liabilities) | What does the *whole* business earn on all long-term money, before tax and financing? | Indian sell-side and management (the dominant Indian convention) |
| **ROIC** — return on invested capital | NOPAT = EBIT × (1 − tax rate) | Average invested capital = net operating assets (fixed assets + net working capital), excluding cash and financial investments | What does the *operating* business earn, after tax, on the capital actually invested in operations? Compare directly with WACC. | Valuation work, DCF, quality investors |

The relationship: ROE is the shareholder's view (after leverage and tax); ROCE is the lender-plus-shareholder view
(before tax); ROIC is the operating view (after tax, excluding financial assets). All three should be computed on
**average** capital (opening + closing)/2 because the profit was earned over the year while the balance sheet is a
year-end snapshot; a fast-growing company's closing capital overstates what was available on average.

## 2. Getting the denominators right

This is where most published numbers go wrong. For Kaveri at 31-Mar-2026 (₹ Cr, from the
[running example](../appendix/running-example/kaveri-pumps.md)):

| Component | ₹ Cr | Equity | Capital employed | Invested capital |
|:--|--:|:--:|:--:|:--:|
| Total equity | 706.1 | ✓ | ✓ | — |
| Non-current borrowings | 92.0 | | ✓ | — |
| Current borrowings | 96.0 | | ✓ | — |
| Lease liabilities | 18.2 | | ✓ | — |
| **Capital employed** | **912.3** | | | |
| Net block (PP&E) | 495.3 | | | ✓ |
| CWIP | 2.0 | | | ✓ |
| Right-of-use assets | 16.5 | | | ✓ |
| Intangibles | 8.0 | | | ✓ |
| Inventories + receivables + other current assets | 574.3 | | | ✓ |
| − Trade payables − other current liabilities | (209.3) | | | ✓ |
| **Invested capital** | **886.8** | | | |
| Cash + current investments (excluded from IC) | 47.5 | | | financing side |
| Deferred tax liability (excluded; quasi-equity) | 22.0 | | | — |

Check: invested capital 886.8 + cash 47.5 = 934.3 = capital employed 912.3 + DTL 22.0. The two views reconcile
because *sources* (equity, debt, leases, DTL) must equal *uses* (operating assets plus cash). This reconciliation
is your error check whenever you build these numbers.

The judgement calls, and the course's conventions:

- **Cash and investments** are excluded from invested capital (they earn other income, which is excluded from
  NOPAT). Some analysts subtract only "excess" cash; the course excludes all financial assets and treats other
  income separately. ROCE, by Indian convention, includes cash in capital employed *and* other income in the
  numerator — consistent, just different.
- **Goodwill and acquired intangibles**: include them (the company paid that money) for judging *management's*
  capital allocation; exclude them for judging the *operating business's* economics. Report both when goodwill is
  large. Kaveri has none.
- **CWIP**: capital that is not yet producing. Include it (it is invested) but recognise that ROIC is depressed
  during a build. Kaveri's FY23–24 CWIP of ₹68 Cr → ₹0 as Hosur was commissioned is a good example: FY24 ROIC
  benefits from a plant that only started depreciating in FY25.
- **Leases**: since Ind AS 116, ROU assets are in invested capital and lease liabilities in capital employed;
  EBIT is *after* ROU amortisation but *before* lease interest — consistent with treating leases as debt.
- **Deferred tax liabilities**: quasi-equity (the company keeps the money until timing differences reverse).
  Exclude from capital employed or treat as part of equity; do not treat as debt.
- **Taxes**: NOPAT uses the *marginal* or effective tax rate on operating profit — 25.17% for Kaveri.

## 3. Kaveri FY21–FY26: the numbers

Computed with `tools/fi/ratios.ratio_dashboard` (which reproduces the running-example table). Averages use the
opening balance sheet at 31-Mar-2020 for FY21.

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| PAT (₹ Cr) | 32.8 | 47.2 | 62.6 | 86.4 | 97.4 | 90.5 |
| EBIT + other income | 58.1 | 69.4 | 92.0 | 129.0 | 132.5 | 138.0 |
| NOPAT = EBIT × 0.7483 | 39.7 | 47.3 | 63.3 | 91.4 | 95.8 | 100.3 |
| Avg equity | 385.9 | 416.9 | 461.3 | 522.7 | 598.0 | 671.7 |
| Avg capital employed | 463.3 | 493.0 | 560.0 | 672.6 | 780.3 | 868.1 |
| Avg invested capital | 394.9 | 408.1 | 470.9 | 607.0 | 738.8 | 836.8 |
| **ROE** | **8.5%** | **11.3%** | **13.6%** | **16.5%** | **16.3%** | **13.5%** |
| **ROCE** (pre-tax) | **12.5%** | **14.1%** | **16.4%** | **19.2%** | **17.0%** | **15.9%** |
| **ROIC** (post-tax) | **10.1%** | **11.6%** | **13.4%** | **15.1%** | **13.0%** | **12.0%** |

```python
from fi.data import load_kaveri
from fi.ratios import ratio_dashboard
dash = ratio_dashboard(load_kaveri())
print(dash.loc[['roe', 'roce', 'roic']].round(4))
```

Three observations:

1. **The FY24 peak.** ROIC of 15.1% against a WACC of about 12.2% ([06.2](../06-valuation/02-cost-of-capital.md))
   — a spread of ~3 pp. Kaveri was creating value, modestly.
2. **The decline since.** By FY26, ROIC of 12.0% is *at* WACC. The company is growing 12–16% a year but the new
   capital — mostly receivables and a motors plant running at 57% utilisation — earns roughly its cost. Growth like
   that adds size, not value ([06.1](../06-valuation/01-what-is-value.md) proves this).
3. **ROE flatters.** ROE (13.5%) is above ROIC (12.0%) because Kaveri carries ₹140 Cr of net debt at an after-tax
   cost (~6.5%) below its operating return. That is leverage doing the work, not the business getting better.

## 4. DuPont: which lever moved?

### 4.1 Three-step DuPont

$$\text{ROE} = \underbrace{\frac{\text{PAT}}{\text{Revenue}}}_{\text{net margin}} \times
\underbrace{\frac{\text{Revenue}}{\text{Avg assets}}}_{\text{asset turnover}} \times
\underbrace{\frac{\text{Avg assets}}{\text{Avg equity}}}_{\text{leverage}}$$

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| Net margin | 5.4% | 6.2% | 7.2% | 8.6% | 8.3% | 6.9% |
| Asset turnover (on avg assets) | 1.06 | 1.22 | 1.23 | 1.20 | 1.20 | 1.21 |
| Leverage (avg assets / avg equity) | 1.50 | 1.49 | 1.53 | 1.61 | 1.63 | 1.62 |
| **ROE** | **8.5%** | **11.3%** | **13.6%** | **16.5%** | **16.3%** | **13.5%** |

```python
from fi.ratios import dupont_3
dupont_3(pat=90.5, revenue=1318.0, avg_assets=1089.7, avg_equity=671.7)
# {'margin': 0.0687, 'turnover': 1.2095, 'leverage': 1.6224, 'roe': 0.1348}
```

The story is unambiguous: **asset turnover has been flat at ~1.2 since FY22 and leverage crept up from 1.5 to 1.6;
everything else is margin.** ROE rose with the net margin to FY24 and fell with it after. Kaveri is not becoming a
more capital-efficient business; it is a margin story wearing a capital-efficiency costume. That tells you where to
spend your research time — on the solar mix and receivables, not on the plant.

### 4.2 Five-step DuPont

The five-step version splits the net margin into tax, interest and operating components so that financing and
tax effects are visible:

$$\text{ROE} = \underbrace{\frac{\text{PAT}}{\text{PBT}}}_{\text{tax burden}} \times
\underbrace{\frac{\text{PBT}}{\text{EBIT}}}_{\text{interest burden}} \times
\underbrace{\frac{\text{EBIT}}{\text{Revenue}}}_{\text{EBIT margin}} \times
\frac{\text{Revenue}}{\text{Avg assets}} \times \frac{\text{Avg assets}}{\text{Avg equity}}$$

(EBIT here includes other income so that PBT/EBIT captures only interest and exceptional items.)

| | FY24 | FY25 | FY26 | Comment |
|:--|--:|--:|--:|:--|
| Tax burden (PAT/PBT) | 0.748 | 0.748 | 0.748 | Constant 25.2% tax — nothing to see |
| Interest burden (PBT/EBIT) | 0.895 | 0.983 | 0.877 | FY25 inflated by the ₹14 Cr exceptional gain; FY26 shows finance costs taking 12% of EBIT |
| EBIT margin (incl. other income) | 12.8% | 11.3% | 10.5% | The real driver |
| Asset turnover | 1.20 | 1.20 | 1.21 | Flat |
| Leverage | 1.61 | 1.63 | 1.62 | Flat |
| **ROE** | **16.5%** | **16.3%** | **13.5%** | 0.748 × 0.877 × 0.1047 × 1.2095 × 1.6224 = 13.5% |

`fi.ratios.dupont_5(pat, pbt, ebit, revenue, avg_assets, avg_equity)` returns all five factors.

!!! info "India notes"
    Indian brokers and Screener.in lead with **ROCE**, usually defined as EBIT ÷ (equity + debt) on *closing*
    balances, sometimes including other income, sometimes not. Screener's ROCE for a company can differ from your
    average-based number by 1–3 pp in a fast-growing year. Management often quotes "ROCE" on *pre-tax* EBIT, which
    makes 20% sound better than the 15% post-tax ROIC it implies. Always restate to one definition before comparing
    companies — `fi.ratios.roce` and `fi.ratios.roic` are the course's definitions.

## 5. Why a high ROE can be a leverage artefact

Financial leverage raises ROE whenever the after-tax return on assets exceeds the after-tax cost of debt:

$$\text{ROE} = \text{ROA} + (\text{ROA} − k_d(1−t)) \times \frac{D}{E}$$

With ROA (NOPAT/assets) of 12% and after-tax debt cost of 6.75%:

| D/E | 0.0 | 0.5 | 1.0 | 2.0 |
|:--|--:|--:|--:|--:|
| ROE | 12.0% | 14.6% | 17.3% | 22.5% |

The 22.5% ROE at D/E = 2 is the same 12% business with more risk; if ROA drops to 5% in a bad year, ROE at D/E = 2
becomes 5 + (5 − 6.75) × 2 = **1.5%**, and at D/E = 4 it is negative. This is why a 20% ROE from an NBFC (leverage
6–8x) and a 20% ROE from an FMCG company (no debt) are not comparable, and why for non-financial companies you
judge the *business* on ROIC and the *financing choice* separately.

!!! tip "Trader's lens"
    Leverage is a constant-notional position financed with borrowed money: it scales the P&L in both directions and
    adds a fixed carry (interest). ROE at high D/E is the return on the margin posted, not on the exposure. A
    lender's 15% ROE at 7x leverage is a ~2% return on assets — a thin edge that a small credit-cost surprise wipes
    out, exactly like a high-Sharpe strategy run at 7x. [07.1](../07-special-valuation/01-banks-and-nbfcs.md)
    builds the RoA tree that makes this precise for Nirmal Finance.

## 6. ROIC vs WACC: the value-creation test

A business creates value only when it earns more on invested capital than the capital costs. The spread
ROIC − WACC, multiplied by invested capital, is the annual **economic profit** (EVA):

$$\text{Economic profit} = (\text{ROIC} − \text{WACC}) \times \text{Invested capital}$$

Kaveri FY26: (12.0% − 12.19%) × 836.8 ≈ **−₹1.6 Cr** — essentially zero. FY24: (15.1% − 12.19%) × 607.0 ≈
**+₹17.6 Cr**. The company went from creating ₹18 Cr of value a year to none, while PAT grew from 86 to 90. That
divergence is invisible in the P&L and is the entire reason this ratio exists.

The corollary, proved in [06.1](../06-valuation/01-what-is-value.md): when ROIC = WACC, growth is worth nothing;
when ROIC < WACC, growth *destroys* value; only when ROIC > WACC does faster growth deserve a higher multiple.

## 7. Incremental ROIC and the reinvestment identity

Average ROIC blends old, depreciated, cheap assets with new ones. What matters for the future is the return on the
*next* rupee — **incremental ROIC**:

$$\text{Incremental ROIC} = \frac{\Delta \text{NOPAT}}{\Delta \text{Invested capital}}$$

| Window | ΔNOPAT (₹ Cr) | ΔInvested capital (₹ Cr) | Incremental ROIC |
|:--|--:|--:|--:|
| FY23 → FY26 (three years) | 100.3 − 63.3 = 37.0 | 886.8 − 523.4 = 363.4 | **10.2%** |
| FY24 → FY26 (two years) | 100.3 − 91.4 = 9.0 | 886.8 − 690.6 = 196.2 | **4.6%** |

Since the FY24 peak, Kaveri has invested ₹196 Cr of new capital (₹77 Cr of it in receivables) and earned an extra
₹9 Cr of NOPAT on it — a 4.6% return, far below WACC. This is the number that should worry a shareholder more than
any margin: the marginal rupee is being wasted, and management guides to more of the same growth. Use 3-year
windows at least; single years are dominated by timing (a plant capitalised, a working-capital swing).

Finally, the identity that links returns to growth — the engine of every DCF:

$$g = \text{Reinvestment rate} \times \text{ROIC}, \qquad
\text{Reinvestment rate} = \frac{\text{Capex} + \Delta\text{NWC} − \text{D\&A}}{\text{NOPAT}}$$

Kaveri FY26: net reinvestment = (52.0 + 89.7 − 47.8) = ₹93.9 Cr, which is **94% of NOPAT** (100.3). At a 12% ROIC
that supports g ≈ 0.94 × 12% ≈ 11% — close to the ~12.5% actually delivered. But the reinvestment is 70% working
capital (receivables from state agencies), not plant, and it consumed nearly all of NOPAT, which is why free cash
flow was just ₹13 Cr on ₹90 Cr of profit ([04.4](04-working-capital-and-cash-conversion.md)). A business that must
reinvest 94% of its profit to grow 12% at a 12% return is running to stand still; one that reinvests 30% to grow
12% is earning 40% on new capital and can pay you the rest. That comparison — reinvestment needed per unit of
growth — is the practical definition of business quality.

## 8. A second worked example — two companies, same ROE

**Vindhya Consumer Ltd** and **Narmada Steel Processors Ltd** (both fictional), FY26, ₹ Cr:

| | Vindhya Consumer | Narmada Steel |
|:--|--:|--:|
| Revenue | 2,000 | 2,000 |
| EBIT | 400 | 180 |
| Tax rate | 25% | 25% |
| Avg invested capital | 1,000 | 1,800 |
| of which cash & investments (excluded) | 600 | 20 |
| Avg equity | 1,500 | 600 |
| Net debt | (600) | 1,200 |
| PAT | 330 | 110 |

```python
t = 0.25
v = dict(ebit=400, ic=1000, eq=1500, pat=330); n = dict(ebit=180, ic=1800, eq=600, pat=110)
for name, c in (('Vindhya', v), ('Narmada', n)):
    print(name, 'ROIC', round(c['ebit']*(1-t)/c['ic'], 3), 'ROE', round(c['pat']/c['eq'], 3))
# Vindhya ROIC 0.30 ROE 0.22
# Narmada ROIC 0.075 ROE 0.183
```

Both report ROEs around 18–22%. Vindhya's is *depressed* by ₹600 Cr of idle cash sitting in equity (its operating
ROIC is 30%); Narmada's is *inflated* by ₹1,200 Cr of debt on a 7.5% ROIC business. Vindhya could double its ROE by
returning cash; Narmada's ROE turns negative in a steel down-cycle. Any comparison on ROE alone gets this backwards.

!!! warning "Common mistakes"
    - Closing instead of average capital (overstates growth-year returns; understates them when capital shrinks).
    - Mixing a pre-tax numerator (EBIT) with an after-tax comparison (WACC). ROCE compares to pre-tax WACC;
      ROIC to WACC.
    - Including other income in NOPAT while excluding cash from invested capital (or the reverse).
    - Judging a company mid-capex on average ROIC — CWIP earns nothing until commissioned; look at incremental
      ROIC over a full cycle.
    - Comparing ROE across different leverage without a DuPont.
    - Taking management's "ROCE" at face value — check numerator (pre/post tax, with/without other income) and
      denominator (closing/average; with/without leases and cash).
    - Ignoring goodwill when judging acquisitive management: the price paid is capital too.

## Key terms

| Term | Meaning |
|:--|:--|
| **ROE** | PAT ÷ average shareholders' equity |
| **ROCE** | (EBIT + other income) ÷ average capital employed (equity + borrowings + lease liabilities); pre-tax |
| **ROIC** | NOPAT ÷ average invested capital; post-tax, operating assets only |
| **NOPAT** | Net operating profit after tax = EBIT × (1 − tax rate) |
| **Capital employed** | Equity + all borrowings + lease liabilities (the sources view) |
| **Invested capital** | Net fixed assets + CWIP + ROU + intangibles + net working capital (the uses view, ex-cash) |
| **DuPont analysis** | Decomposition of ROE into margin × turnover × leverage (3-step) or with tax and interest burdens (5-step) |
| **Asset turnover** | Revenue ÷ average total assets; capital intensity's inverse |
| **Financial leverage (DuPont)** | Average assets ÷ average equity |
| **Economic profit (EVA)** | (ROIC − WACC) × invested capital |
| **Incremental ROIC** | Change in NOPAT ÷ change in invested capital over a multi-year window |
| **Reinvestment rate** | (Capex + ΔNWC − D&A) ÷ NOPAT; the share of profit ploughed back |
| **Reinvestment identity** | Sustainable growth g = reinvestment rate × ROIC |

## Check your understanding

1. Kaveri's ROCE (15.9%) is higher than its ROIC (12.0%) in FY26. Give the two definitional reasons.
<details><summary>Answer</summary>ROCE is pre-tax (EBIT + other income) while ROIC uses NOPAT after 25.17% tax —
the larger effect; and the denominators differ (capital employed includes cash-funded capital and excludes DTL;
invested capital excludes cash). Roughly: 15.9% × 0.748 ≈ 11.9%, close to the 12.0% ROIC once the denominator
difference nets out.</details>

2. Using the 3-step DuPont, what would Kaveri's FY26 ROE have been with the FY24 net margin (8.6%) and everything
   else unchanged?
<details><summary>Answer</summary>0.086 × 1.2095 × 1.6224 = 16.9%. The entire ROE decline is the margin.</details>

3. A company reports ROE of 25% with D/E of 3.0 and after-tax cost of debt of 6%. What is its ROA, and what happens
   to ROE if ROA falls by 3 pp?
<details><summary>Answer</summary>25 = ROA + (ROA − 6) × 3 → 25 = 4·ROA − 18 → ROA = 10.75%. If ROA falls to 7.75%:
ROE = 7.75 + (7.75 − 6) × 3 = 13.0%. A 3-pp fall in ROA cuts ROE by 12 pp.</details>

4. Compute Kaveri's FY26 economic profit if you use ROCE-style pre-tax numbers with a pre-tax WACC of 16.3%
   (12.19% ÷ 0.7483).
<details><summary>Answer</summary>(15.9% − 16.3%) × 868.1 ≈ −₹3.5 Cr — the same conclusion (≈ zero value creation)
as the post-tax version, which is the point of matching pre-tax with pre-tax.</details>

5. Why is the FY24→FY26 incremental ROIC (4.6%) so much lower than the average ROIC (12.0%)?
<details><summary>Answer</summary>The ₹196 Cr of new capital went mostly into receivables (₹77 Cr) and inventory
while the Hosur plant runs at 57% utilisation; the old asset base still earns well, but the marginal rupee earns
little. Average ROIC is history; incremental ROIC is the trend.</details>

6. A company grows revenue and NOPAT at 20% a year with a reinvestment rate of 50%. What ROIC is it earning on new
   capital? If instead it needs to reinvest 120% of NOPAT, what does that imply?
<details><summary>Answer</summary>g = RR × ROIC → ROIC = 20% / 50% = 40% — a very high-quality business. At 120%
reinvestment the implied ROIC is 16.7% and the company is consuming more than it earns (negative FCF, must raise
debt or equity to grow) — fine only if 16.7% comfortably exceeds WACC and the funding is sustainable.</details>

## Go deeper

- McKinsey & Company, *Valuation: Measuring and Managing the Value of Companies* — chapters on ROIC and the
  value-driver formula; the canonical treatment of invested capital.
- Michael Mauboussin, *Return on Invested Capital: How to Calculate ROIC and Handle Common Issues* (Credit Suisse,
  2014) — free, practical, deals with goodwill, leases, cash and R&D.
- Screener.in's ratio definitions page — read exactly how its ROCE and ROE are computed before you compare.
- Warren Buffett's 1979 Berkshire letter — on why return on equity capital, not EPS growth, is the test of
  management.

---
[← Previous: 04.2 Margins & cost structure](02-margins-and-cost-structure.md) · [Module index](index.md) · [Next: 04.4 Working capital & cash conversion →](04-working-capital-and-cash-conversion.md)
