"""Three-country event study figure: youngest age group vs 35-54, per 1 SD of GenAI exposure (2022 = reference)."""
import sys
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
us, au, jp, out = sys.argv[1:5]
spec = [(pd.read_csv(us), "22-25", "(a) United States, ages 22–25"),
        (pd.read_csv(au), "15-24", "(b) Australia, ages 15–24"),
        (pd.read_csv(jp), "15-24", "(c) Japan, ages 15–24")]
plt.rcParams["font.family"] = "DejaVu Sans"
fig, axs = plt.subplots(1, 3, figsize=(12, 3.9), sharey=True)
for ax, (d, young, title) in zip(axs, spec):
    e = d[d.young == young]
    ax.axhline(0, color="#999", lw=0.8); ax.axvline(2022.5, color="#999", lw=0.8, ls="--")
    ax.errorbar(e.year, e.coef, yerr=1.96 * e.se, fmt="o", color="#222", ecolor="#777", capsize=3, ms=4)
    ax.set_title(title, fontsize=9.5); ax.set_xlabel("Year (2022 = reference)", fontsize=9)
    ax.set_xticks(range(int(e.year.min()) + (int(e.year.min()) % 2 == 0), 2027, 2)); ax.tick_params(labelsize=8); ax.spines[["top", "right"]].set_visible(False)
axs[0].set_ylabel("Relative log employment per\nstandard deviation of exposure", fontsize=9)
fig.tight_layout(); fig.savefig(out + ".png", dpi=600); fig.savefig(out + ".pdf"); fig.savefig(out + ".svg")
