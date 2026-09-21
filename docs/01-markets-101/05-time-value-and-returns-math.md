# 01.5 · Time value of money & returns math

> **Why this matters:** every valuation in this course is a discounting exercise, and every performance claim
> you will read ("15% CAGR", "18% XIRR", "the stock re-rated") is a returns calculation. The formulas are
> simple. The mistakes are common and expensive: averaging when you should compound, annualising a SIP
> the wrong way, mixing real and nominal, confusing a multiple change with earnings growth.

**Learning objectives**: after this lesson you can:

- Compute future and present values, CAGR and doubling times, and say when the Rule of 72 breaks down.
- Derive the perpetuity, growing-perpetuity (Gordon) and annuity formulas from a geometric series, and apply
  them to a loan EMI and a terminal value.
- Compute IRR and XIRR for irregular cash flows (a monthly SIP), and explain three ways IRR misleads.
- Convert between nominal and real returns exactly (Fisher), not just approximately.
- Decompose total shareholder return into EPS growth, change in P/E and dividend yield, using Kaveri's
  FY21–FY26 data, both multiplicatively and in logs.
- Explain log vs simple returns, why a 50% loss needs a 100% gain, and volatility drag ($G \approx A - \sigma^2/2$).

**Prerequisites:** [01.2 Shares, market cap & enterprise value](02-shares-market-cap-and-enterprise-value.md)
(EPS, P/E), school algebra, and a Python install for the optional snippets  ·  **Time:** ~100 min

---

## 1. Compounding: the one formula everything else comes from

Money invested at rate $r$ per period for $n$ periods grows to

$$
FV = PV \times (1 + r)^n
$$

where $FV$ is future value and $PV$ is present value. Each period you earn return on the principal *and*
on all previously earned returns. That is **compounding**: growth proportional to the current level, i.e.
exponential growth.

**Compounding frequency.** Rates are usually quoted per year, but interest may be credited more often. A
nominal annual rate $r$ compounded $m$ times a year gives an **effective annual rate (EAR)** of

$$
\text{EAR} = \left(1 + \frac{r}{m}\right)^m - 1 \quad\xrightarrow{m\to\infty}\quad e^{r} - 1
$$

The limit is **continuous compounding**, $FV = PV\,e^{rt}$.

### Worked example 1: a fixed deposit, four ways

