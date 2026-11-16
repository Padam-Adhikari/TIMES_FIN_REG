"""Detailed read-only audit of a solved regional run against the single-region reference run.

    python tools/audit_run.py RUN.gdx --ref REF.gdx --out audit/<name>.md

Sections (every number is national = summed over the internal regions unless stated):
  A  objective and its components (REG_WOBJ), per region
  B  hard checks: dummy imports, COM_PROJ, NCAP_PASTI (year 0 = interpolation code, ignored)
  C  moved power/CHP plants: activity by class and year vs reference, activity left on FI
  D  electricity (ELCHIG) and heat (HETHTH) production by year; prices FI vs regions
  E  internal links: flow by commodity, back-and-forth (cycling) on the same link/year/timeslice
  F  emissions and certificates: production by year vs reference; regional net = 0 (all to hub)
  G  peak equations: where they exist and bind
  H  2030 coal phase-out: capacity of coal/peat classes after 2030
  I  user constraints: shadow prices run vs reference (binding in one run only)
  J  taxes/penalties (CST_COMX, CST_FLOX), largest cost and capacity differences by process
"""
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from check_run import Run, find_gdxdump, is_dummy  # noqa: E402

MOVED = re.compile(r"^(EEPP_|ECHP_|ENFI_|EUHYDDAM00$)")
EMIS = ["ELCCO2N", "ETSCO2", "TOTCO2", "INDCO2N", "GreenCert-ELC", "GreenCert-FIN"]
HUB = "FI"
TOL = 1e-6


class G(Run):
    def rows(self, name, allfields=False):
        if not allfields:
            return self.sym(name)[1]
        key = name + "#all"
        if key not in self._cache:
            import csv
            import io
            import subprocess
            res = subprocess.run([self.gdxdump, self.path, f"symb={name}", "format=csv", "CSVAllFields"],
                                 capture_output=True, text=True)
            rows = list(csv.reader(io.StringIO(res.stdout))) if res.returncode == 0 else []
            self._cache[key] = (rows[0], rows[1:]) if rows else ([], [])
        return self._cache[key][1]

    def agg(self, name, key, filt=None, internal=True):
        regs = set(self.regions())
        out = collections.defaultdict(float)
        for r in self.rows(name):
            if internal and r[0] not in regs:
                continue
            if filt and not filt(r):
                continue
            out[key(r)] += self.num(r[-1])
        return out


def fmt(x):
    return f"{x:,.1f}" if abs(x) >= 100 else f"{x:,.4g}"


def table(L, head, rows):
    L.append("| " + " | ".join(head) + " |")
    L.append("|" + "---|" * len(head))
    for r in rows:
        L.append("| " + " | ".join(fmt(x) if isinstance(x, float) else str(x) for x in r) + " |")
    L.append("")


