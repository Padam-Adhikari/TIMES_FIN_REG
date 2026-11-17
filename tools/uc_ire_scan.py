"""Read-only scan of a VEDA DD folder: national user constraints that count production or consumption of
a commodity crossing an internal TB_* link without the matching UC_IRE correction.

TIMES counts an import as production and an export as consumption. In a national (summed over regions)
constraint, a UC_COMPRD term on a linked commodity therefore counts every internal transfer twice (once
where it is produced, once where it is imported) unless the links carry UC_IRE ... IMP = -coefficient;
likewise UC_COMCON needs UC_IRE ... EXP = -coefficient. UC_COMNET needs nothing (lesson of task 0; task 4b
second run diverged on TUC_MinShareofCenELCinINDELC, audit/task4b.md section 7).

    python tools/uc_ire_scan.py [DD folder, default GAMS_WrkTIMES] [--extra COMM,COMM,...]

--extra adds commodities that will cross links after the next move (checked as if linked).
Aggregates (COM_AGG) are expanded: a term on an aggregate counts its linked components.
"""
import argparse
import collections
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from task0 import ROOT  # noqa: E402

HDR = re.compile(r"^(\w+)\s+' '/$")


def parse(dd):
    """{param: [(key tuple, value)]} and {set: [key tuple]} for the symbols this scan needs."""
    want = {"UC_COMPRD", "UC_COMCON", "UC_IRE", "UC_RHS", "UC_RHST", "UC_RHSTS", "COM_AGG",
            "UC_R_SUM", "TOP_IRE"}
    out = collections.defaultdict(list)
    for fn in glob.glob(os.path.join(dd, "*.dd")):
        cur = None
        for line in open(fn, encoding="latin-1"):
            s = line.strip()
            m = HDR.match(s)
            if m:
                cur = m.group(1)
                continue
            if s.startswith("SET"):
                parts = s.split()
                cur = parts[1] if len(parts) > 1 else None
                continue
            if s.startswith("PARAMETER"):
                cur = None
                continue
            if cur not in want or not s.startswith("'"):
                continue
            m = re.match(r"^(.*?)\s+([-+0-9.eE]+)$", s)
            key, val = (m.group(1), float(m.group(2))) if m else (s, None)
            out[cur].append((tuple(x.strip("'") for x in key.split(".")), val))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dd", nargs="?", default=os.path.join(ROOT, "GAMS_WrkTIMES"))
    ap.add_argument("--extra", default="", help="commodities that will be linked after the next move")
    a = ap.parse_args()
    d = parse(a.dd)

    linked = collections.defaultdict(set)          # commodity -> TB links
    for k, _ in d["TOP_IRE"]:
        # TOP_IRE: r.c.r2.c2.p (export from r of c, import into r2 as c2)
        if len(k) == 5 and k[4].startswith("TB_"):
            linked[k[1]].add(k[4])
            linked[k[3]].add(k[4])
    extra = {c for c in a.extra.split(",") if c}

    national = {k[1] for k, _ in d["UC_R_SUM"] if len(k) == 2}
    national |= {k[0] for p in ("UC_RHS", "UC_RHST", "UC_RHSTS") for k, _ in d[p]}

    agg = collections.defaultdict(set)              # aggregate -> components (COM_AGG r.t.c_comp.c_agg)
    for k, _ in d["COM_AGG"]:
        if len(k) == 4:
            agg[k[3]].add(k[2])

    corr = collections.defaultdict(set)             # (uc, link, side) present
    for k, _ in d["UC_IRE"]:
        # UC_IRE uc.side.r.t.p.c.s.IMP|EXP
        if len(k) == 8 and k[4].startswith("TB_"):
            corr[(k[0], k[5], k[7])].add(k[4])

    terms = collections.defaultdict(dict)           # (uc, attr, comm) -> {region: non-zero coefficient}
    counted = collections.defaultdict(set)          # uc -> commodities it counts (any coefficient)
    for attr, side in (("UC_COMPRD", "IMP"), ("UC_COMCON", "EXP")):
        for k, v in d[attr]:
            # uc.side.r.t.c.s
            if len(k) == 6 and k[0] in national:
                counted[k[0]] |= agg.get(k[4], set()) | {k[4]}
                if v:
                    terms[(k[0], attr, k[4])][k[2]] = v

    rows = []
    for (uc, attr, c), regs in sorted(terms.items()):
        side = "IMP" if attr == "UC_COMPRD" else "EXP"
        comps = agg.get(c, set()) | {c}
        for comp in sorted(comps):
            links = linked.get(comp, set())
            if not links and comp not in extra:
                continue
            have = corr.get((uc, comp, side), set())
            miss = sorted(links - have)
            if comp in extra and not links:
                miss = ["(after the move)"]
            if miss:
                coef = next(iter(regs.values()))
                rows.append((uc, attr, c, comp, coef, len(regs), len(links), len(have), miss[:3]))

    # corrections on a commodity the constraint does not count (e.g. a row pointing at the wrong UC)
    stray = sorted((uc, comp, side, len(lk)) for (uc, comp, side), lk in corr.items()
                   if comp not in counted.get(uc, set()))

    print(f"national UCs: {len(national)}; linked commodities: {len(linked)}; extra: {sorted(extra)}")
    if stray:
        print(f"{len(stray)} UC_IRE corrections on a commodity the constraint does not count (wrong row?):")
        for s in stray:
            print("  uc %s | commodity %s | %s | %d links" % s)
    if not rows:
        print("no national UC_COMPRD/UC_COMCON term on a linked commodity lacks its UC_IRE correction")
        return 1 if stray else 0
    print(f"{len(rows)} terms without (complete) UC_IRE correction:")
    print("uc | attribute | commodity | linked component | coef | regions with term | links | corrected | e.g. missing")
    for r in rows:
        print(" | ".join(str(x) for x in r))
    return 1


if __name__ == "__main__":
    sys.exit(main())
