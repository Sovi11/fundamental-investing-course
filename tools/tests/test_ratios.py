"""The ratio dashboard must reproduce kaveri-pumps.md §6 exactly (one decimal)."""
from __future__ import annotations

import math

import pytest
from conftest import REPO_ROOT

from fi.data import load_kaveri
from fi.ratios import (
    RATIO_LABELS,
    dupont_3,
    dupont_5,
    format_dashboard,
    margins,
    ratio_dashboard,
    roce,
    roe,
    roic,
    working_capital_days,
)

KAVERI_MD = REPO_ROOT / "docs" / "appendix" / "running-example" / "kaveri-pumps.md"


def _md_ratio_table() -> dict[str, list[str]]:
    text = KAVERI_MD.read_text(encoding="utf-8")
    section = text.split("## 6. Key ratios", 1)[1].split("## 7.", 1)[0]
    rows = {}
    for line in section.splitlines():
        if not line.startswith("| ") or line.startswith("| Ratio") or line.startswith("|:--"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows[cells[0]] = cells[1:]
    return rows


def test_dashboard_reproduces_course_table_to_one_decimal():
    md = _md_ratio_table()
    assert len(md) == len(RATIO_LABELS) == 28
    ours = format_dashboard(ratio_dashboard(load_kaveri()), labels=True)
    assert list(ours.index) == list(md)  # same rows, same order
    for label, cells in md.items():
        assert list(ours.loc[label]) == cells, label


def test_dashboard_matches_generator_csv():
    dash = ratio_dashboard(load_kaveri())
    ref = load_kaveri("ratios")
    for key in ref.index:
        for year in ref.columns:
            a, b = dash.at[key, year], ref.at[key, year]
            if math.isnan(b):
                assert math.isnan(a)
            else:
                assert a == pytest.approx(b, abs=6e-5), (key, year)


def test_dashboard_without_opening_leaves_first_year_averages_blank():
    df = load_kaveri()[["FY25", "FY26"]]  # attrs travel, but FY25 has no opening balance here
    dash = ratio_dashboard(df)
    assert math.isnan(dash.at["roe", "FY25"])
    assert dash.at["roe", "FY26"] == pytest.approx(0.1347, abs=1e-4)


def test_building_blocks_on_kaveri_fy26():
    m = margins(1318.0, ebitda=181.9, pat=90.5)
    assert m["ebitda"] == pytest.approx(0.138, abs=5e-4)
    assert roe(90.5, 637.2, 706.1) == pytest.approx(90.5 / 671.65)
    ce25 = 637.2 + 112.0 + 58.0 + 16.7
    ce26 = 706.1 + 92.0 + 96.0 + 18.2
    assert roce(134.1, 3.9, ce25, ce26) == pytest.approx(0.159, abs=5e-4)
    assert roic(134.1, 0.2517, 100.0, 100.0) == pytest.approx(134.1 * 0.7483 / 100)
    wc = working_capital_days(1318.0, 858.0, 188.1, 346.7, 143.4)
    assert round(wc["dso"]) == 96 and round(wc["dio"]) == 80 and round(wc["dpo"]) == 61
    assert wc["ccc"] == pytest.approx(wc["dio"] + wc["dso"] - wc["dpo"])


def test_dupont_identities():
    avg_ta, avg_eq = (1035.8 + 1143.6) / 2, (637.2 + 706.1) / 2
    d3 = dupont_3(90.5, 1318.0, avg_ta, avg_eq)
    assert d3["roe"] == pytest.approx(90.5 / avg_eq)
    d5 = dupont_5(90.5, 121.0, 138.0, 1318.0, avg_ta, avg_eq)
    assert d5["roe"] == pytest.approx(90.5 / avg_eq)
    assert d5["tax_burden"] == pytest.approx(90.5 / 121.0)
