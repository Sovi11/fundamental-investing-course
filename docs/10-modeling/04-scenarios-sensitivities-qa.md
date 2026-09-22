# 10.4 · Scenarios, sensitivities & model QA

> **Why this matters:** a model that produces one number has thrown away most of what it knows. Scenario
> switches, data tables, tornado charts and stress tests turn the same model into a map of outcomes; a QA
> checklist makes sure the map is drawn from a model that actually works. This lesson covers the mechanics —
> in Excel and in Python — and the review discipline that catches the errors every model contains.

**Learning objectives** — after this lesson you can:

- Build scenario switches (base/bull/bear and custom) that change a whole set of inputs at once.
- Run one- and two-way sensitivities (Excel data tables; Python loops) and draw a tornado chart.
- Design stress tests that are stories, not haircuts.
- Run the model-review checklist and find the errors it is designed to find.
- Present model outputs honestly.

**Prerequisites:** [10.3 Forecasting drivers](03-forecasting-drivers.md), [06.4 DCF in practice](../06-valuation/04-dcf-in-practice.md)  ·  **Time:** ~75 min

---

## 1. Scenario switches

A scenario is a *set* of inputs. The mechanics: keep every driver in a table with one column per scenario, and a
single "active scenario" cell that selects the column (Excel: `INDEX`/`CHOOSE` on the scenario number; Python: a
dict of `Assumptions` objects).

| Driver | Bear | Base | Bull |
|:--|:--|:--|:--|
| Revenue growth FY27→FY36 | 3%, 7%, 8%, 8%, 8%, 7%, 7%, 6%, 6%, 5% | 10%, 14%, 14%, 13%, 12%, 11%, 10%, 9%, 8%, 7% | 15%, 17%, 16%, 15%, 14%, 12%, 11%, 10%, 9%, 8% |
| EBITDA margin | 12.0% → 13.0% | 13.3% → 15.5% | 14.0% → 16.5% |
| NWC / revenue | 29% → 27% | 25% → 22% | 23% → 19% |
| Capex / revenue | 3.5% | 3.5% | 3.5% |
| WACC, g, RONIC | unchanged | 12.19%, 5.5%, 18% | unchanged |
| **Value / share** | **₹168** | **₹320** | **₹416** |

```python
from fi.data import load_kaveri
from fi.model import Assumptions, project
scenarios = {
    "bear": Assumptions.kaveri_base(growth=[0.03, 0.07, 0.08, 0.08, 0.08, 0.07, 0.07, 0.06, 0.06, 0.05],
                                    ebitda_margin=[0.12, 0.125, 0.128, 0.13] + [0.13] * 6, nwc_pct=[0.29, 0.28] + [0.27] * 8),
    "base": Assumptions.kaveri_base(),
    "bull": Assumptions.kaveri_base(growth=[0.15, 0.17, 0.16, 0.15, 0.14, 0.12, 0.11, 0.10, 0.09, 0.08],
                                    ebitda_margin=[0.14, 0.15, 0.158, 0.162, 0.165] + [0.165] * 5, nwc_pct=[0.23, 0.21, 0.20] + [0.19] * 7),
}
runs = {k: project(load_kaveri(), a) for k, a in scenarios.items()}
```

Rules: scenarios are stories ([06.4 §2](../06-valuation/04-dcf-in-practice.md)); every driver that the story
touches changes together; WACC stays fixed; the active-scenario cell is on the summary page; and the summary
shows all three values side by side, never just the active one.

## 2. Sensitivities

### 2.1 One-way and tornado

Vary one driver across its plausible range, holding the others at base, and record the value. Rank the drivers
by the width of the swing — the **tornado chart**:

| Driver (plausible range) | Low | High | Swing | Rank |
|:--|--:|--:|--:|:--|
| Revenue growth path (×0.8 / ×1.2) | ₹278 | ₹369 | ₹91 | 1 |
| EBITDA margin path (−1 pp / +1 pp) | ₹287 | ₹352 | ₹65 | 2 |
| Capex (4.5% / 2.5% of revenue) | ₹297 | ₹342 | ₹45 | 3 |
| Terminal RONIC (12.2% / 22%) | ~₹280 | ~₹335 | ~₹55 | 2–3 |
| WACC (+0.5 pp / −0.5 pp) | ₹296 | ₹348 | ₹52 | 3 |
| Terminal NWC (25% / 19% of revenue) | ₹309 | ₹331 | ₹22 | 5 |

(Computed with `project()` and the DCF helpers; RONIC/WACC from `dcf_from_drivers`.) The tornado tells you where
to spend research time (growth and margin) and where a debate is not worth having (terminal NWC — worth ₹22 either
way). It also exposes asymmetry: the growth swing is +₹49/−₹42, mildly convex.

