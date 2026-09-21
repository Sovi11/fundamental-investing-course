"""The three-statement engine must balance, reconcile cash, and rebuild the ₹320 reference value."""
from __future__ import annotations

import pytest

from fi.data import load_kaveri
from fi.model import Assumptions, fcff_from_projection, project
from fi.valuation import dcf_fcff, equity_bridge, kaveri_reference, terminal_value


@pytest.fixture(scope="module")
def hist():
    return load_kaveri()


def _assert_balances(proj):
    chk = proj["checks"]
    assert (chk.loc["balance_diff"].abs() < 1e-6).all()
    assert (chk.loc["cash_recon_diff"].abs() < 1e-6).all()
    assert (chk.loc["balances"] == 1).all()
    bal = proj["balance"]
    assert ((bal.loc["total_assets"] - bal.loc["total_le"]).abs() < 1e-6).all()
    # closing cash on the balance sheet = closing cash in the cash-flow statement
    assert ((bal.loc["cash"].iloc[1:] - proj["cash"].loc["closing_cash"]).abs() < 1e-9).all()


def test_base_projection_balances_every_year(hist):
    proj = project(hist, Assumptions.kaveri_base())
    assert list(proj["income"].columns) == [f"FY{y}" for y in range(27, 37)]
    assert list(proj["balance"].columns)[0] == "FY26"
    _assert_balances(proj)
    assert proj["balance"].at["nwc", "FY26"] == pytest.approx(365.0)


def test_fcff_and_value_match_reference(hist):
    ref = kaveri_reference()
    proj = project(hist, Assumptions.kaveri_base())
    fcff = fcff_from_projection(proj)
    assert fcff.values == pytest.approx(ref["projection"].loc["fcff"].values, abs=1e-9)
    nopat_next = proj["income"].loc["nopat"].iloc[-1] * (1 + 0.055)
    tv = terminal_value(nopat_next, ref["wacc"], 0.055, ronic=0.18)
    dcf = dcf_fcff(fcff.tolist(), ref["wacc"], tv, mid_year=True)
    per_share = equity_bridge(dcf["ev"], net_debt=140.5, leases=18.2) / 6.07
    assert round(per_share) == 320
    assert per_share == pytest.approx(ref["per_share"], abs=1e-9)


def test_days_mode_balances_and_hits_the_days(hist):
    a = Assumptions.kaveri_base(nwc_pct=None, inventory_days=80, receivable_days=75, payable_days=61)
    proj = project(hist, a, years=5)
    _assert_balances(proj)
    bal, inc = proj["balance"], proj["income"]
    gm = 1 - hist.at["mat", "FY26"] / hist.at["rev", "FY26"]
    assert bal.at["receivables", "FY28"] / inc.at["rev", "FY28"] * 365 == pytest.approx(75.0)
    assert bal.at["inventory", "FY28"] / (inc.at["rev", "FY28"] * (1 - gm)) * 365 == pytest.approx(80.0)


def test_revolver_keeps_cash_at_floor_and_still_balances(hist):
    # stress: no growth, thin margins, heavy capex and a big dividend -> cash would go negative
    a = Assumptions(growth=[0.0] * 5, ebitda_margin=0.05, capex_pct=0.12, nwc_pct=0.30, dividend_payout=1.0,
                    lt_debt_change=-20.0, min_cash=25.0)
    proj = project(hist, a)
    _assert_balances(proj)
    assert (proj["balance"].loc["cash"].iloc[1:] >= 25.0 - 1e-9).all()
    assert proj["cash"].loc["revolver_draw"].sum() > 0
    no_revolver = project(hist, Assumptions(**{**a.__dict__, "min_cash": None}))
    _assert_balances(no_revolver)
    assert no_revolver["checks"].loc["cash_negative"].sum() > 0


def test_debt_repayment_cannot_overshoot(hist):
    proj = project(hist, Assumptions.kaveri_base(lt_debt_change=-60.0), years=4)
    _assert_balances(proj)
    assert (proj["balance"].loc["lt_debt"] >= -1e-9).all()


def test_missing_rows_raise(hist):
    with pytest.raises(KeyError):
        project(hist.drop(index="receivables"), Assumptions.kaveri_base())
