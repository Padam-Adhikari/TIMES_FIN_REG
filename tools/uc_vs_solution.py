"""Evaluate the user constraints of one run with the solution of another (read-only).

Typical use: the regional run is infeasible, the single-region run solved. Every UC of the
regional run whose left-hand side only involves FI variables is evaluated with the
single-region levels; a violated UC is a candidate cause of the infeasibility.

    python tools/uc_vs_solution.py REG.gdx SOLVED.gdx [--tol 1e-4]

Limits: only UC_ACT/UC_FLO/UC_CAP/UC_NCAP/UC_COMPRD/UC_COMNET terms on the LHS, only
RHS years that are milestone years (no inter/extrapolation is redone), only UCs without
RHS-side (dynamic) terms.
"""
import argparse
import collections
import csv
import io
import shutil
import subprocess

GDXDUMP = shutil.which("gdxdump") or r"C:\GAMS\54\gdxdump.exe"


def sym(gdx, s, extra=()):
    out = subprocess.run([GDXDUMP, gdx, f"symb={s}", "format=csv", *extra], capture_output=True, text=True).stdout
    rows = list(csv.reader(io.StringIO(out)))
    return (rows[0], rows[1:]) if rows else ([], [])


def num(x):
    x = x.strip().upper()
    if x in ("EPS", ""):
        return 0.0
    if "INF" in x:
        return float("inf") * (-1 if x.startswith("-") else 1)
    return float(x)


def levels(gdx):
    """Variable levels summed to (kind, region, period, item[, comm]) and the TS map."""
    L = collections.defaultdict(float)
    for name, kind, key in (("VAR_ACT", "ACT", lambda r: (r[0], r[2], r[3])),
                            ("VAR_FLO", "FLO", lambda r: (r[0], r[2], r[3], r[4])),
                            ("VAR_CAP", "CAP", lambda r: (r[0], r[1], r[2])),
                            ("VAR_NCAP", "NCAP", lambda r: (r[0], r[1], r[2])),
                            ("VAR_COMPRD", "COMPRD", lambda r: (r[0], r[1], r[2])),
                            ("VAR_COMNET", "COMNET", lambda r: (r[0], r[1], r[2]))):
        h, rows = sym(gdx, name, ("CSVAllFields",))
        if not h:
            continue
        il = h.index("Val")
        for r in rows:
            k = key(r)
            # timeslice-resolved variables are summed (UCs below are matched on ANNUAL)
            L[(kind,) + tuple(k)] += num(r[il])
    return L


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("reg")
    ap.add_argument("solved")
    ap.add_argument("--tol", type=float, default=1e-4)
    a = ap.parse_args()
    mil = {r[0] for r in sym(a.reg, "MILESTONYR")[1]}
    L = levels(a.solved)
    lhs = collections.defaultdict(float)        # (uc, t) -> value
    has = collections.defaultdict(set)
    dynamic = set()
    spec = {"UC_ACT": ("ACT", 4, None), "UC_FLO": ("FLO", 4, 5), "UC_CAP": ("CAP", 4, None),
            "UC_NCAP": ("NCAP", 4, None), "UC_COMPRD": ("COMPRD", 4, None), "UC_COMNET": ("COMNET", 4, None)}
    exact = {"UC_ACT", "UC_FLO", "UC_CAP", "UC_NCAP"}
    for s, (kind, ip, ic) in spec.items():
        h, rows = sym(a.reg, s)
        for r in rows:
            uc, side, reg, t = r[0], r[1], r[2], r[3]
            ts = r[-2] if kind in ("ACT", "FLO", "COMPRD", "COMNET") else "ANNUAL"
            if ts != "ANNUAL":
                has[uc].add("ts-level")
                continue
            if s not in exact:
                has[uc].add("prd/net term (no exact level)")
                continue
            if side != "LHS":
                dynamic.add(uc)
                continue
            if reg != "FI":
                has[uc].add("non-FI")
                continue
            coef = num(r[-1])
            item = r[ip]
            k = (kind, reg, t, item) + ((r[ic],) if ic else ())
            lhs[(uc, t)] += coef * L.get(k, 0.0)
            has[uc].add(t)
    viol, checked = [], set()
    for s in ("UC_RHST", "UC_RHSRT", "UC_RHSTS", "UC_RHSRTS"):
        h, rows = sym(a.reg, s)
        for r in rows:
            if s.startswith("UC_RHSR"):
                reg, uc, t = r[0], r[1], r[2]
                if reg != "FI":
                    continue
            else:
                uc, t = r[0], r[1]
            lim, v = r[-2], num(r[-1])
            if s.endswith("TS") and r[-3] != "ANNUAL":
                continue
            if t not in mil or uc in dynamic or t not in has[uc] or has[uc] & {"non-FI", "ts-level", "prd/net term (no exact level)"}:
                continue
            checked.add(uc)
            x = lhs[(uc, t)]
            bad = (lim == "LO" and x < v - a.tol * max(1, abs(v))) or \
                  (lim == "UP" and x > v + a.tol * max(1, abs(v))) or \
                  (lim == "FX" and abs(x - v) > a.tol * max(1, abs(v)))
            if bad:
                viol.append((uc, t, lim, v, round(x, 6)))
    skipped = {u for u in has if u not in checked}
    print(f"UCs checked: {len(checked)} (FI-only, annual, milestone years); skipped: {len(skipped)} "
          f"(dynamic, timeslice-level or with non-FI terms)")
    print(f"violated by the solved run: {len(viol)}")
    for x in sorted(viol)[:60]:
        print("  ", x)


if __name__ == "__main__":
    main()
