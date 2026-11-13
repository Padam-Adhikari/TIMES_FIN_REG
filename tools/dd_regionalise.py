"""Prototype regionalisation steps directly in VEDA's DD files (read server DDs, write new DDs).

Used to TEST a regionalisation design locally before (and to CHECK it after) the Excel
implementation: the DD files VEDA writes from the edited workbooks must match these.

Operations (all line-based on VEDA's DD syntax: blocks 'SET X' / 'NAME ' '/' ... '/;'):
  add_regions(template='FI1B1', new=[...])   clone every line of an empty region
  move_process(p, shares, keep_fi=False)      clone p's FI lines to regions, scale capacity
  add_link(commodity, region)                 clone the TB_GASBFG_FI_FI1D9 link definition
  uc_* helpers                                 make UCs national / per region

Usage (example): python tools/dd_regionalise.py --src GAMS_WrkTIMES --run baseline-reg.run --out DIR
"""
import argparse
import collections
import csv
import os
import re
import shutil

ALL20 = ["FI", "FI196", "FI198", "FI199", "FI19A", "FI19B", "FI1B1", "FI1C1", "FI1C2", "FI1C5", "FI1C6",
         "FI1C7", "FI1D5", "FI1D7", "FI1D8", "FI1D9", "FI1DA", "FI1DB", "FI1DC", "FI200"]
CAPACITY = {"NCAP_PASTI", "PRC_RESID"}          # split by share
TOK = re.compile(r"'([^']*)'")


class DD:
    """One DD file as a list of blocks: (kind, name, header_lines, data_lines, footer)."""

    def __init__(self, path):
        self.path = path
        self.pre, self.blocks = [], []
        lines = open(path, encoding="latin-1").read().split("\n")
        i = 0
        cur = None
        while i < len(lines):
            l = lines[i]
            m_set = re.match(r"^SET\s+([A-Z_][A-Z0-9_]*)", l)
            m_par = re.match(r"^([A-Z_][A-Z0-9_]*) ' '/\s*$", l)
            if m_set and cur is None:
                cur = dict(kind="SET", name=m_set.group(1), head=[l], data=[], foot=None)
                i += 1
                # header continues until the opening '/'
                while i < len(lines) and lines[i].strip() != "/":
                    cur["head"].append(lines[i]); i += 1
                cur["head"].append(lines[i] if i < len(lines) else "/"); i += 1
                continue
            if m_par and cur is None:
                cur = dict(kind="PAR", name=m_par.group(1), head=[l], data=[], foot=None)
                i += 1
                continue
            if cur is not None:
                if l.strip().startswith("/") and l.strip().endswith(";"):
                    cur["foot"] = l
                    self.blocks.append(cur)
                    cur = None
                else:
                    cur["data"].append(l)
                i += 1
                continue
            self.blocks.append(dict(kind="RAW", name=None, head=[l], data=[], foot=None))
            i += 1

    def write(self, path):
        out = []
        for b in self.blocks:
            out += b["head"] + b["data"] + ([b["foot"]] if b["foot"] is not None else [])
        open(path, "w", encoding="latin-1").write("\n".join(out))


def sub_region(line, old, new):
    return re.sub(r"'" + re.escape(old) + r"'(?=[.\s]|$)", f"'{new}'", line)


def has_tok(line, tok):
    return f"'{tok}'" in line


def add_regions(dds, template, new):
    n = 0
    for d in dds:
        for b in d.blocks:
            if b["kind"] == "RAW":
                continue
            extra = []
            seen = {l.split(" ")[0] if b["kind"] == "PAR" else l.strip() for l in b["data"]}
            for l in b["data"]:
                if has_tok(l, template):
                    for r in new:
                        nl = sub_region(l, template, r)
                        key = nl.split(" ")[0] if b["kind"] == "PAR" else nl.strip()
                        if key not in seen:          # e.g. ALL_REG already lists every region
                            seen.add(key)
                            extra.append(nl)
            b["data"] += extra
            n += len(extra)
    return n


def scale_value(line, f):
    if re.match(r"^\s*'[^']*'\.0\.", line):        # year 0 = interpolation option code, not data
        return line
    m = re.match(r"^(.*?)\s+([-+0-9.eE]+|Eps|EPS)\s*$", line)
    if not m:
        return line
    v = m.group(2)
    if v.upper() == "EPS":
        return line
    return f"{m.group(1)} {float(v) * f:.12g}"


