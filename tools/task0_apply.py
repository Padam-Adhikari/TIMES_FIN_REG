"""Write the task-0 plan into the workbooks with xlwings (never openpyxl).

Called by `tools/task0.py --apply`. Safety rules:
  * every workbook must be in single-region mode (Region_selection!B8 = FINTIMES);
  * every cell is re-read before it is written and must still hold the value the dry
    run saw - any mismatch aborts that workbook without saving;
  * an existing 'RegSum' sheet is never overwritten;
  * after saving, the single-region values of every edited cell are re-read and must
    equal the old values (the switch is transparent in single-region mode).
"""
import os
import re
import shutil
import tempfile

SINGLE = "FINTIMES"
# Colour convention (CLAUDE.md): fill colours for every cell a tool writes
BLUE = "#DDEBF7"     # Region_selection switch formula
ORANGE = "#FCE4D6"   # value computed from a regional key
GREEN = "#E2EFDA"    # new Reg-only table / sheet
YELLOW = "#FFF2CC"   # needs a decision or better data
LEGEND = [("Colour legend (cells written by tools/*.py)", None),
          ("Region switch: single-region value kept, regional value added", BLUE),
          ("Value split with a regional key (see audit/keys.md)", ORANGE),
          ("New table used only in Reg-FINTIMES mode", GREEN),
          ("Needs a decision or better data (see audit/)", YELLOW)]


def write_legend(wb, log=print):
    """Legend on Region_selection (B30:C34), only into empty cells."""
    if "Region_selection" not in [s.name for s in wb.sheets]:
        return
    ws = wb.sheets["Region_selection"]
    rng = ws.range("B30:C34")
    vals = rng.value
    flat = [v for row in vals for v in (row if isinstance(row, list) else [row])]
    if any(v not in (None, "") for v in flat) and ws.range("B30").value != LEGEND[0][0]:
        log("  legend skipped: Region_selection!B30:C34 not empty")
        return
    for i, (text, colour) in enumerate(LEGEND):
        ws.range(f"C{30 + i}").value = text
        if colour:
            ws.range(f"B{30 + i}").color = colour
    ws.range("C30").api.Font.Bold = True


def _same(a, b):
    if a is None or b is None:
        return a == b or (a in ("", None) and b in ("", None))
    try:
        return abs(float(a) - float(b)) <= 1e-9 * max(1.0, abs(float(b)))
    except (TypeError, ValueError):
        return str(a).strip() == str(b).strip()


def _uc_rows(ucs):
    """Rows of the Reg-only ~UC_T table: one row per RHS year, coefficient on every row
    (same layout as the existing Scen_UC_ElcPot tables)."""
    coefs = ["UC_ACT", "UC_CAP", "UC_NCAP", "UC_FLO", "UC_COMPRD", "UC_COMNET"]
    header = ["UC_N", "Pset_PN", "Cset_CN", "Year", "LimType"] + coefs + ["UC_RHST", "UC_RHST~0", "UC_Desc"]
    rows = []
    for u in ucs:
        first = True
        for y, v in sorted(u["rhs"].items()):
            r = [u["name"], u["p"] or "", u["c"] or "", int(y), u["lim"]]
            r += [1 if c == u["coef"] else "" for c in coefs]
            r += [v, (u["ie"] if (first and u["ie"] is not None) else ""),
                  (f"national {u['attr']} {u['lim']} (task 0) from " + "; ".join(sorted(u["srcs"])))[:250]
                  if first else ""]
            rows.append(r)
            first = False
    return header, rows


def _copy_rows(copies):
    header = ["Attribute", "LimType", "Year", "TimeSlice", "Pset_PN", "Pset_PD", "Pset_CI", "Pset_CO",
              "Pset_Set", "Cset_CN", "AllRegions", "FI"]
    rows = []
    for c in copies:
        s = c["sel"]
        r = [c["attr"], c["lim"], c["year"] or "", c["ts"] or "", s.get("PN", ""), s.get("PD", ""),
             s.get("CI", ""), s.get("CO", ""), s.get("SET", ""), c["cset"] or ""]
        r += [c["value"], ""] if c["region"] == "ALLREGIONS" else ["", c["value"]]
        rows.append(r)
    return header, rows


