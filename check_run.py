"""Check a solved TIMES run (VEDA GAMSSAVE .gdx) and compare it with a reference run.

Usage:
    python tools/check_run.py RUN.gdx [--ref REF.gdx] [--out report.md]

Checks:
  1. Dummy imports (IMPDEMZ, IMPNRGZ, IMPMATZ and any process named IMP*Z) carry no activity.
  2. Objective (OBJZ) and its change versus the reference run.
  3. National totals are conserved: each quantity summed over all internal regions
     must match the reference run's total (which may be the single-region FI run):
       COM_PROJ    demand projection     (input; must match exactly)
       NCAP_PASTI  existing capacity     (input; must match exactly)
       VAR_CAP     installed capacity    (result; reported, differences expected)
       VAR_COMNET  emissions (CO2 commodities, result; reported)
  4. Internal trade flows (VAR_IRE) between modelled regions, summed by commodity.

Exit code 1 if a hard check fails (dummy activity, or an input total not conserved).

gdxdump is found from --gdxdump, the GDXDUMP environment variable, the PATH (a GAMS
installation), or the gamspy_base Python package (pip install gamspy_base).
"""
import argparse
import csv
import io
import os
import shutil
import subprocess
import sys
from collections import defaultdict

TOL_ABS = 1e-6
TOL_REL = 1e-6
EMISSION_COMMODITIES = ("TOTCO2", "ETSCO2", "ELCCO2N", "INDCO2N", "SUPCO2N", "COMCO2N",
                        "RSDCO2N", "TRACO2N", "AGRCO2N")


def find_gdxdump(arg):
    for cand in (arg, os.environ.get("GDXDUMP"), shutil.which("gdxdump")):
        if cand and os.path.exists(cand):
            return cand
    try:
        import gamspy_base
        base = os.path.dirname(gamspy_base.__file__)
        for name in ("gdxdump", "gdxdump.exe"):
            p = os.path.join(base, name)
            if os.path.exists(p):
                return p
    except ImportError:
        pass
    sys.exit("gdxdump not found: install GAMS, or `pip install gamspy_base`, or pass --gdxdump")


class Run:
    def __init__(self, path, gdxdump):
        self.path = path
        self.gdxdump = gdxdump
        self._cache = {}

    def sym(self, name):
        """Return (header, rows) of a symbol; empty if absent."""
        if name not in self._cache:
            res = subprocess.run([self.gdxdump, self.path, f"symb={name}", "format=csv"],
                                 capture_output=True, text=True)
            if res.returncode != 0 or not res.stdout.strip():
                self._cache[name] = ([], [])
            else:
                rows = list(csv.reader(io.StringIO(res.stdout)))
                self._cache[name] = (rows[0], rows[1:])
        return self._cache[name]

    @staticmethod
    def num(x):
        x = x.strip()
        if x.upper() in ("EPS", ""):
            return 0.0
        if x.upper() in ("+INF", "INF"):
            return float("inf")
        if x.upper() == "-INF":
            return float("-inf")
        return float(x)

    def regions(self):
        return sorted(r[0] for r in self.sym("REG")[1])

    def objective(self):
        rows = self.sym("OBJZ")[1]
        return self.num(rows[0][-1]) if rows else None

    def total(self, name, key_cols, filt=None):
        """Sum Val over internal regions, keyed by the given column positions."""
        regs = set(self.regions())
        out = defaultdict(float)
        for r in self.sym(name)[1]:
            if r[0] not in regs:
                continue
            if filt and not filt(r):
                continue
            out[tuple(r[i] for i in key_cols)] += self.num(r[-1])
        return out

    def by_region(self, name, filt=None):
        out = defaultdict(float)
        for r in self.sym(name)[1]:
            if filt and not filt(r):
                continue
            out[r[0]] += self.num(r[-1])
        return out


def is_dummy(p):
    p = p.upper()
    return p in ("IMPDEMZ", "IMPNRGZ", "IMPMATZ") or (p.startswith("IMP") and p.endswith("Z"))


