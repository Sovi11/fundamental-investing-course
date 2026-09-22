# 10.3 · Forecasting drivers

> **Why this matters:** a forecast is a set of causal claims — "revenue grows because volumes grow because
> capacity is available and demand exists" — dressed as numbers. The schedules in this lesson are where those
> claims are made explicit: a revenue build, a cost build, working capital via days, a capex-and-depreciation
> schedule, a debt schedule with interest, tax, dividends, and cash as the balancing item. Built this way, a
> three-statement model balances by construction and every number can be traced to an assumption.

**Learning objectives** — after this lesson you can:

- Build revenue from drivers appropriate to the business (volume × price, segments, capacity × utilisation,
  order-book conversion, same-store growth).
- Build costs (gross margin; fixed and variable opex), working capital (days), capex and depreciation (linked to
  capacity), debt and interest (avoiding or controlling circularity), tax and dividends.
- Let cash balance the model and add a revolver for shortfalls.
- Reproduce Kaveri's FY27–FY29 projection from the reference assumptions with `tools/fi/model.py`.

**Prerequisites:** [10.1 Model architecture](01-model-architecture.md), [10.2 Building the historicals](02-historicals-and-data.md),
[06.3 DCF step by step](../06-valuation/03-dcf-step-by-step.md)  ·  **Time:** ~100 min

---

## 1. Revenue builds

Choose the build that matches how the business actually generates sales:

| Build | Formula | Use for | Inputs to defend |
|:--|:--|:--|:--|
| **Growth rate** | Revₜ = Revₜ₋₁ × (1 + g) | First pass; mature businesses; the reference Kaveri model | g by year, with a fade and a reason |
| **Volume × price** | Units × realisation per unit | Manufacturers, autos, cement, steel, pumps | Volume growth (industry + share), price (inflation, mix, commodity pass-through) |
| **Segments** | Σ segment revenue, each with its own build | Multi-segment companies (Kaveri: agri, industrial, solar) | Segment growth and margin; mix effects fall out |
| **Capacity × utilisation** | Capacity (units) × utilisation × price | Capacity-constrained businesses; plants ramping (Kaveri motors at 57%) | Capacity additions timing; utilisation ramp |
| **Order-book conversion** | Opening backlog × conversion rate + new orders × in-year execution | EPC, defence, capital goods | Conversion history; order-inflow forecast |
| **Stores × productivity** | Stores × revenue per store; SSSG on the mature base + new-store ramp | Retail, QSR | Store additions, SSSG, ramp curve |
| **Customers × ARPU** | Subscribers × ARPU × 12 | Telecom, SaaS, platforms | Net adds, churn, ARPU |
| **AUM × yield; loans × NIM** | | AMCs; lenders ([07.1](../07-special-valuation/01-banks-and-nbfcs.md)) | Flows; spread |

For Kaveri, the reference uses a growth-rate build; a better model uses segments. Fictional segment detail from
the running example (FY26: agri 606, industrial 356, solar 356):

| ₹ Cr | FY26 | FY27E | FY28E | FY29E | Driver |
|:--|--:|--:|--:|--:|:--|
| Agri & domestic | 606.2 | 642 | 687 | 735 | +6–7% (rural demand, replacement, share) |
| Industrial | 355.9 | 388 | 434 | 486 | +9–12% (Hosur motors ramp 57% → 75%) |
| Solar | 355.9 | 420 | 532 | 664 | +18–27% (order book ₹410 Cr; selective bidding) |
| **Total** | **1,318.0** | **1,450** | **1,653** | **1,885** | ≈ the reference path (10%, 14%, 14%) |

The segment build gives the same total as the reference path *and* tells you where the growth comes from —
which matters when solar has the worst working capital.

## 2. Cost builds

