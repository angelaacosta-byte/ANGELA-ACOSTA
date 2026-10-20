#!/usr/bin/env bash
# Reproducibility audit of DATE (Kim et al., KDD 2020) -- re-runs every experiment in the audit report.
# Usage:  bash run_audit.sh            (all runs, about 35 min on 2 CPU cores)
#         RUNS=seeded bash run_audit.sh   (seeded runs only)
# Requires: git, Python 3.12, and the packages in requirements-audit-lock.txt
#   pip install -r requirements-audit-lock.txt
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="${WORK:-$HERE/work}"
RUNS="${RUNS:-all}"
PY="${PY:-python}"

rm -rf "$WORK" && mkdir -p "$WORK/logs"
git clone -q https://github.com/Roytsai27/Dual-Attentive-Tree-aware-Embedding.git "$WORK/DATE"
cd "$WORK/DATE"
git checkout -q 5c540d6                       # commit audited (18 July 2021)
git apply "$HERE/01_fix_pandas_weekofyear.patch"
git apply "$HERE/02_fix_torch_load.patch"
git apply "$HERE/03_add_seed_option.patch"

$PY preprocess_data.py  > "$WORK/logs/step1_preprocess.txt" 2>&1
$PY generate_loader.py  > "$WORK/logs/step2_baselines.txt"  2>&1

if [ "$RUNS" = "all" ]; then
  for i in 1 2 3 4 5; do          # original behaviour: no seed
    $PY train.py --device cpu --epoch 5 --output unseeded_$i > "$WORK/logs/unseeded_run$i.txt" 2>&1
  done
fi
$PY train.py --device cpu --epoch 5 --seed 0 --output seed0_repeat > "$WORK/logs/seed0_repeat.txt" 2>&1
for s in 0 1 2 3 4; do            # fixed seeds
  $PY train.py --device cpu --epoch 5 --seed $s --output seed_$s > "$WORK/logs/seeded_seed$s.txt" 2>&1
done
$PY "$HERE/summarize_runs.py" "$WORK/logs"
