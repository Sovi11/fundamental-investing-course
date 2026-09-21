"""Generate the course's two fictional running-example companies.

Kaveri Pumps & Motors Ltd (KPML) - a manufacturer, used for accounting, ratios,
modelling, valuation and forensics lessons.
Nirmal Finance Ltd (NFL) - a vehicle/MSME NBFC, used for lender lessons.

Every line is rounded to 0.1 Rs Cr at the point it is created and every subtotal is
a sum of rounded lines, so the published tables add up exactly. The balance sheet
is checked every year and the cash-flow statement is reconciled to the change in
cash. Run:  python tools/running_example/generate.py
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "tools" / "data"
DOCS = ROOT / "docs" / "appendix" / "running-example"

YEARS = ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]


def r1(x: float) -> float:
    return round(x + 0.0, 1)


# ---------------------------------------------------------------------------
# Kaveri Pumps & Motors Ltd
# ---------------------------------------------------------------------------
K = dict(
    revenue=[612, 758, 874, 1006, 1172, 1318],
    gross_margin=[0.360, 0.330, 0.342, 0.368, 0.356, 0.349],
    employee_pct=[0.102, 0.092, 0.091, 0.090, 0.088, 0.089],
    other_exp_pct=[0.128, 0.118, 0.120, 0.124, 0.121, 0.122],
    sbc=[0, 0, 0, 0.8, 2.0, 2.4],  # share-based payment, inside employee cost
    solar_share=[0.03, 0.04, 0.07, 0.14, 0.22, 0.27],
    industrial_share=[0.31, 0.30, 0.30, 0.29, 0.28, 0.27],
    inv_days=[82, 74, 76, 75, 78, 80],  # on cost of materials
    rec_days=[64, 57, 61, 70, 84, 96],  # on revenue
    pay_days=[66, 60, 62, 63, 64, 61],  # on cost of materials
    oca_pct=0.030,
    ocl_pct=0.050,
    capex_direct=[14, 26, 28, 30, 34, 36],
    cwip_add=[2, 6, 72, 118, 20, 12],
    cwip_transfer=[6, 4, 10, 186, 16, 14],
    intang_capex=[2, 2, 3, 3, 4, 4],
    intang_amort=[2.0, 2.0, 2.5, 3.0, 3.0, 3.5],
    dep_rate=0.052,  # on opening depreciable gross block
    land_sold_bv=[0, 0, 0, 0, 4, 0],
    land_sold_proceeds=[0, 0, 0, 0, 18, 0],
    vrs_cost=[7.5, 0, 0, 0, 0, 0],
    new_leases=[3, 4, 4, 6, 5, 6],
    lease_rate=0.085,
    rou_amort_rate=0.22,
    lease_principal_rate=0.20,
    lt_debt=[28, 20, 70, 132, 112, 92],
    st_debt=[36, 42, 38, 30, 58, 96],
    debt_rate=[0.089, 0.082, 0.086, 0.091, 0.090, 0.087],
    cur_inv=[30, 45, 25, 20, 30, 15],
    treasury_yield=0.068,
    tax_rate=0.2517,
    dtl=[15, 16, 17, 20, 21, 22],
    dps_paid=[1.5, 1.5, 2.0, 2.5, 3.5, 4.0],  # dividend paid in the year (for prior FY)
    shares=6.0,  # crore shares, Rs 5 face value
    diluted_shares=[6.0, 6.0, 6.0, 6.02, 6.05, 6.07],
    related_party_pct=[0.065, 0.070, 0.075, 0.082, 0.091, 0.104],  # of material cost
    price_mar=[210, 320, 360, 610, 780, 520],
    cmp=390,  # 18-Sep-2026
)

OPEN = dict(  # balance sheet at 31-Mar-2020
    gross_block=430.0, land=22.0, acc_dep=165.0, cwip=8.0, rou=12.0, lease_liab=13.0,
    intangibles=6.0, inventory=86.0, receivables=96.0, oca=19.0, cash=34.0, cur_inv=40.0,
    share_capital=30.0, lt_debt=35.0, st_debt=30.0, payables=68.0, ocl=32.0, dtl=14.0,
)
OPEN["other_equity"] = r1(
    OPEN["gross_block"] - OPEN["acc_dep"] + OPEN["cwip"] + OPEN["rou"] + OPEN["intangibles"]
    + OPEN["inventory"] + OPEN["receivables"] + OPEN["oca"] + OPEN["cash"] + OPEN["cur_inv"]
    - OPEN["share_capital"] - OPEN["lt_debt"] - OPEN["st_debt"] - OPEN["lease_liab"]
    - OPEN["payables"] - OPEN["ocl"] - OPEN["dtl"]
)


def build_kaveri():
    rows = []  # per-year dicts
    prev = dict(OPEN)
    for i, fy in enumerate(YEARS):
        y = {}
        rev = r1(K["revenue"][i])
        mat = r1(rev * (1 - K["gross_margin"][i]))
        emp = r1(rev * K["employee_pct"][i])
        oth = r1(rev * K["other_exp_pct"][i])
        ebitda = r1(rev - mat - emp - oth)

        # --- fixed assets
        dep_base = prev["gross_block"] - prev["land"]
        dep_ppe = r1(dep_base * K["dep_rate"])
        rou_amort = r1((prev["rou"] + K["new_leases"][i]) * K["rou_amort_rate"])
        int_amort = r1(K["intang_amort"][i])
        da = r1(dep_ppe + rou_amort + int_amort)
        ebit = r1(ebitda - da)

        other_income = r1((prev["cash"] + prev["cur_inv"]) * K["treasury_yield"])
        avg_debt = (prev["lt_debt"] + prev["st_debt"] + K["lt_debt"][i] + K["st_debt"][i]) / 2
        debt_int = r1(avg_debt * K["debt_rate"][i])
        lease_int = r1(prev["lease_liab"] * K["lease_rate"])
        fin_cost = r1(debt_int + lease_int)
        exceptional = r1(-K["vrs_cost"][i] + (K["land_sold_proceeds"][i] - K["land_sold_bv"][i]))
        pbt = r1(ebit + other_income - fin_cost + exceptional)
        tax = r1(pbt * K["tax_rate"])
        deferred_tax = r1(K["dtl"][i] - prev["dtl"])
        current_tax = r1(tax - deferred_tax)
        pat = r1(pbt - tax)

        # --- balance sheet
        gross_block = r1(prev["gross_block"] + K["capex_direct"][i] + K["cwip_transfer"][i] - K["land_sold_bv"][i])
        land = r1(prev["land"] - K["land_sold_bv"][i])
        acc_dep = r1(prev["acc_dep"] + dep_ppe)
        net_block = r1(gross_block - acc_dep)
        cwip = r1(prev["cwip"] + K["cwip_add"][i] - K["cwip_transfer"][i])
        rou = r1(prev["rou"] + K["new_leases"][i] - rou_amort)
        lease_principal = r1((prev["lease_liab"] + K["new_leases"][i]) * K["lease_principal_rate"])
        lease_payment = r1(lease_principal + lease_int)
        lease_liab = r1(prev["lease_liab"] + K["new_leases"][i] + lease_int - lease_payment)
        intangibles = r1(prev["intangibles"] + K["intang_capex"][i] - int_amort)
        inventory = r1(mat * K["inv_days"][i] / 365)
        receivables = r1(rev * K["rec_days"][i] / 365)
        oca = r1(rev * K["oca_pct"])
        payables = r1(mat * K["pay_days"][i] / 365)
        ocl = r1(rev * K["ocl_pct"])
        cur_inv = r1(K["cur_inv"][i])
        lt_debt = r1(K["lt_debt"][i])
        st_debt = r1(K["st_debt"][i])
        dtl = r1(K["dtl"][i])
        dividends = r1(K["dps_paid"][i] * K["shares"])
        sbc = r1(K["sbc"][i])
        other_equity = r1(prev["other_equity"] + pat - dividends + sbc)

        # --- cash flow (indirect; interest paid in CFF, interest received in CFI)
        d_inv = r1(inventory - prev["inventory"])
        d_rec = r1(receivables - prev["receivables"])
        d_oca = r1(oca - prev["oca"])
        d_pay = r1(payables - prev["payables"])
        d_ocl = r1(ocl - prev["ocl"])
        gain_on_sale = r1(K["land_sold_proceeds"][i] - K["land_sold_bv"][i])
        op_before_wc = r1(pbt + da + fin_cost - other_income - gain_on_sale + sbc)
        wc_change = r1(-d_inv - d_rec - d_oca + d_pay + d_ocl)
        cfo = r1(op_before_wc + wc_change - current_tax)
        capex_ppe = r1(K["capex_direct"][i] + K["cwip_add"][i])
        capex_int = r1(K["intang_capex"][i])
        d_cur_inv = r1(cur_inv - prev["cur_inv"])
        asset_sale = r1(K["land_sold_proceeds"][i])
        cfi = r1(-capex_ppe - capex_int - d_cur_inv + asset_sale + other_income)
        d_lt = r1(lt_debt - prev["lt_debt"])
        d_st = r1(st_debt - prev["st_debt"])
        cff = r1(d_lt + d_st - debt_int - lease_payment - dividends)
        net_cash = r1(cfo + cfi + cff)
        cash = r1(prev["cash"] + net_cash)

        total_assets = r1(net_block + cwip + rou + intangibles + inventory + receivables + oca + cash + cur_inv)
        equity = r1(prev["share_capital"] + other_equity)
        total_le = r1(equity + lt_debt + st_debt + lease_liab + payables + ocl + dtl)
        assert abs(total_assets - total_le) < 0.05, (fy, total_assets, total_le)
        assert cash > 0, (fy, cash)

        y.update(locals())
        y["share_capital"] = prev["share_capital"]
        y = {k: v for k, v in y.items() if isinstance(v, (int, float)) and k not in ("i",)}
        y["fy"] = fy
        rows.append(y)
        prev = dict(
            gross_block=gross_block, land=land, acc_dep=acc_dep, cwip=cwip, rou=rou, lease_liab=lease_liab,
            intangibles=intangibles, inventory=inventory, receivables=receivables, oca=oca, cash=cash,
            cur_inv=cur_inv, share_capital=prev["share_capital"], lt_debt=lt_debt, st_debt=st_debt,
            payables=payables, ocl=ocl, dtl=dtl, other_equity=other_equity,
        )
    return rows


def kaveri_ratios(rows):
    out = []
    prev = OPEN | {"equity": r1(OPEN["share_capital"] + OPEN["other_equity"])}
    prev["net_block"] = prev["gross_block"] - prev["acc_dep"]
    for i, y in enumerate(rows):
        rev = y["rev"]
        avg_eq = (prev["equity"] + y["equity"]) / 2
        cap_emp = y["equity"] + y["lt_debt"] + y["st_debt"] + y["lease_liab"]
        prev_cap_emp = prev["equity"] + prev["lt_debt"] + prev["st_debt"] + prev["lease_liab"]
        avg_ce = (cap_emp + prev_cap_emp) / 2
        net_debt = y["lt_debt"] + y["st_debt"] - y["cash"] - y["cur_inv"]
        fcf = y["cfo"] - y["capex_ppe"] - y["capex_int"]
        nopat = y["ebit"] * (1 - K["tax_rate"])
        ic = y["net_block"] + y["cwip"] + y["rou"] + y["intangibles"] + (
            y["inventory"] + y["receivables"] + y["oca"] - y["payables"] - y["ocl"])
        prev_ic = prev["net_block"] + prev["cwip"] + prev["rou"] + prev["intangibles"] + (
            prev["inventory"] + prev["receivables"] + prev["oca"] - prev["payables"] - prev["ocl"])
        eps = y["pat"] / K["shares"]
        adj_pat = y["pat"] - y["exceptional"] * (1 - K["tax_rate"])
        price = K["price_mar"][i]
        out.append(dict(
            fy=y["fy"],
            rev_growth=None if i == 0 else rev / rows[i - 1]["rev"] - 1,
            gross_margin=(rev - y["mat"]) / rev,
            ebitda_margin=y["ebitda"] / rev,
            ebit_margin=y["ebit"] / rev,
            pat_margin=y["pat"] / rev,
            roe=y["pat"] / avg_eq,
            roce=(y["ebit"] + y["other_income"]) / avg_ce,
            roic=nopat / ((ic + prev_ic) / 2),
            inv_days=y["inventory"] / y["mat"] * 365,
            rec_days=y["receivables"] / rev * 365,
            pay_days=y["payables"] / y["mat"] * 365,
            ccc=(y["inventory"] / y["mat"] + y["receivables"] / rev - y["payables"] / y["mat"]) * 365,
            cfo_to_ebitda=y["cfo"] / y["ebitda"],
            cfo_to_pat=y["cfo"] / y["pat"],
            fcf=fcf,
            net_debt=net_debt,
            nd_to_ebitda=net_debt / y["ebitda"],
            int_cover=y["ebit"] / y["fin_cost"],
            de=(y["lt_debt"] + y["st_debt"]) / y["equity"],
            eps=eps,
            adj_eps=adj_pat / K["shares"],
            bvps=y["equity"] / K["shares"],
            dps_paid=K["dps_paid"][i],
            price=price,
            pe=price / eps,
            pb=price / (y["equity"] / K["shares"]),
            ev_ebitda=(price * K["shares"] + net_debt + y["lease_liab"]) / y["ebitda"],
            asset_turnover=rev / y["total_assets"],
        ))
        prev = y | {"equity": y["equity"]}
    return out


# ---------------------------------------------------------------------------
# Nirmal Finance Ltd (NBFC-ML / investment & credit company)
# ---------------------------------------------------------------------------
N = dict(
    aum=[2610, 3080, 3790, 4700, 5780, 6920],  # closing gross loans (on-book)
    yield_=[0.171, 0.169, 0.167, 0.170, 0.172, 0.169],  # on avg gross loans
    cof=[0.093, 0.086, 0.084, 0.089, 0.091, 0.087],  # on avg borrowings
    fee_pct=[0.006, 0.007, 0.007, 0.008, 0.008, 0.008],  # of avg loans
    opex_pct=[0.044, 0.042, 0.041, 0.040, 0.039, 0.038],
    credit_cost=[0.036, 0.021, 0.014, 0.013, 0.016, 0.019],  # of avg loans
    gnpa_pct=[4.4, 3.6, 2.9, 2.5, 2.6, 2.9],
    pcr=[0.52, 0.55, 0.56, 0.57, 0.56, 0.55],  # stage-3 ECL / stage-3 loans
    stage12_ecl_pct=0.009,  # of stage 1+2 loans
    liquid=[310, 290, 360, 420, 480, 560],  # cash + liquid investments
    other_assets_pct=0.018,  # of gross loans
    other_liab_pct=0.025,
    tax_rate=0.2517,
    equity_raise=[0, 0, 0, 300, 0, 0],  # QIP in FY24
    dividend=[0, 10, 15, 20, 25, 30],
    shares=[10.0, 10.0, 10.0, 11.0, 11.0, 11.0],  # crore shares, Rs 10 FV
    rwa_density=0.95,
    tier2=[60, 60, 80, 80, 110, 140],
    price_mar=[140, 190, 215, 330, 420, 385],
    disbursement=[1540, 1980, 2460, 2950, 3480, 3990],
    cost_income_denominator="NII + fees",
)
N_OPEN = dict(aum=2480.0, borrowings=1960.0, equity=620.0, ecl=103.0, liquid=270.0)


def build_nirmal():
    rows = []
    prev_aum = N_OPEN["aum"]
    prev_eq = N_OPEN["equity"]
    prev_ecl = N_OPEN["ecl"]
    prev_borr = N_OPEN["borrowings"]
    for i, fy in enumerate(YEARS):
        aum = r1(N["aum"][i])
        avg_aum = (prev_aum + aum) / 2
        int_income = r1(avg_aum * N["yield_"][i])
        fees = r1(avg_aum * N["fee_pct"][i])
        opex = r1(avg_aum * N["opex_pct"][i])
        credit_cost = r1(avg_aum * N["credit_cost"][i])
        gnpa = r1(aum * N["gnpa_pct"][i] / 100)
        stage3_ecl = r1(gnpa * N["pcr"][i])
        stage12_ecl = r1((aum - gnpa) * N["stage12_ecl_pct"])
        ecl = r1(stage3_ecl + stage12_ecl)
        write_offs = r1(prev_ecl + credit_cost - ecl)
        nnpa = r1(gnpa - stage3_ecl)
        net_loans = r1(aum - ecl)
        liquid = r1(N["liquid"][i])
        other_assets = r1(aum * N["other_assets_pct"])
        other_liab = r1(aum * N["other_liab_pct"])
        # borrowings are the balancing item; interest on average borrowings creates a
        # circularity, solved by fixed-point iteration.
        borr = prev_borr
        for _ in range(50):
            int_exp = r1((prev_borr + borr) / 2 * N["cof"][i])
            nii = r1(int_income - int_exp)
            ppop = r1(nii + fees - opex)
            pbt = r1(ppop - credit_cost)
            tax = r1(pbt * N["tax_rate"])
            pat = r1(pbt - tax)
            equity = r1(prev_eq + pat + N["equity_raise"][i] - N["dividend"][i])
            new_borr = r1(net_loans + liquid + other_assets - other_liab - equity)
            if abs(new_borr - borr) < 0.01:
                break
            borr = new_borr
        borr = new_borr
        total_assets = r1(net_loans + liquid + other_assets)
        assert abs(total_assets - (borr + other_liab + equity)) < 0.05
        rwa = r1((net_loans + other_assets) * N["rwa_density"] + liquid * 0.2)
        tier1 = r1(equity)
        crar = (tier1 + N["tier2"][i]) / rwa
        avg_eq = (prev_eq + equity) / 2
        avg_assets = (total_assets + (prev_aum - prev_ecl + N_OPEN["liquid"] if i == 0 else rows[-1]["total_assets"])) / 2
        shares = N["shares"][i]
        rows.append(dict(
            fy=fy, aum=aum, disbursement=N["disbursement"][i], int_income=int_income, int_exp=int_exp, nii=nii,
            fees=fees, total_income_net=r1(nii + fees), opex=opex, ppop=ppop, credit_cost=credit_cost,
            pbt=pbt, tax=tax, pat=pat, gnpa=gnpa, stage3_ecl=stage3_ecl, stage12_ecl=stage12_ecl, ecl=ecl,
            write_offs=write_offs, nnpa=nnpa, net_loans=net_loans, liquid=liquid, other_assets=other_assets,
            total_assets=total_assets, borrowings=borr, other_liab=other_liab, equity=equity,
            equity_raise=N["equity_raise"][i], dividend=N["dividend"][i], rwa=rwa, tier2=N["tier2"][i],
            crar=crar, tier1_ratio=tier1 / rwa,
            yield_=int_income / avg_aum, cof=int_exp / ((prev_borr + borr) / 2),
            nim=nii / avg_aum, cost_income=opex / (nii + fees), credit_cost_pct=credit_cost / avg_aum,
            gnpa_pct=gnpa / aum, nnpa_pct=nnpa / net_loans, pcr=stage3_ecl / gnpa,
            roa=pat / avg_assets, roe=pat / avg_eq, leverage=total_assets / equity,
            shares=shares, eps=pat / shares, bvps=equity / shares,
            price=N["price_mar"][i], pb=N["price_mar"][i] / (equity / shares), pe=N["price_mar"][i] / (pat / shares),
        ))
        prev_aum, prev_eq, prev_ecl, prev_borr = aum, equity, ecl, borr
    return rows


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------
def fmt(v, kind="cr"):
    if v is None:
        return "–"
    if isinstance(v, (int, float)) and abs(v) < 0.05 and kind == "cr":
        return "0.0"
    if kind == "pct":
        return f"{v * 100:.1f}%"
    if kind == "x":
        return f"{v:.1f}x"
    if kind == "days":
        return f"{v:.0f}"
    if kind == "rs":
        return f"{v:,.1f}"
    if kind == "int":
        return f"{v:,.0f}"
    if isinstance(v, float) and v < 0:
        return f"({-v:,.1f})"
    return f"{v:,.1f}"


def table(rows, spec, years=YEARS, first="₹ Cr"):
    head = f"| {first} | " + " | ".join(years) + " |"
    sep = "|:--|" + "--:|" * len(years)
    lines = [head, sep]
    for label, key, kind in spec:
        if key is None:
            lines.append(f"| **{label}** |" + " |" * len(years))
            continue
        bold = label.startswith("**")
        cells = []
        for r in rows:
            v = r[key] if not callable(key) else key(r)
            s = fmt(v, kind)
            cells.append(f"**{s}**" if bold else s)
        lines.append(f"| {label} | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def write_csv(path, rows, keys):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["line_item"] + [r["fy"] for r in rows])
        for k in keys:
            w.writerow([k] + [round(r[k], 4) if r[k] is not None else "" for r in rows])


def main():
    kr = build_kaveri()
    kq = kaveri_ratios(kr)
    nr = build_nirmal()

    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    k_keys = ["rev", "mat", "emp", "sbc", "oth", "ebitda", "dep_ppe", "rou_amort", "int_amort", "da", "ebit",
              "other_income", "debt_int", "lease_int", "fin_cost", "exceptional", "pbt", "current_tax",
              "deferred_tax", "tax", "pat", "gross_block", "acc_dep", "net_block", "cwip", "rou", "intangibles",
              "inventory", "receivables", "oca", "cash", "cur_inv", "total_assets", "share_capital",
              "other_equity", "equity", "lt_debt", "st_debt", "lease_liab", "payables", "ocl", "dtl", "total_le",
              "op_before_wc", "d_inv", "d_rec", "d_oca", "d_pay", "d_ocl", "wc_change", "cfo", "capex_ppe",
              "capex_int", "d_cur_inv", "asset_sale", "cfi", "d_lt", "d_st", "lease_payment", "dividends",
              "cff", "net_cash"]
    write_csv(DATA / "kaveri_pumps_annual.csv", kr, k_keys)
    ratio_keys = [k for k in kq[0] if k != "fy"]
    write_csv(DATA / "kaveri_pumps_ratios.csv", kq, ratio_keys)
    n_keys = [k for k in nr[0] if k != "fy"]
    write_csv(DATA / "nirmal_finance_annual.csv", nr, n_keys)

    # quarterly split for FY26 plus Q1 FY27 (reported Aug-2026)
    fy26 = kr[-1]
    q_share = [0.270, 0.200, 0.220, 0.310]
    q_margin_raw = [0.142, 0.121, 0.130, 0.149]
    scale = fy26["ebitda"] / sum(fy26["rev"] * s * m for s, m in zip(q_share, q_margin_raw))
    quarters = []
    rev_acc = ebitda_acc = 0.0
    for qi, (s, m) in enumerate(zip(q_share, q_margin_raw)):
        if qi < 3:
            rev = r1(fy26["rev"] * s)
            ebitda = r1(rev * m * scale)
        else:
            rev = r1(fy26["rev"] - rev_acc)
            ebitda = r1(fy26["ebitda"] - ebitda_acc)
        rev_acc += rev
        ebitda_acc += ebitda
        quarters.append(dict(q=f"Q{qi + 1} FY26", rev=rev, ebitda=ebitda))
    # Q1 FY26 detail vs Q1 FY27
    q1_27 = dict(q="Q1 FY27", rev=368.2, ebitda=r1(368.2 * 0.126))
    quarters.append(q1_27)
    q1_27_below = dict(da=12.3, other_income=0.8, fin_cost=5.1)  # WC debt up, D&A flat
    for qi, q in enumerate(quarters):
        q["ebitda_margin"] = q["ebitda"] / q["rev"]
        for key in ("da", "other_income", "fin_cost"):
            if q["q"] == "Q1 FY27":
                q[key] = q1_27_below[key]
            elif qi < 3:
                q[key] = r1(fy26[key] / 4)
            else:  # Q4 absorbs rounding so the four quarters sum to the annual figure
                q[key] = r1(fy26[key] - sum(quarters[j][key] for j in range(3)))
        q["pbt"] = r1(q["ebitda"] - q["da"] + q["other_income"] - q["fin_cost"])
        if qi == 3:
            q["tax"] = r1(fy26["tax"] - sum(quarters[j]["tax"] for j in range(3)))
        else:
            q["tax"] = r1(q["pbt"] * K["tax_rate"])
        q["pat"] = r1(q["pbt"] - q["tax"])
        q["eps"] = q["pat"] / K["shares"]
    diff_pat = r1(fy26["pat"] - sum(q["pat"] for q in quarters[:4]))
    assert abs(diff_pat) < 0.05 and abs(sum(q["pbt"] for q in quarters[:4]) - fy26["pbt"]) < 0.05
    with open(DATA / "kaveri_pumps_quarterly.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        keys = ["rev", "ebitda", "ebitda_margin", "da", "other_income", "fin_cost", "pbt", "tax", "pat", "eps"]
        w.writerow(["line_item"] + [q["q"] for q in quarters])
        for k in keys:
            w.writerow([k] + [round(q[k], 4) for q in quarters])

    write_kaveri_md(kr, kq, quarters, diff_pat)
    write_nirmal_md(nr)
    print("OK - Kaveri balance sheet balances every year; Nirmal balances every year.")
    for y, q in zip(kr, kq):
        print(y["fy"], "rev", y["rev"], "ebitda", y["ebitda"], "pat", y["pat"], "cfo", y["cfo"], "cash", y["cash"],
              "TA", y["total_assets"], "ROE", f"{q['roe']:.1%}", "ROCE", f"{q['roce']:.1%}", "PE", f"{q['pe']:.1f}")
    for n in nr:
        print(n["fy"], "AUM", n["aum"], "NII", n["nii"], "PAT", n["pat"], "ROA", f"{n['roa']:.2%}", "ROE",
              f"{n['roe']:.1%}", "GNPA", f"{n['gnpa_pct']:.1%}", "CRAR", f"{n['crar']:.1%}", "PB", f"{n['pb']:.2f}")


def write_kaveri_md(kr, kq, quarters, diff_pat):
    pl = [
        ("Revenue from operations", "rev", "cr"),
        ("Cost of materials consumed (incl. change in inventories)", "mat", "cr"),
        ("Employee benefits expense", "emp", "cr"),
        ("&nbsp;&nbsp;*of which share-based payment (non-cash)*", "sbc", "cr"),
        ("Other expenses", "oth", "cr"),
        ("**EBITDA** (excl. other income)", "ebitda", "cr"),
        ("Depreciation – PP&E", "dep_ppe", "cr"),
        ("Amortisation – right-of-use (leases)", "rou_amort", "cr"),
        ("Amortisation – intangibles", "int_amort", "cr"),
        ("**EBIT** (excl. other income)", "ebit", "cr"),
        ("Other income (treasury)", "other_income", "cr"),
        ("Finance costs – borrowings", "debt_int", "cr"),
        ("Finance costs – lease interest", "lease_int", "cr"),
        ("Exceptional items: gain / (loss)", "exceptional", "cr"),
        ("**Profit before tax (PBT)**", "pbt", "cr"),
        ("Current tax", "current_tax", "cr"),
        ("Deferred tax", "deferred_tax", "cr"),
        ("**Profit after tax (PAT)**", "pat", "cr"),
    ]
    bs = [
        ("ASSETS", None, None),
        ("Gross block (PP&E, incl. land)", "gross_block", "cr"),
        ("Less: accumulated depreciation", "acc_dep", "cr"),
        ("Net block (PP&E)", "net_block", "cr"),
        ("Capital work-in-progress (CWIP)", "cwip", "cr"),
        ("Right-of-use assets", "rou", "cr"),
        ("Intangible assets (software, net)", "intangibles", "cr"),
        ("Inventories", "inventory", "cr"),
        ("Trade receivables", "receivables", "cr"),
        ("Other current assets", "oca", "cr"),
        ("Current investments (liquid mutual funds)", "cur_inv", "cr"),
        ("Cash & cash equivalents", "cash", "cr"),
        ("**Total assets**", "total_assets", "cr"),
        ("EQUITY & LIABILITIES", None, None),
        ("Equity share capital (6.0 Cr shares × ₹5)", "share_capital", "cr"),
        ("Other equity (reserves & surplus)", "other_equity", "cr"),
        ("**Total equity**", "equity", "cr"),
        ("Borrowings – non-current (term loans)", "lt_debt", "cr"),
        ("Borrowings – current (working-capital + current maturities)", "st_debt", "cr"),
        ("Lease liabilities", "lease_liab", "cr"),
        ("Trade payables", "payables", "cr"),
        ("Other current liabilities & provisions", "ocl", "cr"),
        ("Deferred tax liability (net)", "dtl", "cr"),
        ("**Total equity & liabilities**", "total_le", "cr"),
    ]
    cf = [
        ("Profit before tax", "pbt", "cr"),
        ("Add: depreciation & amortisation", "da", "cr"),
        ("Add: finance costs (shown in CFF)", "fin_cost", "cr"),
        ("Less: interest / treasury income (shown in CFI)", lambda r: -r["other_income"], "cr"),
        ("Less: gain on sale of land (shown in CFI)", lambda r: -(r["asset_sale"] - (4.0 if r["asset_sale"] else 0)), "cr"),
        ("Add: share-based payment expense (non-cash)", "sbc", "cr"),
        ("**Operating profit before working-capital changes**", "op_before_wc", "cr"),
        ("(Increase)/decrease in inventories", lambda r: -r["d_inv"], "cr"),
        ("(Increase)/decrease in trade receivables", lambda r: -r["d_rec"], "cr"),
        ("(Increase)/decrease in other current assets", lambda r: -r["d_oca"], "cr"),
        ("Increase/(decrease) in trade payables", "d_pay", "cr"),
        ("Increase/(decrease) in other current liabilities", "d_ocl", "cr"),
        ("Income taxes paid", lambda r: -r["current_tax"], "cr"),
        ("**Cash flow from operations (CFO)**", "cfo", "cr"),
        ("Purchase of PP&E incl. CWIP (capex)", lambda r: -r["capex_ppe"], "cr"),
        ("Purchase of intangibles", lambda r: -r["capex_int"], "cr"),
        ("Proceeds from sale of land", "asset_sale", "cr"),
        ("(Purchase)/sale of current investments (net)", lambda r: -r["d_cur_inv"], "cr"),
        ("Interest / treasury income received", "other_income", "cr"),
        ("**Cash flow from investing (CFI)**", "cfi", "cr"),
        ("Proceeds/(repayment) of term loans (net)", "d_lt", "cr"),
        ("Proceeds/(repayment) of working-capital loans (net)", "d_st", "cr"),
        ("Interest paid on borrowings", lambda r: -r["debt_int"], "cr"),
        ("Lease payments (principal + interest)", lambda r: -r["lease_payment"], "cr"),
        ("Dividends paid", lambda r: -r["dividends"], "cr"),
        ("**Cash flow from financing (CFF)**", "cff", "cr"),
        ("**Net change in cash**", "net_cash", "cr"),
        ("Closing cash & cash equivalents", "cash", "cr"),
    ]
    ratios = [
        ("Revenue growth", "rev_growth", "pct"),
        ("Gross margin", "gross_margin", "pct"),
        ("EBITDA margin", "ebitda_margin", "pct"),
        ("EBIT margin", "ebit_margin", "pct"),
        ("PAT margin", "pat_margin", "pct"),
        ("ROE (PAT / avg equity)", "roe", "pct"),
        ("ROCE ((EBIT + other income) / avg capital employed)", "roce", "pct"),
        ("ROIC (NOPAT / avg invested capital)", "roic", "pct"),
        ("Inventory days (on material cost)", "inv_days", "days"),
        ("Receivable days (on revenue)", "rec_days", "days"),
        ("Payable days (on material cost)", "pay_days", "days"),
        ("Cash conversion cycle (days)", "ccc", "days"),
        ("CFO / EBITDA", "cfo_to_ebitda", "pct"),
        ("CFO / PAT", "cfo_to_pat", "pct"),
        ("Free cash flow (CFO – capex), ₹ Cr", "fcf", "cr"),
        ("Net debt (debt – cash – liquid inv.), ₹ Cr", "net_debt", "cr"),
        ("Net debt / EBITDA", "nd_to_ebitda", "x"),
        ("Interest cover (EBIT / finance costs)", "int_cover", "x"),
        ("Debt / equity", "de", "x"),
        ("Asset turnover (revenue / total assets)", "asset_turnover", "x"),
        ("EPS (basic), ₹", "eps", "rs"),
        ("Adjusted EPS (ex-exceptional, post-tax), ₹", "adj_eps", "rs"),
        ("Book value per share, ₹", "bvps", "rs"),
        ("Dividend per share paid in year, ₹", "dps_paid", "rs"),
        ("Share price at 31-March, ₹", "price", "int"),
        ("P/E (trailing, on reported EPS)", "pe", "x"),
        ("P/B", "pb", "x"),
        ("EV/EBITDA (EV incl. lease liabilities)", "ev_ebitda", "x"),
    ]
    seg = []
    for i, y in enumerate(kr):
        solar = r1(y["rev"] * K["solar_share"][i])
        ind = r1(y["rev"] * K["industrial_share"][i])
        agri = r1(y["rev"] - solar - ind)
        seg.append(dict(fy=y["fy"], agri=agri, ind=ind, solar=solar, rpt=r1(y["mat"] * K["related_party_pct"][i]),
                        rpt_pct=K["related_party_pct"][i]))
    seg_tbl = table(seg, [
        ("Agricultural & domestic pumps", "agri", "cr"),
        ("Industrial pumps & motors", "ind", "cr"),
        ("Solar pumping systems (mostly govt. schemes)", "solar", "cr"),
        ("Purchases from Kaveri Castings Pvt Ltd (promoter-owned), ₹ Cr", "rpt", "cr"),
        ("…as % of material cost", "rpt_pct", "pct"),
    ])
    qt = "| ₹ Cr | " + " | ".join(q["q"] for q in quarters) + " |\n|:--|" + "--:|" * len(quarters) + "\n"
    q_lines = [("Revenue", "rev", "cr"), ("EBITDA", "ebitda", "cr"), ("EBITDA margin", "ebitda_margin", "pct"),
               ("Depreciation & amortisation", "da", "cr"), ("Other income", "other_income", "cr"),
               ("Finance costs", "fin_cost", "cr"), ("PBT", "pbt", "cr"), ("Tax", "tax", "cr"), ("PAT", "pat", "cr"),
               ("EPS (₹)", "eps", "rs")]
    for label, key, kind in q_lines:
        qt += f"| {label} | " + " | ".join(fmt(q[key], kind) for q in quarters) + " |\n"

    md = f"""# Running example 1 — Kaveri Pumps & Motors Ltd (fictional)