def move_process(dds, p, shares, keep_fi=False, scale=CAPACITY):
    """Clone every FI line that names process p to each region with share > 0;
    capacity attributes are multiplied by the share; FI lines removed unless keep_fi."""
    regions = {r: s for r, s in shares.items() if s > 0 and r != "FI"}
    n = 0
    for d in dds:
        for b in d.blocks:
            if b["kind"] == "RAW":
                continue
            keep, extra = [], []
            for l in b["data"]:
                toks = TOK.findall(l)
                if p in toks and "FI" in toks and not l.lstrip().startswith("*"):
                    for r, s in regions.items():
                        nl = sub_region(l, "FI", r)
                        if b["name"] in scale:
                            nl = scale_value(nl, s)
                        extra.append(nl)
                    if keep_fi:
                        keep.append(scale_value(l, shares.get("FI", 0.0)) if b["name"] in scale else l)
                    n += 1
                else:
                    keep.append(l)
            b["data"] = keep + extra
    return n


ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
KEYS = os.path.join(ROOT, "data", "keys")

# step 3: existing public power classes -> key file
CLASS_KEY = {
    "EUHYDDAM00": "EUHYDDAM00", "EEPP_windON": "EEPP_windON", "EEPP_windOFF": "EEPP_windOFF",
    "EEPP_PV": "EEPP_PV", "ECHP_coal_thermal": "ECHP_coal_thermal",
    "ECHP_lignite_thermal": "ECHP_lignite_thermal", "ECHP_biomass_thermal": "ECHP_biomass_thermal",
    "ECHP_naturalgas_CCGT": "ECHP_naturalgas", "ECHP_naturalgas_OCGT": "ECHP_naturalgas",
    "ECHP_naturalgas_thermal": "ECHP_naturalgas", "ECHP_HFO_thermal": "ECHP_HFO_thermal",
    "ECHP_LFO_thermal": "ECHP_LFO_thermal", "EEPP_coal_thermal": "EEPP_coal_thermal",
    "EEPP_lignite_thermal": "EEPP_lignite_thermal", "EEPP_naturalgas_CCGT": "EEPP_all",
    "EEPP_naturalgas_OCGT": "EEPP_all", "EEPP_naturalgas_thermal": "EEPP_all",
    "EEPP_HFO_thermal": "EEPP_HFO_thermal", "EEPP_LFO_thermal": "EEPP_LFO_thermal",
    "EEPP_biomass_thermal": "EEPP_biomass_thermal",
}
NUCLEAR = {"ENFI_LOVIISA-1_00": "FI1B1", "ENFI_LOVIISA-2_00": "FI1B1", "ENFI_OLKILUOTO-1_00": "FI196",
           "ENFI_OLKILUOTO-2_00": "FI196", "ENFI_OLKILUOTO-3": "FI196", "ENFI_OLKILUOTO-4": "FI196",
           "ENFI_PYHA-YOKI": "FI1D9"}
# declarations a region needs for a hub commodity; COM_IE (grid losses) stays on the hub only,
# otherwise power generated in a region would lose twice (region and hub)
COMM_BLOCKS = {"COM_TMAP", "COM_UNIT", "COM_DESC", "COM_TSL", "COM_LIM", "NRG_TMAP", "COM_GMAP",
               "COM_PKTS", "VDA_EMCB"}


LOCAL = collections.defaultdict(set)     # commodity -> regions where it is closed locally


def load_key(name):
    s = {r["region"]: float(r["share"]) for r in csv.DictReader(open(os.path.join(KEYS, f"power_{name}.csv"),
                                                                       encoding="utf-8")) if r["region"] in ALL20}
    return s


def blocks(dds, name):
    return [b for d in dds for b in d.blocks if b["name"] == name]


def twins(dds):
    """plant -> LowAF twin, read from UC_VARU_CAP_* (plant +1, twin -1)."""
    terms = collections.defaultdict(dict)
    for b in blocks(dds, "UC_CAP"):
        for l in b["data"]:
            t = TOK.findall(l)
            if len(t) >= 3 and t[0].startswith("UC_VARU_CAP_") and t[1] == "FI":
                v = l.split()[-1]
                terms[t[0]][t[2]] = float(v) if v.upper() != "EPS" else 0.0
    out = {}
    for uc, d in terms.items():
        pos = [p for p, v in d.items() if v > 0]
        neg = [p for p, v in d.items() if v < 0 and p.startswith("LowAF_")]
        if len(pos) == 1 and len(neg) == 1:
            out[pos[0]] = neg[0]
    return out


