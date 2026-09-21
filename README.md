# Fundamental Investing — From Zero

An in-depth, **India-first** course in fundamental equity analysis for numerate people who know markets but have
never studied accounting. From the accounting equation to three-statement models, DCFs, bank valuation, forensic
accounting, investment memos, position sizing, 25 historical case studies, and mock exams.

**Read it:** start at [`docs/index.md`](docs/index.md) (renders on GitHub), or build the site locally
(see below). The full map is in [`docs/syllabus.md`](docs/syllabus.md).

> Educational material only — not investment advice. The running-example companies are fictional.
> See [`docs/disclaimer.md`](docs/disclaimer.md).

## Contents

| Part | Modules |
|:--|:--|
| I · Foundations | [00 Orientation](docs/00-orientation/index.md) · [01 Money, companies & markets 101](docs/01-markets-101/index.md) |
| II · Accounting & filings | [02 Accounting foundations](docs/02-accounting/index.md) · [03 Reading filings & documents](docs/03-reading-filings/index.md) |
| III · Analysis | [04 Financial statement analysis](docs/04-financial-analysis/index.md) · [05 Business & competitive analysis](docs/05-business-analysis/index.md) |
| IV · Valuation | [06 Valuation](docs/06-valuation/index.md) · [07 Valuing special kinds of companies](docs/07-special-valuation/index.md) |
| V · Sectors | [08 Sector playbooks (India)](docs/08-sectors/index.md) |
| VI · Skepticism | [09 Forensic accounting & red flags](docs/09-forensics/index.md) |
| VII · Doing the work | [10 Financial modelling](docs/10-modeling/index.md) · [11 Investment process & portfolio](docs/11-process/index.md) · [12 Macro, cycles & special situations](docs/12-macro-special-sits/index.md) |
| VIII · Case studies | [13 Historical case studies — 10 global, 15 India](docs/13-case-studies/index.md) |
| IX · Practice | [14 Mocks & drills](docs/14-mocks/index.md) · [15 Capstone: your own case studies](docs/15-capstone/index.md) |
| Appendices | [Glossary](docs/appendix/glossary.md) · [Formula sheet](docs/appendix/formula-sheet.md) · [Reading list](docs/appendix/reading-list.md) · [Data sources](docs/appendix/data-sources.md) · [Python tools](docs/appendix/tools.md) · [Running examples](docs/appendix/running-example/kaveri-pumps.md) |

## Repository layout

```
docs/            course content (MkDocs site source; also readable directly on GitHub)
tools/           Python library used in lessons (ratios, DCF, reverse DCF, forensic scores, 3-statement model)
  running_example/  generators for the fictional companies — their statements always balance
  data/             generated CSVs
flashcards/      Anki deck generated from the glossary
STYLE.md         authoring rules (for contributors)
mkdocs.yml       site configuration
```

## Build the site locally

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

## Use the Python tools

```bash
pip install -r tools/requirements.txt
python -m pytest tools/tests -q
python tools/examples/kaveri_dcf_and_reverse_dcf.py
```

On Windows, scripts set UTF-8 stdout so `₹` prints correctly. Fetching live Indian market data uses `yfinance`
(and OpenBB if installed); some VPNs block Yahoo Finance — disable the VPN if downloads fail.

## Licence

- Course text and figures: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — see [`LICENSE-CONTENT.md`](LICENSE-CONTENT.md).
- Code in `tools/`: MIT — see [`LICENSE`](LICENSE).
