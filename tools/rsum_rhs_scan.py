"""Pre-run check: user constraints declared R_SUM in the DD files but given only region-indexed RHS.

TIMES (ppmain.mod, v4.8.3 lines 1109-1118) turns a UC whose RHS is only UC_RHSR/UC_RHSRT/UC_RHSRTS into
UC_R_EACH and drops UC_R_SUM when there is no UC_RHS/UC_RHST/UC_RHSTS: the "national" constraint silently
becomes one constraint per region. In VEDA this happens when a table's ~UC_Sets is switched to R_S but its
RHS header stays UC_RHSR*. Found in 5b run 6 (UC_VARI_ELE_Cons_Cap, UC_VAR_MinStor5h).

Usage: python tools/rsum_rhs_scan.py [DD folder]   (default GAMS_WrkTIMES). Exit code 1 if any is found.
"""
import collections
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def scan(folder):
    rsum = collections.defaultdict(set)
    reg_rhs, nat_rhs = set(), set()
    for f in sorted(glob.glob(os.path.join(folder, "*.dd"))):
        sec = None
        with open(f, encoding="latin-1") as fh:
            for line in fh:
                m = re.match(r"^(?:SET\s+(\w+)|(\w+) ' '/)", line)
                if m:
                    sec = m.group(1) or m.group(2)
                    continue
                if line.startswith("/;"):
                    sec = None
                    continue
                if sec == "UC_R_SUM":
                    m = re.match(r"'([^']+)'\.'([^']+)'", line)
                    if m:
                        rsum[m.group(2)].add(os.path.basename(f))
                elif sec in ("UC_RHSR", "UC_RHSRT", "UC_RHSRTS"):
                    m = re.match(r"'([^']+)'\.'([^']+)'", line)
                    if m:
                        reg_rhs.add(m.group(2))
                elif sec in ("UC_RHS", "UC_RHST", "UC_RHSTS"):
                    m = re.match(r"'([^']+)'", line)
                    if m:
                        nat_rhs.add(m.group(1))
    return rsum, reg_rhs, nat_rhs


def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "GAMS_WrkTIMES")
    rsum, reg_rhs, nat_rhs = scan(folder)
    bad = sorted(u for u in rsum if u in reg_rhs and u not in nat_rhs)
    mixed = sorted(u for u in rsum if u in reg_rhs and u in nat_rhs)
    for u in bad:
        print(f"ERROR  {u}: R_SUM but only regional RHS -> TIMES makes it R_EACH  {sorted(rsum[u])}")
    for u in mixed:
        print(f"WARN   {u}: R_SUM with national and regional RHS  {sorted(rsum[u])}")
    print(f"{len(rsum)} R_SUM UCs; {len(bad)} with only regional RHS; {len(mixed)} with both")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