def com_tsl(dds, comm):
    for b in blocks(dds, "COM_TSL"):
        for l in b["data"]:
            t = TOK.findall(l)
            if t[:2] == ["FI", comm]:
                return l.strip().split(".")[-1]
    return "ANNUAL"


def clone_link(dds, comm, region):
    """Copy every line of the TB_INDELC_FI_FI1D9 link (an electricity link at DAYNITE level)
    with commodity, region and timeslice level replaced."""
    tpl = "TB_INDELC_FI_FI1D9"
    new = f"TB_{comm}_FI_{region}"
    tsl = com_tsl(dds, comm)
    n = 0
    for d in dds:
        for b in d.blocks:
            if b["kind"] == "RAW":
                continue
            have = {l.strip() for l in b["data"]}
            extra = []
            for l in b["data"]:
                if tpl not in l:
                    continue
                nl = sub_region(l.replace(tpl, new).replace("'INDELC'", f"'{comm}'"), "FI1D9", region)
                nl = nl.replace("INDELC from fi to fi1d9", f"{comm} from fi to {region.lower()}")
                if b["name"] == "PRC_TSL":
                    nl = nl.replace(".DAYNITE", f".{tsl}")
                if nl.strip() not in have:
                    extra.append(nl); have.add(nl.strip())
            b["data"] += extra
            n += len(extra)
    return n


def clone_commodity(dds, comm, region):
    n = 0
    for d in dds:
        for b in d.blocks:
            if b["name"] not in COMM_BLOCKS:
                continue
            have = {l.strip() for l in b["data"]}
            extra = []
            for l in b["data"]:
                t = TOK.findall(l)
                if len(t) >= 2 and t[0] == "FI" and comm in t and                         (b["name"] != "VDA_EMCB" or t[1] == comm):
                    nl = sub_region(l, "FI", region)
                    if nl.strip() not in have:
                        extra.append(nl)
                        have.add(nl.strip())
            b["data"] += extra
            n += len(extra)
    return n


def step3(dds, log=print):
    moved = {}                                   # process -> {region: share}
    for p, k in CLASS_KEY.items():
        moved[p] = load_key(k)
    for p, r in NUCLEAR.items():
        moved[p] = {r: 1.0}
    tw = twins(dds)
    for p, t in tw.items():
        if p in moved:
            moved[t] = moved[p]
            log(f"  twin {t} follows {p}")
    n = 0
    for p, sh in moved.items():
        n += move_process(dds, p, sh)
    log(f"  moved {len(moved)} processes ({n} FI lines -> regions)")
    # every commodity a moved plant touches in its region (fuel, renewable resource,
    # heat, power, certificates, auxiliary VAR commodities, emissions via VDA_EMCB) is
    # declared there and linked to the hub; ENV commodities get COM_LIM FX in the region
    # (export = production) so national caps and taxes on the hub still see them.
    declared = {TOK.findall(l)[1] for b in blocks(dds, "COM_UNIT") for l in b["data"]
                if len(TOK.findall(l)) >= 2 and TOK.findall(l)[0] == "FI"}
    emcb = collections.defaultdict(set)
    for b in blocks(dds, "VDA_EMCB"):
        for l in b["data"]:
            t = TOK.findall(l)
            if len(t) >= 3 and t[0] == "FI":
                emcb[t[1]].add(t[2])
    ctype = {}
    for b in blocks(dds, "COM_TMAP"):
        for l in b["data"]:
            t = TOK.findall(l)
            if len(t) >= 3 and t[0] == "FI":
                ctype[t[2]] = t[1]
    used = collections.defaultdict(set)
    for d in dds:
        for b in d.blocks:
            if b["kind"] == "RAW":
                continue
            for l in b["data"]:
                t = TOK.findall(l)
                if len(t) >= 3 and t[0] in ALL20 and t[0] != "FI" and any(x in moved for x in t[1:3]):
                    used[t[0]] |= {x for x in t[2:] if x in declared}
    for r in used:
        used[r] |= {e for c in list(used[r]) for e in emcb.get(c, ())}
    nl = 0
    lim = blocks(dds, "COM_LIM")[0]
    have_lim = {tuple(TOK.findall(l)) for b in blocks(dds, "COM_LIM") for l in b["data"]}
    LOCAL.clear()
    for r, comms in sorted(used.items()):
        for c in sorted(comms):
            clone_commodity(dds, c, r)
            if c.startswith("LowAF_"):          # pseudo commodities of the utilisation module:
                LOCAL[c].add(r)                  # closed inside each region, never traded
                continue
            nl += clone_link(dds, c, r)
            if ctype.get(c) == "ENV" and (r, c) not in have_lim:
                lim["data"].append(f"'{r}'.'{c}'.FX")
    log(f"  links: {sum(len(v) for v in used.values())} region-commodity pairs ({nl} lines); "
        f"commodities {sorted(set().union(*used.values()))}")
    # the free dummy suppliers of the LowAF pseudo inputs, in every region with twins
    for dum, c in (("LowAF_DumBase", "LowAF_Base"), ("LowAF_DumPeak", "LowAF_Peak")):
        if LOCAL.get(c):
            move_process(dds, dum, {r: 1.0 for r in LOCAL[c]}, keep_fi=True, scale=set())
    log(f"  local (not traded): { {c: len(r) for c, r in LOCAL.items()} }")
    uc_regions(dds, moved, log)
    return moved


