"""Compare every parameter of moved processes and commodities: FI in a reference run vs each region in a new run.

CLAUDE.md rule: "after every move compare all parameters of the moved processes (single-run FI vs regional run, new
region)". A process (commodity) counts as moved into region R when it is in R's topology in the new run, was in FI's
topology in the reference run and was not in R there. Its lines of every parameter (region replaced by 'R') must be
the same. Split quantities (NCAP_PASTI, PRC_RESID, COM_PROJ, STOCK-type bounds) and UC coefficients are skipped:
they are checked by check_run (totals) and uc_ire_scan / rsum_rhs_scan.
A difference is not always an error: national bounds summed in a task-0 RS_* UC are expected to disappear.

Only the DD files that the .run file includes are read (other DD files in the folder are stale).

Usage: python tools/moved_compare.py <ref DD folder or git rev> <ref .run> <new DD folder> <new .run> [--regions R1,R2]
  e.g. python tools/moved_compare.py bd1239e 5bfix7.run GAMS_WrkTIMES 5cnewsolver.run
"""
import argparse
import collections
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {"NCAP_PASTI", "PRC_RESID", "COM_PROJ", "TOP", "TOP_IRE"}
HEAD = re.compile(r"^(?:SET\s+(\w+)|(?:PARAMETER\s+)?(\w+) ' '/)")
QUOTED = re.compile(r"'([^']*)'")


def read_text(src, name):
    if os.path.isdir(src):
        p = os.path.join(src, name)
        return open(p, encoding="latin-1").read() if os.path.exists(p) else ""
    r = subprocess.run(["git", "show", f"{src}:GAMS_WrkTIMES/{name}"], capture_output=True, cwd=ROOT)
    return r.stdout.decode("latin-1")


def dd_files(src, run):
    return re.findall(r"^\$BATINCLUDE\s+(\S+\.dd)", read_text(src, run), re.M | re.I)


def load(src, run):
    """-> topology {region: {process: {commodities}}}, rows {(region, item): {section: {lines}}}"""
    top = collections.defaultdict(lambda: collections.defaultdict(set))
    lines = []
    for f in dd_files(src, run):
        sec = None
        for line in read_text(src, f).splitlines():
            m = HEAD.match(line)
            if m:
                sec = m.group(1) or m.group(2)
                continue
            if line.startswith("/;"):
                sec = None
                continue
            if not sec or not line.startswith("'"):
                continue
            t = QUOTED.findall(line)
            if sec == "TOP" and len(t) >= 3:
                top[t[0]][t[1]].add(t[2])
            elif sec not in SKIP and not sec.startswith("UC_") and len(t) >= 2:
                lines.append((sec, t[0], line.strip()))
    return top, lines


def index(lines, regions, items):
    rows = collections.defaultdict(lambda: collections.defaultdict(set))
    for sec, r, l in lines:
        if r not in regions:
            continue
        t = QUOTED.findall(l)
        if t[1] in items:          # parameters owned by the item: indexed by it right after the region
            rows[(r, t[1])][sec].add(l.replace(f"'{r}'", "'R'", 1))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ref")
    ap.add_argument("ref_run")
    ap.add_argument("new")
    ap.add_argument("new_run")
    ap.add_argument("--regions", default="")
    a = ap.parse_args()
    t0, l0 = load(a.ref, a.ref_run)
    t1, l1 = load(a.new, a.new_run)
    regs = [r for r in sorted(t1) if r not in ("FI", "IMPEXP")]
    if a.regions:
        regs = [r for r in regs if r in a.regions.split(",")]
    moved = {}
    for r in regs:
        procs = (set(t1[r]) - set(t0.get(r, {}))) & set(t0["FI"])
        coms = ({c for cs in t1[r].values() for c in cs} - {c for cs in t0.get(r, {}).values() for c in cs}) \
            & {c for cs in t0["FI"].values() for c in cs}
        moved[r] = procs | coms
    items = set().union(*moved.values()) if moved else set()
    old = index(l0, {"FI"}, items)
    new = index(l1, set(regs), items)
    diff = collections.defaultdict(lambda: collections.defaultdict(set))   # section -> item -> regions
    example = {}
    for r in regs:
        for x in moved[r]:
            a_, b_ = old[("FI", x)], new[(r, x)]
            for s in set(a_) | set(b_):
                if a_.get(s, set()) != b_.get(s, set()):
                    diff[s][x].add(r)
                    example.setdefault(s, (x, r, sorted(a_.get(s, set()) - b_.get(s, set()))[:2],
                                           sorted(b_.get(s, set()) - a_.get(s, set()))[:2]))
    print(f"moved into {len(regs)} regions: {len(items)} processes/commodities")
    for s in sorted(diff, key=lambda s: -len(diff[s])):
        x, r, lost, extra = example[s]
        print(f"{s}: {len(diff[s])} items differ in {len(set().union(*diff[s].values()))} regions; e.g. {x} in {r}")
        for l in lost:
            print(f"    FI only: {l}")
        for l in extra:
            print(f"    {r} only: {l}")
    if not diff:
        print("all parameters of the moved items equal FI of the reference run")


if __name__ == "__main__":
    main()
