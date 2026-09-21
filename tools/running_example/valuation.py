"""Reference ("house view") valuation of Kaveri Pumps & Motors Ltd.

Every lesson that values KPML (DCF lesson, modelling build-along, memo examples,
mocks) must quote these outputs so the course stays internally consistent.
Run after generate.py:  python tools/running_example/valuation.py
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "tools" / "data"
DOCS = ROOT / "docs" / "appendix" / "running-example"

A = dict(
    base_year="FY26",
    years=[f"FY{y}" for y in range(27, 37)],
    growth=[0.10, 0.14, 0.14, 0.13, 0.12, 0.11, 0.10, 0.09, 0.08, 0.07],
    ebitda_margin=[0.133, 0.142, 0.148, 0.152, 0.155, 0.155, 0.155, 0.155, 0.155, 0.155],
    da_pct=0.034,
    capex_pct=[0.035] * 10,
    nwc_pct=[0.25, 0.23, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22],
    tax=0.2517,
    rf=0.065, erp=0.060, beta=1.05, kd_pre=0.089, target_debt_weight=0.10,
    g_terminal=0.055, ronic=0.18,
    net_debt=140.5, lease_liab=18.2, diluted_shares=6.07, cmp=390.0,
)

SCENARIOS = {
    "Bull": dict(growth=[0.15, 0.17, 0.16, 0.15, 0.14, 0.12, 0.11, 0.10, 0.09, 0.08],
                 ebitda_margin=[0.140, 0.150, 0.158, 0.162, 0.165] + [0.165] * 5,
                 nwc_pct=[0.23, 0.21, 0.20] + [0.19] * 7,
                 desc="solar dues clear, growth 15–17% fading to 8%, EBITDA margin to 16.5%, NWC to 19% of sales"),
    "Bear": dict(growth=[0.03, 0.07, 0.08, 0.08, 0.08, 0.07, 0.07, 0.06, 0.06, 0.05],
                 ebitda_margin=[0.120, 0.125, 0.128, 0.130] + [0.130] * 6,
                 nwc_pct=[0.29, 0.28] + [0.27] * 8,
                 desc="state dues stay stuck, growth 3–8%, EBITDA margin 12–13%, NWC stays ~27–29% of sales"),
}
PROBS = {"Bull": 0.25, "Base": 0.50, "Bear": 0.25}


def load_fy26():
    rows = {}
    with open(DATA / "kaveri_pumps_annual.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows[r["line_item"]] = float(r["FY26"])
    return rows


def run(a=A, growth=None, margin=None, wacc_override=None, g_override=None, nwc=None):
    fy = load_fy26()
    nwc_pct = nwc or a["nwc_pct"]
    ke = a["rf"] + a["beta"] * a["erp"]
    kd = a["kd_pre"] * (1 - a["tax"])
    wacc = (1 - a["target_debt_weight"]) * ke + a["target_debt_weight"] * kd
    if wacc_override is not None:
        wacc = wacc_override
    g_t = a["g_terminal"] if g_override is None else g_override
    growth = growth or a["growth"]
    margin = margin or a["ebitda_margin"]
    nwc_prev = fy["inventory"] + fy["receivables"] + fy["oca"] - fy["payables"] - fy["ocl"]
    rev = fy["rev"]
    out = []
    pv_sum = 0.0
    for t in range(10):
        rev = rev * (1 + growth[t])
        ebitda = rev * margin[t]
        da = rev * a["da_pct"]
        ebit = ebitda - da
        nopat = ebit * (1 - a["tax"])
        capex = rev * a["capex_pct"][t]
        nwc = rev * nwc_pct[t]
        d_nwc = nwc - nwc_prev
        nwc_prev = nwc
        fcff = nopat + da - capex - d_nwc
        df = 1 / (1 + wacc) ** (t + 0.5)  # mid-year convention, valuation date 31-Mar-2026
        pv = fcff * df
        pv_sum += pv
        out.append(dict(year=a["years"][t], rev=rev, growth=growth[t], ebitda=ebitda, margin=margin[t], da=da,
                        ebit=ebit, nopat=nopat, capex=capex, nwc=nwc, d_nwc=d_nwc, fcff=fcff, df=df, pv=pv))
    last = out[-1]
    # terminal FCFF: grow NOPAT, and set reinvestment consistent with g / RONIC
    ronic = a["ronic"]
    nopat_next = last["nopat"] * (1 + g_t)
    fcff_next = nopat_next * (1 - g_t / ronic)
    tv = fcff_next / (wacc - g_t)
    pv_tv = tv / (1 + wacc) ** 10
    ev = pv_sum + pv_tv
    equity = ev - a["net_debt"] - a["lease_liab"]
    per_share = equity / a["diluted_shares"]
    return dict(rows=out, ke=ke, kd=kd, wacc=wacc, g=g_t, tv=tv, pv_tv=pv_tv, pv_sum=pv_sum, ev=ev,
                equity=equity, per_share=per_share, tv_share=pv_tv / ev, fcff_next=fcff_next, ronic=ronic)


def reverse_dcf(target_price):
    """Solve for the uniform FY27-FY36 revenue growth (margins as base case) that justifies the price."""
    lo, hi = -0.05, 0.40
    for _ in range(100):
        mid = (lo + hi) / 2
        v = run(growth=[mid] * 10)["per_share"]
        if v > target_price:
            hi = mid
        else:
            lo = mid
    return mid


def main():
    base = run()
    w = base["wacc"]
    waccs = [w - 0.01, w - 0.005, w, w + 0.005, w + 0.01]
    gs = [0.04, 0.045, 0.05, 0.055, 0.06]
    sens = [[run(wacc_override=ww, g_override=gg)["per_share"] for gg in gs] for ww in waccs]
    sc = {k: run(growth=v["growth"], margin=v["ebitda_margin"], nwc=v["nwc_pct"]) for k, v in SCENARIOS.items()}
    bull, bear = sc["Bull"], sc["Bear"]
    implied_g = reverse_dcf(A["cmp"])
    pw = PROBS["Bull"] * bull["per_share"] + PROBS["Base"] * base["per_share"] + PROBS["Bear"] * bear["per_share"]

    def f(x, d=1):
        return f"{x:,.{d}f}"

    lines = ["| ₹ Cr | " + " | ".join(r["year"] for r in base["rows"]) + " |",
             "|:--|" + "--:|" * 10]
    for label, key, kind in [("Revenue", "rev", "cr"), ("Growth", "growth", "pct"), ("EBITDA", "ebitda", "cr"),
                             ("EBITDA margin", "margin", "pct"), ("D&A", "da", "cr"), ("EBIT", "ebit", "cr"),
                             ("NOPAT (EBIT × (1 − 25.17%))", "nopat", "cr"), ("Capex", "capex", "cr"),
                             ("Net working capital", "nwc", "cr"), ("Increase in NWC", "d_nwc", "cr"),
                             ("**FCFF** = NOPAT + D&A − capex − ΔNWC", "fcff", "cr"),
                             ("Discount factor (mid-year)", "df", "df"), ("PV of FCFF", "pv", "cr")]:
        cells = []
        for r in base["rows"]:
            v = r[key]
            cells.append(f"{v * 100:.1f}%" if kind == "pct" else (f"{v:.4f}" if kind == "df" else f(v)))
        lines.append(f"| {label} | " + " | ".join(cells) + " |")
    proj = "\n".join(lines)

    sens_t = "| WACC \\ g | " + " | ".join(f"{g * 100:.1f}%" for g in gs) + " |\n|:--|" + "--:|" * len(gs) + "\n"
    for ww, row in zip(waccs, sens):
        sens_t += f"| {ww * 100:.1f}% | " + " | ".join(f"₹{v:,.0f}" for v in row) + " |\n"

    md = f"""# Kaveri Pumps — reference valuation (course "house view")

