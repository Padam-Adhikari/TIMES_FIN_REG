"""Show or switch the model mode of every workbook (what select_model.xlsm does, with a log).

    python tools/model_mode.py status [--root DIR]          # read-only: mode of every workbook
    python tools/model_mode.py set Reg-FINTIMES --root DIR  # flip a COPY of the model (xlwings)

`status` also checks that the saved values were recalculated for the stated mode: in a
workbook in Reg-FINTIMES mode Region_selection!G9 must read 'FI196' (formula
=IF($B$8=$D$9,F9,"")); in FINTIMES mode it must be empty. A mismatch means VEDA would read
values of the other mode.

`set` refuses to run inside the git repository unless --allow-repo is given (flip copies,
not your working files; to switch the real model use select_model.xlsm on the server).
"""
import argparse
import os
import sys
import time

import zipfile

import openpyxl

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
FOLDERS = ["", "SubRES_TMPL", "SuppXLS", os.path.join("SuppXLS", "Trades")]


def has_switch(path):
    """Fast check (no workbook parsing): is there a sheet called Region_selection?"""
    try:
        with zipfile.ZipFile(path) as z:
            return b'name="Region_selection"' in z.read("xl/workbook.xml")
    except Exception:
        return False


def books(root):
    out = []
    for d in FOLDERS:
        p = os.path.join(root, d)
        if not os.path.isdir(p):
            continue
        for f in sorted(os.listdir(p)):
            if f.lower().endswith((".xlsx", ".xlsm")) and not f.startswith("~$") and f != "select_model.xlsm":
                out.append(os.path.join(d, f))
    return out


def status(root):
    rows = []
    for b in books(root):
        if not has_switch(os.path.join(root, b)):
            continue
        try:
            wb = openpyxl.load_workbook(os.path.join(root, b), read_only=True, data_only=True)
        except Exception as e:
            rows.append((b, "unreadable", str(e)[:40]))
            continue
        if "Region_selection" not in wb.sheetnames:
            wb.close()
            continue
        ws = wb["Region_selection"]
        mode, g9 = ws["B8"].value, ws["G9"].value
        ok = (mode == "FINTIMES" and g9 in (None, "")) or (mode == "Reg-FINTIMES" and g9 == "FI196")
        rows.append((b, mode, "ok" if ok else f"NOT RECALCULATED (G9={g9!r})"))
        wb.close()
    modes = {m for _, m, _ in rows}
    for b, m, s in rows:
        print(f"  {m or '?':13s} {s:30s} {b}")
    print(f"{len(rows)} workbooks with the switch; modes: {sorted(str(m) for m in modes)}")
    return 0 if len(modes) == 1 and all(s == "ok" for *_, s in rows) else 1


def set_mode(root, mode, log=print):
    import xlwings as xw
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    app.api.AskToUpdateLinks = False
    done = 0
    try:
        for b in books(root):
            path = os.path.join(root, b)
            if not has_switch(path):
                continue
            t = time.time()
            log(f"  {b} ...", end="", flush=True) if log is print else log(b)
            wb = app.books.open(path, update_links=False)
            try:
                ws = wb.sheets["Region_selection"]
                if ws.range("B8").value != mode:
                    ws.range("B8").value = mode
                    wb.app.calculate()
                    wb.save()
                    done += 1
                    print(f" {mode} ({time.time() - t:.0f}s)", flush=True)
                else:
                    print(" already", flush=True)
            finally:
                wb.close()
    finally:
        app.quit()
    print(f"switched {done} workbooks to {mode}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["status", "set"])
    ap.add_argument("mode", nargs="?", choices=["FINTIMES", "Reg-FINTIMES"])
    ap.add_argument("--root", default=os.path.join(ROOT, "Reg-FINTIMES"))
    ap.add_argument("--allow-repo", action="store_true")
    a = ap.parse_args()
    if a.action == "status":
        sys.exit(status(a.root))
    if not a.mode:
        sys.exit("give the mode: FINTIMES or Reg-FINTIMES")
    if os.path.abspath(a.root).startswith(ROOT) and not a.allow_repo:
        sys.exit("refusing to flip the repository; copy the model folder or use --allow-repo")
    set_mode(a.root, a.mode)


if __name__ == "__main__":
    main()
