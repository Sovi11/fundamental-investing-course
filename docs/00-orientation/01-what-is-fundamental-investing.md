# 00.1 · What fundamental investing is — and isn't

> **Why this matters:** Every later module (accounting, ratios, valuation, forensics) is a tool for one question:
> *is this price a good deal for the cash this business will produce over its life?* Without that question the tools
> turn into trivia. This lesson also sets honest expectations. It covers where an edge can come from, why it takes
> years to show up in your results, and what returns are realistic.

**Learning objectives** — after this lesson you can:

- Explain the difference between price and value, and value a simple stream of cash flows as a claim on a business.
- Apply the three questions (*what is the business, is it good, what is it worth compared with the price*) to a real or fictional company.
- Describe seven schools of fundamental investing and the kind of mispricing each one looks for.
- Classify a claimed edge as behavioural, structural, informational or analytical, and state the efficient-markets objection and its best rebuttal.
- Calculate why a fundamental investor's skill takes years to show up statistically, compared with a market-maker's.
- Set realistic return expectations and spot survivorship bias in "multibagger" stories.

**Prerequisites:** none. This is the first lesson. · **Time:** ~100 min

---

## 1. Price is what you pay; value is what you get

Warren Buffett credits Ben Graham with the line *"Price is what you pay; value is what you get"*
([Berkshire Hathaway 2008 letter](https://www.berkshirehathaway.com/letters/2008ltr.pdf)). The whole discipline
rests on the gap between those two words, so we define them carefully.

- **Price**: the last price at which a buyer and a seller agreed to exchange one share. It is set by whoever happens
  to be trading, for whatever reason they have, and it changes every second.
- **Market capitalisation (market cap)**: price × number of shares outstanding. It is what the market charges for the
  whole of the company's equity.
- **Intrinsic value** (or just **value**): the present value of all the cash the business will hand to its owners
  over its remaining life. You cannot observe it. You can only estimate it, and two careful analysts will get
  different answers.
- **Fundamental investing**: buying a security (or selling it short) because your estimate of its intrinsic value
  differs from its price by enough to pay you for the chance that you are wrong. You then hold it until the gap
  closes or your estimate changes.

Look at what that definition leaves out. It says nothing about predicting next month's price, or about charts,
macro calls or momentum. It does not say that low P/E stocks are good. It does not even say "long-term". A
fundamental investor can hold for six weeks if the gap closes in six weeks. Holding is a consequence, not the goal.

### 1.1 What fundamental investing is *not*

| Approach | What it bets on | Typical horizon | How it differs from fundamental investing |
|:--|:--|:--|:--|
| Technical analysis / chart trading | Patterns in past prices and volumes | Days–weeks | Ignores what the business earns; the price series is the whole input |
| Macro trading | Rates, currencies, commodities, policy | Weeks–months | Trades economies, not individual businesses |
| Quant / factor investing | Statistical regularities across thousands of stocks (value, momentum, quality) | Months | Uses many of the same signals, but systematically; rarely judges an individual business |
| Index investing | Nothing: owns the market at low cost | Decades | Accepts the market's price as the best estimate of value |
| Market-making / volatility trading | Spread capture, flow, the difference between implied and realised volatility | Seconds–weeks | Does not need a view on what the business is worth |
| "Tips" and narratives | A story, or someone else's conviction | Unpredictable | No independent estimate of value, and so no way to know when you are wrong |

Graham described the market as a moody business partner, "Mr. Market" (*The Intelligent Investor*, 1949). Every day
he offers to buy your share of the business or sell you his, at a price that depends on his mood. You are free to
ignore him. His offers are useful only when they are foolish. That is the fundamental investor's relationship with
price: **price is information about other people's expectations, not a verdict on value.**

## 2. A share is a claim on future cash flows

A company has two broad kinds of financiers. **Debt holders** (lenders) are promised fixed interest and repayment.
**Equity holders** (shareholders) are the **residual claimants**: they get whatever is left after lenders, suppliers,
employees and the tax authorities have been paid. Lesson [01.1](../01-markets-101/01-what-is-a-company.md) covers
this in detail. For now the key idea is that a share is a claim on a stream of residual cash that runs for years.

The value of any claim on future cash is its **present value (PV)**. You shrink each future rupee by a **discount
rate** $r$, the annual return you require for bearing the risk and waiting:

$$
V_0 \;=\; \sum_{t=1}^{\infty} \frac{CF_t}{(1+r)^t}
$$

In words: value today equals each year's cash flow to owners, $CF_t$, divided by one-plus-the-required-return
compounded $t$ times, summed over the life of the business. If the cash flow starts at $CF_1$ and then grows at a
constant rate $g < r$ for ever, the sum collapses to the **Gordon growth formula**. You will derive it in
[01.5](../01-markets-101/05-time-value-and-returns-math.md):

$$
V_0 \;=\; \frac{CF_1}{r-g}
$$

### Worked example 1 — a toy business, and where its value comes from

A small, debt-free business will produce **₹10 Cr** of cash for its owners next year. That cash will grow at **5%** a
year for ever, and you require **12%** a year.

$$
V_0 = \frac{10}{0.12 - 0.05} = \frac{10}{0.07} = ₹142.9\text{ Cr}
$$

Now ask how much of that ₹142.9 Cr comes from the next few years. Add up the discounted cash flows for the first $N$
years:

| Horizon | PV of cash flows in years 1…N (₹ Cr) | Share of total value |
|:--|--:|--:|
| 1 year | 8.9 | 6.2% |
| 3 years | 25.2 | 17.6% |
| 5 years | 39.4 | 27.6% |
| 10 years | 67.9 | 47.6% |
| 20 years | 103.6 | 72.5% |
| 30 years | 122.3 | 85.6% |

Less than a fifth of the value comes from the next three years, and more than half comes from beyond year ten.
**A share is mostly a claim on the distant future.** That is why a bad quarter often matters less than the market's
reaction suggests. It is also why a lasting change in the long-run outlook matters much more.

Now change the inputs slightly:

| Required return $r$ | Growth $g$ | Value (₹ Cr) | Change vs base |
|:--|:--|--:|--:|
| 12% | 5% | 142.9 | – |
| 12% | 6% | 166.7 | +16.7% |
| 11% | 5% | 166.7 | +16.7% |
| 11% | 6% | 200.0 | +40.0% |
| 13% | 5% | 125.0 | −12.5% |
| 13% | 4% | 111.1 | −22.2% |

A one-point change in either input moves the value by 12–17%. Change both together and the value moves by 22–40%.
Any single "intrinsic value" figure is really the centre of a wide range. Module 06 turns this into sensitivity
tables and scenario analysis ([06.4](../06-valuation/04-dcf-in-practice.md)).

!!! tip "Trader's lens — equity is a long-duration asset with an implied growth rate"
    Differentiate the Gordon value with respect to $r$: $-\frac{1}{V}\frac{\partial V}{\partial r} = \frac{1}{r-g}$.
    The toy business has an **equity duration** of $1/0.07 \approx 14.3$ years. It behaves like a long-dated bond
    with uncertain coupons. The response is convex: +1 pt on $r$ costs 12.5%, −1 pt gains 16.7%.
    Turn the formula round and the market price tells you what growth the market expects: $g = r - CF_1/P$. At a
    price of ₹200 Cr and $r = 12\%$, the market expects $g = 12\% - 5\% = 7\%$. This is the same move as backing
    implied volatility out of an option price. You are not asking "what is it worth?" but "what does this price
    assume, and do I disagree?" Module 06.6 formalises this as the
    [reverse DCF](../06-valuation/06-reverse-dcf-and-expectations.md).

### Worked example 2 — what do you actually get for ₹390 of Kaveri Pumps?

The course's running example is **Kaveri Pumps & Motors Ltd** (fictional), a Coimbatore pump and motor maker. Its
full data is in the [reference page](../appendix/running-example/kaveri-pumps.md). On 18-Sep-2026 its share price
was **₹390**, with **6.00 Cr** shares outstanding.

| Item | Arithmetic | Result |
|:--|:--|--:|
| Market cap | ₹390 × 6.00 Cr shares | ₹2,340 Cr |
| FY26 profit after tax (PAT) | from the income statement | ₹90.5 Cr |
| **Earnings yield** (PAT ÷ market cap) | 90.5 ÷ 2,340 | 3.9% |
| **P/E** (price ÷ earnings) | 2,340 ÷ 90.5 | 25.9x |
| FY26 dividend per share | from the ratio table | ₹4.0 |
| Dividend yield | 4.0 ÷ 390 | 1.0% |
| FY26 **free cash flow (FCF)** = operating cash flow − capex | 65.1 − 48.0 − 4.0 | ₹13.1 Cr |
| FCF yield | 13.1 ÷ 2,340 | 0.6% |

(**PAT** is profit after all costs, interest and tax. **Operating cash flow** is the cash the business actually
collected from operations. **Capex** is capital expenditure on plant, equipment and software. All three are built
from scratch in Module 02.)

Someone paying ₹390 today gets about 1% a year in dividends and a business that produced only 0.6% of its price in
free cash last year. **Almost all of the return has to come from future growth in cash flow.** The course's
reference valuation ([kaveri-valuation](../appendix/running-example/kaveri-valuation.md)) makes this concrete:

- The present value of the forecast cash flows for FY27–FY29 is 102.4 + 96.1 + 93.4 = ₹291.9 Cr, only **13.9%** of
  the ₹2,100 Cr enterprise value. (**Enterprise value** is the value of the whole business before subtracting debt;
  see [01.2](../01-markets-101/02-shares-market-cap-and-enterprise-value.md).)
- The first ten years together are worth ₹947.7 Cr (**45%**). The **terminal value**, everything after FY36, is
  **55%**.
- The base-case value is **₹320 per share**, against a price of ₹390. The probability-weighted value across bull,
  base and bear scenarios is **₹306**. On those numbers the price is 22% above the base case (390 ÷ 320 = 1.22) and
  value sits 18% below price (320 ÷ 390 − 1 = −17.9%).

This does **not** mean "sell Kaveri". It means that at ₹390 the market expects more than the course's base case.
Module 06.6 shows that ₹390 implies about **14.1%** revenue growth a year for ten years, against a base case of 10.8%.
Deciding whether that expectation is too high is the fundamental investor's actual job. (The valuation is dated
31-Mar-2026. Rolling it forward to September at the cost of equity gives about ₹338. We ignore that refinement until
Module 06.)

## 3. The three questions

Every piece of analysis in this course serves one of three questions. Ask them in this order. Most bad investments
come from skipping the first two because the third looked exciting.

**Q1. What is the business?** How does it make money, from whom, and against whom? What is sold (a pump, a loan, a
subscription)? Who pays, how often, and on what credit terms? What does it cost to make one more unit? If you cannot
explain it in three plain sentences, you do not understand it well enough to value it.
→ Taught in [05.1 Business models](../05-business-analysis/01-business-models-and-unit-economics.md) and
[05.2 Industry analysis](../05-business-analysis/02-industry-analysis.md).

**Q2. Is it a good business, run by people you can trust?** "Good" has a precise meaning. The business earns a
**return on invested capital (ROIC)** above its **cost of capital (WACC)** and can keep doing so. ROIC is operating
profit after tax divided by the capital tied up in the business. WACC is the blended return its lenders and
shareholders require. Behind that sit the **moat** (a durable competitive advantage that protects those returns),
the balance sheet, and the honesty and skill of management.
→ Modules 04 (returns, cash conversion), 05 (moats, management, governance) and 09 (forensics).

**Q3. What is it worth, compared with the price, and what does the price already assume?** Estimate a range of
values, understand what the market is implicitly forecasting, and decide whether the gap is big enough.
→ Modules 06–07.

Apply them quickly to Kaveri (we do this properly in [00.3](03-the-research-workflow-map.md)):

1. *Business:* agricultural, domestic and industrial pumps and motors sold through ~1,800 dealers, plus a fast-growing
   solar-pump segment sold to state agencies under a government scheme. Solar was 27% of FY26 revenue, up from 3% in
   FY21.
2. *Good?* Mixed. FY26 ROIC was **12.0%**, almost exactly equal to the reference WACC of **12.19%**. At today's
   returns, growth barely creates value (Lesson [06.1](../06-valuation/01-what-is-value.md) proves why). Receivables
   are ballooning and the promoters have pledged some shares.
3. *Worth vs price?* Base value ₹320 and probability-weighted ₹306, against a price of ₹390. The price implies more
   growth than our base case.

Point 2 leads to one of the most important ideas in the course. **Growth is only worth paying for when the business
earns more on new capital than that capital costs.** A company growing at 20% with ROIC below WACC destroys value
faster the faster it grows.

## 4. The schools of fundamental investing

All fundamental investors compare price with value. The schools differ in *which* mistakes they think the market
makes and *which* businesses they are willing to own.

| School | Core belief | What they buy | Key figures / texts | Typical failure mode |
|:--|:--|:--|:--|:--|
| **Deep value** | The market overreacts to bad news and neglects dull, cheap assets | Stocks below liquidation value, low P/B, low P/E, "net-nets" | Benjamin Graham & David Dodd, *Security Analysis* (1934); Graham, *The Intelligent Investor* (1949) | **Value traps**: cheap because the business is shrinking or badly run |
| **Quality / compounders** | The market underprices how long great businesses can reinvest at high returns | High-ROIC businesses with moats and long reinvestment runways, bought at fair prices | Philip Fisher, *Common Stocks and Uncommon Profits* (1958); Warren Buffett & Charlie Munger | Overpaying, and moats that erode quietly |
| **Growth** | The market underestimates how large a winner can become | Fast-growing revenue and earnings, often at high multiples | Fisher; many modern tech investors | Mistaking growth for value; buying at bubble prices |
| **GARP** (growth at a reasonable price) | You can get growth without paying bubble prices | Growth stocks with P/E not far above their growth rate (**PEG** = P/E ÷ growth ≈ 1) | Peter Lynch, *One Up On Wall Street* (1989) | PEG ignores return on capital, risk and duration |
| **Special situations** | Corporate events create forced or uninterested sellers | Spin-offs and demergers, buybacks, open offers, delistings, mergers, restructurings | Joel Greenblatt, *You Can Be a Stock Market Genius* (1997) | Deals fall apart; small, illiquid positions |
| **Activism** | Value exists but management won't release it | Large stakes, then pushing for change (board seats, payouts, sales, governance) | Many US hedge funds; rarer in India | Expensive, public and slow; control shareholders can block it |
| **Long/short** | You can be right about *relative* value while hedging the market | Long undervalued, short overvalued stocks | Alfred Winslow Jones's partnership, founded in 1949 and usually called the first hedge fund ([Institutional Investor](https://www.institutionalinvestor.com/article/2btfiovsema7r1ake9534/premium/alfred-winslow-jones)) | Shorts have unlimited loss and can squeeze; borrowing costs |

A few notes on each:

**Deep value.** Graham's cleanest test was the **net-net**: a stock trading below its current assets minus *all*
liabilities, so you get the plant, the brand and the future for less than nothing. His **margin of safety** idea is
to buy only when price is far enough below your value estimate that even a large error leaves you whole. That idea
runs through every school, and we restate it as a probability distribution in
[06.8](../06-valuation/08-margin-of-safety-and-expected-value.md). The weakness of deep value is that cheapness is
often deserved. A stock at 0.5x book value earning 4% on that book is not obviously a bargain.

**Quality and compounders.** Fisher added **scuttlebutt**: talking to customers, suppliers, competitors and former
employees to understand a business beyond its accounts ([05.7](../05-business-analysis/07-scuttlebutt-and-primary-research.md)).
Buffett, pushed by Munger, moved from Graham-style bargains towards great businesses. In his 1989 letter he preferred
*"a wonderful company at a fair price"* to a fair company at a wonderful price, and said Munger understood this
long before he did ([Berkshire 1989 letter](https://www.berkshirehathaway.com/letters/1989.html)). The maths in
Worked example 1 explains why. If most of the value lies beyond year ten, the quality and length of the
reinvestment runway dominate everything else.

**Growth and GARP.** Growth investors accept high multiples because they expect earnings to outgrow them. The Cisco
case ([G3](../13-case-studies/global/03-cisco-2000.md)) shows what happens when the price already assumes more than
even a great company can deliver. GARP tries to control this with ratios such as PEG, but those shortcuts break down
once you understand ROIC and duration.

**Special situations.** These are about the *event*, not the business's long-run quality. Index funds sell a
spun-off subsidiary they never wanted. A buyback tender has a calculable acceptance ratio. An open offer or delisting
sets a price floor. Indian versions of these trades are covered in
[12.3](../12-macro-special-sits/03-special-situations.md).

**Activism** is structurally harder in India, where most listed companies have a controlling **promoter** (the
founding family or group, often owning 50–75%). A contested example: in September 2021, Invesco and OFI Global China
Fund, together holding about 17.9% of Zee Entertainment, asked for a shareholder meeting (EGM) to remove the MD & CEO
and reshape the board. The company rejected the request and there was litigation. Invesco withdrew in March 2022
([Business Standard, Sep-2021](https://www.business-standard.com/article/companies/invesco-seeks-egm-to-remove-punit-goenka-from-zee-entertainment-board-121091301555_1.html);
[Business Standard, Mar-2022](https://www.business-standard.com/article/markets/zee-surges-15-as-invesco-withdraws-egm-notice-for-punit-goenka-s-removal-122032400224_1.html)).
In India, "activism" usually means institutions voting against resolutions, often guided by proxy advisers, rather
than takeover fights.

**Long/short.** Jones's idea was to keep the stock-picking skill and remove the market's direction by pairing longs
with shorts. In India, short selling in the cash market must be covered by delivery at settlement; naked shorting is
not allowed. Institutions may not square off shorts within the day. Most practical short exposure comes through
single-stock futures, which exist only for F&O-eligible stocks, or through securities lending and borrowing (SEBI's
[short-selling framework circular of 5-Jan-2024](https://taxguru.in/sebi/sebi-circular-short-selling-framework-indian-securities-market.html);
verify current rules before acting). [11.7](../11-process/07-fundamentals-meets-derivatives.md) goes further.

The schools overlap more than their followers admit. Buffett is a value investor who buys quality. A growth investor
who insists on ROIC above WACC is doing GARP with better tools. The common core is this course: **understand the
business, judge its quality, estimate value, compare with price, size for uncertainty.** Quantitative
**factor investing** is a close cousin. It harvests the average mispricing across thousands of stocks
systematically, where a fundamental investor tries to be right about a few in depth.

## 5. Why would anything be mispriced?

### 5.1 The efficient-markets objection

The **efficient market hypothesis (EMH)**, associated with Eugene Fama (*Journal of Finance*, 1970), says prices
already reflect available information. It comes in three strengths:

- **Weak form**: past prices can't predict future prices (charts don't work).
- **Semi-strong form**: prices reflect all *public* information (reading the annual report doesn't help).
- **Strong form**: prices reflect even private information (nothing helps).

If the semi-strong form held exactly, this course would be pointless. The evidence against active managers is
serious. In S&P's **SPIVA India Year-End 2025** scorecard, **76.3%** of Indian active large-cap equity funds
underperformed their benchmark (S&P India LargeMidCap) over the ten years to December 2025. The figures were **82.9%**
for tax-saving ELSS funds and **79.0%** for mid/small-cap funds. Even in 2025, a good year for mid/small-cap funds,
75.0% of large-cap funds lagged ([SPIVA India Year-End 2025](https://www.spglobal.com/spdji/en/documents/spiva/spiva-india-scorecard-year-end-2025.pdf),
data as of 31-Dec-2025). These are full-time professionals with research teams. Take the number seriously.

### 5.2 The best rebuttal: Grossman–Stiglitz

Sanford Grossman and Joseph Stiglitz ("On the Impossibility of Informationally Efficient Markets", *American Economic
Review* 70(3), 1980; [AEA PDF](https://www.aeaweb.org/aer/top20/70.3.393-408.pdf)) pointed out a paradox. If prices
reflected all information perfectly, nobody would be paid for gathering it. Then nobody would gather it, and prices
could not reflect it. So in equilibrium there must be **just enough mispricing to pay the people who do the work**.
Three things follow:

1. Edge exists, but it is a **competitive business with costs**: time, data, skill and bearing risk. On average,
   active managers earn roughly what it costs them, and after fees most lose to the index.
2. Your edge has to be *specific*. "I'm smart and I read annual reports" is the price of entry, not an edge.
3. Mispricing is most likely where research is costly, unrewarded or constrained: small, dull, complicated, or
   temporarily unpopular companies, and situations where natural holders are forced to sell.

(Robert Shiller's 1981 work showing that stock prices move far more than later dividends justify is the other
classic challenge to strong efficiency. Fama and Shiller shared the 2013 Nobel memorial prize, which neatly captures
where the debate stands.)

### 5.3 The four sources of mispricing

| Source | Mechanism | Example | How you'd know it's real | Where taught |
|:--|:--|:--|:--|:--|
| **Behavioural** | Predictable human errors: extrapolating recent trends, anchoring on past prices, loss aversion, preferring lottery-like stocks, herding | After three bad quarters a cyclical is priced as if the downturn were permanent | You can show the base rate (how often similar companies recovered) differs from what the price implies | [11.6](../11-process/06-behavioural-finance-and-decision-journals.md), [12.2](../12-macro-special-sits/02-market-cycles-and-sentiment.md) |
| **Structural / time-horizon** | Rules, mandates or incentives *force* other investors to buy or sell regardless of value; many are judged quarterly | Index deletions, fund-category limits, margin calls on pledged promoter shares, career risk | You can name the constrained seller and explain why they can't wait | [01.4](../01-markets-101/04-indian-market-structure.md), [12.3](../12-macro-special-sits/03-special-situations.md) |
| **Informational** | Public but costly information that few people process: dense notes to accounts, regional data, primary research | A receivables-ageing note in a small cap that no analyst covers | You can point to the specific document and show the price hasn't reacted | [03.3](../03-reading-filings/03-notes-to-accounts.md), [05.7](../05-business-analysis/07-scuttlebutt-and-primary-research.md) |
| **Analytical** | Same facts, better interpretation: seeing the economics behind the accounting | Recognising that heavy spending on customer acquisition is investment, not cost; or that profit growth funded by rising receivables isn't turning into cash | You can explain the market's current model and exactly where yours differs | Modules 04, 06, 09 |

Two warnings. First, **structural edges are the most reliable** because they don't depend on your being cleverer
than anyone. Keynes observed that it is *"better for reputation to fail conventionally than to succeed
unconventionally"* (*The General Theory*, 1936, ch. 12), and fund managers still behave that way. A fund manager
who must beat the index every quarter cannot hold a stock that will look bad for two years. You can. In India,
fund-category rules (a large-cap fund must keep at least 80% in large caps, the top 100 companies by market cap;
see SEBI's [categorisation circular of 26-Feb-2026](https://www.sebi.gov.in/legal/circulars/feb-2026/categorization-and-rationalization-of-mutual-fund-schemes_99983.html))
and promoter-pledge margin calls both create sellers who are not asking what the business is worth.

Second, an "informational edge" must never mean **unpublished price-sensitive information (UPSI)**. Trading on
material non-public information is insider trading under SEBI's rules. If your edge is a phone call from someone at
the company, you do not have an edge; you have a legal problem ([05.7](../05-business-analysis/07-scuttlebutt-and-primary-research.md)).

!!! tip "Trader's lens — whose constraint are you harvesting?"
    A market-maker already understands structural edge: you are paid for providing liquidity to people who need it
    and for absorbing flow that is not price-sensitive. SEBI's own data shows the scale in Indian derivatives. Over
    FY22–FY24, 93% of more than 1 crore individual F&O traders lost money, with aggregate losses above ₹1.8 lakh
    crore. In FY24 alone, proprietary traders and FPIs booked gross trading profits of about ₹33,000 Cr and
    ₹28,000 Cr respectively ([SEBI press release, 23-Sep-2024](https://www.sebi.gov.in/media-and-notifications/press-releases/sep-2024/updated-sebi-study-reveals-93-of-individual-traders-incurred-losses-in-equity-fando-between-fy22-and-fy24-aggregate-losses-exceed-1-8-lakh-crores-over-three-years_86906.html)).
    The fundamental version of the same question is: *who is on the other side of my trade, and why are they
    willing to sell to me at this price?* If the answer is "someone who knows more", walk away. If it is "a fund
    that must sell because of a rule", "a promoter facing a margin call", or "people extrapolating a bad quarter",
    you may have something.

**The edge test.** Before any position, write down one sentence for each of these:

1. What does the price imply? (the market's model)
2. What do I believe instead, and why? (my model)
3. Why does the market believe what it does, and why is it wrong? (the source of the mispricing, from the table above)
4. What will make the price move towards my value, and roughly when? (the **catalyst**)
5. What would prove me wrong? (the **thesis-breaker**)

If you cannot fill in line 3, you probably don't have an edge. You have an opinion.

## 6. Your edge as a trader vs your edge as a fundamental investor

If you come from market-making or volatility trading, you already know what a real edge feels like: small, measured,
repeated thousands of times, with the P&L confirming it within days. Fundamental investing's edge is statistically
different in almost every way, and ignoring that difference is the most common failure of smart traders who move to
long-horizon investing.

| Dimension | Market-maker / vol trader | Fundamental investor |
|:--|:--|:--|
| Horizon of each bet | Seconds to weeks | 1–5 years |
| Independent bets per year | Thousands to millions | 5–20 new theses, and they are correlated (same market, often same factors) |
| Edge per bet vs noise per bet | Tiny edge, tiny noise; the law of large numbers works for you | Large hoped-for edge (20–50% mispricing) against huge noise (a single stock often moves 30–50% a year) |
| Feedback loop | Same-day P&L; realised vs theoretical edge measured continuously | Years; in the first 1–3 years price noise usually swamps the signal |
| Shape of outcomes | Aggregated P&L close to normal | Positively skewed: a few big winners, many mediocre outcomes, some near-zeros |
| How you know you were right | P&L attribution (spread, vega, gamma, theta), realised vs expected edge | Did the business do what you predicted (revenue, margins, cash, returns)? The price confirms late and noisily |
| Main risk | Inventory, jumps, model error, tail events | Permanent loss of capital: wrong business judgement, fraud, too much debt, overpaying |
| Capacity limit | Available flow | Liquidity, especially in small caps |

### Worked example 3 — how long before skill shows up in the data?

Measure skill with the **information ratio**, $IR = \alpha / TE$. Here **alpha** ($\alpha$) is your average annual
return above the benchmark, and **tracking error** ($TE$) is the annual standard deviation of that excess return.
After $T$ years your estimated alpha has a standard error of $TE/\sqrt{T}$, so the t-statistic is
$t = IR\sqrt{T}$. For $t = 2$ (roughly "95% confident it isn't luck") you need:

$$
T = \left(\frac{2}{IR}\right)^2
$$

**A very good fundamental investor**: $\alpha = 3\%$ a year after costs, $TE = 8\%$ (a concentrated portfolio).

$$
IR = \frac{0.03}{0.08} = 0.375 \quad\Rightarrow\quad T = \left(\frac{2}{0.375}\right)^2 = 28.4 \text{ years}
$$

Even an excellent investor needs about **28 years** of results to prove skill at conventional significance. With
$\alpha = 5\%$ and $TE = 10\%$ ($IR = 0.5$) it still takes 16 years.

The same investor will **underperform** in any given year with probability
$\Phi(-IR\sqrt{T})$, where $\Phi$ is the standard normal cumulative distribution:

| Window | P(underperform the index) with $IR = 0.375$ |
|:--|--:|
| 1 year | 35.4% |
| 3 years | 25.8% |
| 5 years | 20.1% |
| 10 years | 11.8% |

A genuinely skilled investor trails the index about one year in three, and one five-year stretch in five.

**A market-maker**: expected P&L of ₹1 lakh a day with a daily standard deviation of ₹2 lakh gives a daily IR of 0.5.
Then $T = (2/0.5)^2 = 16$ **trading days**, and the annualised Sharpe ratio is $0.5 \times \sqrt{252} \approx 7.9$.

The contrast is the whole point. **In fundamental investing, results are an extremely noisy measure of skill.** Three
practical consequences run through the course:

1. **Judge the process, not the outcome.** Keep a decision journal that records *why* you acted and what you
   expected, before you know the result ([11.6](../11-process/06-behavioural-finance-and-decision-journals.md)).
2. **Shorten the feedback loop with intermediate predictions.** "Kaveri's receivable days will fall towards 80 by
   March 2027" can be checked in months. "Kaveri is worth ₹320" may never be checked cleanly. Good theses are built
   from falsifiable business predictions ([11.3](../11-process/03-writing-an-investment-memo.md)).
3. **Size for being wrong.** When you can't tell skill from luck quickly, overconfidence is expensive. Position
   sizing ([11.4](../11-process/04-position-sizing-and-portfolio-construction.md)) uses fractional Kelly for exactly
   this reason.

What *does* carry over from trading: thinking in probabilities and expected value, treating price as an implied
forecast, respecting sizing and ruin, and emotional discipline around P&L. What doesn't: treating mark-to-market as
truth, the urge to act every day, and hedging away the very risk you are paid to take.

## 7. What returns are realistic?

Some anchors, each with its date:

| Benchmark | Figure | As of / source |
|:--|--:|:--|
| Nifty 50 **Total Return Index** (dividends reinvested), annualised since 3-Nov-1995 | 12.38% | 31-Aug-2026, [NSE Indices factsheet](https://www.niftyindices.com/Factsheet/ind_nifty50.pdf) |
| Nifty 50 price index, same period | 10.86% | same |
| Nifty 50 TRI, last 5 years (annualised) | 8.32% | same |
| Nifty 50 annualised volatility since inception | 22.4% | same |
| India 10-year government bond yield | ≈7.05% | 21-Sep-2026, [Trading Economics](https://tradingeconomics.com/india/government-bond-yield) |
| CPI inflation, August 2026 | 4.82% | [Trading Economics](https://tradingeconomics.com/india/inflation-cpi) (MoSPI data, released 14-Sep-2026) |
| RBI inflation target | 4% ± 2%, retained to March 2031 | [Business Standard, Mar-2026](https://www.business-standard.com/economy/news/cpi-alignment-and-flexibility-back-4-inflation-target-retention-126032601028_1.html) |
| Indian large-cap active funds lagging the benchmark over 10 years | 76.3% | [SPIVA India YE2025](https://www.spglobal.com/spdji/en/documents/spiva/spiva-india-scorecard-year-end-2025.pdf) |
| Berkshire Hathaway per-share market value vs S&P 500 (with dividends), 1965–2025 | 19.7% vs 10.5% a year | [Berkshire 2025 letter](https://www.berkshirehathaway.com/letters/2025ltr.pdf) (Feb-2026) |

The **Total Return Index (TRI)** assumes dividends are reinvested. It is the fair comparison for anyone's
performance, and the gap to the price index (about 1.5 points a year here) is the dividend yield. Note that the
5-year figure (8.32%) is well below the 30-year figure (12.38%). Returns come in lumps, and a five-year window tells
you little.

Berkshire's 9-point annual margin over 61 years is the best-known long record in public markets. Treat it as the
right tail of the distribution, not a target.

### Worked example 4 — what realistic numbers compound to

Invest ₹10 lakh for 20 years. *These are illustrations of compounding, not forecasts.*

| Scenario | Annual return | Growth multiple (20 yrs) | Ending value |
|:--|--:|--:|--:|
| Index at its since-inception rate | 12.38% | 1.1238²⁰ = 10.32x | ₹1.03 Cr |
| Same, less 1.5% a year of costs (fees, brokerage, impact) | 10.88% | 7.89x | ₹78.9 lakh |
| Index + 3% a year of genuine alpha | 15.38% | 17.48x | ₹1.75 Cr |

Three points of alpha kept for 20 years is **1.7x** the index outcome (17.48 ÷ 10.32). Leaking 1.5% a year in costs
takes away almost a quarter of it (7.89 ÷ 10.32 = 0.76). Anyone who can reliably add 2–4% a year over a decade
**after costs** is very good. Promises of 30–40% a year, sustained, should make you ask what risk is hidden or how
short the sample is.

**Taxes are part of the return.** As of FY27, listed Indian equity gains held more than 12 months are
**long-term capital gains (LTCG)**, taxed at 12.5% above an annual exemption of ₹1.25 lakh. Shorter holdings are
**short-term (STCG)** at 20%. These rates took effect on 23-Jul-2024 and Budget 2026 kept them. The Income-tax Act,
2025 replaced the 1961 Act from 1-Apr-2026 without changing them
([Business Standard on the 2024 change](https://www.business-standard.com/markets/news/budget-2024-hikes-ltcg-tax-rate-to-12-5-stcg-to-20-stt-on-f-o-also-up-124072300553_1.html);
[PIB on the new Act](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2248005); detailed treatment and current
rules in [11.5](../11-process/05-monitoring-and-selling.md)). Take a 13% pre-tax return for 20 years, ignoring the
exemption, surcharge and cess:

| Behaviour | Arithmetic | Multiple | Post-tax CAGR |
|:--|:--|--:|--:|
| No tax (reference) | 1.13²⁰ | 11.52x | 13.0% |
| Buy and hold; pay LTCG once at the end | 1 + (11.52 − 1) × (1 − 0.125) | 10.21x | 12.3% |
| Realise gains every year as LTCG | (1 + 0.13 × 0.875)²⁰ | ≈8.6x | 11.4% |
| Churn: realise every year as STCG | (1 + 0.13 × 0.80)²⁰ | 7.23x | 10.4% |

Deferring tax by holding is worth almost two points a year over churning. That is a **structural edge available to
every patient individual**, and it is invisible in pre-tax performance tables.

## 8. Survivorship bias and the multibagger myth

**Survivorship bias** is the error of drawing conclusions from a sample that includes only the survivors. In
investing it shows up everywhere:

- Articles on "stocks that turned ₹1 lakh into ₹1 crore" (a **multibagger** is a stock that multiplies many times;
  a "10-bagger" rises 10x). Nobody writes about the thousand stocks from the same starting year that went nowhere or
  were delisted.
- Fund advertisements that show the best schemes. SPIVA's year-end 2025 report found that only 79.4% of the 97 Indian
  large-cap funds in existence ten years earlier still existed. Across all categories, 27% of funds had merged or
  been liquidated over the decade. The dead funds' records disappear from the brochures.
- Back-tests on *today's* index members. The Nifty 50 is rebalanced semi-annually. Today's members are, almost by
  definition, companies that did well, so testing them over the past 20 years is biased. (Investing in the index
  itself is not biased. It really did hold the losers until it dropped them.)
- Data sets that quietly exclude delisted and suspended companies.

### What the evidence says

Hendrik Bessembinder's study of all US stocks from 1926 to 2016 found that **most individual stocks had lifetime
buy-and-hold returns below one-month Treasury bills**. The best-performing **4%** of companies accounted for the
entire net wealth created by the US stock market ("Do Stocks Outperform Treasury Bills?", *Journal of Financial
Economics* 129(3), 2018; [RePEc abstract](https://ideas.repec.org/a/eee/jfinec/v129y2018i3p440-457.html)). The cause
is **positive skewness**. A stock can lose at most 100% but can gain 10,000%, and compounding stretches the right
tail further.

A follow-up covering more than 64,000 stocks worldwide over January 1990 to December 2020 found the same pattern
(Bessembinder, Chen, Choi & Wei, "Long-Term Shareholder Returns: Evidence from 64,000 Global Stocks", *Financial
Analysts Journal*, 2023; [SSRN 3710251](https://ssrn.com/abstract=3710251)). 55.2% of US stocks and 57.4% of non-US
stocks underperformed one-month US T-bills, and the top 2.4% of firms accounted for all US$75.7 trillion of net
wealth creation. The **India** rows (3,967 stocks, returns measured in US dollars) are even more extreme:

| India, Jan-1990 to Dec-2020 (lifetime buy-and-hold, USD) | Value |
|:--|--:|
| Mean return per stock | +501% |
| **Median** return per stock | **−33.6%** |
| Share of stocks beating one-month US T-bills | 36.3% |
| Share of stocks beating the value-weighted Indian market | 24.2% |
| Share of gross wealth creation from the top 1% of firms (40 firms) | 65.5% |
| Share of gross wealth creation from the top 5% of firms (199 firms) | 92.1% |

The *average* Indian stock multiplied about 6x, while the *typical* (median) stock lost a third of its value in dollar
terms. Both statements are true at once.

### Worked example 5 — why the median stock loses while the average stock wins

Model each stock's value as a **lognormal** random walk: log returns are normally distributed. Assume an expected
(mean) return of $m = 12\%$ a year, volatility $\sigma = 50\%$ (typical of an Indian small cap), and a 15-year
horizon. If $\ln W_T \sim N(\mu T, \sigma^2 T)$ with $\mu = \ln(1+m) - \sigma^2/2$, then the mean terminal wealth is
$(1+m)^T$ and the median is $e^{\mu T}$:

- $\mu = \ln 1.12 - 0.5^2/2 = 0.1133 - 0.1250 = -0.0117$ a year, so $\mu T = -0.1751$
- $\sigma\sqrt{T} = 0.5 \times \sqrt{15} = 1.9365$

| Quantity | Formula | Result |
|:--|:--|--:|
| Mean multiple | $1.12^{15}$ | 5.47x |
| Median multiple | $e^{-0.1751}$ | 0.84x |
| P(lose money) = P($W<1$) | $\Phi(0.1751/1.9365)$ | 53.6% |
| P(do worse than the average stock) | $\Phi\big((\ln 5.474 + 0.1751)/1.9365\big)$ | 83.4% |
| P(10-bagger) = P($W>10$) | $1-\Phi\big((\ln 10 + 0.1751)/1.9365\big)$ | 10.0% |
| P(100-bagger) = P($W>100$) | $1-\Phi\big((\ln 100 + 0.1751)/1.9365\big)$ | 0.68% |

Simulate 1,000 such stocks (Python, seed 42) and you get: **545 lose money**, 105 are 10-baggers and **4 are
100-baggers**. The top 10 stocks produce **47.9%** of all the gains, and the top 40 produce 70.0%. The sample mean is
6.66x against a theoretical 5.47x. With a tail this heavy, even 1,000 draws give a noisy average.

```python
import math, random
random.seed(42)
m, sig, T = 0.12, 0.50, 15
mu = (math.log(1 + m) - sig**2 / 2) * T
s = sig * math.sqrt(T)
W = sorted((math.exp(random.gauss(mu, s)) for _ in range(1000)), reverse=True)
gains = [w - 1 for w in W]
gross = sum(g for g in gains if g > 0)
print(sum(w < 1 for w in W), sum(w > 10 for w in W), sum(w > 100 for w in W))   # 545 105 4
print(round(sum(gains[:10]) / gross * 100, 1))                                    # 47.9
```

Now imagine a magazine in year 15 profiling the four 100-baggers: "Their founders were visionary; their moats were
obvious in hindsight." Every sentence can be true, and the article still teaches you almost nothing. You would also
need to know how many companies looked just as visionary in year 0 and how many of them ended among the 545 losers.
That number is the **base rate**, and ignoring it is the core of survivorship bias.

Implications for the rest of the course:

1. **Study failures as carefully as successes.** That is why Module 13 has Satyam, IL&FS/DHFL, Yes Bank, Enron and
   Wirecard alongside Asian Paints and Bajaj Finance.
2. **Stock-picking is hard *mathematically*, not only psychologically.** A randomly chosen stock is more likely than
   not to lag the index. Owning the index gives you the right tail automatically. Picking stocks is only worth it if
   you can identify it better than chance, or avoid the left tail better than chance.
3. **Concentration raises the variance of outcomes a lot.** With a skewed distribution, a 5-stock portfolio usually
   lags and occasionally wins big. Sizing ([11.4](../11-process/04-position-sizing-and-portfolio-construction.md))
   is where this is dealt with.
4. **The downside matters as much as the upside.** Avoiding the permanent losers (fraud, over-borrowing, broken
   business models) is a large part of the edge. That is why forensics has its own module.

!!! info "India notes"
    - **Promoter control is the norm.** Most listed Indian companies have a controlling promoter, so minority
      shareholders depend on governance more than on the market for corporate control. Governance analysis
      ([05.6](../05-business-analysis/06-corporate-governance-india.md)) carries more weight here than in US-style
      markets, and activism is rarer.
    - **Index concentration.** On 31-Aug-2026, financial services were 36.5% of the Nifty 50 and HDFC Bank and ICICI
      Bank alone about 19% ([NSE Indices factsheet](https://www.niftyindices.com/Factsheet/ind_nifty50.pdf)). "Beating
      the Nifty" is partly a bet on or against Indian banks.
    - **Short selling** is legal for all investor classes, but naked shorts are prohibited and institutions cannot
      day-trade. Practical shorting for most investors means single-stock futures on F&O-eligible names
      ([SEBI circular of 5-Jan-2024](https://taxguru.in/sebi/sebi-circular-short-selling-framework-indian-securities-market.html)).
      Long/short is therefore harder to run in Indian small caps.
    - **Structural flows** from SEBI's market-cap-based fund categories, index inclusions and exclusions, and steady
      SIP inflows are real and recurring sources of forced buying and selling (see [01.4](../01-markets-101/04-indian-market-structure.md)).
    - **Tax rewards patience**: LTCG at 12.5% after 12 months against STCG at 20% (FY27; verify current rules in
      [11.5](../11-process/05-monitoring-and-selling.md)).

!!! warning "Common mistakes"
    - **Confusing a great company with a great investment.** Quality is question 2; price is question 3. A great
      business at a price that assumes perfection is a poor investment (see the Cisco case, [G3](../13-case-studies/global/03-cisco-2000.md)).
    - **Treating a low P/E as "cheap".** A low multiple is the market's forecast of low or risky future cash flows.
      Your job is to show that forecast is wrong, not to notice that the number is small.
    - **Using price moves to validate or reject a thesis within months.** With an IR of 0.4, a year of
      underperformance is close to a coin toss. Watch the business KPIs instead.
    - **Learning from survivors only**: studying 100-baggers without studying the companies that looked the same and
      failed.
    - **Mistaking information for edge.** If everyone has read it, it is in the price. If almost no one legally could
      have it, it may be UPSI, and trading on it is illegal.
    - **Bringing a trader's clock to an investor's game**: over-trading, reacting to daily P&L, and hedging away the
      exposure you are paid to hold.
    - **Ignoring costs and taxes**, which compound as surely as returns.

## Key terms

| Term | Meaning |
|:--|:--|
| **Price** | The last traded price of a share; set by whoever is trading, for any reason |
| **Market capitalisation** | Share price × shares outstanding; the market price of the company's equity |
| **Intrinsic value** | The present value of all future cash the business will distribute to its owners; an estimate, never observed |
| **Present value (PV)** | A future amount shrunk by the required return for each year of waiting: $CF_t/(1+r)^t$ |
| **Discount rate / required return** | The annual return an investor demands for the risk and the wait; turns future cash into present value |
| **Gordon growth formula** | Value of a cash flow growing at $g$ for ever, discounted at $r$: $CF_1/(r-g)$, valid only if $g<r$ |
| **Residual claimant** | Equity holders: paid last, after lenders, suppliers, employees and taxes, but own all the upside |
| **Free cash flow (FCF)** | Cash from operations minus capital expenditure; cash the business could distribute without shrinking |
| **P/E and earnings yield** | Price ÷ earnings per share; its inverse (earnings ÷ price) is the earnings yield |
| **ROIC / WACC** | Return on invested capital (after-tax operating profit ÷ capital employed in the business) / weighted average cost of capital (the blended return lenders and shareholders require). Growth creates value only if ROIC > WACC |
| **Moat** | A durable competitive advantage that protects returns on capital from competition |
| **Margin of safety** | The gap between estimated value and price, big enough to absorb estimation errors |
| **Net-net** | Graham's test: a stock priced below current assets minus all liabilities |
| **Value trap** | A stock that looks cheap on multiples but stays cheap or falls because the business is deteriorating |
| **GARP / PEG** | Growth at a reasonable price; PEG = P/E ÷ expected earnings growth (in %) |
| **Special situation** | An investment driven by a corporate event (demerger, buyback, open offer, delisting, merger) |
| **Promoter** | India: the founder/controlling shareholder group of a listed company |
| **Efficient market hypothesis (EMH)** | The claim that prices reflect available information (weak, semi-strong, strong forms) |
| **Grossman–Stiglitz paradox** | Perfectly efficient prices are impossible, because nobody would then be paid to gather information |
| **UPSI** | Unpublished price-sensitive information; trading on it is insider trading under SEBI rules |
| **Catalyst / thesis-breaker** | The event expected to close the gap between price and value / the evidence that would prove the thesis wrong |
| **Alpha / tracking error / information ratio** | Excess return over the benchmark / its standard deviation / their ratio, the standard measure of active skill |
| **Total Return Index (TRI)** | An index version that assumes dividends are reinvested; the fair benchmark for performance |
| **LTCG / STCG** | Long-/short-term capital gains; for listed Indian equity, the long-term threshold is 12 months |
| **Survivorship bias** | Drawing conclusions from survivors only, ignoring the failures that dropped out of the sample |
| **Multibagger** | A stock that rises many-fold (a "10-bagger" rises 10x) |
| **Positive skewness** | A distribution with a long right tail; for stocks, the mean is far above the median |
| **Base rate** | How often an outcome happens in the relevant reference class; the starting point before case-specific evidence |

## Check your understanding

1. A business will generate ₹20 Cr of owner cash next year, growing 6% a year for ever. You require 13%. (a) What is
   it worth? (b) The market values it at ₹400 Cr. What growth rate is the market implying at your 13% required return?
<details><summary>Answer</summary>

(a) $V = 20/(0.13 - 0.06) = 20/0.07 = ₹285.7$ Cr.
(b) Rearranging $P = CF_1/(r-g)$: $g = r - CF_1/P = 13\% - 20/400 = 13\% - 5\% = 8\%$. The market expects 8% growth
for ever. You disagree only if you can explain why growth will be closer to 6%, which is the price-implied-expectation
thinking of the Trader's lens.
</details>

2. Classify each proposed edge as behavioural, structural, informational, analytical, or *not an edge*:
   (a) a small cap is being removed from a major index and passive funds must sell on the effective date;
   (b) in the notes to accounts you notice receivables grew 33% a year for three years while revenue grew 15%;
   (c) a friend in the company's finance team tells you the quarter was terrible, before results are published;
   (d) after three weak quarters, a cement stock trades as if today's depressed prices will last for ever.
<details><summary>Answer</summary>

(a) **Structural**: forced, price-insensitive sellers. (b) **Informational/analytical**: public but little-read
data, plus the interpretation that growth is not turning into cash (exactly Kaveri's FY23–FY26 pattern:
receivables compounding at about 33% a year against revenue at 14.7%). (c) **Not an edge.** It is UPSI, and trading
on it is illegal insider trading. (d) **Behavioural**: extrapolation of a cyclical trough. The test is whether the
base rate of cyclical recovery differs from what the price implies.
</details>

3. A manager's alpha is 4% a year with a tracking error of 10%. (a) How many years of data are needed for a t-stat of
   2? (b) What is the probability she underperforms the index in a given year, assuming normal excess returns?
<details><summary>Answer</summary>

$IR = 0.04/0.10 = 0.4$. (a) $T = (2/0.4)^2 = 25$ years. (b) $\Phi(-0.4) = 34.5\%$. So about one year in three, even
though she is genuinely skilled. That is why process, not short-run results, is the right thing to judge.
</details>

4. In the lognormal model of Worked example 5, the *average* stock grows 5.5x over 15 years, yet more than half the
   stocks lose money. Explain in two sentences why both are true, and what it implies for a 5-stock portfolio.
<details><summary>Answer</summary>

Compound returns are positively skewed. A few stocks multiply 50–300x and drag the mean far above the median, while
the typical stock's compounded result is pulled down by volatility (the $-\sigma^2/2$ term makes the median log
return negative here). A 5-stock portfolio will *usually* miss the rare big winners and lag the average, though
occasionally it catches one and wins big. Concentration raises the variance of outcomes and needs genuine skill to
justify it.
</details>

5. Kaveri's FY26 ROIC was 12.0% and the reference WACC is 12.19%. A friend says: "Management guides 15–18% growth,
   so the stock deserves a high multiple." What is wrong with the argument?
<details><summary>Answer</summary>

Growth creates value only when the return on new capital exceeds the cost of capital. At ROIC ≈ WACC, each rupee
reinvested to grow earns about what it costs, so faster growth adds almost no value. Kaveri's growth also consumes
working capital (receivables), which pushes returns on *incremental* capital lower still. The multiple should depend
on growth *and* ROIC together, which Lesson 06.1 formalises.
</details>

6. A fund's marketing says: "Our five best picks since 2016 compounded at 40% a year." List at least three biases or
   missing facts.
<details><summary>Answer</summary>

(i) **Survivorship/selection**: five best out of how many? What did the whole portfolio return? (ii) No benchmark:
40% against what TRI over the same period? (iii) Position sizes: were these large positions or 0.5% holdings?
(iv) Start and end dates chosen after the fact. (v) Funds that were merged or closed are left out; SPIVA found 27%
of Indian funds across categories did not survive the decade to 2025. (vi) Risk: what drawdowns came with the
return?
</details>

7. Which school would be most interested in each: (a) a company trading below the cash on its balance sheet, net of
   all liabilities; (b) a consumer brand with 40% ROCE and a long runway, at a fair multiple; (c) a conglomerate
   announcing the demerger of a subsidiary that index funds won't want; (d) a promoter-controlled company paying
   large royalties to a promoter entity, where institutions own 25%?
<details><summary>Answer</summary>

(a) **Deep value** (a net-net or near net-net). (b) **Quality/compounders**. (c) **Special situations** (demerger,
forced selling of the spun-off entity). (d) **Activism / governance engagement**: realistically in India, voting
against related-party resolutions and engaging through proxy advisers rather than a control fight.
</details>

8. Suppose you earn 15% a year pre-tax for 15 years. Compare buy-and-hold (pay 12.5% LTCG once at the end) with
   churning every year at 20% STCG. Ignore the exemption, surcharge and cess.
<details><summary>Answer</summary>

Pre-tax multiple $1.15^{15} = 8.14$x. Buy-and-hold: $1 + (8.14 - 1)(1 - 0.125) = 7.24$x. Churn:
$(1 + 0.15 \times 0.80)^{15} = 1.12^{15} = 5.47$x. Holding ends about 32% richer (7.24 ÷ 5.47 = 1.32) with identical
stock-picking. That is a structural edge from patience alone.
</details>

## Go deeper

- Benjamin Graham, *The Intelligent Investor* (revised edition with Jason Zweig's commentary, 2003). The chapters on
  "Mr. Market" and "margin of safety" are the philosophical base of this course.
- Warren Buffett's shareholder letters ([berkshirehathaway.com/letters](https://www.berkshirehathaway.com/letters/letters.html)),
  especially 1989 ("Mistakes of the First Twenty-five Years") on moving from cheap to wonderful businesses.
- Michael Mauboussin, *The Success Equation* (2012). Separating skill from luck, and why sample size matters so much
  in investing.
- Bessembinder, Chen, Choi & Wei, "Long-Term Shareholder Returns: Evidence from 64,000 Global Stocks", *Financial
  Analysts Journal* (2023), [SSRN 3710251](https://ssrn.com/abstract=3710251). Read the country tables, including
  India.
- Grossman & Stiglitz (1980), "On the Impossibility of Informationally Efficient Markets" ([AEA](https://www.aeaweb.org/aer/top20/70.3.393-408.pdf)).
  A short paper that explains why an edge must exist and why it must be costly.
- S&P Dow Jones Indices, [SPIVA India scorecards](https://www.spglobal.com/spdji/en/spiva/article/spiva-india), published
  twice a year. The standing evidence on how hard beating the index is.

---
[← Previous: Syllabus](../syllabus.md) · [Module index](index.md) · [Next: How to use this course →](02-how-to-use-this-course.md)