| Line | Build | Kaveri reference |
|:--|:--|:--|
| Materials (COGS) | % of revenue (gross margin), driven by mix and commodity pass-through; or per-unit cost × volume | Implied by EBITDA margin |
| Employee costs | Fixed core growing with inflation + variable share; or headcount × cost per head | In the EBITDA margin path |
| Other expenses | Fixed + variable split ([04.2](../04-financial-analysis/02-margins-and-cost-structure.md)); freight and power as % of revenue; A&P as a decision | |
| **EBITDA margin** | Either the *output* of the lines above, or (first pass) an *input* path | Input: 13.3% → 15.5% |
| D&A | From the PP&E schedule (§4) | 3.4% of revenue |
| Other income | Yield × opening cash and investments | 6.8% |
| Finance costs | From the debt schedule (§5) | 8.9% on opening borrowings; 8.5% on leases |
| Tax | Rate × PBT; deferred tax movement | 25.17% |

A margin path as input is acceptable for a first model and is what the reference does; a line-by-line build is
what you do when margin *is* the question (it is, for Kaveri: mix and Hosur utilisation are the drivers of the
13.8% → 15.5% recovery, and a segment-margin build would show whether 15.5% is reachable).

## 3. Working capital via days

$$\text{Inventory} = \frac{\text{Days}}{365} \times \text{COGS}; \quad
\text{Receivables} = \frac{\text{Days}}{365} \times \text{Revenue}; \quad
\text{Payables} = \frac{\text{Days}}{365} \times \text{COGS}$$

Other current assets and liabilities as % of revenue. The **level** is modelled; the **change** (ΔNWC) falls out
into the cash-flow statement. Kaveri's reference model uses NWC as a % of revenue (25% → 23% → 22%); the days
version (`Assumptions(inventory_days=80, receivable_days=…, payable_days=61, …)`) is more transparent: the base
case's 22% of revenue corresponds to receivable days of roughly 75–80 — which is the claim that must be defended
and monitored.

## 4. Capex and depreciation

| Item | Formula | Notes |
|:--|:--|:--|
| Capex | % of revenue (mature); or capacity additions × cost per unit (growth); or maintenance (≈ D&A) + growth projects | Kaveri: 3.5% of revenue (no new plant while Hosur is at 57%) |
| Gross block | Opening + capex − disposals | Or track net block directly: net₍ₜ₎ = net₍ₜ₋₁₎ + capex − D&A |
| Depreciation | Existing block ÷ remaining life + new capex ÷ life (half-year in year of addition); or % of opening gross block; or % of revenue (first pass) | Kaveri reference: 3.4% of revenue; `model.py`: net block roll |
| CWIP | Projects under construction; moves to gross block at commissioning | Capitalised interest during construction (Ind AS 23) |
| Leases | New leases (ROU additions), amortisation, interest, payments | `model.py` holds leases flat; the running-example generator models them fully |

The check: capex/D&A vs capacity — a model where revenue doubles with capex ≈ D&A is claiming utilisation
headroom that must exist (for Kaveri it does in motors; less so in pumps at 78%).

## 5. Debt and interest — and circularity

Schedule: opening balance → scheduled repayments → new draws → closing; interest = rate × (opening, or average).
Interest on *average* debt is more accurate but circular when debt is drawn to fund a cash shortfall that depends
on interest. Options:

| Approach | Pros | Cons |
|:--|:--|:--|
| Interest on **opening** balances (`model.py` does this) | No circularity; robust | Slightly understates interest in years of large draws |
| Interest on average with **iterative calculation** and a switch | Accurate | Can diverge; errors propagate; must be switchable |
| Interest on average with a **fixed number of manual iterations** (Python loop) | Accurate and controlled | A few lines of code |

A **revolver** (`min_cash`): if closing cash would fall below a minimum, draw short-term debt for the shortfall; if
cash is surplus, repay. This is the mechanism that keeps the balance sheet balancing without negative cash.

## 6. Tax, dividends, equity, shares

- **Tax**: rate × PBT (Kaveri 25.17%); deferred tax as a movement in DTL (hold flat unless tax depreciation
  differs materially); cash tax ≈ current tax.
