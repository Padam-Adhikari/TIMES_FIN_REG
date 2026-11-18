"""Read-only scan: duplicate column headers of VEDA tables as VEDA sees them in Reg mode.

A header cell written as =IF(Region_selection!$B$8=Region_selection!$D$8,"<single>","<reg>") reads "<reg>"
in Reg mode. Two columns of one table with the same Reg-mode header stop the VEDA sync ("Veda-Tag table(s)
has duplicate column names"; task 5b: an FI column switched to AllRegions next to an existing AllRegions).

    python tools/reg_header_scan.py [workbook ...]      (default: every workbook of Reg-FINTIMES)
"""
import glob
import os
import re
import sys

import openpyxl
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from task0 import ROOT  # noqa: E402

SWITCH = re.compile(r'^=IF\(Region_selection!\$B\$8=Region_selection!\$D\$8,(.*),(.*)\)$', re.S)


def reg_value(v):
    """Reg-mode value of a header cell (constant, or the regional branch of a switch formula)."""
    if isinstance(v, str) and v.startswith("="):
        m = SWITCH.match(v)
        if not m:
            return None                     # another formula: value unknown here
        b = m.group(2).strip()
        return b[1:-1] if b.startswith('"') and b.endswith('"') else None
    return v


def scan(path):
    out = []
    wb = openpyxl.load_workbook(path, read_only=True, data_only=False)
    try:
        for ws in wb.worksheets:
            grid = {}
            for row in ws.iter_rows():
                for c in row:
                    if c.value is not None:
                        grid[(c.row, c.column)] = c.value
            for (r, col), v in grid.items():
                tag = reg_value(v)
                if not isinstance(tag, str) or not tag.strip().startswith("~") or tag.strip().upper().startswith("~UC_SETS"):
                    continue
                hr = r + 1
                cc = col
                while (hr, cc - 1) in grid:
                    cc -= 1
                heads = {}
                while (hr, cc) in grid:
                    h = reg_value(grid[(hr, cc)])
                    if isinstance(h, str) and h.strip() and not h.strip().startswith("*"):
                        key = h.strip().upper()
                        heads.setdefault(key, []).append(f"{get_column_letter(cc)}{hr}")
                    cc += 1
                for key, cells in heads.items():
                    if len(cells) > 1:
                        out.append((ws.title, f"{get_column_letter(col)}{r}", tag.strip(), key, cells))
    finally:
        wb.close()
    return out


def main():
    files = sys.argv[1:] or [f for f in glob.glob(os.path.join(ROOT, "Reg-FINTIMES", "**", "*.xls*"), recursive=True)
                             if "~$" not in f and os.sep + "AppData" + os.sep not in f]
    n = 0
    for f in sorted(files):
        try:
            hits = scan(f)
        except Exception as ex:
            print(f"{os.path.relpath(f, ROOT)}: not read ({ex})")
            continue
        for sh, cell, tag, key, cells in hits:
            n += 1
            print(f"{os.path.relpath(f, ROOT)} [{sh}] {cell} {tag}: header {key!r} twice in Reg mode: {cells}")
    print(f"{n} tables with duplicate Reg-mode headers")
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())