def uc_regions(dds, moved, log=print):
    """Region sets of UCs whose terms now live in other regions."""
    rsum = blocks(dds, "UC_R_SUM")
    reach = blocks(dds, "UC_R_EACH")
    in_sum = {tuple(TOK.findall(l)) for b in rsum for l in b["data"]}
    in_each = {tuple(TOK.findall(l)) for b in reach for l in b["data"]}
    sum_ucs = {t[1] for t in in_sum if len(t) == 2}
    each_ucs = collections.defaultdict(set)
    for t in in_each:
        if len(t) == 2:
            each_ucs[t[1]].add(t[0])
    term_regs = collections.defaultdict(set)
    for name in ("UC_ACT", "UC_FLO", "UC_CAP", "UC_NCAP", "UC_COMPRD", "UC_COMCON", "UC_COMNET", "UC_IRE"):
        for b in blocks(dds, name):
            for l in b["data"]:
                t = TOK.findall(l)
                if len(t) >= 3 and any(x in moved for x in t[2:]):
                    term_regs[t[0]].add(t[1])
                if name in ("UC_COMPRD", "UC_COMCON", "UC_COMNET") and len(t) >= 3 and t[1] == "FI"                         and t[2] in LOCAL:
                    term_regs[t[0]] |= {"FI"} | LOCAL[t[2]]
    add_sum, add_each, national, rhs_clone = [], [], set(), collections.defaultdict(set)
    for uc, regs in term_regs.items():
        if uc in sum_ucs:
            add_sum += [f"'{r}'.'{uc}'" for r in regs if (r, uc) not in in_sum]
        elif uc.startswith("UC_VARU_"):                       # per-plant identity: each region
            new = [r for r in regs if (r, uc) not in in_each]
            add_each += [f"'{r}'.'{uc}'" for r in new]
            rhs_clone[uc] |= set(new)
        elif uc in each_ucs:                                  # FI-only system balance -> national
            national.add(uc)
    if rsum:
        rsum[0]["data"] += add_sum
    if reach:
        reach[0]["data"] += add_each
    # RHS of per-region identities (all zero in the source): clone FI -> region
    n_rhs = 0
    for name in ("UC_RHSRT", "UC_RHSRTS"):
        for b in blocks(dds, name):
            extra = []
            for l in b["data"]:
                t = TOK.findall(l)
                if len(t) >= 2 and t[0] == "FI" and t[1] in rhs_clone:
                    extra += [sub_region(l, "FI", r) for r in sorted(rhs_clone[t[1]])]
            b["data"] += extra
            n_rhs += len(extra)
    log(f"  UC_R_SUM +{len(add_sum)}, per-region identities +{len(add_each)} (RHS +{n_rhs}), "
        f"to make national: {len(national)}")
    make_national(dds, national, term_regs, log)
    return national


def link_regions(dds, comm):
    """Regions R with an internal link TB_<comm>_FI_<R>."""
    out = set()
    pat = re.compile(rf"^TB_{re.escape(comm)}_FI_(\w+)$")
    for b in blocks(dds, "TOP_IRE"):
        for l in b["data"]:
            for t in TOK.findall(l):
                m = pat.match(t)
                if m:
                    out.add(m.group(1))
    return out


