"""Summarise DATE runs from the training logs: one row per run, then mean ± SD per group.
Usage: python summarize_runs.py <logs_dir>   ->  writes runs_summary.csv next to this script."""
import re, sys, statistics as st, csv, pathlib

logs = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "logs")
keys = ["Pr@1", "Pr@5", "Pr@10", "Rev@1", "Rev@10", "auc", "f1"]
rows = []
for f in sorted(logs.glob("*.txt")):
    if "run" not in f.name and "seed" not in f.name:
        continue
    text = f.read_text()
    if "Evaluating DATE model" not in text:
        continue
    part = text.split("Evaluating DATE model")[1]
    vals = dict(re.findall(r"(Pr@1|Pr@5|Pr@10|Rev@1|Rev@10|auc|f1):([0-9.]+)", part))
    group = "unseeded" if f.name.startswith("unseeded") else ("seed0_repeat" if "repeat" in f.name else "seeded")
    rows.append({"run": f.stem, "group": group, **{k: float(vals[k]) for k in keys}})

out = pathlib.Path(__file__).with_name("runs_summary.csv")
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["run", "group"] + keys); w.writeheader(); w.writerows(rows)

for r in rows:
    print(r["run"].ljust(20), "  ".join(f"{k}={r[k]:.4f}" for k in keys))
for g in ["unseeded", "seeded"]:
    sub = [r for r in rows if r["group"] == g]
    if len(sub) > 1:
        print(f"\n{g} (n={len(sub)}):")
        for k in keys:
            v = [r[k] for r in sub]
            print(f"  {k:6s} mean={st.mean(v):.4f}  sd={st.stdev(v):.4f}  min={min(v):.4f}  max={max(v):.4f}")
rep = [r for r in rows if r["group"] == "seed0_repeat"]
s0 = [r for r in rows if r["run"] == "seeded_seed0"]
if rep and s0:
    same = all(rep[0][k] == s0[0][k] for k in keys)
    print(f"\nSeed 0 run twice gives identical metrics: {same}")
