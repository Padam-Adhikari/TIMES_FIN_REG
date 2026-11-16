"""Read-only regionalisation scan of VEDA's DD files (a synced GAMS_WrkTIMES folder).

    python tools/regional_scan.py --dd GAMS_WrkTIMES --run baseline-sami.run --out audit/regional_scan.md

Finds the patterns that broke or biased the regional runs so far, before a server run:
  1  national quantities applied per region: the same non-zero bound value in FI and in >= 2 regions
  2  user constraints with a non-zero RHS declared R_E (each region gets the national RHS)
  3  hub-only physics copied to regions: COM_IE, COM_TAXNET/CSTNET, COM_PKTS on hub commodities
  4  attributes on internal links TB_* that belong to real processes (emissions, taxes, bounds)
  5  FI-only constraints (R_E FI / R_S with FI terms only) whose processes now sit in a region
  6  processes in a region whose single-region (FI) attributes are missing there (optional --old)
"""
import argparse
import collections
import os
import re

TOK = re.compile(r"'([^']*)'")
REG = re.compile(r"^FI[0-9][0-9A-Z]{2,3}$")
BOUNDS = {"CAP_BND", "NCAP_BND", "ACT_BND", "FLO_BND", "COM_BNDNET", "COM_BNDPRD", "IRE_BND",
          "FLO_CUM", "ACT_CUM", "COM_CUMNET", "COM_CUMPRD", "RCAP_BND", "STGIN_BND", "STGOUT_BND"}
RHS = {"UC_RHS", "UC_RHSR", "UC_RHST", "UC_RHSRT", "UC_RHSTS", "UC_RHSRTS", "UC_RHSRS", "UC_RHSS"}
TERMS = {"UC_ACT", "UC_FLO", "UC_CAP", "UC_NCAP", "UC_COMPRD", "UC_COMCON", "UC_COMNET", "UC_IRE", "UC_CUMACT",
         "UC_CUMFLO", "UC_CUMCOM"}


