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


def copy_proc(a):
    """Processes still FI-only whose partner moved (e.g. P_COMBATS01 for COMBATS01): every FI line that names one
    of them is copied to each region where the partner is in the topology - what VEDA writes once the process is
    available there (~TFM_AVA). The region is the first quoted token, or the second in UC_* coefficient lines.
    Sections matching --skip (e.g. the FI-hub-only variable-RES UCs) are left alone."""
    regions_of = topology(a.new, a.new_run)
    procs = {p for p in regions_of if re.fullmatch(a.procs, p)}
    if not procs:
        sys.exit(f"no process matches {a.procs}")
    target = {}
    for p in procs:
        partner = re.sub(a.partner_from, a.partner_to, p)
        target[p] = sorted(regions_of.get(partner, set()) - {"FI"} - regions_of[p])
    skip = re.compile(a.skip) if a.skip else None
    files = re.findall(r"^\$BATINCLUDE\s+(\S+\.dd)", read(a.new, a.new_run), re.M | re.I)
    out_dir = os.path.join(ROOT, "cluster", "patches", a.name)
    os.makedirs(out_dir, exist_ok=True)
    total = collections.Counter()
    for f in files:
        pre = os.path.join(out_dir, f)
        text = open(pre, encoding="latin-1").read() if os.path.exists(pre) else read(a.new, f)
        if not any(f"'{p}'" in text for p in procs):
            continue
        lines, out, sec, changed = text.splitlines(), [], None, False
        for line in lines:
            out.append(line)
            m = HEAD.match(line)
            if m:
                sec = m.group(1) or m.group(2)
                continue
            if line.startswith("/;"):
                sec = None
                continue
            if not sec or not line.startswith("'") or (skip and skip.search(sec + " " + line)):
                continue
            t = Q.findall(line)
            p = next((x for x in t if x in procs), None)
            if not p:
                continue
            pos = 1 if sec.startswith("UC_") and len(t) > 1 and t[1] == "FI" else (0 if t[0] == "FI" else None)
            if pos is None:
                continue
            for r in target[p]:
                if pos == 0:
                    new = line.replace("'FI'", f"'{r}'", 1)
                else:
                    i = line.index("'FI'", line.index("'") + len(t[0]) + 2)
                    new = line[:i] + f"'{r}'" + line[i + 4:]
                out.append(new)
                total[(f, sec)] += 1
                changed = True
        if changed:
            with open(pre, "w", encoding="latin-1", newline="\n") as fh:
                fh.write("\n".join(out) + "\n")
    for (f, s), n in sorted(total.items()):
        print(f"{f} {s}: +{n} lines")
    print(f"{sorted(procs)} -> regions of their partners ({', '.join(f'{p}: {len(r)}' for p, r in sorted(target.items()))})"
          f"; patched files in cluster/patches/{a.name}/")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("copy-proc")
    p.add_argument("name")
    p.add_argument("--new", required=True)
    p.add_argument("--new-run", required=True)
    p.add_argument("--procs", required=True, help="regex of the FI-only processes, e.g. 'P_COMBATS0[1-3]'")
    p.add_argument("--partner-from", default=r"^P_", help="regex turning the process name into its partner's")
    p.add_argument("--partner-to", default="")
    p.add_argument("--skip", default="", help="regex on '<section> <line>' to leave alone")
    p = sp.add_parser("copy-fi")
    p.add_argument("name")
    p.add_argument("--ref", required=True)
    p.add_argument("--new", required=True)
    p.add_argument("--new-run", required=True)
    p.add_argument("--file", required=True)
    p.add_argument("--section", required=True)
    p.add_argument("--match", default=".")
    a = ap.parse_args()
    copy_proc(a) if a.cmd == "copy-proc" else copy_fi(a)


if __name__ == "__main__":
    main()
