"""Plot event-study coefficients (Australia)."""
import sys
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ev = pd.read_csv(sys.argv[1]); out = sys.argv[2]
plt.rcParams["font.family"] = "DejaVu Sans"
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.8), sharey=True)
for ax, (young, lab) in zip(axs, [("15-24", "(a) Workers aged 15–24"), ("25-34", "(b) Workers aged 25–34")]):
    e = ev[ev.young == young]
    ax.axhline(0, color="#999", lw=0.8); ax.axvline(2022.5, color="#999", lw=0.8, ls="--")
    ax.errorbar(e.year, e.coef, yerr=1.96 * e.se, fmt="o", color="#222", ecolor="#777", capsize=3, ms=4)
    ax.set_title(lab, fontsize=10); ax.set_xlabel("Year (2022 = reference)", fontsize=9)
    ax.tick_params(labelsize=8); ax.spines[["top", "right"]].set_visible(False)
    ax.text(2022.6, ax.get_ylim()[1] * 0.92 if ax.get_ylim()[1] > 0 else 0.1, "ChatGPT\nrelease", fontsize=7.5, va="top")
axs[0].set_ylabel("Relative log employment per 1 SD\nof generative AI exposure", fontsize=9)
fig.tight_layout(); fig.savefig(out + ".png", dpi=600); fig.savefig(out + ".pdf"); fig.savefig(out + ".svg")