def read(dd, run):
    files = re.findall(r"BATINCLUDE\s+(\S+\.dd)", open(os.path.join(dd, run), encoding="latin-1").read())
    out = collections.defaultdict(list)          # param -> [(file, tokens, value)]
    for f in files:
        name = None
        for l in open(os.path.join(dd, f), encoding="latin-1"):
            m = re.match(r"^SET\s+(\S+)", l) or re.match(r"^([A-Za-z_0-9]+) ' '/", l)
            if m:
                name = m.group(1)
                continue
            if l.startswith("/;"):
                name = None
                continue
            if not name or not l.strip() or l.startswith("$"):
                continue
            t = TOK.findall(l)
            tail = l.rsplit(None, 1)[-1] if not l.rstrip().endswith("'") else None
            num = None
            if tail is not None:
                try:
                    num = float(tail)
                except ValueError:
                    num = None
            yrs = re.findall(r"\.(\d{4}|0)\.", l)
            out[name].append((f, t, num, yrs[0] if yrs else None, l.strip()))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dd", required=True)
    ap.add_argument("--run", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    D = read(a.dd, a.run)
    L = [f"# Regionalisation scan of {a.dd}/{a.run}", ""]
    regs = sorted({t[0] for _, t, *_ in D.get("PRC_MAP", []) if t and REG.match(t[0])})
    L.append(f"Regions with processes: {len(regs)}\n")
    issues = collections.Counter()

    # 1 national quantities repeated
    L.append("## 1. Non-zero bounds with the same value on FI and in >= 2 regions (national quantity per region?)")
    rows = []
    for p in sorted(BOUNDS):
        grp = collections.defaultdict(dict)
        for f, t, v, y, l in D.get(p, []):
            if v is None or v == 0 or y == "0" or not t:
                continue
            key = (p, f, y) + tuple(x for x in t[1:] if not REG.match(x) and x != "FI")
            grp[key][t[0]] = v
        for key, byr in grp.items():
            if "FI" in byr:
                same = [r for r, v in byr.items() if r != "FI" and abs(v - byr["FI"]) < 1e-12 * max(1, abs(v))]
                if len(same) >= 2 and abs(byr["FI"]) < 1e6:
                    rows.append((key, byr["FI"], len(same)))
    agg = collections.defaultdict(lambda: [0, 0.0, 0])
    for key, v, n in rows:
        k = key[:2] + key[3:4]
        agg[k][0] += 1
        agg[k][1] = v
        agg[k][2] = max(agg[k][2], n)
    L.append("| attribute | file | item | entries | example value | regions |")
    L.append("|---|---|---|---|---|---|")
    for k, (n, v, nr) in sorted(agg.items(), key=lambda t: -t[1][0])[:60]:
        L.append(f"| {k[0]} | {k[1]} | {k[2] if len(k) > 2 else ''} | {n} | {v:g} | {nr} |")
    issues["1 national bound per region"] = len(agg)
    L.append("")

    # 2 R_E constraints with non-zero RHS in several regions
    L.append("## 2. User constraints per region (R_E) with a non-zero RHS")
    each = collections.defaultdict(set)
    for f, t, *_ in D.get("UC_R_EACH", []):
        if len(t) == 2:
            each[t[1]].add(t[0])
    rhs = collections.defaultdict(lambda: collections.defaultdict(set))
    for p in RHS:
        for f, t, v, y, l in D.get(p, []):
            if v is None or v == 0 or y == "0" or not t:
                continue
            if REG.match(t[0]) or t[0] == "FI":
                r, uc = t[0], (t[1] if len(t) > 1 else None)
            else:
                r, uc = None, t[0]
            rhs[uc][r].add(v)
    bad = []
    for uc, regs_ in each.items():
        if len(regs_) >= 2 and uc in rhs:
            nz = {r: sorted(vs)[:2] for r, vs in rhs[uc].items()}
            if any(r is None or r in regs_ for r in nz):
                bad.append((uc, len(regs_), nz.get("FI") or nz.get(None)))
    L.append("| UC | regions (R_E) | RHS example |")
    L.append("|---|---|---|")
    for uc, n, ex in sorted(bad)[:60]:
        L.append(f"| {uc} | {n} | {ex} |")
    issues["2 per-region UC with RHS"] = len(bad)
    L.append("")

    # 3 hub-only physics in the regions
    L.append("## 3. Hub-only attributes on commodities in the regions")
    for p in ("COM_IE", "COM_TAXNET", "COM_CSTNET", "COM_TAXPRD", "COM_CSTPRD", "COM_PKTS", "COM_PKRSV", "COM_PKFLX"):
        c = collections.Counter()
        for f, t, *_ in D.get(p, []):
            if t and REG.match(t[0]) and len(t) > 1:
                c[(f, t[1])] += 1
        if c:
            L.append(f"- {p}: " + ", ".join(f"{com} ({f}, {n})" for (f, com), n in c.most_common(12)))
            issues["3 " + p] = len(c)
    L.append("")

    # 4 attributes on internal links
    L.append("## 4. Attributes on internal links TB_* (expected: definitions, ACT_COST, UC_IRE corrections)")
    ok = {"PRC", "PRC_MAP", "PRC_TSL", "PRC_ACTUNT", "PRC_DESC", "TOP_IRE", "ACT_COST", "UC_IRE", "PRC_CAPACT",
          "NCAP_DRATE", "PRC_TS", "IRE_TSCVT", "IRE_CCVT", "NCAP_ILED"}
    c = collections.Counter()
    for p, rows_ in D.items():
        if p in ok:
            continue
        for f, t, v, y, l in rows_:
            if any(x.startswith("TB_") for x in t):
                c[(p, f)] += 1
    for (p, f), n in c.most_common(20):
        L.append(f"- {p} ({f}): {n}")
        issues["4 " + p] += n
    L.append("")

    # 5 FI-only constraints over processes that moved
    L.append("## 5. Constraints with terms only on FI whose processes also exist in regions")
    where = collections.defaultdict(set)
    for f, t, *_ in D.get("PRC_MAP", []):
        if len(t) == 3:
            where[t[2]].add(t[0])
    ucreg = collections.defaultdict(set)
    ucproc = collections.defaultdict(set)
    for p in TERMS:
        for f, t, *_ in D.get(p, []):
            if len(t) >= 3 and (t[1] == "FI" or REG.match(t[1])):
                ucreg[t[0]].add(t[1])
                if p in ("UC_ACT", "UC_FLO", "UC_CAP", "UC_NCAP"):
                    ucproc[t[0]].add(t[2])
    sets = collections.defaultdict(set)
    for p in ("UC_R_SUM", "UC_R_EACH"):
        for f, t, *_ in D.get(p, []):
            if len(t) == 2:
                sets[t[1]].add(t[0])
    rows = []
    for uc, rr in ucreg.items():
        if rr == {"FI"}:
            moved = sorted(p for p in ucproc[uc] if where.get(p) and where[p] - {"FI"})
            if moved:
                rows.append((uc, moved[:4], len(moved)))
    for uc, moved, n in sorted(rows):
        L.append(f"- {uc}: {n} processes also in regions, e.g. {moved}")
    issues["5 FI-only UC over moved processes"] = len(rows)
    L.append("")

    L.append("## Summary")
    for k, v in sorted(issues.items()):
        L.append(f"- {k}: {v}")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("written", a.out)
    for k, v in sorted(issues.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
