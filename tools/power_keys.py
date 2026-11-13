"""Regional keys for the existing power and CHP capacity classes of FINTIMES.

Input : data/keys/power_plants_<tag>.csv (sited registers, tools/power_register.py)
        data/keys/population_2024.csv   (rooftop PV residual)
Output: data/keys/power_<CLASS>.csv  (19 shares, exact sum 1) and audit/power_keys.md

Mapping model class -> register selection (electrical capacity 'Maximum, total, MW'):
  * renewables and nuclear: register of 22.5.2026 (today's fleet)
  * fossil and peat classes: register of 8.11.2019 (Open Power System Data copy) - closer to the
    2010-2020 fleet whose vintages carry most of that capacity; flagged as the weaker basis
  * unsited plants are left out of the shares (= spread like the sited plants of the class);
    their MW share is reported per class
"""
import csv
import datetime
import os
import sys
from collections import defaultdict
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from regional_keys import REGIONS  # noqa: E402

ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
KEYS = os.path.join(ROOT, "data", "keys")

COAL = {"Hard coal and anthracite"}
PEAT = {"Peat"}
GAS = {"Natural gas"}
BIO = {"Forest fuelwood", "Industrial wood residues", "Biogas", "By-products from wood processing industry",
       "Wood pellets and briquettes"}
HFO = {"Heavy distillates"}
LFO = {"Light distillates", "Medium heavy distillates"}
WASTE = {"Gasified waste", "Other by-products and wastes used as fuel", "Mixed fuels"}
DH, IND, SEP = "District heating CHP", "Industry CHP", "Separate electricity production"
OFFSHORE = ("tahkoluoto t1", "tahkoluoto offshore", "ajos")

# class -> (register tag, selector, fallback class, note)
CLASSES = {
    "EUHYDDAM00": ("20260522", lambda p: p["type"] == "Hydro power", None, "hydro power plants"),
    "EEPP_windON": ("20260522", lambda p: p["type"] == "Wind power" and not offshore(p), None, "onshore wind"),
    "EEPP_windOFF": ("20260522", lambda p: p["type"] == "Wind power" and offshore(p), None,
                     "offshore wind: Tahkoluoto (Pori) and Ajos (Kemi)"),
    "EEPP_PV": ("20260522", lambda p: p["type"] == "Solar", None,
                "registered solar parks + rooftop residual by population (see build_pv)"),
    "ECHP_coal_thermal": ("20191108", lambda p: p["type"] == DH and p["fuel"] in COAL, None, "DH CHP, coal"),
    "ECHP_lignite_thermal": ("20191108", lambda p: p["type"] == DH and p["fuel"] in PEAT, None, "DH CHP, peat"),
    "ECHP_biomass_thermal": ("20260522", lambda p: p["type"] == DH and p["fuel"] in BIO, None, "DH CHP, biomass"),
    "ECHP_naturalgas": ("20191108", lambda p: p["type"] == DH and p["fuel"] in GAS, None,
                        "DH CHP, natural gas (CCGT, OCGT and steam classes alike)"),
    "ECHP_HFO_thermal": ("20191108", lambda p: p["type"] == DH and p["fuel"] in HFO | LFO, "ECHP_all",
                         "DH CHP, oil (fallback: all DH CHP)"),
    "ECHP_LFO_thermal": ("20191108", lambda p: p["type"] == DH and p["fuel"] in HFO | LFO, "ECHP_all",
                         "DH CHP, oil (fallback: all DH CHP)"),
    "ECHP_all": ("20191108", lambda p: p["type"] == DH, None, "all DH CHP"),
    "EEPP_coal_thermal": ("20191108", lambda p: p["type"] == SEP and p["fuel"] in COAL, None, "condensing, coal"),
    "EEPP_lignite_thermal": ("20191108", lambda p: p["type"] == SEP and p["fuel"] in PEAT, None, "condensing, peat"),
    "EEPP_naturalgas": ("20191108", lambda p: p["type"] == SEP and p["fuel"] in GAS, "EEPP_all",
                        "separate production, natural gas (fallback: all separate production)"),
    "EEPP_HFO_thermal": ("20191108", lambda p: p["type"] == SEP and p["fuel"] in HFO, "EEPP_oil",
                         "separate production, heavy oil"),
    "EEPP_LFO_thermal": ("20191108", lambda p: p["type"] == SEP and p["fuel"] in LFO, None,
                         "separate production, light/medium oil (reserve plants)"),
    "EEPP_oil": ("20191108", lambda p: p["type"] == SEP and p["fuel"] in HFO | LFO, None, "separate production, oil"),
    "EEPP_biomass_thermal": ("20191108", lambda p: p["type"] in (SEP, DH) and p["fuel"] in BIO, None,
                             "biomass power (separate + DH CHP)"),
    "EEPP_all": ("20191108", lambda p: p["type"] == SEP, None, "all separate production"),
    "CHPAUTOGENBIO00": ("20260522", lambda p: p["type"] == IND and p["fuel"] in BIO, None, "industry CHP, wood"),
    "CHPAUTOGENBLQ00": ("20260522", lambda p: p["type"] == IND and "liquor" in p["fuel"].lower(), None,
                        "industry CHP, black liquor (pulp mills)"),
    "CHPAUTOGENGAS00": ("20191108", lambda p: p["type"] == IND and p["fuel"] in {"Blast furnace gas"} | GAS, None,
                        "industry CHP, process and natural gas"),
    "CHPAUTOGENSOLID00": ("20191108", lambda p: p["type"] == IND and p["fuel"] in COAL | PEAT, None,
                          "industry CHP, peat and coal"),
    "CHPAUTOGENWASTE00": ("20260522", lambda p: p["type"] == IND and p["fuel"] in WASTE, "CHPAUTOGEN_all",
                          "industry CHP, waste"),
    "CHPAUTOGENOIL00": ("20191108", lambda p: p["type"] == IND and p["fuel"] in HFO | LFO, "CHPAUTOGEN_all",
                        "industry CHP, oil"),
    "CHPAUTOGEN_all": ("20260522", lambda p: p["type"] == IND, None, "all industry CHP"),
}


