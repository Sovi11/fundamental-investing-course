# Module 06 · Solutions

## Warm-up

**E06.01** Intrinsic: PV of future cash flows to the owner — the anchor for any decision. Relative: value inferred
from comparable assets' prices — useful to see what the market pays for similar growth/returns, and in
sectors with rich comparables. Book: accounting equity — a floor for lenders and asset-heavy companies, and the
base for residual-income models.

**E06.02** $V = \text{NOPAT}_1(1 − g/\text{ROIC})/(\text{WACC} − g)$; inputs: growth, return on invested capital,
cost of capital; constraints: $g < \text{WACC}$ (finite value) and $g \le \text{ROIC}$ (non-negative reinvestment).

**E06.03** rf: yield on a default-free bond in the cash flows' currency (India 10-yr G-sec); ERP: expected excess
return of equities over rf; beta: sensitivity of the stock to the market; cost of debt: current long-term borrowing
rate, after tax for WACC; WACC: weighted average at target market-value weights. Rule: ₹ cash flows with a ₹ rf and
₹ growth; never mix USD rates with ₹ flows.

**E06.04** FCFF = NOPAT + D&A − capex − ΔNWC (to all providers; discount at WACC → EV). FCFE = PAT + D&A − capex −
ΔNWC + net borrowing (to shareholders; discount at $k_e$ → equity).

**E06.05** P/E₍fwd₎ = (1 − g/ROE)/(r − g); P/B = (ROE − g)/(r − g).

**E06.06** Reverse DCF: solving the model for the input (growth, margin, WACC) that makes value equal price.
Variant perception: a specific, evidence-based belief that differs from the price-implied expectation, with a
falsification test.

**E06.07** Coherent stories (drivers move together); WACC held constant; probabilities written down with reasons
and visible.

## Core

**E06.08** 12/(0.12 − 0.05) = **₹171.4 Cr**. Multiples: ROIC 18%: (1 − 0.06/0.18)/(0.06) = **11.1x**; ROIC 12%:
(1 − 0.5)/0.06 = **8.3x** = 1/WACC — growth adds nothing at ROIC = WACC.

**E06.09** Model: "Growth raises value only when the capital that funds it earns more than it costs; at ROIC = WACC
the value multiple is 1/WACC regardless of growth, and below WACC faster growth lowers value. So 'growth is good'
is true for Kaveri's FY24 business (ROIC 15%) and false for its FY26 incremental business (4.6%)."

**E06.10** $k_e$ = 7.07 + 1.2 × 6.0 = **14.27%**; $k_d$ after tax = 9.0 × 0.7483 = 6.73%; WACC = 0.85 × 14.27 + 0.15 × 6.73
= **13.14%**.

**E06.11** Unlevered: 1.10/(1 + 0.7483×0.10) = 1.023; 0.95/1.0374 = 0.916; 1.25/1.2245 = 1.021; 1.05/1.1122 = 0.944;
average 0.976; relevered at D/E 0.27: 0.976 × (1 + 0.7483 × 0.27) = **1.17**.

**E06.12** Revenue 1,449.8; EBITDA 192.8; D&A 49.3; EBIT 143.5; NOPAT 107.4; capex 50.7; NWC 362.5 → ΔNWC −2.5; FCFF
= 107.4 + 49.3 − 50.7 + 2.5 = **108.5**.

**E06.13** Value-driver: FCFF₃₇ = 332.1 × 1.055 × (1 − 0.055/0.18) = 243.3; TV = 243.3/0.0669 = **₹3,638 Cr**. Naive:
275.6 × 1.055/0.0669 = **₹4,346 Cr** — ₹708 Cr higher, because it implicitly keeps FY36's 17% reinvestment rate
while assuming 5.5% growth, i.e. a 32% RONIC. The value-driver form keeps growth and reinvestment consistent.

**E06.14** PV of FCFF = **₹947.7 Cr**; PV of TV = 3,638.7/1.1219¹⁰ = **₹1,152.3 Cr**; EV **₹2,100.0 Cr**; equity = 2,100.0 −
140.5 − 18.2 = **₹1,941.3 Cr**; per share **₹320**.

**E06.15** 3,638.7/568.5 = **6.4x**. At 10x: TV = 5,685; PV = 1,800.4; EV = 2,748.1; equity 2,589.4; per share **≈ ₹427** —
a third higher from a terminal assumption that a 5.5%-growth industrial trades at 10x for ever.

**E06.16** 0.4 × 168 + 0.4 × 320 + 0.2 × 416 = **₹278**. From ₹300: expected return = 0.25×(−44%) + 0.5×(6.7%) +
0.25×(38.7%) = **+2.0%** on the reference weights (−7.3% on 40/40/20).

