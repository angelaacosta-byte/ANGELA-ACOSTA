"""Figure for the audit report: Precision@1% of every DATE run, with and without fixed seeds.
Usage: python make_figure.py   (reads runs_summary.csv and step2_baselines.txt in this folder) -> fig_precision_runs.png"""
import csv, re, pathlib, statistics as st
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

here = pathlib.Path(__file__).parent
rows = list(csv.DictReader(open(here / "runs_summary.csv")))
groups = {"unseeded": "Original code\n(no seed, 5 runs)", "seeded": "With fixed seeds\n(seeds 0-4, 5 runs)"}
colors = {"unseeded": "#eb6834", "seeded": "#2a78d6"}
base = re.search(r"Training xgboost.*?top 1% suspicious transactions: \d+\nPrecision: ([0-9.]+)",
                 (here / "step2_baselines.txt").read_text(), re.S)
xgb = float(base.group(1)) * 100

INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=200)
fig.patch.set_facecolor("#fcfcfb"); ax.set_facecolor("#fcfcfb")
for i, (g, label) in enumerate(groups.items()):
    v = [float(r["Pr@1"]) * 100 for r in rows if r["group"] == g]
    ax.scatter([i + (k - (len(v) - 1) / 2) * 0.05 for k in range(len(v))], sorted(v), s=70, color=colors[g], edgecolor="#fcfcfb", linewidth=2, zorder=3)
    m, sd = st.mean(v), st.stdev(v)
    ax.plot([i - 0.18, i + 0.18], [m, m], color=INK, linewidth=1.5, zorder=2)
    ax.annotate(f"mean {m:.1f}% ± {sd:.1f} SD\nrange {min(v):.1f}–{max(v):.1f}%", (i + 0.24, m),
                va="center", fontsize=9, color=INK)
ax.axhline(xgb, color=MUTED, linestyle=(0, (4, 3)), linewidth=1.2, zorder=1)
ax.text(1.62, xgb + 0.6, f"XGBoost baseline {xgb:.1f}%", ha="right", fontsize=9, color=MUTED)
ax.set_xticks([0, 1], list(groups.values()), fontsize=9.5, color=INK)
ax.set_xlim(-0.5, 1.7); ax.set_ylim(10, 40)
ax.set_ylabel("Precision at top 1% of declarations (%)", fontsize=9.5, color=MUTED)
ax.yaxis.grid(True, color=GRID, linewidth=0.8); ax.set_axisbelow(True)
for s in ["top", "right", "left"]: ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID); ax.tick_params(colors=MUTED, length=0)
ax.set_title("Same code, same data: without seeds, precision at the top 1%\nranges from 15.8% to 34.7%",
             loc="left", fontsize=11, color=INK, fontweight="bold")
fig.text(0.01, 0.01, "Each dot is one training run (DATE, Kim et al., 2020; synthetic data, 5 epochs, CPU). Each seeded run is exactly repeatable;\nthe spread across seeds is the run-to-run variation a paper should report as mean ± SD.",
         fontsize=8, color=MUTED)
fig.tight_layout(rect=(0, 0.07, 1, 1))
fig.savefig(here / "fig_precision_runs.png", facecolor=fig.get_facecolor())
print("saved fig_precision_runs.png")