def diff_rows(a, b, n=15, rel=1e-4):
    rows = []
    for k in set(a) | set(b):
        x, y = a.get(k, 0.0), b.get(k, 0.0)
        if abs(x - y) > max(TOL, rel * max(abs(x), abs(y))):
            rows.append((abs(x - y), k, x, y))
    rows.sort(key=lambda t: -t[0])
    return [(" / ".join(map(str, k)) if isinstance(k, tuple) else k, x, y, x - y) for _, k, x, y in rows[:n]], len(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run")
    ap.add_argument("--ref", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--gdxdump")
    a = ap.parse_args()
    gx = find_gdxdump(a.gdxdump)
    R, F = G(a.run, gx), G(a.ref, gx)
    regs = R.regions()
    L = [f"# Audit of {os.path.basename(a.run)} vs {os.path.basename(a.ref)}", "",
         f"Regions in run: {len(regs)} ({', '.join(regs)})", ""]
    hard = []

    # A objective
    L.append("## A. Objective")
    o1, o2 = R.objective(), F.objective()
    L.append(f"Run {o1:,.2f} M EUR, reference {o2:,.2f}, difference {o1 - o2:+,.2f} ({(o1 - o2) / o2:+.4%})\n")
    wa = R.agg("REG_WOBJ", lambda r: r[1], internal=False)
    wb = F.agg("REG_WOBJ", lambda r: r[1], internal=False)
    table(L, ["component", "run", "reference", "difference"],
          [(k, wa.get(k, 0.0), wb.get(k, 0.0), wa.get(k, 0.0) - wb.get(k, 0.0)) for k in sorted(set(wa) | set(wb))])
    ro = R.agg("REG_OBJ", lambda r: r[0], internal=False)
    table(L, ["region", "objective share"], sorted(((k, v) for k, v in ro.items()), key=lambda t: -abs(t[1]))[:21])

    # B hard checks
    L.append("## B. Hard checks")
    dum = R.agg("PAR_ACTL", lambda r: (r[0], r[3]), filt=lambda r: is_dummy(r[3]), internal=False)
    dum = {k: v for k, v in dum.items() if abs(v) > TOL}
    L.append(f"- Dummy import activity: {'none' if not dum else dum}")
    if dum:
        hard.append("dummy imports")
    for name, kc, filt in (("COM_PROJ", lambda r: (r[1], r[2]), None),
                           ("NCAP_PASTI", lambda r: r[2], lambda r: r[1] != "0"),
                           ("PRC_RESID", lambda r: (r[2], r[1]), lambda r: r[1] != "0")):
        rows, n = diff_rows(R.agg(name, kc, filt), F.agg(name, kc, filt), rel=1e-9)
        L.append(f"- {name} national totals: {'conserved' if n == 0 else f'{n} keys differ'}")
        if n:
            hard.append(name)
            table(L, ["key", "run", "reference", "diff"], rows)
    L.append("")

    # C moved plants
    L.append("## C. Existing power/CHP plants moved to the regions (activity, PJ)")
    act_r = R.agg("PAR_ACTL", lambda r: (r[3], r[2]), filt=lambda r: MOVED.match(r[3]))
    act_f = F.agg("PAR_ACTL", lambda r: (r[3], r[2]), filt=lambda r: MOVED.match(r[3]))
    left = R.agg("PAR_ACTL", lambda r: r[3], filt=lambda r: r[0] == HUB and MOVED.match(r[3]))
    left = {k: v for k, v in left.items() if abs(v) > TOL}
    L.append(f"- Activity of these classes left on the FI hub: {'none' if not left else left}")
    tot_r = collections.defaultdict(float)
    tot_f = collections.defaultdict(float)
    for (p, t), v in act_r.items():
        tot_r[p] += v
    for (p, t), v in act_f.items():
        tot_f[p] += v
    table(L, ["class", "run (all years)", "reference", "difference"],
          sorted(((p, tot_r.get(p, 0.0), tot_f.get(p, 0.0), tot_r.get(p, 0.0) - tot_f.get(p, 0.0))
                  for p in set(tot_r) | set(tot_f)), key=lambda t: -abs(t[3])))
    rows, n = diff_rows(act_r, act_f, n=12, rel=1e-3)
    L.append(f"By class and year: {n} differ by more than 0.1 %; largest:\n")
    table(L, ["class / year", "run", "reference", "diff"], rows)
    per_reg = R.agg("PAR_ACTL", lambda r: r[0], filt=lambda r: MOVED.match(r[3]))
    table(L, ["region", "activity of moved classes (all years)"], sorted(per_reg.items()))

    # D electricity and heat
    L.append("## D. Electricity and heat production (excluding internal links)")
    for c in ("ELCHIG", "HETHTH"):
        f = (lambda c: lambda r: r[4] == c and not r[3].startswith("TB_"))(c)
        pr = R.agg("F_OUT", lambda r: r[2], f)
        pf = F.agg("F_OUT", lambda r: r[2], f)
        rows = [(t, pr.get(t, 0.0), pf.get(t, 0.0), pr.get(t, 0.0) - pf.get(t, 0.0)) for t in sorted(set(pr) | set(pf))]
        L.append(f"### {c} production by year (PJ)")
        table(L, ["year", "run", "reference", "diff"], rows)
    # prices: balance marginals (annual average of timeslice prices weighted equally)
    for c in ("ELCHIG", "HETHTH"):
        for nm in ("PAR_COMBALEM", "PAR_COMBALGM"):
            pr = collections.defaultdict(list)
            for r in R.rows(nm):
                if r[2] == c:
                    pr[(r[0], r[1])].append(R.num(r[-1]))
            if not pr:
                continue
            years = sorted({t for _, t in pr})[::3]
            hub = {t: sum(v) / len(v) for (rg, t), v in pr.items() if rg == HUB}
            spread = collections.defaultdict(float)
            for (rg, t), v in pr.items():
                if rg != HUB and t in hub:
                    spread[t] = max(spread[t], abs(sum(v) / len(v) - hub[t]))
            L.append(f"### {c} price ({nm}, mean over timeslices): hub vs largest regional deviation")
            table(L, ["year", "FI hub", "max |region - hub|"], [(t, hub.get(t, 0.0), spread.get(t, 0.0)) for t in years])

    # E links
    L.append("## E. Internal links (TB_*)")
    ire = collections.defaultdict(float)
    both = collections.defaultdict(lambda: [0.0, 0.0])
    for r in R.rows("PAR_IRE"):
        if not r[3].startswith("TB_") or r[0] != HUB:
            continue
        v = R.num(r[-1])
        ire[(r[4], r[6])] += v
        both[(r[3], r[2], r[5])][0 if r[6] == "IMP" else 1] += v
    table(L, ["commodity", "into hub (IMP at FI)", "out of hub (EXP at FI)"],
          sorted(((c, ire.get((c, "IMP"), 0.0), ire.get((c, "EXP"), 0.0)) for c in {k[0] for k in ire}),
                 key=lambda t: -(t[1] + t[2])))
    cyc = [(k, min(v)) for k, v in both.items() if min(v) > 1e-4]
    vol = sum(m for _, m in cyc)
    L.append(f"- Back-and-forth on the same link, year and timeslice: {len(cyc)} cases, volume {vol:,.4g}")
    if cyc:
        table(L, ["link / year / ts", "min(imp, exp)"], [(" / ".join(k), m) for k, m in sorted(cyc, key=lambda t: -t[1])[:10]])

    # F emissions
    L.append("## F. Emissions and certificates")
    for c in EMIS:
        f = (lambda c: lambda r: r[4] == c and not r[3].startswith("TB_"))(c)
        pr, pf = R.agg("F_OUT", lambda r: r[2], f), F.agg("F_OUT", lambda r: r[2], f)
        if not pr and not pf:
            continue
        tr, tf = sum(pr.values()), sum(pf.values())
        rows, n = diff_rows(pr, pf, n=5, rel=1e-3)
        L.append(f"- {c}: produced, all years: run {tr:,.1f}, reference {tf:,.1f} ({(tr - tf) / tf if tf else 0:+.2%}); {n} years differ >0.1 %")
    regnet = collections.defaultdict(float)
    for nm in ("PAR_FLO",):
        for r in R.rows(nm):
            pass
    # regional net = production - exports on links must be 0 for the FX commodities
    prod = R.agg("F_OUT", lambda r: (r[0], r[4]), lambda r: r[0] != HUB and r[4] in ("ELCCO2N", "ETSCO2", "GreenCert-ELC")
                 and not r[3].startswith("TB_"))
    expo = collections.defaultdict(float)
    for r in R.rows("PAR_IRE"):
        if r[0] != HUB and r[3].startswith("TB_") and r[4] in ("ELCCO2N", "ETSCO2", "GreenCert-ELC"):
            expo[(r[0], r[4])] += R.num(r[-1]) * (1 if r[6] == "EXP" else -1)
    bad = {k: prod.get(k, 0.0) - expo.get(k, 0.0) for k in set(prod) | set(expo)
           if abs(prod.get(k, 0.0) - expo.get(k, 0.0)) > 1e-3 * max(1.0, abs(prod.get(k, 0.0)))}
    kept = collections.defaultdict(float)
    for (rg, c), v in bad.items():
        kept[c] += v
    L.append(f"- Counted in the region where emitted (production - net export to the hub), all years: "
             f"{ {c: round(v, 1) for c, v in kept.items()} or 'none'} (regional COM_BNDNET makes the net free; "
             f"correct as long as the national targets sum the regions, checked next)")
    # every national CO2 target must have terms in every region that emits CO2
    emitters = {r[0] for r in R.rows("F_OUT") if r[4] in ("ELCCO2N", "ETSCO2", "INDCO2N", "TOTCO2")
                and r[0] != HUB and R.num(r[-1]) > 1e-6}
    uct = collections.defaultdict(set)
    for nm in ("UC_COMNET", "UC_COMPRD"):
        for r in R.rows(nm):
            if re.search(r"CO2|cement|ESR", r[0], re.I):
                uct[r[0]].add(r[2])
    for uc, rr in sorted(uct.items()):
        miss = sorted(emitters - rr)
        L.append(f"- {uc}: terms in {len(rr)} regions" + (f"; MISSING emitting regions {miss}" if miss else ""))
        if miss:
            hard.append(f"{uc} misses regions")
    L.append("")

    # G peak
    L.append("## G. Peak equations (EQ_PEAK)")
    pk = collections.defaultdict(lambda: [0, 0, 0.0])
    for r in R.rows("EQ_PEAK", allfields=True):
        k = (r[0], r[2])
        pk[k][0] += 1
        m = abs(R.num(r[5]))
        if m > 1e-6:
            pk[k][1] += 1
            pk[k][2] += m
    table(L, ["region / commodity", "equations", "binding", "sum |shadow price|"],
          [(" / ".join(k), v[0], v[1], v[2]) for k, v in sorted(pk.items())])
    regional = [k for k in pk if k[0] != HUB]
    L.append(f"- Peak equations outside the hub: {len(regional)} region/commodity pairs "
             f"({'expected none in the hub design' if regional else 'none, as intended'})\n")

    # H coal
    L.append("## H. 2030 coal phase-out")
    coal = R.agg("VAR_CAP", lambda r: (r[0], r[2]), lambda r: re.match(r"^E(CHP|EPP)_(coal|lignite)_thermal$", r[2])
                 and int(r[1]) >= 2030)
    coal = {k: v for k, v in coal.items() if v > 1e-6}
    L.append(f"- Capacity of coal/peat classes from 2030: {'none' if not coal else coal}\n")
    if coal:
        hard.append("coal phase-out")

    # I user constraints (shadow prices of VAR_UC* incl. R_SUM)
    L.append("## I. User constraints: shadow prices")

    def ucm(run):
        out = collections.defaultdict(float)
        for nm, pos in (("VAR_UC", None), ("VAR_UCR", None), ("VAR_UCT", 1), ("VAR_UCTS", 1),
                        ("VAR_UCRT", 2), ("VAR_UCRTS", 2)):
            for r in run.rows(nm, allfields=True):
                if len(r) < 3:
                    continue
                m = run.num(r[len(r) - 4])
                if abs(m) > 1e-6:
                    out[r[0]] += abs(m)
        return out
    ua, ub = ucm(R), ucm(F)
    only_r = sorted((k for k in ua if k not in ub), key=lambda k: -ua[k])
    only_f = sorted((k for k in ub if k not in ua), key=lambda k: -ub[k])
    L.append(f"- Binding in both: {len(set(ua) & set(ub))}; only in run: {len(only_r)}; only in reference: {len(only_f)}")
    table(L, ["binding only in run", "sum |shadow|"], [(k, ua[k]) for k in only_r[:15]])
    table(L, ["binding only in reference", "sum |shadow|"], [(k, ub[k]) for k in only_f[:15]])
    rows, n = diff_rows(ua, ub, n=15, rel=0.05)
    L.append(f"Shadow prices differing by more than 5 %: {n}; largest:\n")
    table(L, ["UC", "run", "reference", "diff"], rows)

    # J taxes and largest differences
    L.append("## J. Taxes/penalties and largest differences by process")
    for nm in ("CST_COMX", "CST_FLOX"):
        xa = R.agg(nm, lambda r: (r[0], r[1], r[2]) if nm == "CST_COMX" else (r[0], r[3]), internal=False)
        xb = F.agg(nm, lambda r: (r[0], r[1], r[2]) if nm == "CST_COMX" else (r[0], r[3]), internal=False)
        rows, n = diff_rows(xa, xb, n=10)
        L.append(f"- {nm}: {n} entries differ")
        if rows:
            table(L, ["key", "run", "reference", "diff"], rows)
    for nm, lab in (("CST_INVC", "investment"), ("CST_FIXC", "fixed O&M"), ("CST_ACTC", "activity"),
                    ("CST_FLOC", "flow/import"), ("VAR_CAP", "capacity (sum over years)")):
        kc = (lambda r: r[3]) if nm.startswith("CST") else (lambda r: r[2])
        rows, n = diff_rows(R.agg(nm, kc, internal=False), F.agg(nm, kc, internal=False), n=12, rel=1e-3)
        L.append(f"### {lab}: {n} processes differ; largest")
        table(L, ["process", "run", "reference", "diff"], rows)

    L.append("## Verdict")
    L.append("FAIL: " + ", ".join(hard) if hard else "Hard checks pass (dummy imports, inputs conserved, "
             "regional emissions sent to the hub, coal phase-out).")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"written {a.out}; " + ("FAIL: " + ", ".join(hard) if hard else "hard checks pass"))
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()