**E06.17** P/E = (1 − 0.05/0.15)/(0.125 − 0.05) = 0.667/0.075 = **8.9x**; P/B = (0.15 − 0.05)/0.075 = **1.33x**. The
trailing 25.9x cannot be justified by a single-stage model at a 12.5% cost of equity: the market is paying for a
long high-growth phase (the DCF's explicit period), a lower cost of equity, or both.

**E06.18** 34.7 × 15.08 = **₹523**; (20.8 × 181.9 − 158.7)/6.07 = **₹597**. Relative valuation says Kaveri is cheap
*within* a peer group; the DCF says the peer group's multiples imply growth and returns a 12.2% WACC cannot
support; and Kaveri's lower ROCE, leverage and receivables risk justify a discount to the group in any case.
Both can be true — the DCF is the anchor, the multiples the cross-check.

**E06.19** `reverse_dcf(300, ...)` → ≈ **10.1%**; at ₹450 → ≈ **16.3%** (run the code — values depend on the base
drivers held fixed). ₹300 requires roughly the base path's growth; ₹450 requires a decade of growth above
anything in Kaveri's history.

**E06.20** Implied RoE = 7 + 3.0 × 6 = **25%** vs actual 16%. Variant perception (bearish): "The market prices a
sustained 25% RoE; I expect 15–17% because [NIM compression / rising credit costs / capital needs]; justified P/B at
16% is 1.5x, i.e. half the price; I will know by FY27 results when RoE prints below 18%."

**E06.21** RI = (0.17 − 0.125) × 2,000 = 90; value = 2,000 + 90/(0.125 − 0.06) = 2,000 + 1,385 = **₹3,385 Cr**; P/B
**1.69x** (= (0.17 − 0.06)/0.065).

**E06.22** Listed stake 4,000 + unlisted 1,500 + cash 200 − capitalised costs 83 = 5,617 → **₹702/share** gross.
Discount 35% on 4,000: 5,617 − 1,400 = 4,217 → **₹527**; 55%: 5,617 − 2,200 = 3,417 → **₹427**.

**E06.23** d₁ = [ln(800/600) + (0.07 + 0.06125) × 2]/(0.35 × √2) = (0.2877 + 0.2625)/0.495 = 1.111; d₂ = 0.616; E = 800
× N(1.111) − 600e^{−0.14} × N(0.616) = 800 × 0.8667 − 521.6 × 0.7311 = 693.4 − 381.3 = **₹312 Cr**; P(default) = 1 −
N(d₂) = **26.9%**. At σ = 50%: d₁ = (0.2877 + 0.39)/0.7071 = 0.958, d₂ = 0.251; E = 800 × 0.831 − 521.6 × 0.599 = 664.8 −
312.4 = **₹352 Cr** — equity gains ~13% from higher vol with no change in assets.

**E06.24** Reference from ₹260: bear −35.4%, base +23.1%, bull +60.0%; expected +17.7%; up/down = (0.5×23.1 +
0.25×60)/(0.25×35.4) = 26.55/8.85 = **3.0**. With a 10% jump to ₹80 (−69.2%) and others scaled to 22.5/45/22.5%:
expected = 0.1×(−69.2) + 0.225×(−35.4) + 0.45×23.1 + 0.225×60 = −6.9 − 8.0 + 10.4 + 13.5 = **+9.0%**; up/down =
23.9/14.9 = **1.6**. The tail halves the attractiveness.

**E06.25** Rubric: code runs; correlated version shows a wider band and fatter left tail (P10 lower by ~₹15–25),
P(value < 390) slightly higher; the report states that independence understates tail risk.

## Stretch

**E06.26** With $V = \text{NOPAT}(1 − g/\text{ROIC})/(r − g)$, if ROIC < r, raising g raises the reinvestment
needed ($g/\text{ROIC}$) faster than the perpetuity factor rises: e.g. ROIC 8%, r 12%: g 3% → 6.9x; g 6% → 4.2x.
Growth funded below the cost of capital transfers value from shareholders to the projects.

**E06.27** Rubric: growth path [0.25×5, 0.21, 0.17, 0.13, 0.09, 0.06] (or a linear fade), RONIC path handled via
margins/capex or via the terminal RONIC = 15%, WACC 11%; TV share reported (expect 60–70%); the answer shows the
implied exit multiple and discusses whether the fade is fast enough.

**E06.28** Rubric: fifteen items each with a detecting question (e.g. "Is terminal g below WACC and nominal GDP?";
"Does terminal reinvestment equal g/RONIC?"; "Is the exit multiple a check or the method?"; "Explicit period ≥ 10
years for > 10% growers?"; "Are WACC and scenarios both carrying the same risk?"; "Same currency/inflation basis?";
"Diluted shares?"; "Leases/NCI/guarantees in the bridge?"; "Target weights?"; "Other income and cash counted
once?"; "Mid-year applied correctly?"; "Valuation date = price date?"; "NWC as a level?"; "Were inputs set before
the price was looked at?").

**E06.29** Rubric: implied volume growth by segment (cash, derivatives, currency), implied transaction-fee
path (regulatory risk), implied margin, implied value of non-volume revenue (data, listing, index licensing),
WACC; data needed: RHP financials by segment, SEBI fee circulars, historical volumes and their sensitivity to
the 2024–25 measures, global exchange multiples ([07.2](../07-special-valuation/02-insurers-amcs-exchanges.md)).

## Real-world task

**E06.30–31** Rubric: documented base drivers with sources; grids including the market price; scenarios as
stories; reverse DCF stated as "the price implies…"; the one-table-three-sentences output; for the lender, implied
vs actual RoE with the expectation named.