def offshore(p):
    s = (p["name"] + " " + p["site"]).lower()
    return any(k in s for k in OFFSHORE)


def load(tag):
    rows = list(csv.DictReader(open(os.path.join(KEYS, f"power_plants_{tag}.csv"), encoding="utf-8")))
    for r in rows:
        for k in ("mw", "mw_sep", "mw_ind", "mw_dh"):
            r[k] = float(r[k] or 0)
    return rows


def population():
    return {r["region"]: float(r["value"]) for r in csv.DictReader(open(os.path.join(KEYS, "population_2024.csv"),
                                                                         encoding="utf-8")) if r["region"] in REGIONS}


def build(cls, regs):
    tag, sel, fb, note = CLASSES[cls]
    plants = [p for p in regs[tag] if sel(p)]
    sited = defaultdict(float)
    unsited = 0.0
    for p in plants:
        if p["region"] in REGIONS:
            sited[p["region"]] += p["mw"]
        else:
            unsited += p["mw"]
    total = sum(sited.values())
    if total <= 0:
        if fb:
            s, info = build(fb, regs)
            info.update(note=f"{note}; no sited plant -> {fb}", fallback=fb)
            return s, info
        return None, dict(note=note + "; no plant in the register", tag=tag)
    shares = {r: Fraction(sited.get(r, 0)).limit_denominator(10**9) for r in REGIONS}
    tot = sum(shares.values())
    shares = {r: v / tot for r, v in shares.items()}
    assert sum(shares.values()) == 1
    return shares, dict(note=note, tag=tag, plants=len(plants), mw=total + unsited, unsited=unsited, fallback=None)


def build_pv(regs, model_pv_gw):
    """Registered solar parks at their sites + the rest of the model's PV (rooftop) by population."""
    parks = defaultdict(float)
    for p in regs["20260522"]:
        if p["type"] == "Solar" and p["region"] in REGIONS:
            parks[p["region"]] += p["mw"] / 1000.0
    pop = population()
    rest = max(model_pv_gw - sum(parks.values()), 0.0)
    val = {r: parks.get(r, 0) + rest * pop[r] / sum(pop.values()) for r in REGIONS}
    shares = {r: Fraction(v).limit_denominator(10**9) for r, v in val.items()}
    tot = sum(shares.values())
    return {r: v / tot for r, v in shares.items()}, dict(
        note=f"solar parks {sum(parks.values()):.3f} GW at sites + {rest:.3f} GW rooftop by population 2024",
        tag="20260522", plants=None, mw=None, unsited=0, fallback=None)


def main():
    regs = {t: load(t) for t in ("20260522", "20191108")}
    out, infos = {}, {}
    for cls in CLASSES:
        if cls == "EEPP_PV":
            s, info = build_pv(regs, model_pv_gw=2.2)
        else:
            s, info = build(cls, regs)
        if s is None:
            print(f"{cls:22s} NO KEY ({info['note']})")
            continue
        out[cls], infos[cls] = s, info
        path = os.path.join(KEYS, f"power_{cls}.csv")
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["region", "name", "share"])
            for r in REGIONS:
                w.writerow([r, REGIONS[r], f"{float(s[r]):.12f}"])
            w.writerow(["TOTAL", "sum of regions", f"{float(sum(s.values())):.12f}"])
        top = sorted(s.items(), key=lambda x: -x[1])[:3]
        uns = f"unsited {info['unsited']:.0f}/{info['mw']:.0f} MW" if info.get("mw") else ""
        print(f"{cls:22s} {info['tag']}  {', '.join(f'{r} {float(v):.0%}' for r, v in top):40s} {uns}")
    lines = ["# Power keys (existing capacity classes)", "",
             f"Generated by `tools/power_keys.py` on {datetime.date.today().isoformat()} from the sited Energy "
             "Authority registers (`data/keys/power_plants_*.csv`, `tools/power_register.py`). Each key is the "
             "class's electrical capacity by region; the 19 shares sum to exactly 1 (rational arithmetic). "
             "Unsited plants are left out (= spread like the sited plants of the class).", "",
             "| Class | Register | Basis | Plants | MW | Unsited MW | " + " | ".join(REGIONS) + " |",
             "|---|---|---|---|---|---|" + "---|" * len(REGIONS)]
    for cls, s in out.items():
        i = infos[cls]
        lines.append(f"| {cls} | {i['tag']} | {i['note']} | {i.get('plants') or ''} | "
                     f"{i['mw']:.0f} | {i['unsited']:.0f} | " if i.get("mw") else
                     f"| {cls} | {i['tag']} | {i['note']} | | | | ")
        lines[-1] += " | ".join(f"{float(s[r]):.3f}" for r in REGIONS) + " |"
    open(os.path.join(ROOT, "audit", "power_keys.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("wrote audit/power_keys.md")


if __name__ == "__main__":
    main()
