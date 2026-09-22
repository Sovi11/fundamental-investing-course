# 09.6 · Forensic scoring models

> **Why this matters:** the red-flag lessons give you judgement; scoring models give you *screens* — mechanical,
> reproducible, comparable across hundreds of companies, and blind to the story. Beneish's M-score, Altman's Z,
> Piotroski's F, the accruals ratio and a few others each compress a handful of ratios into one number with a
> published threshold. They are not verdicts. They are the first filter, and the numbers a forensic analyst quotes
> when they say "this one needs a closer look".

**Learning objectives** — after this lesson you can:

- Compute and interpret the Beneish M-score (all eight indices), Altman Z (original and Z″), Piotroski F
  (nine signals), Sloan accruals and Montier's C-score, and describe the Dechow F-score.
- Run them with `tools/fi/forensics.py` on Kaveri FY25 and FY26 and interpret the results.
- State each model's assumptions, base rates and failure modes — including why lenders are excluded and how Indian
  by-nature P&Ls must be mapped.
- Combine the scores into a screen without over-reading them.

**Prerequisites:** [04.7 Quality of earnings](../04-financial-analysis/07-quality-of-earnings.md), [09.2](02-revenue-red-flags.md)–[09.4](04-cash-flow-games.md)  ·  **Time:** ~90 min

---

## 1. Beneish M-score — is this company likely manipulating earnings?

Messod Beneish (1999) fitted a model on companies later found to have manipulated earnings. Eight indices, each
comparing this year with last (a value above 1 means the variable moved in the "manipulator" direction):

| Index | Formula | Captures | Manipulator mean (Beneish) | Non-manipulator mean |
|:--|:--|:--|--:|--:|
| **DSRI** — days' sales in receivables | (Rec/Sales)ₜ ÷ (Rec/Sales)ₜ₋₁ | Revenue booked faster than collected | 1.465 | 1.031 |
| **GMI** — gross margin | GMₜ₋₁ ÷ GMₜ | Deteriorating margins → pressure to manipulate | 1.193 | 1.014 |
| **AQI** — asset quality | (1 − (CA + PPE + securities)/TA)ₜ ÷ same ₜ₋₁ | Growth in "soft" assets (capitalised costs) | 1.254 | 1.039 |
| **SGI** — sales growth | Salesₜ ÷ Salesₜ₋₁ | Growth companies face pressure and have opportunity | 1.607 | 1.134 |
| **DEPI** — depreciation | Dep rateₜ₋₁ ÷ dep rateₜ | Slowing depreciation | 1.077 | 1.001 |
| **SGAI** — SG&A | (SGA/Sales)ₜ ÷ (SGA/Sales)ₜ₋₁ | Rising overheads → pressure | 1.041 | 1.054 |
| **LVGI** — leverage | (Debt/TA)ₜ ÷ (Debt/TA)ₜ₋₁ | Rising leverage → covenant pressure | 1.111 | 1.037 |
| **TATA** — total accruals to total assets | (PAT − CFO)ₜ ÷ TAₜ | Accrual-heavy profit | 0.031 | 0.018 |

$$M = −4.84 + 0.920\,\text{DSRI} + 0.528\,\text{GMI} + 0.404\,\text{AQI} + 0.892\,\text{SGI} + 0.115\,\text{DEPI} − 0.172\,\text{SGAI} + 4.679\,\text{TATA} − 0.327\,\text{LVGI}$$

Threshold: **M > −1.78** flags a likely manipulator (the 8-variable model; a 5-variable version uses −2.22).
In Beneish's sample the model caught ~76% of manipulators with ~17.5% false positives — so a flag means "one in
several flagged companies is a manipulator", not "this one is".

### 1.1 Kaveri

```python
from fi.data import load_kaveri
from fi.forensics import forensic_summary
for y in ("FY24", "FY25", "FY26"):
    b = forensic_summary(load_kaveri(), y)["beneish"]
    print(y, {k: round(v, 3) for k, v in b.items() if isinstance(v, float)})
```

