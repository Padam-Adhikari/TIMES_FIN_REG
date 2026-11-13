"""Power plants of the Energy Authority register -> NUTS-3 region -> regional keys.

Sources (downloaded into data/sources/, read-only):
  * Energy Authority power plant register (Energiaviraston voimalaitosrekisteri), 22.5.2026
    https://energiavirasto.fi/toimitusvarmuus
  * Statistics Finland classification kunta_1_20260101 -> maakunta_1_20260101
    https://data.stat.fi/api/classifications/v2/
  * OpenStreetMap Nominatim geocoder (place names -> municipality), cached in
    data/sources/register_geocode.csv (usage policy: 1 request/s, identified user agent)

Siting of a plant (column 'Location' = Laitospaikka, the plant site; 'Town'/'Postal code'
are the company's address and are NOT used except as a flagged last resort):
  1. a municipality name (fi or sv) appears in the site name            -> confidence 'name'
  2. OpenStreetMap geocoding of the site name in Finland                -> 'geocoded'
  3. the company's town                                                  -> 'company-town' (yellow)
Manual corrections (with reason) in MANUAL below override everything    -> 'manual'.

Outputs: data/keys/power_plants_20260522.csv (plant list with region and method),
         data/keys/power_<category>.csv (19 shares per category, exact sum 1),
         audit/power_keys.md.
"""
import csv
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from fractions import Fraction

import openpyxl

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
SRC = os.path.join(ROOT, "data", "sources")
KEYS = os.path.join(ROOT, "data", "keys")
REGISTER_URL = ("https://energiavirasto.fi/documents/11120570/0/Energiaviraston%20voimalaitosrekisteri%2022052026"
                ".xlsx/11b87623-45e2-f7a2-7208-6d6e96aca617?t=1780051925076")
REGISTER = os.path.join(SRC, "energiavirasto_voimalaitosrekisteri_20260522.xlsx")
CLASS_URL = ("https://data.stat.fi/api/classifications/v2/correspondenceTables/"
             "kunta_1_20260101%23maakunta_1_20260101/maps?content=data&meta=max&lang=fi")
GEOCACHE = os.path.join(SRC, "register_geocode.csv")
UA = "Reg-FINTIMES-regionalisation/1.0 (research model data preparation)"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from regional_keys import REGIONS, MK_TO_NUTS  # noqa: E402

# Site corrections that the data cannot settle; each needs a reason.
MANUAL = {
    "Olkiluoto 1": ("Eurajoki", "Olkiluoto nuclear site, Eurajoki"),
    "Olkiluoto 2": ("Eurajoki", "Olkiluoto nuclear site, Eurajoki"),
    "Olkiluoto 3": ("Eurajoki", "Olkiluoto nuclear site, Eurajoki"),
    "Loviisa 1": ("Loviisa", "Hästholmen nuclear site, Loviisa"),
    "Loviisa 2": ("Loviisa", "Hästholmen nuclear site, Loviisa"),
    "Joutseno": ("Lappeenranta", "Joutseno, former municipality merged into Lappeenranta in 2009 "
                                 "(Metsä Fibre Joutseno mill and the 3.9 MW plant)"),
    "Suomenojan voimalaitos": ("Espoo", "Suomenoja power plant, Espoo"),
    "Tahkoluoto T1-T10": ("Pori", "Tahkoluoto offshore wind farm, Pori"),
    "Ajos Wind Oy": ("Kemi", "Ajos wind farm, Kemi"),
}


def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def municipalities():
    """{normalised name: (kunta code, NUTS-3)} for Finnish and Swedish names."""
    out = {}
    for lang in ("fi", "sv"):
        u = CLASS_URL.replace("lang=fi", f"lang={lang}")
        for m in json.load(urllib.request.urlopen(u, timeout=60)):
            names = [n["name"] for n in m["sourceItem"]["classificationItemNames"]]
            nuts = MK_TO_NUTS["MK" + m["targetItem"]["code"]]
            for n in names:
                out[norm(n)] = (m["sourceItem"]["code"], nuts, n)
    return out


