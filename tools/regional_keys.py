"""Build regional keys (shares of a national quantity by NUTS-3 region) from public data.

Every key is fetched from its source API, mapped to the model's NUTS-3 codes, checked
(19 regions, no gaps, shares >= 0, sum = 1 exactly after normalisation) and written to
    data/keys/<key>.csv          region, value, share   (one file per key and year)
    audit/keys.md                source, table, query, date fetched, values, checks
The CSVs are plain text so every change is visible in git. Nothing in the model is
written here; tools/<task>.py scripts read these files.

Usage:
    python tools/regional_keys.py            # build every key
    python tools/regional_keys.py --key population
"""
import argparse
import csv
import datetime
import json
import os
import sys
import unicodedata
import urllib.request
from fractions import Fraction

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
OUT = os.path.join(ROOT, "data", "keys")

# Model regions (SysSettings / Region_selection) and their maakunta names (Finnish).
REGIONS = {
    "FI1B1": "Uusimaa", "FI1C1": "Varsinais-Suomi", "FI196": "Satakunta", "FI1C2": "Kanta-Häme",
    "FI19B": "Pirkanmaa", "FI1C6": "Päijät-Häme", "FI1C7": "Kymenlaakso", "FI1C5": "Etelä-Karjala",
    "FI1DA": "Etelä-Savo", "FI1DB": "Pohjois-Savo", "FI1DC": "Pohjois-Karjala", "FI198": "Keski-Suomi",
    "FI199": "Etelä-Pohjanmaa", "FI19A": "Pohjanmaa", "FI1D5": "Keski-Pohjanmaa",
    "FI1D9": "Pohjois-Pohjanmaa", "FI1D8": "Kainuu", "FI1D7": "Lappi", "FI200": "Ahvenanmaa",
}
# Statistics Finland maakunta codes (MKxx) -> NUTS-3 (2024 classification used by the model)
MK_TO_NUTS = {
    "MK01": "FI1B1", "MK02": "FI1C1", "MK04": "FI196", "MK05": "FI1C2", "MK06": "FI19B",
    "MK07": "FI1C6", "MK08": "FI1C7", "MK09": "FI1C5", "MK10": "FI1DA", "MK11": "FI1DB",
    "MK12": "FI1DC", "MK13": "FI198", "MK14": "FI199", "MK15": "FI19A", "MK16": "FI1D5",
    "MK17": "FI1D9", "MK18": "FI1D8", "MK19": "FI1D7", "MK21": "FI200",
}
PXWEB = "https://pxdata.stat.fi/PxWeb/api/v1/en/StatFin"