def compare(run_tot, ref_tot, label, lines, hard, limit=25):
    keys = set(run_tot) | set(ref_tot)
    bad = []
    for k in keys:
        a, b = run_tot.get(k, 0.0), ref_tot.get(k, 0.0)
        if abs(a - b) > max(TOL_ABS, TOL_REL * max(abs(a), abs(b))):
            bad.append((abs(a - b), k, a, b))
    bad.sort(reverse=True)
    status = "PASS" if not bad else ("FAIL" if hard else "DIFF")
    lines.append(f"\n### {label}: {status} ({len(bad)} of {len(keys)} keys differ)\n")
    if bad:
        lines.append("| key | run | reference | difference |\n|---|---|---|---|")
        for d, k, a, b in bad[:limit]:
            lines.append(f"| {' / '.join(k)} | {a:.6g} | {b:.6g} | {a - b:+.6g} |")
        if len(bad) > limit:
            lines.append(f"\n… {len(bad) - limit} more")
    return not bad


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run")
    ap.add_argument("--ref", help="reference run, e.g. the single-region FI baseline")
    ap.add_argument("--out", help="write the report to this markdown file")
    ap.add_argument("--gdxdump")
    a = ap.parse_args()
    gd = find_gdxdump(a.gdxdump)
    run = Run(a.run, gd)
    ref = Run(a.ref, gd) if a.ref else None
    ok = True
    L = [f"# Run check: {os.path.basename(a.run)}",
         f"\nRegions ({len(run.regions())}): {', '.join(run.regions())}"]

    # 1. Dummy imports
    act = run.sym("VAR_ACT")[1]
    dummy = defaultdict(float)
    for r in act:
        if is_dummy(r[3]):
            dummy[(r[0], r[3], r[2])] += Run.num(r[-1])
    dummy = {k: v for k, v in dummy.items() if abs(v) > 1e-3}
    L.append(f"\n## 1. Dummy imports: {'PASS' if not dummy else 'FAIL'}\n")
    if dummy:
        ok = False
        L.append("| region | process | year | activity |\n|---|---|---|---|")
        for (reg, p, t), v in sorted(dummy.items()):
            L.append(f"| {reg} | {p} | {t} | {v:.6g} |")
        flo = run.sym("VAR_FLO")[1]
        sup = defaultdict(float)
        for r in flo:
            if is_dummy(r[3]) and abs(Run.num(r[-1])) > 1e-3:
                sup[(r[0], r[4])] += Run.num(r[-1])
        if sup:
            L.append("\nCommodities supplied by dummy imports (find why these cannot be met):\n")
            L.append("| region | commodity | flow summed over years |\n|---|---|---|")
            for (reg, c), v in sorted(sup.items(), key=lambda x: -abs(x[1]))[:30]:
                L.append(f"| {reg} | {c} | {v:.6g} |")

    # 2. Objective
    o = run.objective()
    L.append("\n## 2. Objective\n")
    L.append(f"Run: {o:,.6g}" if o is not None else "Run: not found")
    if ref:
        orf = ref.objective()
        if o is not None and orf:
            L.append(f"\nReference: {orf:,.6g}  ·  difference {o - orf:+,.6g} ({(o - orf) / orf:+.4%})")

    # 3. Conservation of national totals
    if ref:
        L.append("\n## 3. National totals (sum over regions vs reference)")
        ok &= compare(run.total("COM_PROJ", [1, 2]), ref.total("COM_PROJ", [1, 2]),
                      "COM_PROJ demand by year, commodity", L, hard=True)
        ok &= compare(run.total("NCAP_PASTI", [2]), ref.total("NCAP_PASTI", [2]),
                      "NCAP_PASTI existing capacity by process", L, hard=True)
        compare(run.total("VAR_CAP", [1, 2]), ref.total("VAR_CAP", [1, 2]),
                "VAR_CAP installed capacity by year, process (result)", L, hard=False)
        em = lambda r: r[2] in EMISSION_COMMODITIES
        compare(run.total("VAR_COMNET", [1, 2], em), ref.total("VAR_COMNET", [1, 2], em),
                "Emissions (VAR_COMNET) by year, commodity (result)", L, hard=False)

    # 4. Internal trade
    regs = set(run.regions())
    ire = run.sym("VAR_IRE")[1]
    trade = defaultdict(float)
    for r in ire:
        # VAR_IRE(r, v, t, p, c, s, ie): keep the export side between modelled regions
        if r[0] in regs and r[-2].upper() == "EXP" and r[3].upper().startswith("TB_"):
            trade[(r[0], r[3], r[4])] += Run.num(r[-1])
    L.append("\n## 4. Internal trade (exports on TB_* links, summed over years)\n")
    if trade:
        L.append("| from region | link | commodity | flow |\n|---|---|---|---|")
        for (reg, p, c), v in sorted(trade.items(), key=lambda x: -abs(x[1]))[:40]:
            L.append(f"| {reg} | {p} | {c} | {v:.6g} |")
    else:
        L.append("No flows on internal links.")

    L.append(f"\n## Verdict: {'PASS' if ok else 'FAIL'}")
    text = "\n".join(L) + "\n"
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
    print(text)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