def apply_plan(plan, root, template_book, sel, sheet_name, log=print):
    import xlwings as xw
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    results = {}
    try:
        # private copy: the template workbook may itself be one of the edited books
        tmp_dir = tempfile.mkdtemp(prefix="task0_")
        tpl_path = os.path.join(tmp_dir, "region_selection_template.xlsx")
        shutil.copyfile(os.path.join(root, template_book), tpl_path)
        tpl = app.books.open(tpl_path, update_links=False, read_only=True)
        tpl_ws = tpl.sheets["Region_selection"]
        books = sorted(set(plan.edits) | set(plan.new_tables) | set(plan.copies))
        for book in books:
            path = os.path.join(root, book)
            new_book = not os.path.exists(path)
            if new_book:
                wb = app.books.add()
                first = wb.sheets[0]
            else:
                wb = app.books.open(path, update_links=False)
            try:
                names = [s.name for s in wb.sheets]
                if "Region_selection" in names:
                    mode = wb.sheets["Region_selection"].range("B8").value
                    if mode != SINGLE:
                        raise RuntimeError(f"Region_selection!B8 = {mode!r}, expected {SINGLE!r}")
                elif book in plan.need_rs:
                    tpl_ws.copy(after=wb.sheets[-1])
                    ws = wb.sheets[-1]
                    ws.name = "Region_selection"
                    if ws.range("B8").value != SINGLE or ws.range("D8").value != SINGLE:
                        raise RuntimeError("copied Region_selection sheet is not in FINTIMES mode")
                # 1) verify every old value first (all-or-nothing per workbook); a cell that
                #    already holds the planned switch (earlier apply) is left as it is
                todo = []
                for sheet, cell, old, new, why in plan.edits.get(book, []):
                    rng = wb.sheets[sheet].range(cell)
                    if isinstance(new, str) and new.startswith("{="):      # array formula
                        done = rng.formula == new[1:-1]
                    elif isinstance(new, str) and new.startswith("="):
                        done = rng.formula == new
                    else:
                        done = _same(rng.value, new)
                    if done:
                        continue
                    if not _same(rng.value, old):
                        raise RuntimeError(f"{sheet}!{cell} holds {rng.value!r}, dry run saw {old!r}")
                    todo.append((sheet, cell, new))
                # 2) write switches
                for sheet, cell, new in todo:
                    rng = wb.sheets[sheet].range(cell)
                    if isinstance(new, str) and new.startswith("{="):
                        rng.formula_array = new[1:-1]
                    elif isinstance(new, str) and new.startswith("="):
                        rng.formula = new
                    else:
                        rng.value = new
                log(f"  {book}: {len(todo)} cell(s) written, "
                    f"{len(plan.edits.get(book, [])) - len(todo)} already in place")
                # 2b) undo cell blanks written by an earlier version of the plan
                planned = {(s, c) for s, c, *_ in plan.edits.get(book, [])}
                blank = re.compile(r'^=IF\(' + re.escape(sel) + r',(.*),""\)$')
                for ws_ in wb.sheets:
                    if ws_.name in ("Region_selection", sheet_name):
                        continue
                    ur = ws_.used_range
                    forms = ur.formula
                    if not isinstance(forms, (list, tuple)):
                        forms = ((forms,),)
                    elif forms and not isinstance(forms[0], (list, tuple)):
                        forms = (forms,)
                    for i, row in enumerate(forms):
                        for j, f in enumerate(row):
                            m = blank.match(f) if isinstance(f, str) else None
                            if not m:
                                continue
                            cell = ur[i, j]
                            addr = cell.get_address(False, False)
                            if (ws_.name, addr) in planned:
                                continue
                            inner = m.group(1)
                            try:
                                cell.value = float(inner)
                            except ValueError:
                                cell.formula = "=" + inner if not inner.startswith('"') else inner[1:-1].replace('""', '"')
                            log(f"  restored {ws_.name}!{addr} (blank from an earlier plan) -> {inner}")
                # 3) Reg-only tables (a RegSum sheet written by this tool is regenerated)
                if plan.new_tables.get(book) or plan.copies.get(book):
                    if sheet_name in [s.name for s in wb.sheets]:
                        old_ws = wb.sheets[sheet_name]
                        if not str(old_ws.range("A1").value or "").startswith("Task 0 (tools/task0.py)"):
                            raise RuntimeError(f"sheet {sheet_name} exists and was not made by this tool")
                        old_ws.delete()
                    ws = wb.sheets.add(sheet_name, after=wb.sheets[-1])
                    ws.range("A1").value = ("Task 0 (tools/task0.py): national bounds as UC_R_SUM. "
                                            "Read by VEDA only when Region_selection!B8 = Reg-FINTIMES.")
                    r = 3
                    if plan.new_tables.get(book):
                        ws.range(f"B{r}").formula = f'=IF({sel},"UC_Sets: R_S: AllRegions","~UC_Sets: R_S: AllRegions")'
                        ws.range(f"B{r+1}").formula = f'=IF({sel},"UC_Sets: T_E:","~UC_Sets: T_E:")'
                        ws.range(f"B{r+3}").formula = f'=IF({sel},"UC_T","~UC_T")'
                        hdr, rows = _uc_rows(plan.new_tables[book])
                        ws.range(f"B{r+4}").value = [hdr] + rows
                        ws.range(f"B{r}").resize(5 + len(rows), len(hdr)).color = GREEN
                        r = r + 6 + len(rows) + 2
                    if plan.copies.get(book):
                        ws.range(f"B{r}").formula = f'=IF({sel},"TFM_INS","~TFM_INS")'
                        hdr, rows = _copy_rows(plan.copies[book])
                        ws.range(f"B{r+1}").value = [hdr] + rows
                        ws.range(f"B{r}").resize(2 + len(rows), len(hdr)).color = GREEN
                # colours: every switched / written cell (idempotent)
                colours = getattr(plan, "colours", {})
                for sheet, cell, old, new, why in plan.edits.get(book, []):
                    wb.sheets[sheet].range(cell).color = colours.get((book, sheet, cell), BLUE)
                write_legend(wb, log)
                app.calculate()
                # 4) single-region transparency check before saving
                for sheet, cell, old, new, why in plan.edits.get(book, []):
                    if isinstance(new, str) and new.startswith("=IF("):
                        cur = wb.sheets[sheet].range(cell).value
                        if not _same(cur, old):
                            raise RuntimeError(f"after edit {sheet}!{cell} shows {cur!r} in single mode, "
                                               f"expected {old!r}")
                if new_book:
                    first.delete() if len(wb.sheets) > 1 and first.name.startswith("Sheet") else None
                    os.makedirs(os.path.dirname(path), exist_ok=True)
                    wb.save(path)
                else:
                    wb.save()
                results[book] = "ok"
                log(f"  saved {book}")
            except Exception as ex:          # leave the file untouched
                results[book] = f"FAILED: {ex}"
                log(f"  FAILED {book}: {ex} (not saved)")
            finally:
                wb.close()
        tpl.close()
    finally:
        app.quit()
    return results


def flip_and_read(root, books, cells, mode, log=print):
    """Test helper for copies of the model: set B8 = mode, recalc, return cell values
    {(book, sheet, cell): value}. Saves the flipped workbooks (so a rescan sees them)."""
    import xlwings as xw
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    out = {}
    try:
        for book in books:
            wb = app.books.open(os.path.join(root, book), update_links=False)
            try:
                if "Region_selection" in [s.name for s in wb.sheets]:
                    wb.sheets["Region_selection"].range("B8").value = mode
                app.calculate()
                for (b, sheet, cell) in cells:
                    if b == book:
                        out[(b, sheet, cell)] = wb.sheets[sheet].range(cell).value
                wb.save()
            finally:
                wb.close()
    finally:
        app.quit()
    return out