!!! note "Why this page exists"
    Several lessons value Kaveri Pumps & Motors (fictional). To keep the course consistent they all use the
    **assumptions and outputs on this page**, produced by `tools/running_example/valuation.py`. Lessons may
    *vary* assumptions to teach sensitivity, but must quote these as the base case. This is a teaching
    example — not a view on any real security.

## Assumptions (valuation date 31-Mar-2026; base year FY26)

| Driver | Base case |
|:--|:--|
| Revenue growth FY27→FY36 | {", ".join(f"{g * 100:.1f}%" for g in A["growth"])} (FY27 cut below the 15–18% guidance after the weak Q1) |
| EBITDA margin | {", ".join(f"{m * 100:.1f}%" for m in A["ebitda_margin"])} |
| D&A | {A["da_pct"] * 100:.1f}% of revenue |
| Capex | {A["capex_pct"][0] * 100:.1f}% of revenue every year |
| Net working capital | {A["nwc_pct"][0] * 100:.0f}% of revenue FY27, {A["nwc_pct"][1] * 100:.0f}% FY28, {A["nwc_pct"][2] * 100:.0f}% from FY29 (FY26 actual: 27.7%) — assumes solar receivables partly normalise |
| Capacity | Hosur motors plant at 57% utilisation, so capex stays near maintenance + automation levels |
| Tax rate | 25.17% |
| Risk-free rate (India 10-yr G-sec) | {A["rf"] * 100:.1f}% |
| Equity risk premium (India) | {A["erp"] * 100:.1f}% |
| Beta | {A["beta"]:.2f} |
| Cost of equity (CAPM) | {base["ke"] * 100:.2f}% |
| Pre-tax / post-tax cost of debt | {A["kd_pre"] * 100:.1f}% / {base["kd"] * 100:.2f}% |
| Target debt / capital | {A["target_debt_weight"] * 100:.0f}% |
| **WACC** | **{base["wacc"] * 100:.2f}%** |
| Terminal growth (nominal ₹) | {A["g_terminal"] * 100:.1f}% |
| Terminal reinvestment | consistent with RONIC {base["ronic"] * 100:.0f}%: reinvestment rate = g / RONIC = {A["g_terminal"] / base["ronic"] * 100:.1f}% of NOPAT |
| Discounting | mid-year convention (cash flow of year *t* discounted by (1+WACC)^(t−0.5)); TV discounted 10 full years |
| Equity bridge | EV − net debt ₹{A["net_debt"]} Cr − lease liabilities ₹{A["lease_liab"]} Cr; ÷ {A["diluted_shares"]} Cr diluted shares |

