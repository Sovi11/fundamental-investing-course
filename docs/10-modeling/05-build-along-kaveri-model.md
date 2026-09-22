# 10.5 · Build-along: the Kaveri model in Python

> **Why this matters:** you have read about every piece — historicals, drivers, schedules, statements, DCF,
> scenarios, checks. This lesson puts them together in ~60 lines of Python that reproduce the reference valuation
> (₹320), extend it with a stress case, and then point the same code at a real Indian company. Type it, run it,
> break it, fix it. The model you understand is the one you built.

**Learning objectives** — after this lesson you can:

- Build a three-statement projection and DCF for Kaveri with `tools/fi` and reproduce ₹320/share.
- Extend it with a receivables stress case and a margin scenario, and read the balance-sheet consequences.
- Adapt the pipeline to a real NSE-listed company using `fi.data.fetch_statements`, and know what to check.
- Explain the simplifications the model makes and when they matter.

**Prerequisites:** [10.1](01-model-architecture.md)–[10.4](04-scenarios-sensitivities-qa.md); Python with `pandas`; the course tools installed ([appendix](../appendix/tools.md))  ·  **Time:** ~120 min hands-on

---

## 0. Setup

```bash
pip install -r tools/requirements.txt
python -m pytest tools/tests -q          # 46 passed
python tools/examples/build_kaveri_model.py
```

The example script is the finished build-along; the sections below reconstruct it step by step. Work in a
script or notebook with `sys.path` including `tools/` (the examples do this for you).

## 1. Load the historicals and prove they tie

```python
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")     # ₹ on Windows consoles
sys.path.insert(0, "tools")
from fi.data import load_kaveri
hist = load_kaveri()                     # line items × FY21…FY26, ₹ Cr
print(hist.loc[["rev", "ebitda", "pat", "cfo", "cash", "total_assets", "total_le"]].round(1))
assert (abs(hist.loc["total_assets"] - hist.loc["total_le"]) < 0.05).all()
```

Six balanced years. For a real company this step is [10.2](02-historicals-and-data.md) and takes a day.

## 2. State the drivers

```python
from fi.model import Assumptions
base = Assumptions.kaveri_base()
print(base)
```

`Assumptions.kaveri_base()` returns the reference drivers: growth 10%, 14%, 14%, 13%, 12%, 11%, 10%, 9%, 8%, 7%;
EBITDA margin 13.3% → 15.5%; D&A 3.4% and capex 3.5% of revenue; NWC 25%, 23%, then 22% of revenue; tax 25.17%;
dividend payout 25% of prior-year PAT; interest 8.9% on opening borrowings; 8.5% on leases; 6.8% treasury yield;
term-loan repayments of ₹20 Cr a year for four years. Override anything by keyword: `Assumptions.kaveri_base(nwc_pct=0.277)`.

## 3. Project the statements

```python
from fi.model import project
proj = project(hist, base)
inc, bs, cf, checks = proj["income"], proj["balance"], proj["cash"], proj["checks"]
print(inc.round(1)); print(bs.round(1)); print(cf.round(1))
print(checks.loc[["balance_diff", "cash_recon_diff", "cash_negative"]].round(6))
```

What to look at, in order:

1. **Checks first.** `balance_diff` and `cash_recon_diff` are zero in every year; `cash_negative` is zero. If any
   is not, stop.
2. **The P&L path.** Revenue 1,450 → 3,667; EBITDA 193 → 568; PAT 96 → ~370 by FY36. Finance costs fall as term
   debt is repaid; other income rises as cash builds.
3. **The balance sheet.** Cash climbs from ₹32 Cr to ₹87 Cr (FY27), ₹150 Cr (FY28), ₹220 Cr (FY29) and keeps rising
   — the model is telling you that if the drivers hold, Kaveri becomes cash-rich, and the capital-allocation
   question of [05.5](../05-business-analysis/05-management-and-capital-allocation.md) becomes live.
4. **The cash-flow statement.** CFO jumps from ₹65 Cr (FY26) to ₹163 Cr (FY27) — the working-capital normalisation.
   That line *is* the thesis; everything else follows from it.

## 4. From statements to value

