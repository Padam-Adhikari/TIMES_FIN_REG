"""Test a workbook fix in the DD files first (CLAUDE.md): write a patched copy of one DD file for cluster_run.py.

copy-fi: the FI lines of <section> in <file> of a reference run whose process matches --match are added for every
region where that process is in the topology of the new run - what VEDA writes once the table's FI column becomes
AllRegions (a Copy-rule fix). Lines already present are kept; the patched file goes to cluster/patches/<name>/<file>.

  python tools/dd_patch.py copy-fi <name> --ref bd1239e --new GAMS_WrkTIMES --new-run 5cnewsolver.run
         --file uc_rsd-com.dd --section ACT_EFF --match "^C_ES-"
--ref: a git revision (its GAMS_WrkTIMES) or a folder.
"""
import argparse
import collections
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEAD = re.compile(r"^(?:SET\s+(\w+)|(?:PARAMETER\s+)?(\w+) ' '/)")
Q = re.compile(r"'([^']*)'")


def read(src, name):
    if os.path.isdir(os.path.join(ROOT, src)):
        return open(os.path.join(ROOT, src, name), encoding="latin-1").read()
    r = subprocess.run(["git", "show", f"{src}:GAMS_WrkTIMES/{name}"], capture_output=True, cwd=ROOT)
    if r.returncode:
        sys.exit(f"{src}:{name} not found")
    return r.stdout.decode("latin-1")


def topology(folder, run):
    procs = collections.defaultdict(set)
    files = re.findall(r"^\$BATINCLUDE\s+(\S+\.dd)", read(folder, run), re.M | re.I)
    for f in files:
        sec = None
        for line in read(folder, f).splitlines():
            m = HEAD.match(line)
            if m:
                sec = m.group(1) or m.group(2)
            elif line.startswith("/;"):
                sec = None
            elif sec == "TOP":
                t = Q.findall(line)
                if len(t) >= 2:
                    procs[t[1]].add(t[0])
    return procs


def section_lines(text, section):
    out, sec = [], None
    for line in text.splitlines():
        m = HEAD.match(line)
        if m:
            sec = m.group(1) or m.group(2)
        elif line.startswith("/;"):
            sec = None
        elif sec == section and line.startswith("'"):
            out.append(line.rstrip())
    return out


def copy_fi(a):
    regions_of = topology(a.new, a.new_run)
    rx = re.compile(a.match)
    ref = section_lines(read(a.ref, a.file), a.section)
    new_text = read(a.new, a.file)
    have = set(section_lines(new_text, a.section))
    add, procs = [], set()
    for line in ref:
        t = Q.findall(line)
        if not t or t[0] != "FI":
            continue
        p = next((x for x in t[1:] if x in regions_of), None)
        if not p or not rx.search(p):
            continue
        procs.add(p)
        for r in sorted(regions_of[p]):
            new = line.replace("'FI'", f"'{r}'", 1)
            if new not in have:
                add.append(new)
                have.add(new)
    if not add:
        sys.exit("nothing to add")
    lines = new_text.splitlines()
    head = next((i for i, l in enumerate(lines) if (m := HEAD.match(l)) and (m.group(1) or m.group(2)) == a.section),
                None)
    if head is None:                                   # section absent: append a new one
        lines += ["", f"PARAMETER {a.section} ' '/"] + add + ["/;"]
    else:
        end = next(i for i in range(head + 1, len(lines)) if lines[i].startswith("/;"))
        lines[end:end] = add
    out = os.path.join(ROOT, "cluster", "patches", a.name)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, a.file), "w", encoding="latin-1", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    regs = sorted({l.split(".")[0] for l in add})
    print(f"{a.file} {a.section}: {len(add)} lines added for {len(procs)} processes in {len(regs)} regions "
          f"-> cluster/patches/{a.name}/{a.file}")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("copy-fi")
    p.add_argument("name")
    p.add_argument("--ref", required=True)
    p.add_argument("--new", required=True)
    p.add_argument("--new-run", required=True)
    p.add_argument("--file", required=True)
    p.add_argument("--section", required=True)
    p.add_argument("--match", default=".")
    a = ap.parse_args()
    copy_fi(a)


if __name__ == "__main__":
    main()