def load_register(path=None):
    path = path or REGISTER
    if path == REGISTER and not os.path.exists(REGISTER):
        os.makedirs(SRC, exist_ok=True)
        req = urllib.request.Request(REGISTER_URL, headers={"User-Agent": UA})
        open(REGISTER, "wb").write(urllib.request.urlopen(req, timeout=120).read())
    ws = openpyxl.load_workbook(path, read_only=True, data_only=True)["English"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = [str(h).strip() if h else "" for h in rows[1]]
    out = []
    for r in rows[2:]:
        if not r[0]:
            continue
        d = dict(zip(hdr, r))
        out.append(dict(name=str(r[0]).strip(), company=r[1], town=r[4], site=str(r[6] or r[0]).strip(),
                        type=r[7] or "", fuel=r[20] or "", mw=float(r[17] or 0),
                        mw_sep=float(r[8] or 0), mw_ind=float(r[11] or 0), mw_dh=float(r[14] or 0)))
    return out


def geocache():
    c = {}
    if os.path.exists(GEOCACHE):
        for r in csv.DictReader(open(GEOCACHE, encoding="utf-8")):
            c[r["query"]] = r
    return c


def geocode(q, cache):
    if q in cache:
        return cache[q]
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
        {"q": q, "countrycodes": "fi", "format": "jsonv2", "addressdetails": 1, "limit": 1})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    time.sleep(1.1)                                   # Nominatim usage policy
    try:
        res = json.load(urllib.request.urlopen(req, timeout=60))
    except Exception as e:
        res = []
        print("  geocode failed", q, e, file=sys.stderr)
    a = res[0]["address"] if res else {}
    row = dict(query=q, municipality=a.get("municipality") or a.get("city") or a.get("town") or "",
               region=a.get("state") or a.get("region") or "", display=res[0]["display_name"] if res else "")
    cache[q] = row
    new = not os.path.exists(GEOCACHE)
    with open(GEOCACHE, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["query", "municipality", "region", "display"])
        if new:
            w.writeheader()
        w.writerow(row)
    return row


OSM = os.path.join(SRC, "osm_power_plants_FI.json")
MAAKUNTA = os.path.join(SRC, "maakunta_2026_wgs84.geojson")
STOP = {"voimalaitos", "vesivoimalaitos", "voimala", "tuulipuisto", "tuulivoimapuisto", "tuulivoimala",
        "aurinkovoimala", "aurinkopuisto", "lampovoimalaitos", "voimalaitoksen", "voimalaitokset", "oy",
        "ab", "oyj", "kraftverk", "power", "plant", "station", "bv", "vp", "lv", "hydro", "wind", "farm",
        "park", "the", "ja", "och", "tuulivoimapuiston", "tehtaan", "tehdas", "voimalaitos", "vesivoimala"}
# register type -> compatible OSM plant:source values
SOURCES = {"Hydro power": {"hydro"}, "Wind power": {"wind"}, "Solar": {"solar"},
           "Nuclear energy": {"nuclear"}}
THERMAL = {"gas", "biomass", "oil", "coal", "waste", "gas;oil", "biogas", "peat", "?", "biofuel", "diesel"}


def toks(s):
    return {t for t in norm(s).split() if t not in STOP and len(t) > 1}


def in_poly(x, y, ring):
    inside = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside


def region_of(lon, lat, polys):
    for nuts, geom in polys:
        parts = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
        for poly in parts:
            if in_poly(lon, lat, poly[0]) and not any(in_poly(lon, lat, h) for h in poly[1:]):
                return nuts
    return None


def osm_plants():
    polys = []
    for f in json.load(open(MAAKUNTA, encoding="utf-8"))["features"]:
        polys.append((MK_TO_NUTS["MK" + f["properties"]["maakunta"]], f["geometry"]))
    out = []
    for e in json.load(open(OSM, encoding="utf-8"))["elements"]:
        t = e.get("tags", {})
        names = [t.get(k) for k in ("name", "name:fi", "name:sv", "alt_name", "official_name", "old_name") if t.get(k)]
        if not names:
            continue
        c = e.get("center") or {"lat": e.get("lat"), "lon": e.get("lon")}
        if c.get("lat") is None:
            continue
        reg = region_of(c["lon"], c["lat"], polys)
        if reg:
            out.append(dict(names=names, toks=[toks(n) for n in names], source=t.get("plant:source", "?"),
                            region=reg, osm=f"{e['type']}/{e['id']}", label=names[0]))
    return out


def same_word(x, y):
    """Finnish inflection tolerant: Isohaara ~ Isohaaran, Vuosaari ~ Vuosaaren."""
    if x == y:
        return True
    n = 0
    for cx, cy in zip(x, y):
        if cx != cy:
            break
        n += 1
    return n >= 6 and n >= 0.7 * min(len(x), len(y))


