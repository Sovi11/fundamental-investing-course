# Running example 2 — Nirmal Finance Ltd (fictional NBFC)

!!! warning "Fictional company"
    Nirmal Finance Ltd (NFL) is **invented** for this course. Numbers come from
    `tools/running_example/generate.py` (borrowings are the balancing item; the balance sheet balances every year).
    Use these numbers in every lesson, exercise and mock that references NFL. ₹ crore unless stated.

## 1. Profile

| Item | Detail |
|:--|:--|
| Business | Nashik-based NBFC (NBFC–Investment & Credit Company, **middle layer** under RBI's scale-based regulation). Loans for used commercial vehicles (55%), tractors (20%), and secured MSME loans against property (25%) across Maharashtra, Gujarat, MP and Karnataka |
| Branches | 410 (FY26), mostly in tier-3/4 towns |
| Funding mix (FY26) | Bank term loans 58%, NCDs 24%, securitisation/DA 11%, commercial paper 4%, sub-debt 3% |
| ALM | Assets (loans) avg. tenor ~34 months; liabilities avg. tenor ~30 months — broadly matched; CP < 5% of borrowings |
| Promoter | Founder family 38% + a PE fund 17% (entered FY19); QIP of ₹300 Cr in FY24 at ₹300/share (1.0 Cr new shares) |
| Share price | ₹385 at 31-Mar-2026; **₹402 on 18-Sep-2026** |
| Credit rating | "AA– / Stable" |

## 2. Profit & loss (₹ Cr)

| ₹ Cr | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| Interest income | 435.2 | 480.8 | 573.6 | 721.7 | 901.3 | 1,073.2 |
| Interest expense (finance costs) | 191.5 | 201.1 | 239.2 | 304.9 | 376.5 | 442.1 |
| **Net interest income (NII)** | **243.7** | **279.7** | **334.4** | **416.8** | **524.8** | **631.1** |
| Fee & other operating income | 15.3 | 19.9 | 24.0 | 34.0 | 41.9 | 50.8 |
| **Net total income** | **259.0** | **299.6** | **358.4** | **450.8** | **566.7** | **681.9** |
| Operating expenses (employee + other + depreciation) | 112.0 | 119.5 | 140.8 | 169.8 | 204.4 | 241.3 |
| **Pre-provision operating profit (PPOP)** | **147.0** | **180.1** | **217.6** | **281.0** | **362.3** | **440.6** |
| Impairment on financial instruments (credit cost) | 91.6 | 59.7 | 48.1 | 55.2 | 83.8 | 120.6 |
| **Profit before tax** | **55.4** | **120.4** | **169.5** | **225.8** | **278.5** | **320.0** |
| Tax | 13.9 | 30.3 | 42.7 | 56.8 | 70.1 | 80.5 |
| **Profit after tax** | **41.5** | **90.1** | **126.8** | **169.0** | **208.4** | **239.5** |

## 3. Balance sheet (as at 31-March, ₹ Cr)

Opening (31-Mar-2020): gross loans 2,480.0; ECL 103.0; liquid assets 270.0; borrowings 1,960.0; equity 620.0.

| ₹ Cr | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| Gross loans (AUM, all on-book) | 2,610.0 | 3,080.0 | 3,790.0 | 4,700.0 | 5,780.0 | 6,920.0 |
| Less: ECL allowance (stage 1+2+3) | 82.2 | 87.7 | 94.6 | 108.2 | 134.9 | 170.9 |
| Net loans | 2,527.8 | 2,992.3 | 3,695.4 | 4,591.8 | 5,645.1 | 6,749.1 |
| Cash, bank & liquid investments | 310.0 | 290.0 | 360.0 | 420.0 | 480.0 | 560.0 |
| Other assets | 47.0 | 55.4 | 68.2 | 84.6 | 104.0 | 124.6 |
| **Total assets** | **2,884.8** | **3,337.7** | **4,123.6** | **5,096.4** | **6,229.1** | **7,433.7** |
| Borrowings (NCDs, bank loans, CPs, securitisation) | 2,158.1 | 2,519.1 | 3,175.4 | 3,676.5 | 4,598.8 | 5,565.4 |
| Other liabilities & provisions | 65.2 | 77.0 | 94.8 | 117.5 | 144.5 | 173.0 |
| Net worth (equity) | 661.5 | 741.6 | 853.4 | 1,302.4 | 1,485.8 | 1,695.3 |
| &nbsp;&nbsp;*of which fresh equity raised in the year (QIP)* | 0.0 | 0.0 | 0.0 | 300.0 | 0.0 | 0.0 |
| Dividends paid in the year | 0.0 | 10.0 | 15.0 | 20.0 | 25.0 | 30.0 |

## 4. Asset quality & capital (₹ Cr)

| ₹ Cr | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| Disbursements | 1,540.0 | 1,980.0 | 2,460.0 | 2,950.0 | 3,480.0 | 3,990.0 |
| Gross stage-3 loans (GNPA) | 114.8 | 110.9 | 109.9 | 117.5 | 150.3 | 200.7 |
| Stage-3 ECL | 59.7 | 61.0 | 61.5 | 67.0 | 84.2 | 110.4 |
| Stage 1+2 ECL | 22.5 | 26.7 | 33.1 | 41.2 | 50.7 | 60.5 |
| Net stage-3 (NNPA) | 55.1 | 49.9 | 48.4 | 50.5 | 66.1 | 90.3 |
| Write-offs (derived) | 112.4 | 54.2 | 41.2 | 41.6 | 57.1 | 84.6 |
| Risk-weighted assets | 2,508.1 | 2,953.3 | 3,647.4 | 4,526.6 | 5,557.6 | 6,642.0 |
| Tier-2 capital (sub-debt) | 60.0 | 60.0 | 80.0 | 80.0 | 110.0 | 140.0 |

## 5. Key ratios

| Ratio | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|:--|--:|--:|--:|--:|--:|--:|
| Yield on avg loans | 17.1% | 16.9% | 16.7% | 17.0% | 17.2% | 16.9% |
| Cost of funds (on avg borrowings) | 9.3% | 8.6% | 8.4% | 8.9% | 9.1% | 8.7% |
| NIM (NII / avg loans) | 9.6% | 9.8% | 9.7% | 9.8% | 10.0% | 9.9% |
| Cost-to-income (opex / net total income) | 43.2% | 39.9% | 39.3% | 37.7% | 36.1% | 35.4% |
| Credit cost (on avg loans) | 3.6% | 2.1% | 1.4% | 1.3% | 1.6% | 1.9% |
| GNPA % | 4.4% | 3.6% | 2.9% | 2.5% | 2.6% | 2.9% |
| NNPA % (on net loans) | 2.2% | 1.7% | 1.3% | 1.1% | 1.2% | 1.3% |
| Provision coverage (stage-3 ECL / GNPA) | 52.0% | 55.0% | 56.0% | 57.0% | 56.0% | 55.0% |
| RoA (PAT / avg total assets) | 1.5% | 2.9% | 3.4% | 3.7% | 3.7% | 3.5% |
| RoE (PAT / avg equity) | 6.5% | 12.8% | 15.9% | 15.7% | 14.9% | 15.1% |
| Leverage (total assets / equity) | 4.4x | 4.5x | 4.8x | 3.9x | 4.2x | 4.4x |
| CRAR | 28.8% | 27.1% | 25.6% | 30.5% | 28.7% | 27.6% |
| Tier-1 ratio | 26.4% | 25.1% | 23.4% | 28.8% | 26.7% | 25.5% |
| Shares outstanding (crore) | 10.0 | 10.0 | 10.0 | 11.0 | 11.0 | 11.0 |
| EPS, ₹ | 4.2 | 9.0 | 12.7 | 15.4 | 18.9 | 21.8 |
| Book value per share, ₹ | 66.2 | 74.2 | 85.3 | 118.4 | 135.1 | 154.1 |
| Share price at 31-March, ₹ | 140 | 190 | 215 | 330 | 420 | 385 |
| P/E | 33.7x | 21.1x | 17.0x | 21.5x | 22.2x | 17.7x |
| P/B | 2.1x | 2.6x | 2.5x | 2.8x | 3.1x | 2.5x |

Note: yields, cost of funds, NIM and credit cost are on **average** balances. RWA are simplified
(loans at 95% risk weight, liquid assets at 20%). FY21 credit cost reflects COVID-19 stress and the
RBI moratorium; FY25–26 show a mild uptick in stage-3 in the used-CV book.