- **Dividends**: payout × prior-year PAT (declared after year-end; `model.py` convention) or × current PAT; check
  against the dividend policy and the promoter's cash needs.
- **Equity**: other equity₍ₜ₎ = other equity₍ₜ₋₁₎ + PAT − dividends + SBC + issuance.
- **Shares**: basic count; add ESOP dilution via treasury-stock method for per-share value; model any planned
  issuance explicitly (Nirmal's QIP-driven growth).

## 7. Cash as the balancing item

$$\text{Closing cash} = \text{Opening cash} + \text{CFO} + \text{CFI} + \text{CFF}$$

and the balance sheet's cash line *is* that number. Total assets then equals total equity and liabilities by
construction — and if it does not, one of the schedules has a flow that never reached the cash-flow statement (the
usual culprit: a balance-sheet line moved without a corresponding CFS line). `project()`'s `checks` frame reports
`balance_diff` and `cash_recon_diff` for every year; they must be zero.

## 8. Kaveri FY27–FY29 — the projection

```python
from fi.data import load_kaveri
from fi.model import Assumptions, project
p = project(load_kaveri(), Assumptions.kaveri_base())
print(p["income"].round(1).iloc[:, :3]); print(p["balance"].round(1).iloc[:, :4]); print(p["cash"].round(1).iloc[:, :3])
print(p["checks"].round(3))
```

| ₹ Cr | FY26A | FY27E | FY28E | FY29E |
|:--|--:|--:|--:|--:|
| Revenue | 1,318.0 | 1,449.8 | 1,652.8 | 1,884.2 |
| EBITDA | 181.9 | 192.8 | 234.7 | 278.9 |
| D&A | 47.8 | 49.3 | 56.2 | 64.1 |
| EBIT | 134.1 | 143.5 | 178.5 | 214.8 |
| Other income | 3.9 | 3.2 | 6.9 | 11.2 |
| Finance costs | 17.0 | 18.3 | 16.5 | 14.7 |
| PBT | 121.0 | 128.5 | 168.9 | 211.3 |
| PAT | 90.5 | 96.1 | 126.4 | 158.1 |
| NWC | 365.0 | 362.5 | 380.1 | 414.5 |
| Net fixed assets | 521.8 | 523.2 | 524.9 | 526.8 |
| Cash | 32.5 | 87.1 | 150.2 | 220.4 |
| Term debt | 92.0 | 72.0 | 52.0 | 32.0 |
| Equity | 706.1 | 779.6 | 882.0 | 1,008.5 |
| CFO | 65.1 | 163.0 | 174.5 | 191.3 |
| Capex | 52.0 | 50.7 | 57.8 | 65.9 |
| FCFF (for the DCF) | — | 108.5 | 114.2 | 124.5 |
| Balance check | 0 | 0 | 0 | 0 |

The model's FCFF matches the reference DCF exactly (108.5, 114.2, 124.5, …), so the same drivers produce the same
₹320 — the three-statement model and the driver-based DCF are one architecture. What the full model adds: the
**balance sheet** (cash builds to ₹220 Cr by FY29 as term debt is repaid — which raises the question of what
management would do with it), the **finance-cost path** (falling as debt is repaid, lifting PAT growth above EBIT
growth), and the **checks**.

Note the conventions that differ from the historical generator: `model.py` holds lease liabilities flat, treats
new leases as within capex, and pays dividends on the prior year's PAT — documented simplifications that do not
affect FCFF.

!!! tip "Trader's lens"
    Drivers are the parameters; the statements are the pricing surface. The reason to model line by line is the
    same reason you would not price a book off a single implied vol: the interactions (working capital funded by
    short-term debt raising interest, which lowers PAT, which lowers retained equity…) are where the risk lives,
    and only a linked model shows them.

!!! warning "Common mistakes"
    - Forecasting margins without a cost build when margin is the thesis.
    - Working capital as % of *growth* rather than as a level.
    - Capex below D&A for a growing manufacturer.
    - Interest on average debt with uncontrolled circularity.
    - Dividends that exceed cash generation with no funding line.
    - A balance sheet that "balances" because equity was plugged.
    - Segment builds whose totals silently diverge from the consolidated history.

## Key terms

| Term | Meaning |
|:--|:--|
| **Revenue build** | The driver structure that produces the revenue forecast |
| **Cost build** | Line-by-line forecast of costs from drivers (margins, fixed/variable, per unit) |
| **Days-based working capital** | Inventory, receivable and payable balances forecast from days assumptions |
| **Capex schedule** | Forecast of capital expenditure and the resulting fixed-asset and depreciation roll |
| **Debt schedule** | Forecast of borrowings, repayments, draws and interest |
| **Revolver** | Short-term borrowing that draws to maintain a minimum cash balance |
| **Circularity** | Interest depending on debt depending on cash depending on interest |
| **Balancing item** | Cash (or revolver) — the line that makes the balance sheet balance |
| **Treasury-stock method** | Diluted share count from options net of shares repurchasable with exercise proceeds |

## Check your understanding

1. Rebuild FY27 finance costs from the schedule: term debt ₹92 Cr and working-capital debt ₹96 Cr at 8.9% on
   opening balances, leases ₹18.2 Cr at 8.5%.
<details><summary>Answer</summary>(92 + 96) × 8.9% = 16.7; 18.2 × 8.5% = 1.5; total 18.3 ✓ (matches the projection).
Interest is on opening balances, so the ₹20 Cr repaid during FY27 lowers FY28's charge, not FY27's.</details>

2. Why does the model's FY27 CFO (₹163 Cr) differ from the DCF's FY27 FCFF (₹108.5 Cr)?
<details><summary>Answer</summary>CFO is before capex (−50.7), and — under Kaveri's classification — before
interest paid (in CFF) and excluding interest received (in CFI); it is after actual tax on PBT rather than
notional tax on EBIT. FCFF = NOPAT + D&A − capex − ΔNWC is the unlevered, after-notional-tax measure the DCF
needs: 107.4 + 49.3 − 50.7 + 2.5 = 108.5.</details>

3. Convert the FY29 NWC assumption (22% of revenue) into receivable days, holding inventory at 80 days on COGS,
   payables at 61 days on COGS, OCA 3% and OCL 5% of revenue, gross margin 35%.
<details><summary>Answer</summary>COGS = 0.65 × rev. Inventory = 80/365 × 0.65 = 14.2% of rev; payables = 61/365 ×
0.65 = 10.9%; OCA − OCL = −2%. So receivables = 22% − 14.2% + 10.9% + 2% = 20.7% of revenue → 76 days. The base
case assumes receivable days fall from 96 to ~76.</details>

4. Cash reaches ₹220 Cr by FY29 in the base model. What are the modelling options, and why does the choice not
   change the DCF value?
<details><summary>Answer</summary>Hold it (other income rises), repay the working-capital lines, raise the payout,
or buy back. FCFF is unlevered and pre-financing, so none of these change EV; they change the bridge (net debt) and
per-share value only through timing and any value created/destroyed by the use of cash.</details>

## Go deeper

- `tools/fi/model.py` — `Assumptions`, `project()`, the days-mode drivers and the revolver; read the docstrings.
- `tools/running_example/generate.py` — the fuller schedule (leases, CWIP transfers, exceptional items) that
  produced the historicals; a good template for a detailed model.
- McKinsey, *Valuation*, "Forecasting Performance" — driver logic, explicit-period length, fade.
- [10.5 Build-along](05-build-along-kaveri-model.md) — the whole thing, end to end.

---
[← Previous: 10.2 Building the historicals](02-historicals-and-data.md) · [Module index](index.md) · [Next: 10.4 Scenarios, sensitivities & model QA →](04-scenarios-sensitivities-qa.md)
