"""Finnish industrial installations of the EU ETS (EUTL) with location, activity, verified emissions
and free allocation, placed in their maakunta (NUTS-3). Read-only: writes data/sources only.

Source: EU Transaction Log (EUTL), public installation and compliance data, via the open API of
EUETS.INFO (https://www.euets.info, J. Abrell; code https://github.com/jabrell/pyeutl).
Free allocation 2013-2020 follows the EU product benchmarks x historical activity level of each
installation, so it is a production proxy also where emissions are mostly biogenic (pulp and paper).

    python tools/industry_register.py            # writes data/sources/eutl_FI_industry.csv

Placement: installation coordinates (EUTL geocoding) in the official maakunta polygons
(data/sources/maakunta_2026_wgs84.geojson); without coordinates the postal town of the address is
matched to a municipality (Statistics Finland classification).
"""
import base64
import csv
import json
import os
import re
import sys
import time
import urllib.request
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from power_register import MAAKUNTA, SRC, municipalities, norm, region_of  # noqa: E402
from regional_keys import MK_TO_NUTS  # noqa: E402

API = "https://2j6zr78sq1.execute-api.eu-central-1.amazonaws.com/prod"
OUT = os.path.join(SRC, "eutl_FI_industry.csv")
RAW = os.path.join(SRC, "eutl_FI_installations_raw.json")
# EUTL geocoding errors found by checking each site's region against the postal town of its address
# (village postal towns resolved to their municipality by hand; these three disagreed):
OVERRIDE = {
    "FI_533": ("FI1B1", "Porvoon jalostamo = Neste Porvoo refinery, Kilpilahti, Porvoo (Uusimaa); EUTL geocode in Keski-Suomi"),
    "FI_554": ("FI19A", "Metsa Board Kaskinen BCTMP mill, Kaskinen (Pohjanmaa); EUTL geocode in Keski-Suomi"),
    "FI_487": ("FI1D8", "Sotkamon tehdas, Sotkamo (Kainuu); EUTL geocode in Pohjois-Pohjanmaa"),
}
UA = "Reg-FINTIMES-regionalisation/1.0 (research model data preparation)"
YEARS = list(range(2008, 2025))
NOT_INDUSTRY = ("35", "50", "51", "52", "63", "86", "41", "01")      # energy supply, transport, services
# installations without a NACE code are industrial when their ETS activity is (hydrogen, refining, chemicals)
NO_CODE_SKIP = ("Combustion", "Other activity", "Maritime", "EU Effort")


def get(path):
    req = urllib.request.Request(API + path, headers={"User-Agent": UA})
    d = json.load(urllib.request.urlopen(req, timeout=120))
    b = d.get("body", d)
    if isinstance(b, str):
        try:
            return json.loads(zlib.decompress(base64.b64decode(b)).decode("utf-8"))
        except Exception:
            return json.loads(b)
    return b


def polys():
    out = []
    for f in json.load(open(MAAKUNTA, encoding="utf-8"))["features"]:
        out.append((MK_TO_NUTS["MK" + f["properties"]["maakunta"]], f["geometry"]))
    return out


def main():
    allrows = get("/installations?limit=")
    json.dump([r for r in allrows if r["id"].startswith("FI_")], open(RAW, "w", encoding="utf-8"), ensure_ascii=False)
    fi = [r for r in allrows if r["id"].startswith("FI_") and r["activityCategory"] not in ("Aircrafts",)
          and r["registry"] == "Finland"]
    ind = [r for r in fi if (r.get("nace_id") and not str(r["nace_id"]).split(".")[0].zfill(2).startswith(NOT_INDUSTRY)
                             and r["activityCategory"] not in ("Maritime",))
           or (not r.get("nace_id") and not r["activity"].startswith(NO_CODE_SKIP))]
    print(f"{len(fi)} stationary Finnish installations, {len(ind)} industrial (NACE outside energy/transport/services)")
    P = polys()
    munis = municipalities()          # name -> (code, nuts)
    rows = []
    for i, r in enumerate(sorted(ind, key=lambda r: r["id"])):
        comp = get(f"/compliance?id={r['id']}")
        time.sleep(0.2)
        ver = {c["year"]: c.get("verified") for c in comp}
        alo = {c["year"]: c.get("allocatedTotal") for c in comp}
        lat, lon = r.get("latitudeGoogle"), r.get("longitudeGoogle")
        nuts, how = None, ""
        if lat and lon:
            nuts, how = region_of(lon, lat, P), "coordinates"
        if r["id"] in OVERRIDE:
            nuts, how = OVERRIDE[r["id"]][0], "manual: " + OVERRIDE[r["id"]][1]
        if not nuts:
            lines = r["address"].split("\n")
            town = ""
            for ln in lines:
                m = re.match(r"^\s*\d{5}\s+(.+)$", ln)
                if m:
                    town = m.group(1).strip()
            hit = munis.get(norm(town)) if town else None
            if hit:
                nuts, how = hit[1], f"postal town {town}"
        rows.append(dict(id=r["id"], name=r["name"], nace=r["nace_id"], nace_text=r["nace"], activity=r["activity"],
                         category=r["activityCategory"], lat=lat or "", lon=lon or "", region=nuts or "", method=how,
                         address=" / ".join(x.strip() for x in r["address"].split("\n")[1:] if x.strip()),
                         **{f"ver{y}": ver.get(y) if ver.get(y) is not None else "" for y in YEARS},
                         **{f"alloc{y}": alo.get(y) if alo.get(y) is not None else "" for y in YEARS}))
        if (i + 1) % 20 == 0:
            print(f"  {i + 1}/{len(ind)}")
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    miss = [r["id"] + " " + r["name"] for r in rows if not r["region"]]
    print(f"written {OUT}: {len(rows)} installations; not placed: {miss}")


if __name__ == "__main__":
    main()
