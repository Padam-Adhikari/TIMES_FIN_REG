"""Read-only check: every formula of the git HEAD version of a workbook is still there, unchanged,
except cells listed in a dry-run file (planned edits). Also lists external links.

    python tools/formula_diff.py audit/task3_power_dryrun.txt BOOK [BOOK ...]
"""
import io
import re
import subprocess
import sys
import warnings
import zipfile

import openpyxl

warnings.filterwarnings("ignore")


def formulas(src):
    wb = openpyxl.load_workbook(src, read_only=True, data_only=False)
    d = {}
    for ws in wb.worksheets:
        try:
            for row in ws.iter_rows():
                for c in row:
                    v = getattr(c, "value", None)
                    if v is not None and not isinstance(v, (int, float, str)):
                        v = getattr(v, "text", str(v))
                    if isinstance(v, str) and v.startswith("="):
                        d[(ws.title, c.coordinate)] = v
        except Exception:
            pass
    return d


def main():
    dry, books = sys.argv[1], sys.argv[2:]
    planned, cur = set(), None
    for l in open(dry, encoding="utf-8"):
        m = re.match(r"^--- (.+)$", l)
        if m:
            cur = m.group(1).strip()
        m = re.match(r"^  ~ '(.+)'!([A-Z]+\d+) ", l)
        if m and cur:
            planned.add((cur, m.group(1), m.group(2)))
    bad = 0
    for b in books:
        head = subprocess.run(["git", "show", f"HEAD:{b}"], capture_output=True).stdout
        a = formulas(io.BytesIO(head))
        n = formulas(b)
        lost = [k for k in a if k not in n and (b, *k) not in planned]
        changed = [k for k in a if k in n and a[k] != n[k] and (b, *k) not in planned]
        z = zipfile.ZipFile(b)
        ext = [t for x in z.namelist() if x.startswith("xl/externalLinks/_rels")
               for t in re.findall(r'Target="([^"]+)"', z.read(x).decode())]
        zh = zipfile.ZipFile(io.BytesIO(head))
        exth = [t for x in zh.namelist() if x.startswith("xl/externalLinks/_rels")
                for t in re.findall(r'Target="([^"]+)"', zh.read(x).decode())]
        newext = [t for t in ext if t not in exth]
        print(f"{b}: HEAD formulas {len(a)}, lost {len(lost)}, changed {len(changed)}, new external links {newext}")
        for k in (lost + changed)[:10]:
            print("    ", k, a[k][:80], "->", n.get(k, "<value>")[:80] if isinstance(n.get(k), str) else n.get(k))
        bad += len(lost) + len(changed) + len(newext)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