def _norm(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower().replace(" ", "")


def pxweb(table, selection):
    """POST a PxWeb json-stat2 query; return (metadata, response)."""
    url = f"{PXWEB}/{table}"
    meta = json.load(urllib.request.urlopen(url, timeout=60))
    q = {"query": [{"code": c, "selection": {"filter": "item", "values": v}} for c, v in selection.items()],
         "response": {"format": "json-stat2"}}
    req = urllib.request.Request(url, data=json.dumps(q).encode(), headers={"Content-Type": "application/json"})
    return meta, json.load(urllib.request.urlopen(req, timeout=120))


def check_and_share(values, name):
    """values: {nuts: number}. Returns {nuts: share} with an exact sum check."""
    missing = set(REGIONS) - set(values)
    if missing:
        sys.exit(f"{name}: missing regions {sorted(missing)}")
    if any(v < 0 for v in values.values()):
        sys.exit(f"{name}: negative values")
    total = sum(values.values())
    shares = {r: values[r] / total for r in REGIONS}
    exact = sum(Fraction(values[r]) / Fraction(total) for r in REGIONS)
    assert exact == 1, f"{name}: shares do not sum to 1"
    return shares, total


def write_key(name, year, values, shares, total, national, source, tol=0.0, why=""):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"{name}_{year}.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["region", "name", "value", "share"])
        for r in REGIONS:
            w.writerow([r, REGIONS[r], values[r], f"{shares[r]:.12f}"])
        w.writerow(["TOTAL", "sum of regions", total, f"{sum(shares.values()):.12f}"])
    if national is None or abs(total - national) <= 1e-9 * max(1, national):
        check = "OK"
    elif abs(total - national) <= tol * national:
        check = f"OK within {abs(total - national) / national:.3%} of the national total ({why})"
    else:
        check = f"MISMATCH (regions {total} vs national {national})"
    res = dict(name=name, year=year, path=os.path.relpath(path, ROOT).replace("\\", "/"),
               total=total, national=national, check=check, source=source, shares=shares)
    with open(os.path.join(OUT, f"{name}_{year}.json"), "w", encoding="utf-8") as f:
        json.dump(dict(res, fetched=datetime.date.today().isoformat()), f, indent=1, ensure_ascii=False)
    return res


# --------------------------------------------------------------------------- keys
def key_population(years=("2010", "2015", "2020", "2024")):
    """Population 31 Dec by maakunta - Statistics Finland table 11ra."""
    table = "vaerak/11ra.px"
    meta = json.load(urllib.request.urlopen(f"{PXWEB}/{table}", timeout=60))
    area = next(v for v in meta["variables"] if v["code"].startswith("alue"))
    codes = [c for c in area["values"] if c in MK_TO_NUTS] + ["SSS"]
    meta, data = pxweb(table, {area["code"]: codes, "contentscode": ["vaerak-vaesto"],
                               "timeperiod_y": list(years)})
    dims = data["id"]
    size = data["size"]
    idx = {d: data["dimension"][d]["category"]["index"] for d in dims}
    out = []
    for y in years:
        vals, national = {}, None
        for c in codes:
            pos = [idx[d][c] if d.startswith("alue") else idx[d]["vaerak-vaesto"] if d == "contentscode"
                   else idx[d][y] for d in dims]
            flat = 0
            for p, s in zip(pos, size):
                flat = flat * s + p
            v = data["value"][flat]
            if c == "SSS":
                national = v
            else:
                vals[MK_TO_NUTS[c]] = v
        shares, total = check_and_share(vals, "population")
        out.append(write_key("population", y, vals, shares, total, national,
                             dict(org="Statistics Finland", table="StatFin vaerak 11ra",
                                  item="Population 31 Dec", url=f"{PXWEB}/{table}")))
    return out


def px_cube(table, selection):
    """Fetch a json-stat2 cube; return get(**codes) -> value (None if suppressed)."""
    meta, data = pxweb(table, selection)
    dims, size = data["id"], data["size"]
    idx = {d: data["dimension"][d]["category"]["index"] for d in dims}

    def get(**codes):
        flat = 0
        for d, n in zip(dims, size):
            flat = flat * n + idx[d][codes[d]]
        return data["value"][flat]
    return get


def _regional(get, area, fixed):
    """{nuts: value} and the national value of one cube cell (area dimension varies)."""
    vals = {MK_TO_NUTS[c]: get(**{area: c, **fixed}) for c in MK_TO_NUTS}
    return vals, get(**{area: "SSS", **fixed})


def key_buildings(years=("2010",)):
    """Building floor area (m2) by maakunta, building class and heat source - Statistics Finland raku/15f7.
    Keys bld_<class>_<heat>; heat 'all' = every heat source."""
    table = "raku/15f7.px"
    area = "alue_23_20260101"
    classes = {"0110_0111": "detached", "0112": "terraced", "012": "flats", "013_014": "special",
               "03": "commercial", "04": "office", "05": "transport", "06": "care", "07": "assembly",
               "08": "education", "11": "utility", "12": "warehouse", "13": "rescue", "19": "other"}
    heats = {"SSS": "all", "01": "dh", "02_03_05": "oilgas", "04": "elc", "06": "coal", "07_08": "wood",
             "09": "ground", "99": "other"}
    get = px_cube(table, {area: list(MK_TO_NUTS) + ["SSS"], "rakennus_6_20180101": list(classes),
                          "polttoaineet_12_20260101": list(heats), "timeperiod_y": list(years),
                          "contentscode": ["kerrosala_rakennus"]})
    out = []
    for y in years:
        for cc, cn in classes.items():
            for hc, hn in heats.items():
                fixed = {"rakennus_6_20180101": cc, "polttoaineet_12_20260101": hc, "timeperiod_y": y,
                         "contentscode": "kerrosala_rakennus"}
                vals, national = _regional(get, area, fixed)
                vals = {k: (v or 0) for k, v in vals.items()}
                if sum(vals.values()) <= 0:
                    continue
                name = f"bld_{cn}_{hn}"
                shares, total = check_and_share(vals, name)
                out.append(write_key(name, y, vals, shares, total, national, dict(
                    org="Statistics Finland", table="StatFin raku 15f7",
                    item=f"Building floor area (m2), class {cc}, heat source {hc}", url=f"{PXWEB}/{table}")))
        # composite classes (task 5c, audit/task5c.md section 2): sums of the native classes above
        for cn, parts in COMPOSITE_CLASSES.items():
            for hc, hn in heats.items():
                vals = {r: 0 for r in REGIONS}
                national = 0
                for cc in parts:
                    fixed = {"rakennus_6_20180101": cc, "polttoaineet_12_20260101": hc, "timeperiod_y": y,
                             "contentscode": "kerrosala_rakennus"}
                    v, n = _regional(get, area, fixed)
                    for k in vals:
                        vals[k] += v.get(k) or 0
                    national += n or 0
                if sum(vals.values()) <= 0:
                    continue
                name = f"bld_{cn}_{hn}"
                shares, total = check_and_share(vals, name)
                out.append(write_key(name, y, vals, shares, total, national, dict(
                    org="Statistics Finland", table="StatFin raku 15f7",
                    item=f"Building floor area (m2), classes {'+'.join(parts)}, heat source {hc}",
                    url=f"{PXWEB}/{table}")))
    return out


# services buildings of the model (commercial, office, care, assembly, education) and offices incl. education
COMPOSITE_CLASSES = {"services": ["03", "04", "06", "07", "08"], "officeedu": ["04", "08"]}


def key_vehicles(years=("2011", "2024")):
    """Vehicles in traffic by maakunta and class - Traficom via Statistics Finland mkan/11ic (from 2011)."""
    table = "mkan/11ic.px"
    area = "alue_28_20210101"
    classes = {"01": "cars", "02": "vans", "03": "lorries", "04": "buses", "06": "motorcycles", "07": "mopeds"}
    get = px_cube(table, {area: list(MK_TO_NUTS) + ["SSS"], "ajoneuvolaji_2_20190101": list(classes),
                          "ajot_36_20180207": ["0"], "timeperiod_y": list(years), "contentscode": ["mkan-lkm"]})
    out = []
    for y in years:
        for cc, cn in classes.items():
            fixed = {"ajoneuvolaji_2_20190101": cc, "ajot_36_20180207": "0", "timeperiod_y": y,
                     "contentscode": "mkan-lkm"}
            vals, national = _regional(get, area, fixed)
            name = f"veh_{cn}"
            shares, total = check_and_share(vals, name)
            out.append(write_key(name, y, vals, shares, total, national, dict(
                org="Traficom / Statistics Finland", table="StatFin mkan 11ic",
                item=f"Vehicles in traffic, class {cc} ({cn})", url=f"{PXWEB}/{table}"),
                tol=0.01, why="vehicles without a known municipality are in the national total only"))
    return out


def key_industry(years=("2018",)):
    """Value added (EUR 1,000) and personnel (staff-years) of enterprise establishments by maakunta and
    industry (TOL 2008) - Statistics Finland alyr/13x2. A combination with a suppressed or negative
    regional value is not written (not usable as a key). Keys va_<TOL>, staff_<TOL>."""
    table = "alyr/13x2.px"
    area = "alue_23_20210101"
    tols = ["C", "C10", "C11", "C13", "C16", "C18", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27",
            "C28", "C29", "C30", "C31", "C32", "C33", "A01", "B08"]
    contents = {"EUMukTuotJalostusarvo2": "va", "henkmaara2": "staff"}
    get = px_cube(table, {area: list(MK_TO_NUTS) + ["SSS"], "toimiala_79_20180101": tols,
                          "timeperiod_y": list(years), "contentscode": list(contents)})
    out = []
    for y in years:
        for t in tols:
            for cc, cn in contents.items():
                fixed = {"toimiala_79_20180101": t, "timeperiod_y": y, "contentscode": cc}
                vals, national = _regional(get, area, fixed)
                if any(v is None or v < 0 for v in vals.values()):
                    print(f"  {cn}_{t} {y}: suppressed or negative regional values - not written")
                    continue
                name = f"{cn}_{t}"
                shares, total = check_and_share(vals, name)
                what = "Value added (EUR 1,000)" if cn == "va" else "Personnel (staff-years)"
                out.append(write_key(name, y, vals, shares, total, national, dict(
                    org="Statistics Finland", table="StatFin alyr 13x2",
                    item=f"{what}, establishments of enterprises, TOL {t}", url=f"{PXWEB}/{table}"),
                    tol=0.005, why="rounding and confidential establishments in the national total"))
    return out


CLASSIFICATIONS = "https://data.stat.fi/api/classifications/v2/correspondenceTables"


def municipality_regions(year="20260101"):
    """Municipality code (KUxxx) -> NUTS-3 from Statistics Finland's official correspondence table."""
    url = (f"{CLASSIFICATIONS}/kunta_1_{year}%23maakunta_1_{year}/maps?content=data&meta=max&lang=en&format=json")
    out = {}
    for m in json.load(urllib.request.urlopen(url, timeout=60)):
        ku = "KU" + m["sourceLocalId"].split("/")[1]
        mk = "MK" + m["targetLocalId"].split("/")[1]
        out[ku] = MK_TO_NUTS[mk]
    return out


def key_employment(years=("2010", "2018")):
    """Employed labour force by area of workplace and industry (TOL 2008) - Statistics Finland tyokay/115h,
    municipalities summed to regions with the official municipality-region correspondence (2026 division).
    Keys emp_<TOL>: complete (no suppression), used where value added is suppressed."""
    table = "tyokay/115h.px"
    area = "alue_23_20260101"
    tols = ["C", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26",
            "27", "28", "29", "30", "31", "32", "33", "A", "01", "02", "08", "GTU"]
    # composites (model sectors): manufacturing outside the separately modelled branches, and basic metals
    # without the steel towns (the steel works are modelled as IIS at their sites)
    composites = {
        "ioi": ([t for t in ("10", "11", "12", "13", "14", "15", "16", "18", "21", "22", "25", "26", "27", "28", "29",
                             "30", "31", "32", "33")], set(),
                "manufacturing excl. paper 17, refining 19, chemicals 20, minerals 23, basic metals 24"),
        "24nonsteel": (["24"], {"KU678", "KU851", "KU153", "KU109"},
                       "basic metals 24 excl. the steel towns Raahe, Tornio, Imatra, Hameenlinna"),
    }
    kmap = municipality_regions()
    meta = json.load(urllib.request.urlopen(f"{PXWEB}/{table}", timeout=60))
    codes = next(v for v in meta["variables"] if v["code"] == area)["values"]
    unknown = [c for c in codes if c != "SSS" and c not in kmap]
    get = px_cube(table, {area: codes, "toimiala_108_20230101": tols, "timeperiod_y": list(years),
                          "sukupuoli_9_20180101": ["SSS"], "contentscode": ["tyolliset3"]})
    out = []
    for y in years:
        for t in tols:
            fixed = {"toimiala_108_20230101": t, "timeperiod_y": y, "sukupuoli_9_20180101": "SSS",
                     "contentscode": "tyolliset3"}
            vals = {r: 0 for r in REGIONS}
            for c in codes:
                if c in kmap:
                    vals[kmap[c]] += get(**{area: c, **fixed}) or 0
            national = get(**{area: "SSS", **fixed})
            name = f"emp_{t}"
            shares, total = check_and_share(vals, name)
            out.append(write_key(name, y, vals, shares, total, national, dict(
                org="Statistics Finland", table="StatFin tyokay 115h",
                item=f"Employed labour force in area (workplaces), TOL {t}; municipalities -> regions "
                     f"(kunta_1_20260101#maakunta_1_20260101)", url=f"{PXWEB}/{table}"),
                tol=0.02, why="workplace municipality unknown or abroad: national total only"
                + (f"; unmapped area codes {unknown}" if unknown else "")))
        for cname, (parts, excl, desc) in composites.items():
            vals = {r: 0 for r in REGIONS}
            national = 0
            for t in parts:
                fixed = {"toimiala_108_20230101": t, "timeperiod_y": y, "sukupuoli_9_20180101": "SSS",
                         "contentscode": "tyolliset3"}
                for c in codes:
                    if c in kmap and c not in excl:
                        vals[kmap[c]] += get(**{area: c, **fixed}) or 0
                national += sum((get(**{area: c, **fixed}) or 0) for c in codes if c in kmap and c not in excl)
            name = f"emp_{cname}"
            shares, total = check_and_share(vals, name)
            out.append(write_key(name, y, vals, shares, total, national, dict(
                org="Statistics Finland", table="StatFin tyokay 115h",
                item=f"Employed labour force in area (workplaces), {desc} (TOL {'+'.join(parts)}"
                     + (f"; excluded municipalities {sorted(excl)}" if excl else "") + ")",
                url=f"{PXWEB}/{table}")))
    return out


KEYS = {"population": key_population, "buildings": key_buildings, "vehicles": key_vehicles,
        "industry": key_industry, "employment": key_employment}


def all_results():
    """Every key documented by a .json sidecar (all keys built so far, not only this run's)."""
    return [json.load(open(os.path.join(OUT, fn), encoding="utf-8"))
            for fn in sorted(os.listdir(OUT)) if fn.endswith(".json")]


def write_audit(results):
    path = os.path.join(ROOT, "audit", "keys.md")
    lines = ["# Regional keys", "",
             f"Generated by `tools/regional_keys.py` on {datetime.date.today().isoformat()}. "
             "Each key is a share of a national quantity by NUTS-3 region; the 19 shares of a key "
             "sum to exactly 1 (checked with exact rational arithmetic) and the regional total is "
             "checked against the national figure of the same source.", "",
             "Åland (FI200) is a normal region of the model, connected to the rest of Finland by links.", ""]
    for r in results:
        s = r["source"]
        lines += [f"## {r['name']} {r['year']}", "",
                  f"- Source: {s['org']}, {s['table']}, item \"{s['item']}\" ({s['url']})",
                  f"- File: `{r['path']}`",
                  f"- Regional total {r['total']:,} vs national {r['national'] if r['national'] is None else format(r['national'], ',')}: **{r['check']}**", "",
                  "| Region | Name | Share |", "|---|---|---|"]
        lines += [f"| {k} | {REGIONS[k]} | {v:.4%} |" for k, v in r["shares"].items()]
        lines.append("")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", choices=sorted(KEYS))
    a = ap.parse_args()
    results = []
    for k, fn in KEYS.items():
        if a.key and k != a.key:
            continue
        results += fn()
    for r in results:
        print(f"{r['name']:24s} {r['year']}  total {r['total']:>14,}  national {str(r['national']):>14}  {r['check']}")
    print("wrote", os.path.relpath(write_audit(all_results()), ROOT))


if __name__ == "__main__":
    main()