```python
from fi.model import fcff_from_projection
from fi.valuation import capm, wacc, terminal_value, dcf_fcff, equity_bridge
w = wacc(capm(rf=0.065, beta=1.05, erp=0.06), kd_pre_tax=0.089, tax_rate=0.2517, debt_weight=0.10)   # 0.1219
fcff = fcff_from_projection(proj)                     # FY27…FY36: 108.5, 114.2, 124.5, … 275.6
nopat_next = inc.loc["nopat"].iloc[-1] * 1.055
tv = terminal_value(nopat_next, w, 0.055, ronic=0.18)          # 3,638.7
d = dcf_fcff(fcff.tolist(), w, tv, mid_year=True)               # EV 2,100.0
equity = equity_bridge(d["ev"], net_debt=140.5, leases=18.2)    # 1,941.3
print(round(equity / 6.07))                                      # 320
```

The three-statement model's FCFF equals the driver-DCF's FCFF to the rupee, and the value is ₹320: one set of
drivers, two presentations. The full model earned its keep by producing the balance sheet and the checks.

## 5. Extend: the receivables stress

```python
stress = project(hist, Assumptions.kaveri_base(nwc_pct=0.277))     # NWC stays at FY26's 27.7% of revenue
fcff_s = fcff_from_projection(stress)
tv_s = terminal_value(stress["income"].loc["nopat"].iloc[-1] * 1.055, w, 0.055, ronic=0.18)
ps_s = equity_bridge(dcf_fcff(fcff_s.tolist(), w, tv_s)["ev"], 140.5, 18.2) / 6.07
print(round(ps_s), round(stress["balance"].loc["cash", "FY27"], 1))
# ₹297 (−7% vs base); FY27 cash 48.0 instead of 87.1
```

Notice what the stress does *not* do: it does not write anything off, cut growth or margins. It only says
"receivables never normalise", and that alone removes ₹23/share and ₹39 Cr of FY27 cash. Add the write-off and the
growth cut and you are at the reference bear case (₹168). Try:

```python
margin_down = project(hist, Assumptions.kaveri_base(ebitda_margin=[0.133, 0.138] + [0.14] * 8))   # → ₹277
revolver = project(hist, Assumptions.kaveri_base(nwc_pct=0.30, min_cash=40.0))                    # watch revolver_draw in cf
```

`min_cash` switches on the revolver: if closing cash would fall below ₹40 Cr, current borrowings are drawn to
cover it (`cf.loc["revolver_draw"]`), and interest follows the next year. That is how a model answers "can the
company fund this scenario?" rather than merely "what is it worth?".

## 6. Point it at a real company

```python
from fi.data import fetch_statements, fetch_price_info, revenue_row
t = "KIRLOSBROS.NS"                     # a real pump maker — any NSE ticker; disable VPN first
stm = fetch_statements(t, period="annual", in_crore=True)
inc_r, bs_r, cf_r = stm["income"], stm["balance"], stm["cash"]
print(inc_r.index.tolist()); print(bs_r.index.tolist())      # inspect row names — they vary
```

Then build a `history` frame in the Kaveri layout — the rows `project()` needs are listed in its docstring:
`rev, mat, pat, net_block, cwip, rou, intangibles, inventory, receivables, oca, cur_inv, cash, share_capital,
other_equity, lt_debt, st_debt, lease_liab, payables, ocl, dtl`. Map them from the Yahoo labels (e.g.
`total_revenue` → `rev`; `cost_of_revenue` → `mat`; `net_ppe` → `net_block`; `inventory`; `accounts_receivable`;
`cash_and_cash_equivalents`; `long_term_debt`/`current_debt`; `accounts_payable`; `stockholders_equity` less
`common_stock` → `other_equity`). Fill missing rows with zero *and say so*. Then:

```python
import pandas as pd
history = pd.DataFrame({...}, index=[...])          # your mapped rows × years, last column = latest FY
a = Assumptions(growth=[0.10] * 10, ebitda_margin=0.12, nwc_pct=0.20, lt_debt_change=0.0)
p = project(history, a); print(p["checks"].round(3))
```

The checks will pass (the model balances by construction) — which is exactly why the *historical* tie-out in
[10.2](02-historicals-and-data.md) must be done first: `project()` starts from your last column and cannot know
whether it was right. Then set drivers from the company's own history (`fi.ratios.ratio_dashboard` on your
mapped frame), value it, run the reverse DCF at the market price, and write down what the price implies.

## 7. What the model simplifies