## Base-case projection (₹ Cr)

{proj}

## Result

| Item | ₹ Cr |
|:--|--:|
| Sum of PV of FCFF, FY27–FY36 | {f(base["pv_sum"])} |
| Terminal-year FCFF (FY37) | {f(base["fcff_next"])} |
| Terminal value at end-FY36 = FCFF₍FY37₎ / (WACC − g) | {f(base["tv"])} |
| PV of terminal value | {f(base["pv_tv"])} |
| **Enterprise value** | **{f(base["ev"])}** |
| Less: net debt | ({f(A["net_debt"])}) |
| Less: lease liabilities | ({f(A["lease_liab"])}) |
| **Equity value** | **{f(base["equity"])}** |
| **Value per share (6.07 Cr diluted shares)** | **₹{base["per_share"]:,.0f}** |
| Terminal value as % of EV | {base["tv_share"] * 100:.0f}% |
| Current market price (18-Sep-2026) | ₹{A["cmp"]:,.0f} |
| Implied upside / (downside) vs CMP | {(base["per_share"] / A["cmp"] - 1) * 100:+.0f}% |

Timing note: the valuation date is 31-Mar-2026 but the price is from 18-Sep-2026. Rolling the equity value forward
~0.47 years at the cost of equity gives ₹{base["per_share"] * (1 + base["ke"]) ** (171 / 365):,.0f} (a ~{((1 + base["ke"]) ** (171 / 365) - 1) * 100:.0f}% uplift, ignoring
dividends). Lessons may ignore the roll-forward for simplicity, but should mention that it exists.

## Sensitivity — value per share (₹)

{sens_t}
## Scenarios

| Scenario | Key assumptions | Value / share | Probability |
|:--|:--|--:|--:|
| Bull | {SCENARIOS["Bull"]["desc"]} | ₹{bull["per_share"]:,.0f} | 25% |
| Base | as above | ₹{base["per_share"]:,.0f} | 50% |
| Bear | {SCENARIOS["Bear"]["desc"]} | ₹{bear["per_share"]:,.0f} | 25% |
| **Probability-weighted** | | **₹{pw:,.0f}** | |

## Reverse DCF — what does ₹{A["cmp"]:,.0f} imply?

Holding base-case margins, capex, working capital, WACC ({base["wacc"] * 100:.2f}%) and terminal growth
({A["g_terminal"] * 100:.1f}%) fixed, the market price of ₹{A["cmp"]:,.0f} is justified by a **uniform revenue growth
of {implied_g * 100:.1f}% a year for FY27–FY36**. Compare with the 10-year base case CAGR of
{((base["rows"][-1]["rev"] / 1318) ** 0.1 - 1) * 100:.1f}% and the FY23–FY26 historical CAGR of
{((1318 / 874) ** (1 / 3) - 1) * 100:.1f}%.

*Trader's lens:* this is the fundamental analogue of backing out implied volatility from an option price — the
question is not "what is it worth?" but "what growth is the market already paying for, and do I disagree?"
"""
    (DOCS / "kaveri-valuation.md").write_text(md, encoding="utf-8")
    print(f"WACC {base['wacc']:.4f} Ke {base['ke']:.4f} EV {base['ev']:.1f} equity {base['equity']:.1f} "
          f"per share {base['per_share']:.0f} TV% {base['tv_share']:.2f} bull {bull['per_share']:.0f} "
          f"bear {bear['per_share']:.0f} PW {pw:.0f} implied g {implied_g:.4f}")
    for r in sens:
        print([round(v) for v in r])


if __name__ == "__main__":
    main()