| | FY24 | FY25 | FY26 | Read |
|:--|--:|--:|--:|:--|
| DSRI | 1.147 | 1.200 | 1.143 | Above 1.1 three years running — the receivables story |
| GMI | 0.929 | 1.034 | 1.020 | Margins slipping slightly since FY24 |
| AQI | 0.837 | 1.021 | 0.966 | No soft-asset growth |
| SGI | 1.151 | 1.165 | 1.125 | Healthy, not explosive growth |
| DEPI | 1.211 | 0.759 | 0.954 | FY24 slower (pre-plant), FY25 faster (new plant) — noise |
| SGAI | 1.014 | 0.977 | 1.010 | Flat |
| LVGI | 1.074 | 0.989 | 0.997 | Flat |
| TATA | −0.000 | 0.035 | 0.022 | Accruals appeared in FY25 |
| **M-score** | **−2.32** | **−1.98** | **−2.14** | Below −1.78 every year; FY25 came within 0.2 of the line |

Kaveri is not flagged, but the *movement* — from −2.32 toward −1.98 — and the *composition* (DSRI and TATA doing the
work) say exactly what the red-flag lessons said: watch receivables. The mapping caveat: Indian P&Ls are by
nature, so "SG&A" = employee + other expenses and "COGS" = materials; the `forensic_inputs` docstring lists every
assumption — quote them when you quote a score.

## 2. Altman Z-score — is this company heading for distress?

Edward Altman (1968) discriminated bankrupt from surviving manufacturers with five ratios:

$$Z = 1.2\,X_1 + 1.4\,X_2 + 3.3\,X_3 + 0.6\,X_4 + 1.0\,X_5$$

