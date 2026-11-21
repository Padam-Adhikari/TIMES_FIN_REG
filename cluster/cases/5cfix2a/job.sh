#!/bin/bash
#SBATCH --job-name=5cfix2a
#SBATCH --partition=batch-milan
#SBATCH --cpus-per-task=32
#SBATCH --mem=120G
#SBATCH --time=2-00:00:00
#SBATCH --output=/scratch/work/adhikap1/reg-fintimes/cases/5cfix2a/slurm-%j.out
set -e
cd /scratch/work/adhikap1/reg-fintimes/cases/5cfix2a
mkdir -p GAMSSAVE scratch
export TMPDIR=/scratch/work/adhikap1/reg-fintimes/cases/5cfix2a/scratch
sed -i "s/^threads .*/threads $SLURM_CPUS_PER_TASK/" cplex.opt
grep -q "^threads" cplex.opt || echo "threads $SLURM_CPUS_PER_TASK" >> cplex.opt
echo "start $(date) on $(hostname), $SLURM_CPUS_PER_TASK cpus"
/scratch/work/adhikap1/gams/gams54.3_linux_x64_64_sfx/gams 5cfix2a.run r=/scratch/work/adhikap1/reg-fintimes/GAMS_SrcTIMES.v4.8.3/_times idir1=/scratch/work/adhikap1/reg-fintimes/GAMS_SrcTIMES.v4.8.3/ idir2=/scratch/work/adhikap1/reg-fintimes/ gdx=GAMSSAVE/5cfix2a \
  ps=99999 pw=255 scrdir=scratch lo=3 > 5cfix2a_run_log.txt 2>&1 || echo "gams exit $?"
echo "end $(date)"