You put ₹1,00,000 in a 5-year deposit at 7.5% a year. (Many Indian bank term deposits compound quarterly.
Check your bank's terms.)

| Compounding | Formula | Value after 5 years | EAR |
|:--|:--|--:|--:|
| Annual | $1{,}00{,}000 \times 1.075^{5}$ | ₹1,43,563 | 7.50% |
| Quarterly | $1{,}00{,}000 \times (1 + 0.075/4)^{20}$ | ₹1,44,995 | 7.71% |
| Monthly | $(1 + 0.075/12)^{12} - 1$ | — | 7.76% |
| Continuous | $1{,}00{,}000 \times e^{0.075 \times 5}$ | ₹1,45,499 | 7.79% |

The quoted rate is the same in every row. Only the effective rate changes. **Always convert to EAR before
comparing** two instruments, such as an FD quoted "7.5% compounded quarterly" and a bond with a 7.6%
annual coupon.

## 2. CAGR: the growth rate that actually connects two numbers

The **compound annual growth rate (CAGR)** is the constant rate that turns a starting value into an ending
value over $n$ years:

$$
\text{CAGR} = \left(\frac{V_{\text{end}}}{V_{\text{start}}}\right)^{1/n} - 1
$$

It answers: *if growth had been smooth, what rate would have produced the same result?*

**CAGR vs the average of annual growth rates.** Kaveri Pumps' revenue
([reference data](../appendix/running-example/kaveri-pumps.md)) went from ₹612.0 Cr (FY21) to ₹1,318.0 Cr
(FY26), five years of growth:

$$
\text{CAGR} = (1{,}318 / 612)^{1/5} - 1 = 16.58\%
$$

The simple average of the five annual growth rates (23.9%, 15.3%, 15.1%, 16.5%, 12.5%) is 16.64%, almost
the same, because revenue growth was fairly steady. Now do the same for Kaveri's **share price** at each
31 March: ₹210, 320, 360, 610, 780, 520.

| Year | Price at 31-Mar (₹) | Return in year |
|:--|--:|--:|
| FY21 | 210 | – |
| FY22 | 320 | 52.4% |
| FY23 | 360 | 12.5% |
| FY24 | 610 | 69.4% |
| FY25 | 780 | 27.9% |
| FY26 | 520 | (33.3%) |
| **Arithmetic mean of returns** | | **25.8%** |
| **CAGR FY21→FY26** | | **19.9%** |

The arithmetic mean overstates what an investor earned by six percentage points. If you had compounded
₹210 at 25.8% for five years you would have ₹661, not ₹520. The gap between the two means grows with
volatility. §10 shows it is almost exactly $\sigma^2/2$.

**CAGR is hostage to its endpoints.** From FY21 to FY25 (₹210 → ₹780, four years) Kaveri's price CAGR was
**38.8%**. Add one bad year and FY21→FY26 is **19.9%**. From 31-Mar-2021 to ₹390 on 18-Sep-2026 (5.47 years)
it is **12.0%**. All three are "correct". When someone quotes you a CAGR, ask *from when to when*, and
recompute it with the endpoints moved.

**A real long-run example.** The BSE Sensex had a base value of 100 in 1978–79 (base date 1-Apr-1979)
([background](https://en.wikipedia.org/wiki/BSE_SENSEX)) and closed at about **71,948** on 30-Mar-2026, the
last session of FY26 (Yahoo Finance, `^BSESN`). That is a multiple of about 719× over 47.0 years:

$$
\text{CAGR} = 719.5^{1/47.0} - 1 \approx 15.0\% \text{ a year}
$$

This is a *price* index, so dividends are excluded and a total-return series would be higher. It is also
*nominal*. §8 shows how to strip out inflation.

## 3. The Rule of 72

How long does it take to double at rate $r$? Solve $(1+r)^n = 2$:

$$
n = \frac{\ln 2}{\ln(1 + r)} \approx \frac{0.693}{r}\left(1 + \frac{r}{2}\right) \approx \frac{69.3 + 0.35 \times (100r)}{100r}
$$

using $\ln(1+r) \approx r - r^2/2$. At $r = 8\%$ the numerator is $69.3 + 2.8 \approx 72$. That is the
**Rule of 72**: doubling time ≈ 72 ÷ (rate in %). The number 72 is also convenient because it divides by 2,
3, 4, 6, 8, 9 and 12.

| Rate | Exact doubling time (years) | Rule of 72 | Error of the rule |
|--:|--:|--:|--:|
| 2% | 35.00 | 36.00 | +2.8% |
| 6% | 11.90 | 12.00 | +0.9% |
| 8% | 9.01 | 9.00 | −0.1% |
| 12% | 6.12 | 6.00 | −1.9% |
| 15% | 4.96 | 4.80 | −3.2% |
| 20% | 3.80 | 3.60 | −5.3% |
| 36% | 2.25 | 2.00 | −11.3% |

The rule is excellent between about 5% and 12%. It gets worse at high rates, which is exactly where Indian
small-cap narratives live. For continuous compounding use 69.3 exactly.

Use it for fast sanity checks. The reference valuation's reverse DCF says ₹390 implies Kaveri revenue
growth of ~14.1% a year for ten years ([kaveri-valuation.md](../appendix/running-example/kaveri-valuation.md)).
Rule of 72: $72/14.1 \approx 5.1$ years to double (exact: 5.25), so ten years is about two doublings. The
market is pricing revenue of roughly 4× FY26 within ten years (exactly $1.141^{10} = 3.7\times$). That is a much easier claim to argue with than "14.1%".

## 4. Present value and discounting

Rearrange the compounding formula and you have **discounting**, the core operation of valuation:

$$
PV = \frac{CF_n}{(1 + r)^n}
$$

Here $r$ is the **discount rate**: the return you could earn elsewhere on an investment of similar risk (your
**opportunity cost**). The factor $1/(1+r)^n$ is the **discount factor**. A stream of cash flows is worth the
sum of their present values. Subtracting the upfront cost gives the **net present value (NPV)**:

$$
NPV = -C_0 + \sum_{t=1}^{n} \frac{CF_t}{(1 + r)^t}
$$

**Example.** ₹1 Cr receivable in 10 years, discounted at 12%, is worth $1{,}00{,}00{,}000 / 1.12^{10} =
₹32.2$ lakh today. At 12%, a rupee ten years out is worth under a third of a rupee now. That is why the
discount rate matters so much in any DCF.

**Link to Kaveri.** The reference valuation discounts each year's free cash flow at WACC = 12.19% (12.186%
unrounded, from $0.9 \times 12.8\% + 0.1 \times 6.66\%$; derived in
[06.2](../06-valuation/02-cost-of-capital.md)). It uses a **mid-year convention**, since cash arrives through
the year rather than on 31 March, so FY27's cash flow is discounted half a year:

$$
DF_{FY27} = \frac{1}{1.12186^{0.5}} = 0.9441 \qquad PV = 108.5 \times 0.9441 = ₹102.4\text{ Cr}
$$

exactly as in the reference table. Everything in [06.3 DCF step by step](../06-valuation/03-dcf-step-by-step.md)
is this operation repeated, plus one trick for the infinite tail, which comes next.

## 5. Perpetuities and the Gordon growth formula

### Level perpetuity

A **perpetuity** pays $C$ every year forever, starting in one year. Its value is a geometric series:

$$
PV = \frac{C}{1+r} + \frac{C}{(1+r)^2} + \cdots = \frac{C}{1+r}\sum_{k=0}^{\infty}\left(\frac{1}{1+r}\right)^k
= \frac{C}{1+r}\cdot\frac{1}{1 - \frac{1}{1+r}} = \frac{C}{r}
$$

₹10 a year forever at 12% is worth $10/0.12 = ₹83.33$. Infinite payments have a finite value because
distant payments are discounted towards zero.

### Growing perpetuity (Gordon)

Now let the payment grow at $g$ a year: $C_1$ next year, $C_1(1+g)$ the year after, and so on. Then

$$
PV = \sum_{t=1}^{\infty}\frac{C_1(1+g)^{t-1}}{(1+r)^t}
= \frac{C_1}{1+r}\sum_{k=0}^{\infty} q^k, \qquad q = \frac{1+g}{1+r}
$$

The series converges only if $q < 1$, i.e. $g < r$, and then

$$
PV = \frac{C_1}{1+r}\cdot\frac{1}{1-q} = \frac{C_1}{1+r}\cdot\frac{1+r}{r-g} = \boxed{\frac{C_1}{r - g}}
$$

This is the **Gordon growth model** (after Myron Gordon). Three things to notice:

1. **$C_1$ is *next* year's cash flow**, not this year's. Using $C_0$ is a classic error that understates value
   by a factor of $(1+g)$.
2. **$g$ must be below $r$**, and for a perpetuity it must be sustainable forever. In nominal rupees that
   means roughly nominal GDP growth or less. A company cannot outgrow the economy forever.
3. **Value is extremely sensitive to $r - g$.** The denominator is a small difference between two uncertain
   numbers, so the output is *convex* in it.

### Worked example 2: a dividend stream and Kaveri's terminal value

**(a) A dividend discount model.** A stock will pay ₹10 per share next year, dividends grow at 6% forever, and
you require 12%:

$$
P = \frac{10}{0.12 - 0.06} = ₹166.67
$$

At 11% the value is ₹200.00. At 13% it is ₹142.86. A ±1 point change in $r$ moves value by +20% / −14%. The
asymmetry is the convexity in $r-g$.

Rearranged, $r = C_1/P + g$: **expected return = dividend yield + growth**. This identity comes back in §9,
and in [06.5](../06-valuation/05-relative-valuation-and-multiples.md) it becomes the justified P/E.

**(b) Kaveri's terminal value.** The reference valuation assumes free cash flow of ₹243.3 Cr in FY37, growing
at 5.5% forever, discounted at 12.186%:

$$
TV_{FY36} = \frac{243.3}{0.12186 - 0.055} = \frac{243.3}{0.06686} \approx ₹3{,}639\text{ Cr}
$$

(The reference page shows ₹3,638.7 because it carries unrounded cash flows.) Discounted ten full years,
$3{,}639 / 1.12186^{10} \approx ₹1{,}152$ Cr, which is 55% of Kaveri's enterprise value. Sensitivity: at
$g = 5.0\%$ the TV is ₹3,386 Cr. At $g = 6.0\%$ it is ₹3,933 Cr. Half a point of *perpetual* growth moves
the TV by about 8%. The course's `tools/fi/valuation.py::gordon_value(cf_next, r, g)` implements this
formula, and it refuses $g \ge r$.

!!! tip "Trader's lens: the discount rate is an implied quantity"
    Rearranging Gordon to $r = C_1/P + g$ turns the valuation question inside out. Instead of "what is it
    worth at my $r$?", ask "what return is the market price *implying*?" That is exactly what you do when you
    back an implied vol out of an option price. IRR (§7) is the same inversion for irregular cash flows, and
    the reverse DCF in [06.6](../06-valuation/06-reverse-dcf-and-expectations.md) inverts for growth instead
    of the rate. In every case the price is the input and the expectation is the output. You then compare
    that implied number with your own estimate, just as you would compare implied with forecast realised vol.

## 6. Annuities: finite streams, loans and EMIs

An **annuity** pays $C$ a period for $n$ periods. Here is the neat trick: an annuity is a perpetuity starting
now *minus* a perpetuity starting after period $n$:

$$
PV_{\text{annuity}} = \frac{C}{r} - \frac{1}{(1+r)^n}\cdot\frac{C}{r} = C\cdot\frac{1 - (1+r)^{-n}}{r}
$$

and the **growing annuity** (first payment $C$, growth $g$) follows the same way:

$$
PV = \frac{C}{r-g}\left[1 - \left(\frac{1+g}{1+r}\right)^{n}\right]
$$

Examples: ₹1 lakh a year for 10 years at 10% is worth ₹6,14,457. A payment of 100 growing at 8% for 10
years, discounted at 12%, is worth 762.21 (checked by brute-force summation).

**Loans.** An **EMI** (equated monthly instalment) is just an annuity solved for the payment. With principal
$P$, monthly rate $i$ and $n$ months:

$$
\text{EMI} = P\cdot\frac{i}{1 - (1+i)^{-n}}
$$

### Worked example 3: a Nirmal Finance vehicle loan, and the flat-rate trap

Nirmal Finance (fictional; [reference](../appendix/running-example/nirmal-finance.md)) earned a 16.9% yield on
its loans in FY26. Take a used-truck loan of **₹10,00,000 at 16.9% a year for 36 months**, reducing balance:

$$
i = 0.169/12 = 1.4083\% \qquad \text{EMI} = 10{,}00{,}000 \times \frac{0.014083}{1 - 1.014083^{-36}} = ₹35{,}603
$$

Total paid = 36 × ₹35,603 ≈ ₹12,81,707, so total interest ≈ ₹2,81,707. In month 1, interest is
₹10,00,000 × 1.4083% = ₹14,083 and principal repaid is ₹21,520. Each month the interest share falls, because
interest is charged only on the balance still outstanding.

**The flat-rate trap.** Informal vehicle and consumer lending in India has often quoted a **flat rate**, with
interest computed on the *original* principal for the whole tenure. A "9% flat" loan of ₹10 lakh for 3 years
charges 9% × 3 × ₹10 lakh = ₹2,70,000 of interest, so the EMI = ₹12,70,000/36 = **₹35,278**. Solve the annuity
formula for the rate that produces that EMI on a reducing balance and you get **1.354% a month = 16.24% a
year nominal (17.5% effective)**. The "9%" loan costs almost as much as Nirmal's 16.9% loan. The borrower
repays principal every month but keeps paying interest on money already returned. A flat rate is roughly
*half* the true rate. When you analyse lenders ([07.1](../07-special-valuation/01-banks-and-nbfcs.md)), always
work in yields on average balances.

## 7. IRR and XIRR

The **internal rate of return (IRR)** is the discount rate that makes NPV zero:

$$
0 = \sum_{t=0}^{n}\frac{CF_t}{(1 + \text{IRR})^t}
$$

It is the single "yield" of a cash-flow stream. No closed form exists in general, so you solve numerically
(bisection or Newton's method). **XIRR** is the same idea with actual dates. Each cash flow is discounted by
$(1+r)^{(d_i - d_0)/365}$, which is the convention in Excel's and Google Sheets' `XIRR`.

**IRR of owning Kaveri, FY21–FY26.** Buy at ₹210 on 31-Mar-2021, receive the dividends paid in FY22–FY26
(₹1.5, 2.0, 2.5, 3.5, 4.0; assume each arrives at year-end), sell at ₹520 on 31-Mar-2026:

$$
0 = -210 + \frac{1.5}{1+r} + \frac{2.0}{(1+r)^2} + \frac{2.5}{(1+r)^3} + \frac{3.5}{(1+r)^4} + \frac{4.0 + 520}{(1+r)^5}
\;\Rightarrow\; r = 20.7\%
$$

(With dividends mid-year, 20.8%.) The **multiple on invested capital** is $(520 + 13.5)/210 = 2.54\times$.
IRR tells you the *rate*, MOIC the *amount*. A 50% IRR held for three months can be worth less than a 15%
IRR held for ten years.

### Worked example 4: a monthly SIP and its XIRR

You invest **₹10,000 on the 5th of every month** (next weekday if the 5th is a weekend) from Oct-2025 to
Sep-2026 in a fund with the (fictional) NAVs below, and value the holding on 18-Sep-2026 at a NAV of ₹53.10.

| # | Date | NAV (₹) | Units bought (₹10,000 ÷ NAV) |
|--:|:--|--:|--:|
| 1 | 06-Oct-2025 | 50.00 | 200.0000 |
| 2 | 05-Nov-2025 | 51.20 | 195.3125 |
| 3 | 05-Dec-2025 | 49.80 | 200.8032 |
| 4 | 05-Jan-2026 | 47.50 | 210.5263 |
| 5 | 05-Feb-2026 | 46.10 | 216.9197 |
| 6 | 05-Mar-2026 | 44.00 | 227.2727 |
| 7 | 06-Apr-2026 | 45.30 | 220.7506 |
| 8 | 05-May-2026 | 47.90 | 208.7683 |
| 9 | 05-Jun-2026 | 49.20 | 203.2520 |
| 10 | 06-Jul-2026 | 50.60 | 197.6285 |
| 11 | 05-Aug-2026 | 51.80 | 193.0502 |
| 12 | 07-Sep-2026 | 52.40 | 190.8397 |
| | **Total** | | **2,465.1237** |

- Invested: 12 × ₹10,000 = **₹1,20,000**. Value on 18-Sep-2026: 2,465.1237 × ₹53.10 = **₹1,30,898**.
- **Absolute return** = 1,30,898 / 1,20,000 − 1 = **9.08%**.
- **XIRR** (solve $\sum_i CF_i/(1+r)^{(d_i-d_0)/365} = 0$ with twelve −₹10,000 flows and one +₹1,30,898 flow) = **18.9%**.
- A tempting wrong answer: "9.08% over 0.95 years (Oct to Sep), so about 9.6% a year." This treats all
  ₹1,20,000 as if it were invested on day one. On average each rupee was invested for only **180 days**
  (0.49 years), so the annualised return is about double the absolute return. XIRR does this weighting
  properly.

Two more lessons from the same table:

- **Your average cost** is ₹1,20,000 / 2,465.1237 = **₹48.68**, which is the *harmonic* mean of the NAVs. The
  simple average NAV was ₹48.82. A fixed rupee amount buys more units when the price is low. The harmonic
  mean is always ≤ the arithmetic mean, and that is "rupee-cost averaging".
- **It is not a free lunch.** Here the SIP (XIRR 18.9%) beat investing ₹1,20,000 on day one (6.2% absolute,
  ≈6.5% annualised) only because the NAV dipped mid-way and recovered. In a market that rises steadily, a
  lump sum invested earlier wins, because it spends more time invested. A SIP is valuable as *discipline and
  time-diversification*, not as a return enhancer.

Fund platforms and portfolio trackers in India typically report SIP performance as XIRR, and you can
reproduce it yourself:

```python
from datetime import date

def xirr(flows, lo=-0.99, hi=10.0, tol=1e-10):
    """flows: list of (date, amount). Negative = money in, positive = money out. Bisection on XNPV."""
    d0 = flows[0][0]
    f = lambda r: sum(a / (1 + r) ** ((d - d0).days / 365) for d, a in flows)
    for _ in range(300):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
        if hi - lo < tol:
            break
    return (lo + hi) / 2

sip_dates = [date(2025,10,6), date(2025,11,5), date(2025,12,5), date(2026,1,5), date(2026,2,5), date(2026,3,5),
             date(2026,4,6), date(2026,5,5), date(2026,6,5), date(2026,7,6), date(2026,8,5), date(2026,9,7)]
flows = [(d, -10_000) for d in sip_dates] + [(date(2026, 9, 18), 130_898.07)]
print(f"XIRR = {xirr(flows):.2%}")   # XIRR = 18.94%
```

To try it on real data, pull an index or fund NAV series with `yfinance` (e.g. `^NSEI` for the Nifty 50,
which ignores dividends and costs) and replace the fictional NAVs. Disable any VPN first, because
`yfinance` calls often fail behind one. On Windows, wrap stdout for ₹ output as described in
`tools/SPEC.md` and [the tools appendix](../appendix/tools.md).

### Three ways IRR misleads

1. **Multiple IRRs.** If cash flows change sign more than once, there can be several IRRs. The stream
   −100, +230, −132 has NPV = 0 at **both** 10% and 20%. Check: $-100 + 230/1.1 - 132/1.21 = 0$ and
   $-100 + 230/1.2 - 132/1.44 = 0$. Use NPV at a stated discount rate instead.
2. **The reinvestment assumption.** IRR implicitly assumes interim cash flows are reinvested at the IRR itself.
   A 40% IRR project that returns cash early does not make you 40% on that cash afterwards.
3. **Scale and duration blindness.** IRR ignores how much money is at work and for how long. Private-equity
   funds that borrow to delay capital calls raise their IRR without raising MOIC. Always look at IRR *and*
   MOIC together.

## 8. Real vs nominal returns

A **nominal** return is measured in rupees. A **real** return is measured in purchasing power. With
inflation $\pi$, the exact relation (the **Fisher equation**) is

$$
(1 + n) = (1 + r_{\text{real}})(1 + \pi) \quad\Rightarrow\quad r_{\text{real}} = \frac{1 + n}{1 + \pi} - 1 \approx n - \pi
$$

The approximation is fine for small numbers. Use the exact form when inflation is high or you are
compounding over many years.

**India's anchor.** The Central Government has retained the RBI's inflation target at **4% CPI inflation with a
2%–6% tolerance band for April 2026 to March 2031**
([RBI, Monetary Policy overview](https://www.rbi.org.in/scripts/FS_Overview.aspx?fn=2752), checked Sep-2026).
Use 4% as a reasonable long-run planning assumption, but check MoSPI's latest CPI release for the current
print, which can sit well away from target.

| Nominal return | Inflation | Exact real return | Approximation $n - \pi$ |
|:--|--:|--:|--:|
| FD at 7.0% (pre-tax) | 4.0% | 2.88% | 3.00% |
| FD after tax at a 30% marginal rate: $7.0\% \times 0.7 = 4.9\%$ | 4.0% | 0.87% | 0.90% |
| Same, if inflation runs at the 6% upper band | 6.0% | (1.04%) | (1.10%) |

(The 30% marginal rate is an assumption for illustration. Interest income is taxed at your slab rate, and
current slabs are in [11.5](../11-process/05-monitoring-and-selling.md).) A "safe" deposit can lose purchasing
power after tax. That is the base rate any equity investment has to beat.

**Two applications.**

- **Kaveri's terminal growth of 5.5% is nominal.** In real terms it is $1.055/1.04 - 1 = 1.44\%$ a year
  forever. That is modest next to India's real GDP growth, and deliberately so: a perpetuity rate must hold
  *forever*, after competitive advantages have faded, so it should sit well below the economy's growth rate.
- **The Sensex's 15.0% nominal CAGR** (§2): if CPI inflation averaged, say, 7% over 1979–2026 (an assumption
  for illustration; check the Labour Bureau/MoSPI series for the actual figure), the real price CAGR would be
  $1.150/1.07 - 1 \approx 7.5\%$ a year before dividends.

**Consistency rule:** discount nominal cash flows at a nominal rate and real cash flows at a real rate. Mixing
them (e.g., a nominal 12% WACC on cash flows projected in today's prices) is one of the DCF mistakes listed in
[06.4](../06-valuation/04-dcf-in-practice.md).

## 9. Total shareholder return: where did the money come from?

**Total shareholder return (TSR)** is price change plus dividends. Since price = EPS × P/E,

$$
\frac{P_1}{P_0} = \frac{\text{EPS}_1}{\text{EPS}_0} \times \frac{(P/E)_1}{(P/E)_0}
\quad\Rightarrow\quad
1 + \text{price return} = (1 + g_{\text{EPS}})(1 + \Delta_{P/E})
$$

and adding the dividend yield gives the familiar approximation

$$
\text{TSR} \approx g_{\text{EPS}} + \Delta_{P/E} + \text{dividend yield}
$$

In logs the price part is **exactly** additive, $\ln\frac{P_1}{P_0} = \ln\frac{\text{EPS}_1}{\text{EPS}_0} + \ln\frac{(P/E)_1}{(P/E)_0}$,
which is one reason analysts like log returns (§10).

This decomposition is the most useful diagnostic in equity investing. It separates what the **business**
delivered (EPS growth, dividends) from what the **market's mood** delivered (the multiple). A fundamental
investor wants returns from the first. Returns from the second are borrowed from the future, or from the next
buyer.

### Worked example 5: Kaveri FY21 → FY26

Data from the reference page: EPS = PAT / 6.00 Cr shares (FY21: 32.8/6 = ₹5.47; FY26: 90.5/6 = ₹15.08); price
at 31 March; dividend per share paid in the year.

| Year | EPS (₹) | Price (₹) | P/E | EPS growth | P/E change | Price return | Div. yield (DPS ÷ opening price) | TSR |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| FY21 | 5.47 | 210 | 38.4x | – | – | – | – | – |
| FY22 | 7.87 | 320 | 40.7x | 43.9% | 5.9% | 52.4% | 0.7% | 53.1% |
| FY23 | 10.43 | 360 | 34.5x | 32.6% | (15.2%) | 12.5% | 0.6% | 13.1% |
| FY24 | 14.40 | 610 | 42.4x | 38.0% | 22.8% | 69.4% | 0.7% | 70.1% |
| FY25 | 16.23 | 780 | 48.0x | 12.7% | 13.4% | 27.9% | 0.6% | 28.4% |
| FY26 | 15.08 | 520 | 34.5x | (7.1%) | (28.2%) | (33.3%) | 0.5% | (32.8%) |

Check one row multiplicatively. FY24: $1.380 \times 1.228 = 1.694$, i.e. a 69.4% price return ✓.

**Five-year totals (CAGR):**

| Component | FY21→FY26 CAGR | In logs (5-year total) |
|:--|--:|--:|
| EPS growth | 22.5% | +1.015 |
| P/E change (38.4x → 34.5x) | (2.1%) | −0.108 |
| **Price return** = $1.225 \times 0.979 - 1$ | **19.9%** | **+0.907** |
| Dividend yield (average) | ≈0.6% | |
| **TSR** (IRR with dividends, §7) | **20.7%** | |

The additive approximation gives $22.5 - 2.1 + 0.6 = 21.0\%$ against an exact 20.7%. That is close, but the
cross-terms matter when components are large, so use the multiplicative form (or logs) for anything precise.

**Reading the story:** over five years, *all* of Kaveri's return came from earnings growth. The multiple was a
slight drag. But the year-by-year table shows two different regimes. In FY24–FY25 the multiple *expanded*
from 34.5× to 48.0× (+39%) on top of strong EPS growth, as the market extrapolated the solar boom. In FY26
it gave back 28% while EPS fell 7%. Then, from 31-Mar-2026 to 18-Sep-2026, the price fell from ₹520 to ₹390
(−25.0%). On FY26 EPS of ₹15.08 the trailing P/E went from 34.5× to **25.9×**, so the entire fall was
**multiple compression**. That is the market repricing the risk in the receivables and the pledge
(the Q1 FY27 miss is in [03.4](../03-reading-filings/04-quarterly-results-and-concalls.md)). A 34.5× P/E needs
growth *and* credibility to hold, and losing either one costs a quarter of the price even with earnings flat.

## 10. Log returns vs simple returns

The **simple return** is $R = P_1/P_0 - 1$. The **log (continuously compounded) return** is
$\ell = \ln(P_1/P_0) = \ln(1 + R)$. They are close for small moves ($\ell \approx R - R^2/2$) and far apart
for big ones: +50% is $\ell = +0.405$, and −50% is $\ell = -0.693$.

| Property | Simple returns | Log returns |
|:--|:--|:--|
| Add **across time** (multi-period) | No: multiply $(1+R_1)(1+R_2)$ | **Yes**: $\ell_{0\to2} = \ell_1 + \ell_2$ |
| Add **across assets** (portfolio) | **Yes**: $R_p = \sum w_i R_i$ | No |
| Symmetric (up $x$ then down $x$ = flat) | No | Yes |
| Bounded below | −100% | $-\infty$ (so a normal model is at least possible) |

**Examples.** Kaveri's five annual log returns (0.421, 0.118, 0.527, 0.246, −0.405) sum to 0.907, exactly
$\ln(520/210)$. Their mean, 0.181, gives $e^{0.181} - 1 = 19.9\%$, the CAGR. So the mean log return *is* the
geometric growth rate. The other way round: a 50/50 portfolio of a stock up 20% and one down 10% returns
exactly $+5\%$ (simple returns average across assets), while averaging the log returns gives a wrong 3.9%.
**Rule:** use logs to chain returns through time and for statistics. Use simple returns to aggregate a
portfolio at a point in time.

### Why a 50% loss needs a 100% gain

After a loss $L$, you need a gain of $L/(1-L)$ to get back to where you started:

| Loss | 10% | 20% | 25% | 33.3% | 50% | 60% | 75% | 90% |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Gain needed to recover | 11.1% | 25.0% | 33.3% | 50.0% | 100% | 150% | 300% | 900% |

In logs this is obvious: −50% is $\ln 0.5 = -0.693$, and recovering needs $+0.693 = \ln 2$, i.e. +100%.
**Kaveri:** from its ₹812 peak (Jan-2025) to ₹390 is a **52.0%** drawdown. Getting back to ₹812 needs
**+108.2%**. If earnings compounded at 14.1% a year (the revenue growth the market already prices in) and
the multiple held, that recovery would take about 5.6 years. Avoiding large losses matters more than capturing large gains, which
is why [11.4](../11-process/04-position-sizing-and-portfolio-construction.md) treats position size and
downside first.

## 11. Volatility drag: why the average return is not your return

§2 showed Kaveri's arithmetic mean return (25.8%) exceeding its CAGR (19.9%). The general result: if the
arithmetic mean simple return is $A$ and the volatility (standard deviation) of returns is $\sigma$, the
geometric (compound) growth rate $G$ is approximately

$$
G \approx A - \frac{\sigma^2}{2}
$$

**Derivation sketch.** Take logs: $\ln(1+R) \approx R - R^2/2$. Take expectations: $E[\ln(1+R)] \approx
E[R] - \tfrac{1}{2}E[R^2] \approx A - \tfrac{1}{2}(\sigma^2 + A^2)$. For modest $A$ the $A^2$ term is small,
which leaves $A - \sigma^2/2$. If annual *log* returns are normal with mean $\mu$ and s.d. $\sigma$, the
result is exact in log space: $\ln(1 + A) = \mu + \sigma^2/2$, and the compound growth rate is $e^{\mu} - 1$.

**Check on Kaveri:** $A = 25.8\%$, $\sigma = 35.5\%$ (population s.d. of the five returns), so $A - \sigma^2/2 =
25.8\% - 6.3\% = 19.5\%$, against the actual CAGR of 19.9%. The approximation works even on five noisy years.

**The alternating example.** +50% then −50%, repeated: the arithmetic mean is 0%, but each pair multiplies
wealth by $1.5 \times 0.5 = 0.75$. The geometric return is $\sqrt{0.75} - 1 = -13.4\%$ per period. The
approximation gives $0 - 0.5^2/2 = -12.5\%$.

### Worked example 6: two stocks with the same average return

Both stocks have an **arithmetic mean simple return of 12% a year**. Stock A's annual log returns have
volatility 15%, stock B's 45%. Log returns are normal. Over 20 years, starting from ₹1:

| | Stock A (σ = 15%) | Stock B (σ = 45%) |
|:--|--:|--:|
| Mean log return $\mu = \ln 1.12 - \sigma^2/2$ | 10.21% | 1.21% |
| Compound growth $e^{\mu} - 1$ | **10.75%** | **1.22%** |
| **Mean** wealth after 20 yrs, $1.12^{20}$ | 9.65× | 9.65× |
| **Median** wealth after 20 yrs, $e^{20\mu}$ | **7.70×** | **1.27×** |
| Probability of ending below ₹1, $\Phi(-\mu\sqrt{20}/\sigma)$ | 0.1% | 45.2% |

A 200,000-path Monte Carlo reproduces these numbers (median 7.72× and 1.27×; loss probability 0.12% and
45.3%). Both stocks have the same *average* outcome, but B's average is carried by a few enormous winners.
The typical holder of B ends up roughly where they started, and nearly half lose money over 20 years. When a
fund or a backtest reports an "average annual return", find the volatility before you believe it.

!!! tip "Trader's lens: volatility drag is Itô's $-\sigma^2/2$, and you already trade it"
    For a stock following geometric Brownian motion, $dS/S = \mu\,dt + \sigma\,dW$, Itô's lemma gives
    $d\ln S = (\mu - \tfrac{1}{2}\sigma^2)\,dt + \sigma\,dW$. The $-\sigma^2/2$ is exactly the drag above. It is
    the same convexity term that makes a log contract replicate a variance swap, and the reason a daily-rebalanced
    2× leveraged ETF decays in a choppy market (its drag scales with $(2\sigma)^2/2$). For position sizing,
    levering an asset with excess return $\mu$ and volatility $\sigma$ by $f$ gives a growth rate of roughly
    $f\mu - f^2\sigma^2/2$. That is maximised at $f^* = \mu/\sigma^2$ (Kelly), where the growth rate is
    $\mu^2/2\sigma^2$. With $\mu = 6\%$ and $\sigma = 20\%$: $f^* = 1.5$ and growth ≈ 4.5% a year above cash.
    Estimation error in $\mu$ is why practitioners use a fraction of Kelly
    ([11.4](../11-process/04-position-sizing-and-portfolio-construction.md)).

!!! info "India notes"
    - **Numbers and years.** Work in ₹ crore and Indian financial years (FY26 = Apr-2025 to Mar-2026). A
      "5-year CAGR FY21–FY26" has **five** compounding periods, not six. Counting the years in the label
      instead of the gaps between them is a very common error in Indian broker reports.
    - **Quoted rates.** Bank deposit rates are usually nominal annual rates with quarterly compounding.
      Some vehicle, consumer and microfinance loans have been marketed on flat rates. Always convert to an
      effective annual rate. (RBI has tightened loan-pricing disclosure through its Key Facts Statement rules.
      *We did not re-verify the current circular for this lesson; check rbi.org.in.*)
    - **SIP returns.** Indian platforms report SIP returns as XIRR. Lump-sum mutual-fund returns over periods
      longer than a year are normally shown as CAGR. Neither is directly comparable with the other without
      thinking about timing.
    - **Taxes and costs** turn gross returns into what you keep. Equity capital-gains tax, STT and the
      grandfathering history are covered with current, sourced rates in
      [11.5](../11-process/05-monitoring-and-selling.md).

!!! warning "Common mistakes"
    - **Averaging returns instead of compounding them.** Use CAGR/geometric means for multi-period growth.
      The arithmetic mean overstates it by about $\sigma^2/2$.
    - **Counting years wrong in a CAGR.** FY21→FY26 is 5 periods.
    - **Using this year's cash flow in Gordon.** The numerator is next year's, $C_1 = C_0(1+g)$.
    - **Letting $g$ approach $r$.** Value explodes as $r - g \to 0$. A perpetual $g$ above long-run nominal GDP
      growth is a red flag.
    - **Annualising a SIP's absolute return over the whole calendar span.** Money went in gradually. Use XIRR.
    - **Taking IRR at face value.** Check for multiple sign changes, and report MOIC alongside.
    - **Mixing real and nominal.** Discount nominal cash flows at nominal rates.
    - **Calling multiple expansion "growth".** Decompose TSR. If most of the return came from the P/E, it was
      the market's mood, not the business.
    - **Adding log returns across assets or simple returns across time.** Use logs through time and simple
      returns across a portfolio.

## Key terms

| Term | Meaning |
|:--|:--|
| **Compounding** | Earning returns on previous returns: $FV = PV(1+r)^n$ |
| **Effective annual rate (EAR)** | The true annual rate after intra-year compounding: $(1 + r/m)^m - 1$ |
| **CAGR** | Constant annual rate linking a start and end value: $(V_n/V_0)^{1/n} - 1$ |
| **Rule of 72** | Doubling time ≈ 72 ÷ rate (%). Accurate near 8% |
| **Present value / discount factor** | Today's value of a future cash flow; $1/(1+r)^n$ |
| **Discount rate** | The opportunity-cost return used to discount. For a company, typically WACC |
| **NPV** | Sum of discounted cash flows minus the upfront cost |
| **Perpetuity** | A cash flow forever: $PV = C/r$ |
| **Gordon growth model** | Growing perpetuity: $PV = C_1/(r - g)$, valid only for $g < r$ |
| **Annuity / EMI** | A finite level stream: $PV = C[1-(1+r)^{-n}]/r$. An EMI is the annuity payment that repays a loan |
| **Flat rate** | Interest charged on the original principal throughout. Roughly half the true reducing-balance rate |
| **IRR** | The discount rate at which NPV = 0 |
| **XIRR** | IRR for dated, irregular cash flows, using $(d_i - d_0)/365$ year fractions |
| **MOIC** | Multiple on invested capital: total money back ÷ money in |
| **Real vs nominal** | Return in purchasing power vs in rupees: $(1+n) = (1+r)(1+\pi)$ (Fisher) |
| **TSR** | Total shareholder return = price change + dividends ≈ EPS growth + P/E change + dividend yield |
| **Multiple expansion / compression** | Return from a rising / falling P/E, as distinct from earnings growth |
| **Log return** | $\ln(P_1/P_0)$. Additive through time |
| **Drawdown** | Fall from a peak. Recovering from loss $L$ needs a gain of $L/(1-L)$ |
| **Volatility drag** | Gap between arithmetic and geometric mean returns, ≈ $\sigma^2/2$ |

## Check your understanding

1. A bond pays 8% a year compounded semi-annually. An FD pays 7.9% compounded monthly. Which has the higher
   effective annual rate?

    <details markdown="1"><summary>Answer</summary>

    Bond: $(1 + 0.08/2)^2 - 1 = 8.16\%$. FD: $(1 + 0.079/12)^{12} - 1 = 8.19\%$. The **FD** is marginally higher,
    despite the lower quoted rate.

    </details>

2. Kaveri's EPS went from ₹10.43 (FY23) to ₹15.08 (FY26). Compute the EPS CAGR. Using the Rule of 72, how
   long would EPS take to double at that rate?

    <details markdown="1"><summary>Answer</summary>

    Three periods: $(15.08/10.43)^{1/3} - 1 = 13.1\%$. Doubling ≈ $72/13.1 \approx 5.5$ years (exact:
    $\ln 2/\ln 1.131 = 5.6$ years).

    </details>

3. A company will pay a dividend of ₹12 next year. You expect 7% growth forever and require 13%. What is the
   share worth? If the market price is ₹300, what return is the market implying (same growth)?

    <details markdown="1"><summary>Answer</summary>

    $P = 12/(0.13 - 0.07) = ₹200$. Implied return $r = D_1/P + g = 12/300 + 7\% = 4\% + 7\% = 11\%$. The
    market is accepting a lower return than you require (or it expects faster growth).

    </details>

4. You borrow ₹5,00,000 for 24 months at 12% a year on a reducing balance. What is the EMI and the total
   interest? A rival lender offers "6.5% flat" for the same tenure. Which is cheaper?

    <details markdown="1"><summary>Answer</summary>

    $i = 1\%$: EMI $= 5{,}00{,}000 \times 0.01/(1 - 1.01^{-24}) = ₹23{,}537$ (total paid ₹5,64,881; interest
    ≈ ₹64,881). Flat: interest $= 5{,}00{,}000 \times 6.5\% \times 2 = ₹65{,}000$; EMI $= 5{,}65{,}000/24 =
    ₹23{,}542$. The flat loan is **slightly more expensive**. Its reducing-balance equivalent is about 12.0%
    a year nominal (12.7% effective). A "6.5%" headline is really about 12%.

    </details>

5. You invest ₹1,00,000 on 1-Jan-2025 and another ₹1,00,000 on 1-Jan-2026. On 31-Dec-2026 the holding is
   worth ₹2,30,000. What is the absolute return? Is the XIRR above or below 10%? Estimate it.

    <details markdown="1"><summary>Answer</summary>

    Absolute return = 2,30,000/2,00,000 − 1 = **15%**. The first ₹1 lakh was invested for ~2 years and the
    second for ~1 year, so the money-weighted average holding is ~1.5 years. The annualised rate is roughly
    $1.15^{1/1.5} - 1 \approx 9.8\%$. Solving exactly, $1{,}00{,}000(1+r)^{2} + 1{,}00{,}000(1+r) = 2{,}30{,}000$
    gives $r \approx 9.7\%$, so **just below 10%**. (Excel's XIRR, using actual day counts, gives a very similar
    figure.)

    </details>

6. Over three years a stock's EPS rose 60% while its P/E fell from 40× to 30×, and it paid a 1% dividend yield
   each year. What was the total price return? Roughly what was the annual TSR? Where did the return come from?

    <details markdown="1"><summary>Answer</summary>

    Price multiple = $1.60 \times (30/40) = 1.20$, so the price return is **+20%** in total, or $1.2^{1/3} - 1 =
    6.3\%$ a year. Add ≈1% dividend yield: TSR ≈ **7.3% a year**. EPS growth (16.9% a year) was strong, but
    multiple compression (−9.1% a year) took more than half of it. The business did well and the investor
    did mediocrely, because the starting P/E was too high.

    </details>

7. A fund reports an average annual return of 18% with an annual volatility of 40%. Estimate its compound
   annual growth rate. What does that imply for a claim like "18% a year"?

    <details markdown="1"><summary>Answer</summary>

    $G \approx 18\% - 0.40^2/2 = 18\% - 8\% = 10\%$. An investor who stayed in the whole time compounded at
    roughly **10%**, not 18%. The arithmetic average overstates realised growth by the volatility drag. Always
    ask for CAGR (or XIRR), not the average of yearly returns.

    </details>

8. A stock falls 40%, then rises 40%. Where does it end up relative to the start? What gain would it have
   needed after the fall to break even?

    <details markdown="1"><summary>Answer</summary>

    $0.6 \times 1.4 = 0.84$, so it ends **16% below** the start. Break-even needs $0.4/0.6 = 66.7\%$. In logs:
    $\ln 0.6 = -0.511$, $\ln 1.4 = +0.336$, net $-0.174 = \ln 0.84$.

    </details>

## Go deeper

- **Brealey, Myers & Allen, *Principles of Corporate Finance*, chapters 2–3.** The standard treatment of
  present value, perpetuities, annuities and bond maths, with more exercises.
- **Aswath Damodaran, *Investment Valuation* (Wiley), the chapter on time value of money**, and his free
  lecture notes at [pages.stern.nyu.edu/~adamodar](https://pages.stern.nyu.edu/~adamodar/). The bridge from
  these formulas to DCF.
- **John C. Bogle, *The Little Book of Common Sense Investing*.** Bogle splits long-run stock returns into
  dividend yield + earnings growth + "speculative return" (change in P/E), which is the TSR decomposition of
  §9 applied to whole markets.
- **William Poundstone, *Fortune's Formula*.** A readable history of the Kelly criterion, geometric vs
  arithmetic growth and volatility drag, for the trader in you.
- **Microsoft Support, "XIRR function"** ([support.microsoft.com](https://support.microsoft.com/)). The exact
  day-count convention your spreadsheet uses, so your Python and Excel numbers match.

---
[← Previous: 01.4 Indian market plumbing](04-indian-market-structure.md) · [Module index](index.md) · [Next: 02.1 The accounting equation & double entry →](../02-accounting/01-the-accounting-equation.md)
