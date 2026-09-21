"""Offline tests for fi.data (network functions are tested for import/signature only)."""
from __future__ import annotations

import inspect
import sys

import pandas as pd
import pytest

from fi import data
from fi.data import (
    fetch_price_info,
    fetch_statements,
    kaveri_opening_balance,
    load_kaveri,
    load_nirmal,
    revenue_row,
    standardise_statement,
    to_snake_case,
)

YEARS = ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]


def test_load_kaveri_annual_layout():
    df = load_kaveri()
    assert list(df.columns) == YEARS
    assert df.index.name == "line_item"
    assert df.at["rev", "FY26"] == pytest.approx(1318.0)
    assert df.at["pat", "FY26"] == pytest.approx(90.5)
    assert df.at["cfo", "FY25"] == pytest.approx(60.9)
    assert set(data.KAVERI_LINE_ITEMS) <= set(df.index)


def test_kaveri_balance_sheet_and_cash_flow_tie():
    df = load_kaveri()
    assert ((df.loc["total_assets"] - df.loc["total_le"]).abs() < 0.05).all()
    closing = [34.0] + list(df.loc["cash"].iloc[:-1])
    assert ((pd.Series(closing, index=YEARS) + df.loc["net_cash"] - df.loc["cash"]).abs() < 0.05).all()


def test_kaveri_attrs_and_opening_balance():
    df = load_kaveri()
    assert df.attrs["opening_for"] == "FY21"
    assert df.attrs["tax_rate"] == pytest.approx(0.2517)
    assert df.attrs["price"]["FY26"] == 520
    assert df.attrs["cmp"] == 390
    o = kaveri_opening_balance()
    assert o["total_assets"] == pytest.approx(566.0)
    assert o["total_assets"] == pytest.approx(o["total_le"])
    assert o["other_equity"] == pytest.approx(344.0)


def test_load_kaveri_other_kinds():
    q = load_kaveri("quarterly")
    assert list(q.columns) == ["Q1 FY26", "Q2 FY26", "Q3 FY26", "Q4 FY26", "Q1 FY27"]
    assert q.loc["rev", ["Q1 FY26", "Q2 FY26", "Q3 FY26", "Q4 FY26"]].sum() == pytest.approx(1318.0)
    r = load_kaveri("ratios")
    assert r.at["roe", "FY26"] == pytest.approx(0.1347, abs=1e-4)
    with pytest.raises(ValueError):
        load_kaveri("monthly")


def test_load_nirmal():
    n = load_nirmal()
    assert list(n.columns) == YEARS
    assert n.at["pat", "FY26"] == pytest.approx(239.5)
    assert n.at["aum", "FY26"] == pytest.approx(6920.0)
    assert ((n.loc["total_assets"] - n.loc["borrowings"] - n.loc["other_liab"] - n.loc["equity"]).abs() < 0.05).all()
    assert n.attrs["opening"]["aum"] == pytest.approx(2480.0)


def test_import_of_generators_does_not_hijack_stdout():
    before = sys.stdout
    data._MODULE_CACHE.clear()
    load_kaveri()
    assert sys.stdout is before


def test_snake_case_matches_openbb_convention():
    assert to_snake_case("TotalRevenue") == "total_revenue"
    assert to_snake_case("OperatingRevenue") == "operating_revenue"
    assert to_snake_case("BasicEPS") == "basic_eps"
    assert to_snake_case("EBITDA") == "ebitda"
    assert to_snake_case("NetIncomeCommonStockholders") == "net_income_common_stockholders"


def test_period_normalisation():
    assert data._normalise_period("quarterly") == "quarter"
    assert data._normalise_period("Annual") == "annual"
    with pytest.raises(ValueError):
        data._normalise_period("monthly")


def test_standardise_handles_operating_revenue_only():
    raw = pd.DataFrame({pd.Timestamp("2026-03-31"): [5.0e9, 1.0e9, 20.0],
                        pd.Timestamp("2025-03-31"): [4.0e9, 0.8e9, 16.0]},
                       index=["OperatingRevenue", "NetIncome", "BasicEPS"])
    std = standardise_statement(raw, "income", in_crore=True)
    assert list(std.columns) == ["2025-03-31", "2026-03-31"]  # oldest -> newest
    assert std.at["revenue", "2026-03-31"] == pytest.approx(500.0)  # rupees -> crore
    assert std.at["eps_basic", "2026-03-31"] == pytest.approx(20.0)  # per-share not scaled
    assert revenue_row(std)["2025-03-31"] == pytest.approx(400.0)


def test_standardise_prefers_total_revenue_and_fills_gaps():
    raw = pd.DataFrame({"2026-03-31": [None, 90.0], "2025-03-31": [100.0, 80.0]},
                       index=["total_revenue", "operating_revenue"])
    std = standardise_statement(raw, "income")
    assert std.at["revenue", "2025-03-31"] == 100.0
    assert std.at["revenue", "2026-03-31"] == 90.0  # falls back to operating_revenue


def test_network_function_signatures():
    sig = inspect.signature(fetch_statements)
    assert list(sig.parameters)[:3] == ["ticker", "period", "provider"]
    assert sig.parameters["period"].default == "annual"
    assert sig.parameters["provider"].default == "yfinance"
    assert list(inspect.signature(fetch_price_info).parameters) == ["ticker"]
    assert "VPN" in (fetch_statements.__doc__ or "")
