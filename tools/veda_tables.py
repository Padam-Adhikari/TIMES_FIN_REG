"""Parse VEDA tables (~FI_Process, ~FI_T, ~FI_Comm) of a workbook into rows with cell addresses.
Read-only helper (openpyxl read_only). Used by the task-4 audit and tool.

    from veda_tables import read_tables
    tabs = read_tables(path)   # [{sheet, tag, tag_cell, header_row, cols: {name: col}, rows: [...]}]

Each row: {"row": n, "cells": {header: (coordinate, value, formula)}}. A table ends at the first
row whose cells under the header are all empty; columns end at the first empty header cell.
"""
import re

import openpyxl
from openpyxl.utils import get_column_letter


def _grid(ws):
    vals = {}
    for row in ws.iter_rows():
        for c in row:
            v = getattr(c, "value", None)
            if v is not None and v != "":
                vals[(c.row, c.column)] = v
    return vals


def read_tables(path, sheets=None, tags=("~FI_T", "~FI_PROCESS", "~FI_COMM")):
    wv = openpyxl.load_workbook(path, read_only=True, data_only=True)
    wf = openpyxl.load_workbook(path, read_only=True, data_only=False)
    out = []
    for name in wv.sheetnames:
        if sheets and name not in sheets:
            continue
        try:
            V = _grid(wv[name])
            Fm = _grid(wf[name])
        except Exception:
            continue
        for (r, c), v in sorted(V.items()):
            if not isinstance(v, str) or not v.strip().upper().startswith(tags):
                continue
            hr = r + 1
            cols = {}
            cc = c
            # header may start left of the tag (tables are often indented): scan left
            while (hr, cc - 1) in V:
                cc -= 1
            while (hr, cc) in V:
                h = V[(hr, cc)]
                cols[str(h).strip()] = cc
                cc += 1
            rows = []
            rr = hr + 1
            while any((rr, k) in V for k in cols.values()):
                cells = {}
                for h, k in cols.items():
                    if (rr, k) in V:
                        f = Fm.get((rr, k))
                        cells[h] = (f"{get_column_letter(k)}{rr}", V[(rr, k)],
                                    f if isinstance(f, str) and f.startswith("=") else None)
                rows.append({"row": rr, "cells": cells})
                rr += 1
            out.append({"sheet": name, "tag": v.strip(), "tag_cell": f"{get_column_letter(c)}{r}",
                        "header_row": hr, "cols": cols, "rows": rows,
                        "header_formulas": {h: Fm.get((hr, k)) for h, k in cols.items()
                                            if isinstance(Fm.get((hr, k)), str) and str(Fm.get((hr, k))).startswith("=")}})
    return out


def tech_rows(tab):
    """Rows of a ~FI_T table grouped by TechName (comment rows '*' skipped)."""
    out = {}
    tn = next((h for h in tab["cols"] if h.lower() == "techname"), None)
    cur = None
    for r in tab["rows"]:
        name = r["cells"].get(tn, (None, None, None))[1] if tn else None
        if isinstance(name, str) and name.strip():
            # '*' comment rows and '\I:' unit rows end the current block
            cur = None if name.startswith(("*", "\\I")) else name.strip()
        if cur:
            # rows without a TechName continue the process above (VEDA convention)
            out.setdefault(cur, []).append(r)
    return out
