"""Evaluate workbooks in Reg mode before a server run (read-only on the model: works on copies).

Copies each workbook to a temporary folder, opens it with Excel (xlwings), sets Region_selection!B8 to
the multi-region model, recalculates and reports every formula cell that is an Excel error (#VALUE!, #REF!, ...) in Reg mode
but not in single mode. Errors in Reg mode are silently dropped by VEDA (lesson of task 4b:
pulp stocks referenced blanked generic cells and vanished in the regional run).

    python tools/regmode_check.py Reg-FINTIMES/VT_FINTIMES_IND.xlsx [more workbooks ...]
"""
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from task0 import ROOT  # noqa: E402

XL_FORMULAS, XL_ERRORS = -4123, 16


def check(paths):
    import xlwings as xw
    tmp = tempfile.mkdtemp(prefix="regmode_")
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    total = 0
    try:
        for rel in paths:
            src = os.path.join(ROOT, rel)
            dst = os.path.join(tmp, os.path.basename(rel))
            shutil.copyfile(src, dst)
            wb = app.books.open(dst, update_links=False)
            try:
                names = [s.name for s in wb.sheets]
                if "Region_selection" not in names:
                    print(f"{rel}: no Region_selection sheet - skipped")
                    continue
                rs = wb.sheets["Region_selection"]
                def errors():
                    app.calculate()
                    out = {}
                    for ws in wb.sheets:
                        try:
                            errs = ws.api.UsedRange.SpecialCells(XL_FORMULAS, XL_ERRORS)
                        except Exception:
                            continue          # no error cells on this sheet
                        out[ws.name] = {c.Address.replace("$", "") for c in errs}
                    return out
                single = errors()
                rs.range("B8").value = rs.range("D9").value
                reg = errors()
                n = 0
                for sh, cells in reg.items():
                    new = sorted(cells - single.get(sh, set()))
                    if new:
                        n += len(new)
                        print(f"{rel} [{sh}]: {len(new)} cells are errors only in Reg mode, e.g. {new[:10]}")
                print(f"{rel}: {n} new error cells in Reg mode "
                      f"(errors already in single mode: {sum(len(v) for v in single.values())})")
                total += n
            finally:
                wb.close()
    finally:
        app.quit()
        shutil.rmtree(tmp, ignore_errors=True)
    return total


if __name__ == "__main__":
    sys.exit(1 if check(sys.argv[1:]) else 0)