```python
import matplotlib.pyplot as plt
rows = [("Growth ×0.8/×1.2", 278, 369), ("Margin ∓1pp", 287, 352), ("WACC ±0.5pp", 296, 348),
        ("Capex 4.5%/2.5%", 297, 342), ("NWC 25%/19%", 309, 331)]
rows.sort(key=lambda r: r[2] - r[1])
fig, ax = plt.subplots(figsize=(7, 3.5))
for i, (name, lo, hi) in enumerate(rows):
    ax.barh(i, hi - lo, left=lo, color="#4c72b0"); ax.text(lo - 3, i, f"₹{lo}", ha="right", va="center"); ax.text(hi + 3, i, f"₹{hi}", va="center")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows]); ax.axvline(320, color="k", ls="--"); ax.set_xlabel("Value per share (₹)")
plt.tight_layout(); plt.savefig("kaveri_tornado.png", dpi=150)
```

### 2.2 Two-way tables

Excel: *Data → What-If Analysis → Data Table* with the row input (e.g., terminal g) and column input (WACC) cells
pointing at the inputs sheet; the corner cell references the value-per-share output. Python: `fi.valuation.sensitivity(fn, rows, cols)`
returns a DataFrame. Conventions: base case in the centre; extend to include the market price; shade cells above
the price. The WACC × g and growth × margin grids for Kaveri are in [06.4](../06-valuation/04-dcf-in-practice.md).

### 2.3 Break-even solves

"What margin makes the base case worth ₹390?" — Excel *Goal Seek* or `fi.valuation.reverse_dcf` ([06.6](../06-valuation/06-reverse-dcf-and-expectations.md)).
Break-evens are the most communicable sensitivity: "the price needs 17.4% margins for a decade" is a sentence;
a grid is not.

## 3. Stress tests

A stress test is a bear scenario built around a *specific mechanism* and taken to the balance sheet, not just
the value:

| Stress | Mechanism | Model changes | What to read off |
|:--|:--|:--|:--|
| Receivables stuck | Two state agencies delay two more years; ₹60 Cr written off in FY28 | NWC 29% → 30%; exceptional loss 60 in FY28; WC lines rise; `min_cash` = 30 | Peak working-capital debt; interest cover trough; covenant headroom; value ₹~200 |
| Copper spike | Materials +3 pp of revenue for two years, 50% passed through with a lag | Margin path −1.5 pp FY27–28 | EPS trough; FCF sign |
| Demand shock | Revenue −15% in FY27 (bad monsoon), recovery FY28–29 | Growth −15%, +12%, +14% | Operating leverage on EBIT; cash position |
| Rate shock | Borrowing rate +200 bps; WACC +100 bps | `interest_rate` 0.109; WACC 13.2% | Interest cover; value |
| Combined | Receivables + demand | Both | Whether the revolver draws beyond available lines (the survival test) |

The `checks` frame's `cash_negative` flag and the revolver draw are the outputs that matter in a stress: does the
company need money it does not have? For Kaveri, even the combined stress keeps net debt/EBITDA under 2.5x — which
is why the equity risk is a valuation and receivables risk, not a solvency risk ([04.5](../04-financial-analysis/05-leverage-solvency-liquidity.md)).

## 4. The model-review checklist

Run it on your own model before showing anyone; run it on any model you are handed.