| Simplification (`model.py`) | Effect | When to extend |
|:--|:--|:--|
| Lease liabilities held flat; new leases treated as part of capex | FCFF unaffected; BS lease line static | Lease-heavy companies (retail, QSR): model ROU additions, amortisation, payments as `generate.py` does |
| Interest on opening balances | Slight interest understatement in draw years | Highly levered or fast-changing debt: iterate |
| Dividends = payout × prior-year PAT | Timing convention | Interim dividends; buybacks: add explicitly |
| Tax fully cash; DTL flat | Cash tax ≈ book tax | Companies with large tax-depreciation timing differences |
| Single entity, no NCI, no associates | Bridge is net debt + leases only | Groups: add NCI and investments to the bridge and to the model |
| No exceptional items in forecasts | | Add a row when a known one-off is coming (a land sale, a write-off) |
| Margin as an input path | No cost build | When margin is the thesis: build materials/employees/other separately |

Every one of these is a conscious choice you can see in the code; that is the advantage over a spreadsheet you
inherited.

!!! tip "Trader's lens"
    You have now built the equity analyst's pricer: parameters (drivers) → cash-flow surface (statements) →
    price (value), with risk outputs (scenarios, stress, checks). The next step in your world would be to
    calibrate it to the market (reverse DCF) and trade the difference between your parameters and the implied
    ones. That is [Module 11](../11-process/index.md).

!!! warning "Common mistakes"
    - Running `project()` on unreconciled historicals (it will balance anyway — and be wrong).
    - Forgetting `in_crore=True` and mixing rupees and crore.
    - Trusting Yahoo's row labels without printing them.
    - Changing drivers without recording why (keep a dated assumptions log).
    - Reading the value and ignoring the balance sheet the model produced.

## Key terms

| Term | Meaning |
|:--|:--|
| **`Assumptions`** | The `fi.model` dataclass holding every forecast driver |
| **`project()`** | The `fi.model` function that turns history + assumptions into three balanced statements and checks |
| **`fcff_from_projection()`** | FCFF series derived from the projected statements |
| **Revolver (`min_cash`)** | Model logic that draws short-term debt to keep cash above a floor |
| **Row mapping** | Translating a data source's labels into the model's required rows |
| **Reference valuation** | The course's base case (₹320) that the build must reproduce |

## Check your understanding

1. Reproduce ₹320 and then change *only* the dividend payout to 60%. Does the value change? Should it?
<details><summary>Answer</summary>Value per share is unchanged: FCFF is pre-financing and the bridge uses FY26 net
debt. The balance sheet changes (less cash accumulates). In reality a higher payout could change value only via
what the cash would otherwise have earned — which the model captures as other income, excluded from FCFF by
design.</details>

2. Set `nwc_pct=0.30` and `min_cash=40`. In which year does the revolver draw, and what does that tell you?
<details><summary>Answer</summary>Run it: with NWC at 30% of a growing revenue base, working capital absorbs more
than operating cash in the early years and the revolver draws (check `cf.loc["revolver_draw"]`), raising interest
the following year. It tells you the company's working-capital lines, not its term loans, are the funding risk
— consistent with [04.5](../04-financial-analysis/05-leverage-solvency-liquidity.md).</details>

3. Why does the model's FY27 PAT (₹96.1 Cr) exceed the "adjusted" FY26 PAT by only ~6% when EBITDA grows 6%?
<details><summary>Answer</summary>Because finance costs *rise* in FY27 (interest on the higher opening debt of
FY26; ₹18.3 vs ₹17.0) and other income *falls* (lower opening cash), offsetting part of the EBITDA growth; from
FY28 both reverse and PAT grows faster than EBITDA. The linked model shows the financing drag the DCF does not.</details>

4. You map a real company and `project()` shows cash going negative in FY27 with no revolver. What are the two
   possible causes?
<details><summary>Answer</summary>Either the drivers genuinely imply a funding gap (high NWC or capex vs cash
generation — set `min_cash` or model a debt draw), or the mapping is wrong (e.g., current debt maturing that the
company will refinance was treated as a repayment; a missing row set to zero). Check the historicals tie first.</details>

## Go deeper

- `tools/examples/build_kaveri_model.py` — the complete script; `tools/tests/test_model.py` — the tests that
  guarantee it balances and reproduces ₹320.
- `tools/running_example/generate.py` — a fuller schedule (leases, CWIP, exceptional items) worth reading as a
  template for detailed models.
- [15.3 Worked capstone](../15-capstone/03-worked-example-kaveri.md) — the same model inside a full case study.

---
[← Previous: 10.4 Scenarios, sensitivities & model QA](04-scenarios-sensitivities-qa.md) · [Module index](index.md) · [Next: 11.1 Idea generation →](../11-process/01-idea-generation.md)
