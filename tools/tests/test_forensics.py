"""Forensic scores: formula checks on hand-built inputs, then the Kaveri mapping."""
from __future__ import annotations

import pytest

from fi.data import load_kaveri
from fi.forensics import (
    BENEISH_COEFFS,
    BENEISH_THRESHOLD,
    accruals_ratio,
    altman_z,
    altman_zone,
    balance_sheet_accruals,
    beneish_m,
    cash_yield_check,
    forensic_inputs,
    forensic_summary,
    piotroski_f,
)

NEUTRAL = dict(sales=1000.0, cogs=600.0, sga=150.0, receivables=100.0, current_assets=400.0, ppe=300.0,
               securities=0.0, total_assets=800.0, depreciation=30.0, current_liabilities=200.0,
               long_term_debt=100.0, net_income=80.0, cfo=80.0)


def test_beneish_neutral_company_scores_minus_2_48():
    r = beneish_m(NEUTRAL, NEUTRAL)
    for k in ("DSRI", "GMI", "AQI", "SGI", "DEPI", "SGAI", "LVGI"):
        assert r[k] == pytest.approx(1.0)
    assert r["TATA"] == pytest.approx(0.0)
    expected = sum(v for k, v in BENEISH_COEFFS.items() if k != "TATA")  # all indices = 1
    assert r["m_score"] == pytest.approx(expected)
    assert r["m_score"] == pytest.approx(-2.48, abs=1e-9)
    assert r["threshold"] == BENEISH_THRESHOLD == -1.78
    assert r["likely_manipulator"] is False


def test_beneish_receivables_and_accruals_push_score_up():
    cur = dict(NEUTRAL, receivables=180.0, net_income=120.0, cfo=40.0)
    r = beneish_m(cur, NEUTRAL)
    assert r["DSRI"] == pytest.approx(1.8)
    assert r["TATA"] == pytest.approx(80.0 / 800.0)
    manual = -2.48 + 0.920 * 0.8 + 4.679 * 0.1
    assert r["m_score"] == pytest.approx(manual)
    assert r["likely_manipulator"] is True


def test_altman_variants():
    args = dict(wc=0.2, re=0.3, ebit=0.1, mve=1.5, sales=1.2, ta=1.0, tl=0.5)
    z = altman_z(**args)
    assert z == pytest.approx(1.2 * 0.2 + 1.4 * 0.3 + 3.3 * 0.1 + 0.6 * 3.0 + 1.0 * 1.2)
    zpp = altman_z(**args, variant="z_double_prime")
    assert zpp == pytest.approx(6.56 * 0.2 + 3.26 * 0.3 + 6.72 * 0.1 + 1.05 * 3.0)
    assert altman_z(**args, variant="z_double_prime_em") == pytest.approx(zpp + 3.25)
    zp = altman_z(**args, variant="z_prime")
    assert zp == pytest.approx(0.717 * 0.2 + 0.847 * 0.3 + 3.107 * 0.1 + 0.420 * 3.0 + 0.998 * 1.2)
    assert altman_zone(1.5) == "distress" and altman_zone(2.5) == "grey" and altman_zone(3.5) == "safe"
    assert altman_zone(1.0, "z_double_prime") == "distress" and altman_zone(2.7, "z_double_prime") == "safe"
    with pytest.raises(ValueError):
        altman_z(**args, variant="z_triple")


def test_piotroski_all_good_scores_9_and_all_bad_scores_0():
    prev = dict(net_income=50.0, cfo=60.0, total_assets_begin=1000.0, total_assets=1000.0, long_term_debt=200.0,
                current_assets=300.0, current_liabilities=200.0, sales=1000.0, cogs=700.0, share_capital=10.0)
    good = dict(net_income=80.0, cfo=120.0, total_assets_begin=1000.0, total_assets=1050.0, long_term_debt=150.0,
                current_assets=360.0, current_liabilities=200.0, sales=1200.0, cogs=780.0, share_capital=10.0)
    r = piotroski_f(good, prev)
    assert r["score"] == 9
    bad = dict(net_income=-10.0, cfo=-20.0, total_assets_begin=1000.0, total_assets=1000.0, long_term_debt=300.0,
               current_assets=250.0, current_liabilities=250.0, sales=900.0, cogs=700.0, share_capital=12.0)
    assert piotroski_f(bad, prev)["score"] == 0


def test_accruals_and_cash_yield():
    assert accruals_ratio(90.5, 65.1, (1035.8 + 1143.6) / 2) == pytest.approx(0.02331, abs=1e-5)
    # Sloan: (dCA - dCash) - (dCL - dSTD - dTP) - Dep
    assert balance_sheet_accruals(97.6, -10.5, 56.4, 38.0, 47.8, 1089.7) == pytest.approx(41.9 / 1089.7)
    assert cash_yield_check((28.0 + 30.0 + 32.5 + 15.0) / 2, 3.9) == pytest.approx(3.9 / 52.75)
    with pytest.raises(ValueError):
        cash_yield_check(0.0, 1.0)


def test_kaveri_input_mapping_fy26():
    df = load_kaveri()
    x = forensic_inputs(df, "FY26")
    assert x["sga"] == pytest.approx(117.3 + 160.8)
    assert x["current_assets"] == pytest.approx(188.1 + 346.7 + 39.5 + 15.0 + 32.5)
    assert x["current_liabilities"] == pytest.approx(96.0 + 143.4 + 65.9)
    assert x["ppe"] == pytest.approx(495.3 + 2.0 + 16.5)
    assert x["total_assets_begin"] == pytest.approx(1035.8)
    assert x["ebit"] == pytest.approx(121.0 + 17.0)  # PBT + finance costs - exceptional
    assert x["market_cap"] == pytest.approx(520 * 6.0)
    assert forensic_inputs(df, "FY21")["total_assets_begin"] == pytest.approx(566.0)


def test_kaveri_summary_fy26():
    s = forensic_summary(load_kaveri(), "FY26")
    b = s["beneish"]
    assert b["DSRI"] == pytest.approx((346.7 / 1318.0) / (269.7 / 1172.0))
    assert b["m_score"] == pytest.approx(-2.142, abs=5e-4)
    assert b["likely_manipulator"] is False
    assert s["piotroski"]["score"] == 4
    assert s["altman_original_zone"] == "safe"
    assert s["cash_yield"] == pytest.approx(0.0739, abs=1e-4)
    with pytest.raises(ValueError):
        forensic_summary(load_kaveri(), "FY21")