!!! warning "Fictional company"
    Kaveri Pumps & Motors Ltd ("KPML", NSE: *KAVERIPMP* — not a real ticker) is **invented** for this course.
    Its numbers are generated by `tools/running_example/generate.py`, which enforces that the balance sheet
    balances every year and that the cash-flow statement reconciles exactly to the change in cash.
    Any lesson, exercise or mock that uses KPML must use **these** numbers. Amounts are in **₹ crore**
    (1 crore = 10 million) unless stated. Financial year FY26 = 1-Apr-2025 to 31-Mar-2026.

## 1. Company profile

| Item | Detail |
|:--|:--|
| Business | Designs and manufactures agricultural submersible & monoblock pumps, domestic pumps, industrial pumps and electric motors; since FY23 a fast-growing **solar pumping systems** business sold mainly into state-government tenders under the PM-KUSUM scheme |
| Headquarters / plants | Coimbatore, Tamil Nadu (India's pump manufacturing cluster). Plant 1 (Coimbatore, 1996), Plant 2 (Hosur, motors — commissioned end-FY24 at a cost of ~₹190 Cr) |
| Distribution | ~1,800 dealers across 14 states; top-3 states = 52% of agri sales. Solar: direct to state nodal agencies/DISCOMs |
| Promoters | The Raghunathan family, **58.4%** holding. From Q3 FY26, **6% of promoter shares are pledged** (disclosed under SEBI SAST) |
| Other holders (Mar-26) | Mutual funds 14.2%, FPIs 7.9%, insurance 2.1%, retail & others 17.4% |
| Share data | 6.00 crore shares of ₹5 face value; ESOPs granted FY24 (diluted share count FY26: 6.07 Cr) |
| Share price | Peak ₹812 (Jan-2025); ₹520 at 31-Mar-2026; **₹{K['cmp']} on 18-Sep-2026** after falling ~25% since March on the Q1 FY27 miss and the promoter-pledge disclosure (market cap ≈ ₹{K['cmp'] * K['shares']:,.0f} Cr); beta vs Nifty 500 ≈ 1.05 |
| Auditor | Mid-sized Chennai firm; rotated in FY25 (mandatory rotation under the Companies Act, 2013) |
| Credit rating | Long-term bank facilities: "A / Stable" (FY26) |

## 2. Income statement (consolidated, ₹ Cr)

{table(kr, pl)}

Notes: Tax rate is 25.17% throughout (new corporate regime, Sec. 115BAA, 22% + surcharge + cess).
FY21 exceptional item = ₹7.5 Cr **cash** VRS cost on closing an old foundry line. FY25 exceptional item =
₹14.0 Cr **gain** on sale of a land parcel (book value ₹4.0 Cr, proceeds ₹18.0 Cr) — a one-off that flatters FY25 PAT.
Other income is entirely treasury income on cash and liquid funds.

## 3. Balance sheet (as at 31-March, ₹ Cr)

Opening balance sheet at 31-Mar-2020: gross block 430.0 (of which land 22.0), accumulated depreciation 165.0,
CWIP 8.0, right-of-use 12.0, intangibles 6.0, inventories 86.0, receivables 96.0, other current assets 19.0,
cash 34.0, current investments 40.0; share capital 30.0, other equity {OPEN['other_equity']:.1f}, non-current
borrowings 35.0, current borrowings 30.0, lease liabilities 13.0, payables 68.0, other current liabilities 32.0,
DTL 14.0. Total assets = 566.0.

{table(kr, bs)}

## 4. Cash-flow statement (indirect method, ₹ Cr)

Presentation choices (both permitted under Ind AS 7 for a non-financial company, and common in India):
interest **paid** is classified in financing; interest/treasury income **received** is classified in investing.

{table(kr, cf)}

## 5. Segment revenue and related-party purchases (₹ Cr)

{seg_tbl}

## 6. Key ratios (computed by the generator — use these values)

Definitions: averages use opening and closing balance sheets. Capital employed = equity + all borrowings + lease
liabilities. Invested capital = net block + CWIP + right-of-use + intangibles + (inventories + receivables + other
current assets − payables − other current liabilities). NOPAT = EBIT × (1 − 25.17%). Market data is fictional.

{table(kq, ratios, first="Ratio")}

## 7. Quarterly results (₹ Cr) — FY26 by quarter and Q1 FY27 (reported 8-Aug-2026)

{qt}
FY26 quarterly revenue, EBITDA, PBT and PAT sum exactly to the annual figures. Seasonality: Q4 (Jan–Mar) and Q1 (Apr–Jun) are peak pump seasons ahead of summer
irrigation demand.

**Q1 FY27 (Apr–Jun 2026) headline:** revenue +{(368.2 / quarters[0]['rev'] - 1) * 100:.1f}% YoY (vs. management's
FY27 guidance of 15–18% growth), EBITDA margin 12.6% (vs. 14.0–15.0% guided), PAT {(quarters[4]['pat'] / quarters[0]['pat'] - 1) * 100:+.1f}% YoY.
Finance costs rose as working-capital borrowings increased. Management blamed "delayed tender
finalisation in two states" for the solar segment and said receivables from state agencies "remain elevated but
fully recoverable". Days receivable at 30-Jun-2026 were not disclosed in the results; the investor presentation
showed a bar chart without numbers.

## 8. Notes-to-accounts items (FY26 annual report)

| Item | FY25 | FY26 | Comment |
|:--|--:|--:|:--|
| Receivables overdue > 6 months, ₹ Cr | 31.0 | 62.4 | Mostly from two state nodal agencies (solar) |
| Expected credit loss allowance on receivables, ₹ Cr | 3.1 | 4.0 | Allowance only ~6% of the >6-month bucket |
| Contingent liability — GST demand under appeal, ₹ Cr | 0.0 | 38.0 | Classification dispute on solar systems (5% vs 12%/18% GST rate) |
| Contingent liability — income-tax disputes, ₹ Cr | 9.0 | 11.0 | Old assessment years |
| Bank guarantees given (performance / tender), ₹ Cr | 58.0 | 96.0 | Grows with solar tender wins |
| Promoter shares pledged (% of promoter holding) | 0% | 6% | Pledge created Nov-2025 for a promoter-group real-estate venture |
| Related-party purchases (Kaveri Castings), % of material cost | 9.1% | 10.4% | Pricing stated to be "at arm's length"; approved by audit committee |
| Order book — solar (unexecuted), ₹ Cr | 290 | 410 | State tenders, typically executed in 6–12 months |
| Employees (nos.) | 2,310 | 2,480 | |
| Installed capacity — pumps (lakh units p.a.) / utilisation | 9.0 / 71% | 9.0 / 78% | |
| Installed capacity — motors (lakh units p.a.) / utilisation | 3.5 / 48% | 3.5 / 57% | Hosur plant ramping up |

## 9. Management guidance and narrative (from FY26 Q4 earnings call, May-2026 — fictional)

- FY27 revenue growth guided at **15–18%**; EBITDA margin **14–15%**; capex ₹45–50 Cr (maintenance + automation).
- "Solar is a multi-year opportunity; we are being selective on states with good payment track records."
- Working capital: "We expect receivable days to normalise towards 75–80 by end-FY27 as two large state dues clear."
- Capital allocation: dividend payout ~25%; no large capex planned; "open to acquisitions in the motors space".

## 10. Fictional peer set (for relative valuation exercises; market data as of 18-Sep-2026)

| Company (fictional) | Mcap ₹ Cr | Revenue FY26 | EBITDA margin | PAT FY26 | ROCE | Rev CAGR FY23–26 | Net debt/EBITDA | P/E | EV/EBITDA |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nilgiri Pumps Ltd | 6,850 | 1,640 | 16.8% | 172 | 24% | 13% | −0.4x | 39.8x | 24.5x |
| Deccan Flow Systems Ltd | 2,100 | 980 | 11.5% | 58 | 14% | 9% | 1.2x | 36.2x | 20.1x |
| Sabarmati Motors & Drives Ltd | 3,900 | 1,210 | 15.2% | 118 | 21% | 17% | 0.1x | 33.1x | 21.4x |
| Konkan Solar Pumps Ltd | 1,450 | 720 | 12.1% | 49 | 18% | 38% | 0.9x | 29.6x | 17.8x |
| **Kaveri Pumps & Motors (at ₹{K['cmp']})** | **{K['cmp'] * K['shares']:,.0f}** | **1,318** | **13.8%** | **{kr[-1]['pat']:.1f}** | **{kq[-1]['roce'] * 100:.0f}%** | **{((1318 / 874) ** (1 / 3) - 1) * 100:.0f}%** | **{kq[-1]['nd_to_ebitda']:.1f}x** | **{K['cmp'] / kq[-1]['eps']:.1f}x** | **{(K['cmp'] * K['shares'] + kq[-1]['net_debt'] + kr[-1]['lease_liab']) / kr[-1]['ebitda']:.1f}x** |

Raw CSVs: `tools/data/kaveri_pumps_annual.csv`, `tools/data/kaveri_pumps_ratios.csv`, `tools/data/kaveri_pumps_quarterly.csv`.
"""
    (DOCS / "kaveri-pumps.md").write_text(md, encoding="utf-8")


def write_nirmal_md(nr):
    pl = [
        ("Interest income", "int_income", "cr"),
        ("Interest expense (finance costs)", "int_exp", "cr"),
        ("**Net interest income (NII)**", "nii", "cr"),
        ("Fee & other operating income", "fees", "cr"),
        ("**Net total income**", "total_income_net", "cr"),
        ("Operating expenses (employee + other + depreciation)", "opex", "cr"),
        ("**Pre-provision operating profit (PPOP)**", "ppop", "cr"),
        ("Impairment on financial instruments (credit cost)", "credit_cost", "cr"),
        ("**Profit before tax**", "pbt", "cr"),
        ("Tax", "tax", "cr"),
        ("**Profit after tax**", "pat", "cr"),
    ]
    bs = [
        ("Gross loans (AUM, all on-book)", "aum", "cr"),
        ("Less: ECL allowance (stage 1+2+3)", "ecl", "cr"),
        ("Net loans", "net_loans", "cr"),
        ("Cash, bank & liquid investments", "liquid", "cr"),
        ("Other assets", "other_assets", "cr"),
        ("**Total assets**", "total_assets", "cr"),
        ("Borrowings (NCDs, bank loans, CPs, securitisation)", "borrowings", "cr"),
        ("Other liabilities & provisions", "other_liab", "cr"),
        ("Net worth (equity)", "equity", "cr"),
        ("&nbsp;&nbsp;*of which fresh equity raised in the year (QIP)*", "equity_raise", "cr"),
        ("Dividends paid in the year", "dividend", "cr"),
    ]
    asset_q = [
        ("Disbursements", "disbursement", "cr"),
        ("Gross stage-3 loans (GNPA)", "gnpa", "cr"),
        ("Stage-3 ECL", "stage3_ecl", "cr"),
        ("Stage 1+2 ECL", "stage12_ecl", "cr"),
        ("Net stage-3 (NNPA)", "nnpa", "cr"),
        ("Write-offs (derived)", "write_offs", "cr"),
        ("Risk-weighted assets", "rwa", "cr"),
        ("Tier-2 capital (sub-debt)", "tier2", "cr"),
    ]
    ratios = [
        ("Yield on avg loans", "yield_", "pct"),
        ("Cost of funds (on avg borrowings)", "cof", "pct"),
        ("NIM (NII / avg loans)", "nim", "pct"),
        ("Cost-to-income (opex / net total income)", "cost_income", "pct"),
        ("Credit cost (on avg loans)", "credit_cost_pct", "pct"),
        ("GNPA %", "gnpa_pct", "pct"),
        ("NNPA % (on net loans)", "nnpa_pct", "pct"),
        ("Provision coverage (stage-3 ECL / GNPA)", "pcr", "pct"),
        ("RoA (PAT / avg total assets)", "roa", "pct"),
        ("RoE (PAT / avg equity)", "roe", "pct"),
        ("Leverage (total assets / equity)", "leverage", "x"),
        ("CRAR", "crar", "pct"),
        ("Tier-1 ratio", "tier1_ratio", "pct"),
        ("Shares outstanding (crore)", "shares", "rs"),
        ("EPS, ₹", "eps", "rs"),
        ("Book value per share, ₹", "bvps", "rs"),
        ("Share price at 31-March, ₹", "price", "int"),
        ("P/E", "pe", "x"),
        ("P/B", "pb", "x"),
    ]
    md = f"""# Running example 2 — Nirmal Finance Ltd (fictional NBFC)

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

{table(nr, pl)}

## 3. Balance sheet (as at 31-March, ₹ Cr)

Opening (31-Mar-2020): gross loans 2,480.0; ECL 103.0; liquid assets 270.0; borrowings 1,960.0; equity 620.0.

{table(nr, bs)}

## 4. Asset quality & capital (₹ Cr)

{table(nr, asset_q)}

## 5. Key ratios

{table(nr, ratios, first="Ratio")}

Note: yields, cost of funds, NIM and credit cost are on **average** balances. RWA are simplified
(loans at 95% risk weight, liquid assets at 20%). FY21 credit cost reflects COVID-19 stress and the
RBI moratorium; FY25–26 show a mild uptick in stage-3 in the used-CV book.
"""
    (DOCS / "nirmal-finance.md").write_text(md, encoding="utf-8")


if __name__ == "__main__":
    main()
