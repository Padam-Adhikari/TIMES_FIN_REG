"""Regional keys for industry sectors from the EU ETS register (data/sources/eutl_FI_industry.csv,
built by tools/industry_register.py). Read-only: writes data/keys/ind_*.csv and audit/industry_keys.md.

Key value per installation = free allocation summed over 2013-2020 (EU ETS phase 3). Phase-3 free
allocation = EU product benchmark x historical activity level (production) of the installation, so
within one sector it is proportional to production; it also covers pulp and paper, whose verified
emissions are mostly biogenic and therefore not reported. Installations that entered the EU ETS in
2021 (hydrogen plants) use their 2021-2024 allocation (same benchmark logic, phase 4) in keys of their
own. (Hydrogen / chlor-alkali by-product plants have no allocation in the register, so no key: the
small chlor-alkali sector ICL stays on the hub for now.) Every key: 19 regions, shares >= 0, exact sum 1 (rational arithmetic), regional total = sum of
the sector's installations.

    python tools/industry_keys.py
"""
import csv
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from regional_keys import REGIONS, ROOT  # noqa: E402

SRC = os.path.join(ROOT, "data", "sources", "eutl_FI_industry.csv")
OUT = os.path.join(ROOT, "data", "keys")
AUDIT = os.path.join(ROOT, "audit", "industry_keys.md")
P3 = range(2013, 2021)
P4 = range(2021, 2025)


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def sector(r):
    n, a, nm = r["nace"] or "", r["activity"], r["name"].lower()
    if n.startswith("17") or "pulp" in a.lower() or "paper" in a.lower():
        return "ipp"
    if n.startswith("19") or "Refining" in a:
        return "refinery"
    if n.startswith("24.1") or "pig iron" in a:
        return "iis"
    if n.startswith("24.44"):
        return "icu"
    if n.startswith("24.4") or "non-ferrous" in a or "ore roast" in a:
        return "inf"
    if n.startswith("23.51"):
        return "icm"
    if n.startswith("23.52") or "lime" in a.lower():
        return "ilm"
    if n in ("23.13", "23.19"):
        return "igh"
    if n.startswith("23") or "gypsum" in a or "ceramic" in a.lower() or "mineral wool" in a:
        return "inm"
    if n.startswith("20.15") or "nitric" in a:
        return "iam"
    if "hydrogen" in a.lower():
        return "h2"
    if n.startswith("20") or "chemical" in a.lower():
        return "ich"
    return "ioi"


# key name -> (sector filter, period, description)
KEYS = {
    "ind_ipp": (lambda r: r["sector"] == "ipp", P3, "pulp and paper (all IPP processes, IPP heat plant, black-liquor CHP)"),
    "ind_iis": (lambda r: r["sector"] == "iis", P3, "iron and steel sites (finishing IISFINPRO00)"),
    "ind_iis_eaf": (lambda r: r["sector"] == "iis" and r["region"] in ("FI1D7", "FI1C5"), P3,
                    "electric-arc furnaces: Outokumpu Tornio and Ovako Imatra"),
    "ind_ilm": (lambda r: r["sector"] == "ilm", P3, "lime kilns"),
    "ind_icm": (lambda r: r["sector"] == "icm", P3, "cement clinker (generic cement processes; site processes go to their plant)"),
    "ind_ich": (lambda r: r["sector"] == "ich", P3, "chemicals (bulk/organic/inorganic, excl. fertiliser and hydrogen)"),
    "ind_iam": (lambda r: r["sector"] == "iam", P3, "fertiliser / nitric acid (ammonia processes)"),
    "ind_inm": (lambda r: r["sector"] == "inm", P3, "other non-metallic minerals (glass fibre, mineral wool, bricks, gypsum, LECA)"),
    "ind_ioi": (lambda r: r["sector"] == "ioi", P3, "other industries in the ETS (food, wood products, ...)"),
}


def main():
    rows = list(csv.DictReader(open(SRC, encoding="utf-8")))
    for r in rows:
        r["sector"] = sector(r)
    os.makedirs(OUT, exist_ok=True)
    L = ["# Industry keys (EU ETS free allocation)", "",
         "Built by `tools/industry_keys.py` from `data/sources/eutl_FI_industry.csv` (`tools/industry_register.py`: "
         "EUTL via the open EUETS.INFO API, sites placed by coordinates in the official maakunta polygons, "
         "three geocoding errors corrected by hand with reasons in the tool).", "",
         "Key value = free allocation of the installation summed over the period (phase 3 2013-2020 = EU product "
         "benchmark x historical production). Each key: 19 shares >= 0 summing to exactly 1 (rational arithmetic).", ""]
    for name, (filt, period, desc) in KEYS.items():
        sel = [r for r in rows if filt(r)]
        vals = {reg: Fraction(0) for reg in REGIONS}
        for r in sel:
            vals[r["region"]] += Fraction(str(sum(num(r[f"alloc{y}"]) for y in period)))
        total = sum(vals.values())
        if total == 0:
            sys.exit(f"{name}: zero total")
        shares = {k: v / total for k, v in vals.items()}
        assert sum(shares.values()) == 1 and all(s >= 0 for s in shares.values())
        tag = f"{period.start}-{period.stop - 1}"
        path = os.path.join(OUT, f"{name}_{tag}.csv")
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["region", "name", "value", "share"])
            for reg in REGIONS:
                w.writerow([reg, REGIONS[reg], float(vals[reg]), f"{float(shares[reg]):.12f}"])
            w.writerow(["TOTAL", "sum of regions", float(total), f"{float(sum(shares.values())):.12f}"])
        L += [f"## {name} ({tag}): {desc}", "",
              f"- File `data/keys/{name}_{tag}.csv`; {len(sel)} installations; total {float(total):,.0f} allowances; "
              f"sum of shares = {sum(shares.values())} (exact)", "",
              "| Region | Share | Installations (allocation) |", "|---|---|---|"]
        for reg in sorted(REGIONS, key=lambda k: -shares[k]):
            if shares[reg] > 0:
                inst = "; ".join(f"{r['name']} ({sum(num(r[f'alloc{y}']) for y in period):,.0f})"
                                 for r in sel if r["region"] == reg)
                L.append(f"| {reg} {REGIONS[reg]} | {float(shares[reg]):.4%} | {inst} |")
        L.append("")
        print(f"{name}: {len(sel)} installations, " + ", ".join(f"{k}:{float(v):.1%}" for k, v in
                                                               sorted(shares.items(), key=lambda t: -t[1]) if v > 0))
    open(AUDIT, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("written", AUDIT)


if __name__ == "__main__":
    main()
