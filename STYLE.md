# Authoring & style guide

Every page in this course follows these rules. They exist so that ~150 pages written at different times read like
one coherent course.

## 1. Who we are writing for

A sharp, numerate reader (think: an engineer or a derivatives trader) who has **never studied accounting or company
analysis**. They are comfortable with algebra, probability, Python and markets, and they get bored by fluff. They do
not know what "CWIP", "deferred tax" or "ROCE" mean until we tell them.

Consequences:

- **Define every term the first time it appears in a lesson** (bold it, define it in one line; the glossary has the
  long version). Never assume a term from a later module.
- Go **deep, not wide**: prefer one fully worked example over five hand-waved ones. Show the arithmetic.
- Use maths freely (LaTeX `$...$` inline, `$$...$$` display) but always say in words what the formula means.
- Build intuition first, then rules, then edge cases, then practice.
- Where it genuinely helps, add a **Trader's lens** callout drawing an analogy to options/markets (implied vs realised,
  convexity, carry, duration, gamma, skew, Kelly). Don't force it — one or two per lesson at most.

## 2. Market focus and currency of facts

- **India first**: ₹, crore/lakh (1 crore = 10 million; write "₹1,318 Cr"), Indian financial years (FY26 = Apr-2025
  to Mar-2026), Ind AS, Schedule III, SEBI/RBI/NSE/BSE, Screener.in. Add **global comparisons** (US GAAP, 10-K) where
  they help.
- The course is dated **September 2026**. Any regulation, tax rate, threshold or market fact that can change
  (tax rates, SEBI/RBI rules, index rules, lot sizes, ECL transition for banks, etc.) must be **verified with a web search**
  and stated with an "as of" date and a source link. If you cannot verify something, say so explicitly ("verify the
  current rule at …") rather than guessing.
- Facts about real companies (numbers, dates, events) must be verified and **sourced** (annual report, exchange filing,
  regulator order, reputable press). Round and mark approximate figures with "≈". Never invent a real company's number.
- Present allegations as allegations and regulatory findings as findings, with dates. Be fair and factual about living
  people and existing companies.

## 3. Running examples (mandatory consistency)

- Use the fictional **Kaveri Pumps & Motors Ltd** (`docs/appendix/running-example/kaveri-pumps.md`) and **Nirmal Finance
  Ltd** (`nirmal-finance.md`) whenever a lesson needs a worked example of a company's numbers. **Use their numbers
  exactly** — do not invent new historical figures for them. You may add *new* fictional details (e.g., a concall quote)
  only if they do not contradict the reference pages, and label them as fictional.
- Any valuation of Kaveri must quote the base case in `kaveri-valuation.md` (WACC 12.19%, g 5.5%, ₹320/share base,
  ₹416 bull, ₹168 bear, ₹306 probability-weighted, CMP ₹390, reverse-DCF implied growth ≈14.1%).
- For exercises you may also create **small self-contained fictional companies** with their own numbers.

## 4. Lesson page template

Every lesson file uses this skeleton (headings exactly as shown, in this order; omit a section only if truly N/A):

```markdown
# 02.6 · How the three statements link

> **Why this matters:** one or two sentences on why a practitioner cares.

**Learning objectives** — after this lesson you can:
- …(3–6 bullets, each testable)

**Prerequisites:** [02.3 The income statement](03-the-income-statement.md), …  ·  **Time:** ~75 min

---

## 1. <first concept section>
…body with worked examples, tables, diagrams…

## 2. …

!!! tip "Trader's lens"
    …analogy (optional, max 2 per lesson)…

!!! info "India notes"
    …India-specific rules, practice, quirks (when relevant)…

!!! warning "Common mistakes"
    - …

## Key terms
| Term | Meaning |
|:--|:--|
| **CWIP** | Capital work-in-progress: … |

## Check your understanding
1. Question…
<details><summary>Answer</summary>…</details>
(4–8 questions; mix conceptual and numerical)

## Go deeper
- Book/article/document — one line on why (2–5 items; real, verifiable resources only)

---
[← Previous: …](…) · [Module index](index.md) · [Next: … →](…)
```

Admonitions use MkDocs-Material syntax (`!!! tip "Title"` with a 4-space-indented body). `<details>` blocks are
used for answers so the learner can self-test. Mermaid diagrams (```` ```mermaid ````) are encouraged for flows.

## 5. Length and depth

- A lesson is typically **3,000–5,000 words**; foundational lessons (e.g. three-statement linkage, DCF) can run to
  ~7,000. Depth beats length: every section should teach something concrete.
- Every lesson includes **at least two fully worked numerical examples** (with the arithmetic shown) unless the topic
  is purely qualitative, in which case use concrete real-world or running-example illustrations.
- Tables: right-align numbers, show units in the header, use brackets for negatives in financial statements
  (e.g., `(14.0)`), percentages to one decimal.

## 6. Exercises & solutions (per module)

- `exercises.md`: 25–40 problems in four tiers — **Warm-up** (recall/definitions), **Core** (calculations and
  interpretation, mostly on Kaveri/Nirmal or self-contained fictional data), **Stretch** (multi-step, judgement,
  open-ended), **Real-world task** (do it on an actual listed Indian company using primary documents; e.g., "download
  the latest annual report of any Nifty 500 manufacturer and…"). Number problems `E04.12` etc.
- `solutions.md`: complete worked solutions with arithmetic, and a rubric for open-ended questions. **Every numerical
  answer must be verified by actually computing it (use Python).**
- Each module also has `index.md`: overview, why the module matters, lesson list with one-line summaries and times,
  how it connects to other modules, and a checklist "you're ready to move on when you can…".

## 7. Voice

- Direct, precise, a little dry humour allowed. No filler ("In today's fast-paced world…"), no motivational fluff.
- Second person ("you") for instructions; "we" for shared reasoning.
- British/Indian spelling (capitalise, amortisation, modelling) consistently.
- Don't recommend buying or selling any real security. The course is educational; valuation conclusions about
  real companies must be framed as illustrations of method, historically.

## 8. Copyright and quoting

- Do not reproduce text from books, annual reports or articles beyond short quotes (< 15 words, attributed).
  Paraphrase and cite. Tables of public financial figures are fine with a source.
- "Excerpts" of documents used for reading practice must be **written from scratch** (fictional companies) — not copied.

## 9. Links

- Relative links between pages (`../02-accounting/06-linking-the-three-statements.md`).
- Glossary terms can link to `../appendix/glossary.md#term-slug` (slug = lowercase, spaces → hyphens).
- Python tools are referenced by path (`tools/fi/valuation.py`) and function name.
