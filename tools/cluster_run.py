"""Solve TIMES cases on the Aalto Triton cluster; every input and result stays in this repository.

The cluster only computes. A case is a local folder cluster/cases/<case>/ holding exactly what VEDA would hand to GAMS
(the .run file, the DD files it includes, cplex.opt); results come back to cluster/cases/<case>/out/.

  prepare  python tools/cluster_run.py prepare <case> --src-run GAMS_WrkTIMES/5cnewsolver.run
                 [--opt runs/cplex_5c_r2.opt] [--reslim 200000] [--patch <dir with replacement .dd files>]
           Copies the .run (RUN_NAME and RESLIM changed) and only the DD files it includes; files in --patch replace
           their namesakes (fixes tested in the DD files before the workbooks, CLAUDE.md). Writes case.json.
  submit   python tools/cluster_run.py submit <case> [--partition batch-milan] [--cpus 32] [--mem 120G] [--time 2-00:00:00]
           Uploads the TIMES source (once) and the case to /scratch/work/<user>/reg-fintimes, writes job.sh, sbatch.
  status   python tools/cluster_run.py status <case>       (SLURM state and the last lines of the GAMS log)
  fetch    python tools/cluster_run.py fetch <case>        (lst, log, QA_CHECK.LOG, GDX -> cluster/cases/<case>/out/)

GAMS on Triton: GAMS 54.3.1 Linux in /scratch/work/<user>/gams (Aalto academic license, GEN platform, with CPLEX).
The GAMS call reproduces VEDA's VT_GAMS (restart _times.g00 of TIMES v4.8.3, idir1 = source, gdx = GAMSSAVE/<case>).
CPLEX "threads" is set to the CPUs SLURM gives the job (threads -1 would take every core of the node).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES = os.path.join(ROOT, "cluster", "cases")
HOST = "triton"
USER = "adhikap1"
REMOTE = f"/scratch/work/{USER}/reg-fintimes"
GAMS = f"/scratch/work/{USER}/gams/gams54.3_linux_x64_64_sfx/gams"
SRC_LOCAL = os.environ.get("TIMES_SRC", os.path.join(ROOT, "cluster", "GAMS_SrcTIMES.v4.8.3"))
SRC_REMOTE = f"{REMOTE}/GAMS_SrcTIMES.v4.8.3"


def sh(cmd, check=True, capture=True):
    r = subprocess.run(cmd, capture_output=capture, text=True)
    if check and r.returncode:
        sys.exit(f"failed ({r.returncode}): {' '.join(cmd)}\n{r.stdout}\n{r.stderr}")
    return r.stdout if capture else ""


def ssh(script, check=True):
    return sh(["ssh", "-o", "BatchMode=yes", HOST, script], check=check)


def case_dir(case):
    if not re.fullmatch(r"[A-Za-z0-9_\-]+", case):
        sys.exit(f"case name {case!r}: letters, digits, _ and - only")
    return os.path.join(CASES, case)


def includes(run_text):
    return re.findall(r"^\$BATINCLUDE\s+(\S+\.dd)\s*$", run_text, re.M | re.I)


# ----------------------------------------------------------------------------------------------- prepare
def prepare(a):
    d = case_dir(a.case)
    if os.path.exists(d):
        sys.exit(f"{d} exists; choose a new case name (results of a case are never overwritten)")
    src_run = os.path.join(ROOT, a.src_run)
    src_dir = os.path.dirname(src_run)
    text = open(src_run, encoding="latin-1").read()
    old = re.search(r"\$SET RUN_NAME '([^']+)'", text).group(1)
    text = text.replace(f"$SET RUN_NAME '{old}'", f"$SET RUN_NAME '{a.case}'")
    text = re.sub(rf"^\$BATINCLUDE {re.escape(old)}_ts\.dd", f"$BATINCLUDE {a.case.lower()}_ts.dd", text,
                  flags=re.M | re.I)
    if a.reslim:
        text, n = re.subn(r"RESLIM=\d+", f"RESLIM={a.reslim}", text)
        if n != 1:
            sys.exit("RESLIM not found once in the run file")
    patch = {}
    if a.patch:
        for f in os.listdir(a.patch):
            if f.lower().endswith(".dd"):
                patch[f.lower()] = os.path.join(a.patch, f)
    os.makedirs(d)
    files = []
    for f in includes(text):
        name = f.lower()
        srcf = os.path.join(src_dir, f"{old}_ts.dd") if name == f"{a.case.lower()}_ts.dd" else \
            patch.pop(name, None) or os.path.join(src_dir, f)
        if not os.path.exists(srcf):
            shutil.rmtree(d)
            sys.exit(f"missing input {srcf}")
        shutil.copyfile(srcf, os.path.join(d, name))
        files.append(name)
    if patch:
        shutil.rmtree(d)
        sys.exit(f"patch files not included by the run file: {sorted(patch)}")
    with open(os.path.join(d, f"{a.case.lower()}.run"), "w", encoding="latin-1", newline="\n") as fh:
        fh.write(text.replace("\r\n", "\n"))
    opt = os.path.join(ROOT, a.opt) if a.opt else os.path.join(src_dir, "cplex.opt")
    shutil.copyfile(opt, os.path.join(d, "cplex.opt"))
    meta = {"case": a.case, "from_run": a.src_run, "from_run_name": old, "opt": os.path.relpath(opt, ROOT),
            "reslim": a.reslim, "patch": a.patch, "patched": sorted(os.listdir(a.patch)) if a.patch else [],
            "dd_files": len(files), "prepared": time.strftime("%Y-%m-%d %H:%M")}
    json.dump(meta, open(os.path.join(d, "case.json"), "w"), indent=1)
    print(f"prepared {d}: {len(files)} DD files, opt {meta['opt']}, patched {meta['patched']}")


# ------------------------------------------------------------------------------------------------ submit
JOB = """#!/bin/bash
#SBATCH --job-name={case}
#SBATCH --partition={partition}
#SBATCH --cpus-per-task={cpus}
#SBATCH --mem={mem}
#SBATCH --time={time}
#SBATCH --output={remote}/cases/{case}/slurm-%j.out
set -e
cd {remote}/cases/{case}
mkdir -p GAMSSAVE scratch
export TMPDIR={remote}/cases/{case}/scratch
sed -i "s/^threads .*/threads $SLURM_CPUS_PER_TASK/" cplex.opt
grep -q "^threads" cplex.opt || echo "threads $SLURM_CPUS_PER_TASK" >> cplex.opt
echo "start $(date) on $(hostname), $SLURM_CPUS_PER_TASK cpus"
{gams} {run} r={src}/_times idir1={src}/ idir2={remote}/ gdx=GAMSSAVE/{case} \\
  ps=99999 pw=255 scrdir=scratch lo=3 > {case}_run_log.txt 2>&1 || echo "gams exit $?"
