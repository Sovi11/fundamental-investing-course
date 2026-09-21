"""Valuation building blocks and the Kaveri reference valuation (₹320 base)."""
from __future__ import annotations

import pytest
from conftest import REPO_ROOT

from fi.valuation import (
    capm,
    dcf_fcff,
    dcf_from_drivers,
    equity_bridge,
    gordon_value,
    justified_pb,
    justified_pe,
    kaveri_base_drivers,
    kaveri_reference,
    reverse_dcf,
    sensitivity,
    terminal_value,
    wacc,
)

VALUATION_MD = REPO_ROOT / "docs" / "appendix" / "running-example" / "kaveri-valuation.md"


@pytest.fixture(scope="module")
def ref():
    return kaveri_reference()


def test_capm_and_wacc_match_reference():
    ke = capm(0.065, 1.05, 0.06)
    assert ke == pytest.approx(0.128)
    assert wacc(ke, 0.089, 0.2517, 0.10) == pytest.approx(0.12186, abs=1e-5)
    with pytest.raises(ValueError):
        wacc(ke, 0.089, 0.25, 1.5)


def test_gordon_and_terminal_value():
    assert gordon_value(100.0, 0.12, 0.05) == pytest.approx(100 / 0.07)
    with pytest.raises(ValueError):
        gordon_value(100.0, 0.05, 0.05)
    # value-driver formula: reinvestment g/RONIC
    assert terminal_value(100.0, 0.12, 0.05, ronic=0.20) == pytest.approx(100 * 0.75 / 0.07)
    # RONIC = WACC -> growth adds nothing: TV = NOPAT / WACC
    assert terminal_value(100.0, 0.12, 0.05, ronic=0.12) == pytest.approx(100 / 0.12)
    assert terminal_value(0.0, 0.12, 0.05, fcff_next=70.0) == pytest.approx(1000.0)
    with pytest.raises(ValueError):
        terminal_value(100.0, 0.12, 0.05)


def test_dcf_fcff_mid_year_and_end_year():
    d = dcf_fcff([100.0, 100.0], 0.10, 1000.0, mid_year=True)
    assert d["discount_factors"][0] == pytest.approx(1.1 ** -0.5)
    assert d["pv_tv"] == pytest.approx(1000 / 1.21)
    e = dcf_fcff([100.0, 100.0], 0.10, 1000.0, mid_year=False)
    assert e["pv_explicit"] == pytest.approx(100 / 1.1 + 100 / 1.21)
    assert d["ev"] > e["ev"]


def test_equity_bridge_kaveri():
    assert equity_bridge(2100.0, 140.5, leases=18.2) == pytest.approx(1941.3)
    assert equity_bridge(1000.0, 100.0, leases=10.0, nci=5.0, investments=50.0) == pytest.approx(935.0)


def test_kaveri_reference_reproduces_house_view(ref):
    assert round(ref["per_share"]) == 320
    assert ref["ev"] == pytest.approx(2100.0, abs=0.05)
    assert ref["equity"] == pytest.approx(1941.3, abs=0.05)
    assert ref["wacc"] == pytest.approx(0.1219, abs=5e-5)
    assert ref["pv_explicit"] == pytest.approx(947.7, abs=0.05)
    assert ref["tv"] == pytest.approx(3638.7, abs=0.05)
    assert round(ref["tv_share"] * 100) == 55
    assert round(ref["scenarios"]["Bull"]) == 416
    assert round(ref["scenarios"]["Bear"]) == 168
    assert round(ref["probability_weighted"]) == 306
    assert round(ref["implied_growth"] * 100, 1) == 14.1
    assert round(ref["roll_forward_per_share"]) == 338
    assert ref["cross_check_per_share"] == pytest.approx(ref["per_share"], abs=1e-9)


def test_reference_sensitivity_matches_published_grid(ref):
    text = VALUATION_MD.read_text(encoding="utf-8")
    section = text.split("## Sensitivity", 1)[1].split("## Scenarios", 1)[0]
    published = [[int(c.strip().lstrip("₹").replace(",", "")) for c in line.strip().strip("|").split("|")[1:]]
                 for line in section.splitlines() if line.startswith("| 1")]
    ours = ref["sensitivity"].round(0).astype(int).values.tolist()
    assert ours == published


def test_dcf_from_drivers_reproduces_projection(ref):
    base = dcf_from_drivers(**kaveri_base_drivers())
    assert round(base["per_share"]) == 320
    ours = base["projection"].loc["fcff"].round(1).tolist()
    theirs = ref["projection"].loc["fcff"].round(1).tolist()
    assert ours == theirs == [108.5, 114.2, 124.5, 132.0, 157.3, 179.3, 202.5, 226.5, 251.1, 275.6]


def test_reverse_dcf_generic_and_kaveri():
    # invert a known monotone function
    assert reverse_dcf(4.0, lambda x: x * x, lo=0.0, hi=10.0) == pytest.approx(2.0, abs=1e-6)
    # decreasing function also works
    assert reverse_dcf(0.5, lambda x: 1 - x, lo=0.0, hi=1.0) == pytest.approx(0.5, abs=1e-6)
    with pytest.raises(ValueError):
        reverse_dcf(1000.0, lambda x: x, lo=0.0, hi=1.0)
    drivers = kaveri_base_drivers()
    g = reverse_dcf(390.0, lambda x: dcf_from_drivers(**{**drivers, "growth": [x] * 10})["per_share"])
    assert round(g * 100, 1) == 14.1


def test_sensitivity_grid_shape_and_values():
    t = sensitivity(lambda r, g: 100 / (r - g), {"r": [0.10, 0.12]}, {"g": [0.03, 0.05]})
    assert t.shape == (2, 2)
    assert t.index.name == "r" and t.columns.name == "g"
    assert t.loc[0.12, 0.03] == pytest.approx(100 / 0.09)
    with pytest.raises(ValueError):
        sensitivity(lambda r, g: 0, {"r": [1], "x": [2]}, {"g": [1]})


def test_justified_multiples():
    # P/E = (1 - g/ROE)/(r - g)
    assert justified_pe(0.18, 0.128, 0.055) == pytest.approx((1 - 0.055 / 0.18) / 0.073)
    # explicit payout, with sustainable g = ROE x (1 - payout)
    assert justified_pe(0.4, 0.14, None, roe=0.15) == pytest.approx(0.4 / (0.14 - 0.09))
    assert justified_pe(0.18, 0.128, 0.055, trailing=True) == pytest.approx(
        justified_pe(0.18, 0.128, 0.055) * 1.055)
    assert justified_pb(0.15, 0.14, 0.08) == pytest.approx(0.07 / 0.06)
    assert justified_pb(0.14, 0.14, 0.08) == pytest.approx(1.0)  # ROE = cost of equity -> P/B 1
    with pytest.raises(ValueError):
        justified_pb(0.2, 0.1, 0.1)
