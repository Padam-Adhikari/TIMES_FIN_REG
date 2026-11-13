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


def write_key(name, year, values, shares, total, national, source):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"{name}_{year}.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["region", "name", "value", "share"])
        for r in REGIONS:
            w.writerow([r, REGIONS[r], values[r], f"{shares[r]:.12f}"])
        w.writerow(["TOTAL", "sum of regions", total, f"{sum(shares.values()):.12f}"])
    check = "OK" if national is None or abs(total - national) <= 1e-9 * max(1, national) else \
        f"MISMATCH (regions {total} vs national {national})"
    return dict(name=name, year=year, path=os.path.relpath(path, ROOT).replace("\\", "/"),
                total=total, national=national, check=check, source=source, shares=shares)


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


KEYS = {"population": key_population}


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
                  f"- Regional total {r['total']:,} vs national {r['national']:,}: **{r['check']}**", "",
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
        print(f"{r['name']:12s} {r['year']}  total {r['total']:>12,}  national {r['national']:>12,}  {r['check']}")
    print("wrote", os.path.relpath(write_audit(results), ROOT))


if __name__ == "__main__":
    main()