def make_national(dds, ucs, term_regs, log=print):
    """R_E (FI) user constraints whose terms now sit in several regions become one
    constraint summed over the regions (UC_R_SUM): RHSRT(S) -> RHST(S), UC_ATTR copied,
    COMPRD/COMCON terms copied to every region and corrected on the internal links
    (TIMES counts an internal import as production, an export as consumption)."""
    if not ucs:
        return
    regs = {uc: set(term_regs[uc]) | {"FI"} for uc in ucs}
    # COMPRD / COMCON terms: copy to every region, correct on links
    ire = []
    for name, ie in (("UC_COMPRD", "IMP"), ("UC_COMCON", "EXP")):
        for b in blocks(dds, name):
            extra = []
            for l in b["data"]:
                t = TOK.findall(l)
                if len(t) >= 3 and t[0] in ucs and t[1] == "FI":
                    m = re.match(r"^'([^']*)'\.(\w+)\.'FI'\.(\d+)\.'([^']*)'\.(\S+)\s+(\S+)$", l.strip())
                    if not m:
                        log(f"    ! unparsed {name}: {l.strip()}")
                        continue
                    uc, side, yr, c, ts, v = m.groups()
                    for r in sorted(LOCAL.get(c, ())):      # produced in the region, not traded
                        regs[uc].add(r)
                        extra.append(sub_region(l, "FI", r))
                    links = link_regions(dds, c)
                    for r in sorted(links):
                        regs[uc].add(r)
                        extra.append(sub_region(l, "FI", r))
                        neg = f"{-float(v):.14g}"
                        lk = f"TB_{c}_FI_{r}"
                        ire.append(f"'{uc}'.{side}.'FI'.{yr}.'{lk}'.'{c}'.{ts}.{ie} {neg}")
                        ire.append(f"'{uc}'.{side}.'{r}'.{yr}.'{lk}'.'{c}'.{ts}.{ie} {neg}")
            b["data"] += extra
    uire = blocks(dds, "UC_IRE")
    uire[0]["data"] += ire
    # region sets
    for b in blocks(dds, "UC_R_EACH"):
        b["data"] = [l for l in b["data"] if not (len(TOK.findall(l)) == 2 and TOK.findall(l)[1] in ucs)]
    have = {tuple(TOK.findall(l)) for b in blocks(dds, "UC_R_SUM") for l in b["data"]}
    blocks(dds, "UC_R_SUM")[0]["data"] += [f"'{r}'.'{uc}'" for uc in sorted(ucs) for r in sorted(regs[uc])
                                           if (r, uc) not in have]
    # RHS: regional -> national (FI values; other regions' copies dropped)
    moved = collections.Counter()
    for src, dst in (("UC_RHSRT", "UC_RHST"), ("UC_RHSRTS", "UC_RHSTS")):
        out = []
        for b in blocks(dds, src):
            keep = []
            for l in b["data"]:
                t = TOK.findall(l)
                if len(t) >= 2 and t[1] in ucs:
                    if t[0] == "FI":
                        out.append(re.sub(r"^\s*'FI'\.", "", l))
                        moved[dst] += 1
                else:
                    keep.append(l)
            b["data"] = keep
        if out:
            tgt = blocks(dds, dst)
            if not tgt:
                raise SystemExit(f"no {dst} block in the DD files")
            tgt[0]["data"] += out
    # UC_ATTR (e.g. GROWTH of the non-decreasing capacity UCs): every summed region
    n_attr = 0
    for b in blocks(dds, "UC_ATTR"):
        have = {l.strip() for l in b["data"]}
        extra = []
        for l in b["data"]:
            t = TOK.findall(l)
            if len(t) >= 2 and t[0] == "FI" and t[1] in ucs:
                for r in sorted(regs[t[1]] - {"FI"}):
                    nl = sub_region(l, "FI", r)
                    if nl.strip() not in have:
                        extra.append(nl); have.add(nl.strip())
        b["data"] += extra
        n_attr += len(extra)
    log(f"  national: {len(ucs)} UCs, RHS {dict(moved)}, link corrections {len(ire)}, UC_ATTR +{n_attr}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--run", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--step3", action="store_true", help="power and CHP plants to their regions")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    run = open(os.path.join(a.src, a.run), encoding="latin-1").read()
    files = [f for f in re.findall(r"BATINCLUDE\s+(\S+\.dd)", run)]
    dds = [DD(os.path.join(a.src, f)) for f in files]
    present = {"FI", "FI1B1", "FI1D9"}
    n = add_regions(dds, "FI1B1", [r for r in ALL20 if r not in present])
    print(f"empty regions added: {n} lines cloned from FI1B1")
    if a.step3:
        step3(dds)
    for d, f in zip(dds, files):
        d.write(os.path.join(a.out, f))
    shutil.copy(os.path.join(a.src, a.run), os.path.join(a.out, a.run))


if __name__ == "__main__":
    main()