echo "end $(date)"
"""


CASE_LINKS = (f"cd {SRC_REMOTE} && for f in *.*; do e=\"${{f##*.}}\"; u=\"${{e^^}}\"; "
              f"[ \"$e\" != \"$u\" ] && [ ! -e \"${{f%.*}}.$u\" ] && ln -s \"$f\" \"${{f%.*}}.$u\"; done; true")


def ensure_src():
    """TIMES source on the cluster. Linux names are case-sensitive: TIMES includes its extensions as
    <name>.%EXTEND% (e.g. initmty.VDA), the files are lower case (initmty.vda) and '$IF EXIST' skips them
    silently on Linux -> every extension file also gets an upper-case-extension link."""
    if ssh(f"test -f {SRC_REMOTE}/_times.g00 && echo ok", check=False).strip() == "ok":
        ssh(CASE_LINKS)
        return
    if not os.path.exists(os.path.join(SRC_LOCAL, "_times.g00")):
        sys.exit(f"TIMES source not found in {SRC_LOCAL} (set TIMES_SRC)")
    tgz = os.path.join(CASES, "_src.tgz")
    with tarfile.open(tgz, "w:gz") as t:
        t.add(SRC_LOCAL, arcname="GAMS_SrcTIMES.v4.8.3")
    ssh(f"mkdir -p {REMOTE}")
    sh(["scp", "-q", tgz, f"{HOST}:{REMOTE}/_src.tgz"])
    ssh(f"cd {REMOTE} && tar xzf _src.tgz && rm _src.tgz")
    ssh(CASE_LINKS)
    os.remove(tgz)
    print(f"TIMES source uploaded to {SRC_REMOTE}")


def submit(a):
    d = case_dir(a.case)
    meta = json.load(open(os.path.join(d, "case.json")))
    if meta.get("job"):
        if not a.again:
            sys.exit(f"{a.case} was already submitted as job {meta['job']} (--again to rerun it from scratch)")
        meta.setdefault("earlier_jobs", []).append(meta.pop("job"))
        ssh(f"rm -rf {REMOTE}/cases/{a.case}")
        if os.path.isdir(os.path.join(d, "out")):
            shutil.rmtree(os.path.join(d, "out"))
    ensure_src()
    run = f"{a.case.lower()}.run"
    job = JOB.format(case=a.case, partition=a.partition, cpus=a.cpus, mem=a.mem, time=a.time, remote=REMOTE,
                     gams=GAMS, run=run, src=SRC_REMOTE)
    with open(os.path.join(d, "job.sh"), "w", newline="\n") as fh:
        fh.write(job)
    tgz = os.path.join(CASES, f"_{a.case}.tgz")
    with tarfile.open(tgz, "w:gz") as t:
        for f in os.listdir(d):
            if f != "out":
                t.add(os.path.join(d, f), arcname=f"{a.case}/{f}")
    ssh(f"mkdir -p {REMOTE}/cases && test ! -e {REMOTE}/cases/{a.case}")
    sh(["scp", "-q", tgz, f"{HOST}:{REMOTE}/cases/_{a.case}.tgz"])
    os.remove(tgz)
    out = ssh(f"cd {REMOTE}/cases && tar xzf _{a.case}.tgz && rm _{a.case}.tgz && "
              f"sed -i 's/\\r$//' {a.case}/job.sh && sbatch --parsable {a.case}/job.sh")
    meta.update(job=out.strip(), partition=a.partition, cpus=a.cpus, mem=a.mem, time=a.time,
                submitted=time.strftime("%Y-%m-%d %H:%M"))
    json.dump(meta, open(os.path.join(d, "case.json"), "w"), indent=1)
    print(f"submitted {a.case}: job {meta['job']} ({a.partition}, {a.cpus} cpus, {a.mem}, {a.time})")


# ------------------------------------------------------------------------------------------ status/fetch
def status(a):
    d = case_dir(a.case)
    meta = json.load(open(os.path.join(d, "case.json")))
    job = meta.get("job")
    print(ssh(f"sacct -j {job} -X -n -o JobID,State,Elapsed,NodeList,MaxRSS 2>/dev/null; "
              f"tail -n {a.lines} {REMOTE}/cases/{a.case}/{a.case}_run_log.txt 2>/dev/null", check=False))


def fetch(a):
    d = case_dir(a.case)
    o = os.path.join(d, "out")
    os.makedirs(o, exist_ok=True)
    rc = f"{REMOTE}/cases/{a.case}"
    names = ssh(f"cd {rc} && ls {a.case.lower()}.lst {a.case}_run_log.txt QA_CHECK.LOG slurm-*.out GAMSSAVE/*.gdx "
                f"2>/dev/null", check=False).split()
    for n in names:
        sh(["scp", "-q", f"{HOST}:{rc}/{n}", os.path.join(o, os.path.basename(n))])
    print(f"fetched {len(names)} files to {o}: {names}")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("prepare")
    p.add_argument("case")
    p.add_argument("--src-run", required=True)
    p.add_argument("--opt")
    p.add_argument("--reslim", type=int)
    p.add_argument("--patch")
    p = sp.add_parser("submit")
    p.add_argument("case")
    p.add_argument("--partition", default="batch-milan")
    p.add_argument("--cpus", type=int, default=32)
    p.add_argument("--mem", default="120G")
    p.add_argument("--time", default="2-00:00:00")
    p.add_argument("--again", action="store_true", help="rerun a submitted case from scratch (old results dropped)")
    for c in ("status", "fetch"):
        p = sp.add_parser(c)
        p.add_argument("case")
        p.add_argument("--lines", type=int, default=15)
    a = ap.parse_args()
    {"prepare": prepare, "submit": submit, "status": status, "fetch": fetch}[a.cmd](a)


if __name__ == "__main__":
    main()