| | Ratio | Kaveri FY26 |
|:--|:--|--:|
| X₁ | Working capital ÷ total assets (liquidity) | 0.277 |
| X₂ | Retained earnings ÷ total assets (cumulative profitability, age) | 0.591 |
| X₃ | EBIT ÷ total assets (productivity) | 0.121 |
| X₄ | Market value of equity ÷ total liabilities (market's cushion) | 7.13 (at the 31-Mar-2026 market cap of ₹3,120 Cr) |
| X₅ | Sales ÷ total assets (turnover) | 1.153 |
| **Z** | | **6.99** (safe zone > 2.99); **5.92** at the September price (₹2,340 Cr market cap) |

Zones: Z < 1.81 distress; 1.81–2.99 grey; > 2.99 safe. Variants: **Z′** (private companies; book equity in X₄;
zones 1.23/2.90) and **Z″** (non-manufacturers and emerging markets; drops X₅ because asset turnover is
industry-specific): Z″ = 6.56X₁ + 3.26X₂ + 6.72X₃ + 1.05X₄ (book equity), zones 1.10/2.60; Altman's emerging-market
version adds 3.25 to map to bond-rating equivalents. Kaveri Z″ = **6.25** — safe. `fi.forensics.altman_z(..., variant=...)`.

Altman is a solvency screen, not a fraud screen: it says whether a company with *these* reported numbers looks
like companies that went bankrupt. It fails when the numbers are false (Satyam's Z was fine), it penalises
capital-intensive and young companies, and X₄ makes it a function of the share price — a falling stock lowers Z,
which is partly circular. Use it for levered industrials, never for lenders.

## 3. Piotroski F-score — is this cheap stock fundamentally improving?

Joseph Piotroski (2000) built nine binary signals to separate winners from losers among low price-to-book stocks:

| # | Signal | Kaveri FY26 | Kaveri FY25 |
|:--|:--|:--:|:--:|
| 1 | ROA > 0 | 1 | 1 |
| 2 | CFO > 0 | 1 | 1 |
| 3 | ΔROA > 0 | 0 | 0 |
| 4 | CFO > PAT (accrual quality) | 0 | 0 |
| 5 | ΔLeverage (LTD/avg TA) < 0 | 1 | 1 |
| 6 | ΔCurrent ratio > 0 | 0 | 0 |
| 7 | No new equity issued | 1 | 1 |
| 8 | ΔGross margin > 0 | 0 | 0 |
| 9 | ΔAsset turnover > 0 | 0 | 0 |
| **F** | | **4** | **4** (7 in FY24) |

Piotroski found that high-F (8–9) value stocks outperformed low-F (0–2) by ~23 pp a year in his sample; the score
is a *momentum-of-fundamentals* screen. Kaveri's slide from 7 to 4 — losing the profitability-trend, accrual,
liquidity, margin and turnover signals at once — is the numerical version of "the business deteriorated in FY25".
`fi.forensics.piotroski_f(cur, prev)` returns the signals and the underlying values.

## 4. Accruals, C-score, Dechow F-score

| Model | What it does | Threshold / read | Tool |
|:--|:--|:--|:--|
| **Sloan accruals ratio** | (PAT − CFO) ÷ average total assets | > +5% is high (top decile); Kaveri FY26 +2.3% | `accruals_ratio` |
| **Balance-sheet accruals** | ΔNet operating assets ÷ average NOA | Same idea from the balance sheet; Kaveri 3.8% on the tool's definition | `balance_sheet_accruals` |
| **Montier C-score** (2008) | Six binary flags: growing CFO/PAT divergence; rising DSO; rising inventory days; growing other current assets/revenue; falling depreciation rate; asset growth > 10% (from acquisitions) | 0–6; ≥ 4 flags a "cooking the books" candidate; Kaveri would score ~2–3 (DSO up; CFO/PAT divergence; asset growth) | Build from the inputs |
| **Dechow F-score** (2011) | A logistic model on accrual quality (RSST accruals, Δreceivables, Δinventory, soft assets), performance (Δcash sales, ΔROA), and market signals (securities issuance), fitted on SEC enforcement cases | F > 1.0 = above-normal misstatement probability; > 2.45 = high | Not in the tools; the paper gives coefficients |
| **Cash-yield test** | Other income ÷ average cash and investments | Far below market yields = suspect cash; Kaveri 7.4% | `cash_yield_check` |

## 5. Using the models as a screen

```python
from fi.data import load_kaveri
from fi.forensics import forensic_summary
s = forensic_summary(load_kaveri(), "FY26")
print(s["beneish"]["m_score"], s["altman_original"], s["piotroski"]["score"], s["accruals_ratio"], s["cash_yield"])
```

| Model | Kaveri FY26 | Flag? |
|:--|--:|:--|
| Beneish M | −2.14 | No (but trending toward the line; DSRI-driven) |
| Altman Z (original) | 6.99 | No — solvent |
| Piotroski F | 4/9 | Deteriorating fundamentals |
| Sloan accruals | 2.3% | Elevated, not extreme |
| Cash yield | 7.4% | Clean |

Rules for using scores:

1. **Run them on everything, every year.** Their value is in the cross-section and the trend, not in one number.
2. **A flag starts an investigation; a clean score ends nothing.** Beneish misses a quarter of manipulators;
   Altman is blind to fraud; Piotroski measures direction, not integrity.
3. **State the mapping.** By-nature P&Ls, lease accounting, and consolidation choices change the inputs; use one
   consistent mapping across the companies you compare.
4. **Exclude lenders and insurers** (no COGS, no inventory, leverage is the business) — use the lender
   checklist in [07.1](../07-special-valuation/01-banks-and-nbfcs.md) instead.
5. **Beware sector bias**: fast-growing companies score badly on SGI and TATA by construction; capital-light
   companies score well on Altman by construction. Compare within sector.
6. **Combine, don't average.** A company with M > −1.78 *and* rising DSO *and* an auditor change is a different
   animal from one with M > −1.78 because it grew 60%.

!!! tip "Trader's lens"
    Scores are signals with known hit rates and false-positive rates — the same statistics a systematic desk uses to
    judge an alpha. Beneish at ~76% sensitivity and ~17% false positives is a decent but noisy signal; you would not
    trade it alone, and you would not ignore it. Treat the forensic scores as a factor in the screen that feeds the
    discretionary process, and track their realised hit rate on your own universe.

!!! info "India notes"
    - The Beneish thresholds were fitted on US data; Indian studies (various, 2010s) find the model useful but
      with different base rates; treat −1.78 as a starting cut-off and look at the distribution across your
      universe.
    - Screener.in and some Indian data providers publish M-scores and Z-scores with undisclosed input mappings —
      recompute with your own mapping before relying on them.
    - Piotroski was designed for low-P/B stocks; Indian small-cap value screens combining P/B < 1.5 and F ≥ 7 have
      been popular with quant-value investors — with the governance overlay of [09.5](05-governance-red-flags-india.md)
      as the necessary filter that the score lacks.

!!! warning "Common mistakes"
    - Reading M > −1.78 as proof of manipulation.
    - Reading a high Altman Z as proof of health when the inputs may be false.
    - Using Piotroski on growth stocks (it penalises equity issuance and rising leverage that growth needs).
    - Mixing mappings across companies.
    - Running Beneish on a lender.
    - Not looking at *which* indices drive the score — the composition is the diagnosis.

## Key terms

| Term | Meaning |
|:--|:--|
| **Beneish M-score** | Eight-index logistic model of earnings-manipulation probability; flag above −1.78 |
| **DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA** | The Beneish indices (receivables, gross margin, asset quality, sales growth, depreciation, SG&A, leverage, accruals) |
| **Altman Z-score** | Five-ratio discriminant model of bankruptcy risk; safe above 2.99 (original) |
| **Z′ / Z″** | Altman variants for private companies / non-manufacturers and emerging markets |
| **Piotroski F-score** | Nine binary fundamental-strength signals; 8–9 strong, 0–2 weak |
| **Sloan accruals ratio** | (PAT − CFO) ÷ average total assets |
| **Montier C-score** | Six-flag "cooking the books" screen |
| **Dechow F-score** | Logistic misstatement model fitted on SEC enforcement cases |
| **Sensitivity / false-positive rate** | Share of true cases flagged / share of clean cases wrongly flagged |
| **Input mapping** | The translation of a company's reported lines into a model's variables |

## Check your understanding

1. Kaveri's FY25 M-score was −1.98. Which two indices contributed most to the rise from −2.32, and what does
   that tell you?
<details><summary>Answer</summary>DSRI (1.147 → 1.200; coefficient 0.92) and TATA (0.000 → 0.035; coefficient
4.679 — the largest weight): receivables and accruals. The score is saying "profit is not turning into cash because
receivables are growing" — the same diagnosis as the ratio analysis, mechanically.</details>

2. Recompute Kaveri's Altman Z at a market cap of ₹1,500 Cr (a 36% fall from September) and interpret.
<details><summary>Answer</summary>X₄ = 1,500/437.5 = 3.43; Z = 1.2×0.277 + 1.4×0.591 + 3.3×0.121 + 0.6×3.43 +
1.0×1.153 = 0.332 + 0.827 + 0.399 + 2.057 + 1.153 = 4.77 — still safe. The balance sheet, not the stock price,
is what keeps Kaveri solvent; X₄ is the price-dependent term.</details>

3. Why would Satyam have passed Altman and possibly Beneish in 2008?
<details><summary>Answer</summary>Both models take the reported numbers as inputs: fabricated cash raised working
capital and equity (Altman), and fabricated revenue with matching fabricated receivables and cash kept the
Beneish indices in normal ranges. Only cross-checks *outside* the model (interest income on cash, tax paid vs
profit) exposed it — models fitted on manipulators who bent numbers do not catch inventors of numbers.</details>

4. A fast-growing company has M = −1.6 with SGI = 1.6 and all other indices near 1. Manipulator?
<details><summary>Answer</summary>Not on this evidence — the score is driven by the sales-growth index alone
(0.892 × 1.6). Growth raises the *prior* of manipulation, which is why SGI is in the model, but with DSRI, AQI and
TATA normal the accounting shows no marks. Investigate, don't conclude.</details>

5. Name three reasons Piotroski's F-score is inappropriate for a bank.
<details><summary>Answer</summary>No gross margin (signal 8); leverage is the business, so "falling leverage" is
not a quality signal (5); the current ratio is meaningless for a bank (6); and CFO for a lender swings with loan
and deposit flows, so CFO > PAT (4) is uninformative.</details>

## Go deeper

- Messod Beneish, "The Detection of Earnings Manipulation", *Financial Analysts Journal* 55(5), 1999.
- Edward Altman, "Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy",
  *Journal of Finance*, 1968; and his 2000/2005 updates on Z′, Z″ and emerging markets.
- Joseph Piotroski, "Value Investing: The Use of Historical Financial Statement Information to Separate Winners
  from Losers", *Journal of Accounting Research*, 2000.
- Patricia Dechow, Weili Ge, Chad Larson & Richard Sloan, "Predicting Material Accounting Misstatements",
  *Contemporary Accounting Research*, 2011.
- James Montier, "Cooking the Books, or More Sailing Under the Black Flag" (Société Générale, 2008).
- `tools/fi/forensics.py` and `tools/examples/forensic_scores_kaveri.py` — read the code and the mapping docstring.

---
[← Previous: 09.5 Governance red flags in India](05-governance-red-flags-india.md) · [Module index](index.md) · [Next: 09.7 The forensic checklist →](07-the-forensic-checklist.md)