def word_score(a, b):
    """Share of the register words found in the OSM name (and vice versa)."""
    if not a or not b:
        return 0.0
    hit_a = sum(1 for x in a if any(same_word(x, y) for y in b))
    hit_b = sum(1 for y in b if any(same_word(x, y) for x in a))
    return min(hit_a / len(a), hit_b / len(b))


def osm_plant_mw(o):
    return None


def osm_match(plant, osm):
    ok = SOURCES.get(plant["type"], THERMAL)
    scored = []
    for o in osm:
        if not (o["source"] in ok or o["source"] == "?"):
            continue
        s = max(word_score(toks(c), b) for c in (plant["name"], plant["site"]) for b in o["toks"])
        if s >= 0.5:
            scored.append((s, o))
    if not scored:
        return None, 0.0, ""
    top = max(s for s, _ in scored)
    best = [o for s, o in scored if s == top]
    regions = {o["region"] for o in best}
    if len(regions) > 1:
        return None, top, "ambiguous: " + ", ".join(sorted(f"{o['label']}->{o['region']}" for o in best))[:120]
    return best[0], top, ""


def site(plant, munis, osm):
    if plant["name"] in MANUAL:
        m, why = MANUAL[plant["name"]]
        return munis[norm(m)], "manual", why
    o, s, why = osm_match(plant, osm)
    if o:
        return (None, o["region"], ""), "osm", f"{o['osm']} '{o['label']}' ({o['source']}, match {s:.2f})"
    for cand in [plant["site"], plant["name"]]:
        n = norm(cand)
        if n in munis:
            return munis[n], "name", cand
        for part in str(cand).split(","):          # "Pahkakoski, Ii": exact municipality part
            if norm(part) in munis:
                return munis[norm(part)], "name", cand
        for tok in n.split():
            if len(tok) > 3 and tok in munis:
                return munis[tok], "name", cand
        for mk, nuts in MAAKUNTA_NAMES.items():   # "Ii, Pohjois Pohjanmaa"
            if mk in n:
                return (None, nuts, ""), "name", cand
    # CHP / separate production: the company's town is the plant's town for local utilities
    # and mill companies - not for national head offices (flagged yellow in the audit)
    if plant["type"] in ("District heating CHP", "Industry CHP", "Separate electricity production"):
        t = norm(plant["town"] or "")
        t = next((munis[x] for x in [t] + t.split() if x in munis), None)
        if t and t[2] not in HQ_TOWNS:
            return t, "company-town", f"company address {plant['town']}"
    # wind / solar farm names are distinctive: geocode the site, take the maakunta (OSM 'state')
    if plant["type"] in ("Wind power", "Solar"):
        for cand in [plant["site"], plant["name"]]:
            g = geocode(f"{cand}, Finland", GEOCACHE_DATA)
            nuts = MAAKUNTA_NAMES.get(norm(g.get("region", "")))
            if nuts:
                return (None, nuts, ""), "geocoded", g["display"][:80]
    return None, "unsited", (why or "no OSM plant with matching name and source") + f"; company town {plant['town']}"


HQ_TOWNS = {"Helsinki", "Espoo", "Vantaa"}
MAAKUNTA_NAMES = {}
GEOCACHE_DATA = {}


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--register", default=REGISTER)
    ap.add_argument("--tag", default="20260522")
    a = ap.parse_args()
    munis = municipalities()
    plants = load_register(a.register)
    osm = osm_plants()
    for f in json.load(open(MAAKUNTA, encoding="utf-8"))["features"]:
        pr = f["properties"]
        for nm in (pr["nimi"], pr["namn"], pr["name"]):
            MAAKUNTA_NAMES[norm(nm)] = MK_TO_NUTS["MK" + pr["maakunta"]]
    GEOCACHE_DATA.update(geocache())
    print(f"{len(osm)} named OSM power plants inside Finnish maakunta polygons")
    rows = []
    for p in plants:
        loc, how, note = site(p, munis, osm)
        p.update(kunta=(loc[2] or "") if loc else "", region=loc[1] if loc else "", method=how, note=note)
        rows.append(p)
    os.makedirs(KEYS, exist_ok=True)
    path = os.path.join(KEYS, f"power_plants_{a.tag}.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["name", "site", "type", "fuel", "mw", "mw_sep", "mw_ind", "mw_dh",
                                          "kunta", "region", "method", "note", "company", "town"])
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k) for k in w.fieldnames})
    from collections import Counter
    c = Counter(r["method"] for r in rows)
    mw = Counter()
    for r in rows:
        mw[r["method"]] += r["mw"]
    print("siting:", {k: f"{c[k]} plants / {mw[k]:.0f} MW" for k in c})
    print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