| # | Check | How |
|:--|:--|:--|
| 1 | Balance sheet balances every period | `balance_diff` = 0; Excel check row |
| 2 | Cash reconciles | `cash_recon_diff` = 0; CFS closing = BS cash |
| 3 | No negative cash without a revolver | `cash_negative` = 0 |
| 4 | Historicals tie to source | [10.2 §5](02-historicals-and-data.md) |
| 5 | No hard-codes in formula blocks | Excel: *Formulas → Show Formulas*; Ctrl+[ to trace; conditional formatting for constants; Python: all numbers in `Assumptions` |
| 6 | One formula per row across forecast columns | Excel: *Inconsistent formula* audit; Python: vectorised by construction |
| 7 | Sign conventions consistent | Spot-check: a cost increase should lower PAT and CFO |
| 8 | Units consistent | Headers; shares in crore vs units; ₹ Cr vs ₹ |
| 9 | Circularity controlled | Switch exists; model returns to zero when switched off |
| 10 | Drivers within plausible ranges | Margins vs history and peers; days vs history; capex vs D&A; growth vs industry |
| 11 | Terminal assumptions consistent | g < WACC; reinvestment = g/RONIC; implied exit multiple sane |
| 12 | Bridge complete | Net debt, leases, NCI, investments, dilution |
| 13 | Dates consistent | Valuation date; FY labels; mid-year convention |
| 14 | Scenario switch changes everything it should | Flip it; watch every driver |
| 15 | Outputs reconcile to a second method | Model FCFF = `dcf_from_drivers` FCFF; multiples cross-check |
| 16 | Sensitivities behave | Value rises with growth (if RONIC > WACC), falls with WACC — monotone and sensible |
| 17 | The summary page shows checks, scenarios, sensitivities and the date | Not a single number |

Excel-specific error hunts: `Ctrl+~` (show formulas) and scan for constants; *Formulas → Error Checking*; a
"trace precedents" pass on the value cell to see every input it touches; and a **fresh-eyes rule** — someone else,
or you after a day, reads the model cold.

## 5. Presenting outputs honestly

The summary page (or the memo table) contains: the valuation date and price; base/bull/bear values with
probabilities and the weighted value; the two-way grid that includes the price; the tornado; the break-even
sentence; the checks (all zero); and the three or four assumptions the value depends on, each with the evidence
behind it. A single target price to two decimals, with no ranges, is not an output — it is a marketing document
([06.4 §5](../06-valuation/04-dcf-in-practice.md)).

!!! tip "Trader's lens"
    Scenario and sensitivity analysis is the equity analyst's risk report: the tornado is the Greeks ladder, the
    two-way grid is the scenario matrix, the stress test is the tail-risk report, and the checks are the P&L
    reconciliation nobody skips. Present a valuation the way you would present a book: position, Greeks, stresses,
    and the reconciliation — not just the mark.

!!! warning "Common mistakes"
    - Sensitivities on inputs nobody disputes (WACC to the second decimal) instead of the ones that matter.
    - Scenarios that change one driver each.
    - Data tables pointing at the wrong input cell (Excel's silent failure).
    - Stress tests that stop at the P&L and never ask whether the company can fund the loss.
    - Skipping the checks because the model "looks right".
    - Presenting the active scenario as if it were the only one.

## Key terms

| Term | Meaning |
|:--|:--|
| **Scenario switch** | A single input that selects a full set of driver values |
| **Data table** | Excel's what-if tool for one- and two-way sensitivities |
| **Tornado chart** | Ranked horizontal bars showing each driver's value swing across its range |
| **Break-even solve** | Finding the input value that makes model value equal a target (Goal Seek / reverse DCF) |
| **Stress test** | A scenario built around a specific adverse mechanism, run through to the balance sheet |
| **Model QA** | Structured review for logical, arithmetic and presentation errors |
| **Fresh-eyes review** | Reading a model cold, by another person or after a gap |
| **Circularity switch** | An input that zeroes the self-referential term so an Excel model can be reset |

## Check your understanding

1. From the tornado, which two drivers deserve the most research time for Kaveri, and why is terminal NWC not one
   of them?
<details><summary>Answer</summary>Revenue growth (₹91 swing) and EBITDA margin (₹65): they move value most per
plausible unit of change. Terminal NWC moves it ₹22 across a wide range — the receivables question matters for the
*bear-case probability* and for near-term cash, not for the terminal level.</details>

2. Design a stress test for Nirmal Finance analogous to Kaveri's "receivables stuck".
<details><summary>Answer</summary>Credit cost rises from 1.9% to 4.5% for two years (used-CV stress), disbursements
fall 20%, cost of funds +100 bps; run through to PAT (RoE ~6%), CRAR (still > 20%), and the funding line — can
borrowings be rolled if NCD spreads widen? The balance-sheet outputs are the point.</details>

3. An Excel data table returns the same value in every cell. What is wrong?
<details><summary>Answer</summary>The row/column input cells do not point at the cells the model actually uses
(a common error when inputs are on another sheet — data tables need the input cell on the same sheet or a linked
cell), or calculation is set to "automatic except data tables".</details>

4. Why should WACC not be part of the bear scenario?
<details><summary>Answer</summary>Company-specific risk is captured in the bear cash flows; raising WACC too
double-counts it. WACC is varied separately in the sensitivity grid to show discount-rate uncertainty.</details>

5. List three items on the review checklist that a model can fail while still balancing perfectly.
<details><summary>Answer</summary>Hard-codes inside formulas; implausible drivers (margins above any peer); terminal
inconsistency (g ≥ WACC or reinvestment not equal to g/RONIC); an incomplete bridge; wrong units. Balancing proves
internal consistency, not correctness.</details>

## Go deeper

- `tools/examples/build_kaveri_model.py` — runs the base and the receivables stress; extend it with the table above.
- `tools/fi/valuation.sensitivity` and `reverse_dcf` — the Python data table and Goal Seek.
- Ian Dunlop, *Financial Modelling in Practice*, or Danielle Stein Fairhurst, *Using Excel for Business and
  Financial Modelling* — Excel mechanics and review practices.
- [06.4 DCF in practice](../06-valuation/04-dcf-in-practice.md) — the valuation logic behind the scenarios.

---
[← Previous: 10.3 Forecasting drivers](03-forecasting-drivers.md) · [Module index](index.md) · [Next: 10.5 Build-along: the Kaveri model in Python →](05-build-along-kaveri-model.md)
