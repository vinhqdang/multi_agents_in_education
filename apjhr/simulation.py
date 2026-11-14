import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = sys.argv[1]
T = 15
def run(entry_cut, hollow):
    J, E, D = 50.0, 50.0, 0.0           # juniors, experienced verifiers, verification debt
    hire0 = 10.0                         # baseline junior hires per year
    res = {k: [] for k in ["perf", "E", "fail", "D"]}
    for t in range(T + 1):
        O = 100 * 1.12 ** t              # AI-assisted output grows 12% a year
        V = 2.2 * E * 1.08 ** t           # capacity per verifier rises 8% a year with better tools
        fail = 0.35 * D                  # share of debt converted into failures each year
        cost = 1.0 * J + 2.0 * E         # labour cost (experienced staff cost twice as much)
        res["perf"].append(O / cost)     # output-based performance indicator
        res["E"].append(E); res["fail"].append(fail); res["D"].append(D)
        # flows
        hires = hire0 * (1 - entry_cut) if t >= 1 else hire0
        formation = (J / 5.0) * (1 - hollow if t >= 1 else 1)   # ~5 years to become a verifier
        overload = max(O - V, 0) / max(V, 1)                    # strain from unchecked load
        exits_E = E * (0.06 + 0.10 * min(overload, 1.0))        # turnover rises with overload
        D = D + max(O - V, 0) - fail
        J = J + hires - formation - 0.10 * J
        E = E + formation - exits_E
    return res

A = run(entry_cut=0.8, hollow=0.3)   # substitutes entry-level work
B = run(entry_cut=0.0, hollow=0.0)   # deliberate expertise formation
yrs = list(range(T + 1))
plt.rcParams["font.family"] = "DejaVu Sans"
fig, axs = plt.subplots(1, 3, figsize=(12, 3.8))
panels = [("perf", "(a) Output-based performance\n(output per unit labour cost)"),
          ("E", "(b) Oversight capability\n(experienced verifiers)"),
          ("fail", "(c) AI-related failures\n(per year)")]
for ax, (k, title) in zip(axs, panels):
    ax.plot(yrs, A[k], color="#222", lw=2, label="Organisation A: cuts entry-level hiring")
    ax.plot(yrs, B[k], color="#888", lw=2, ls="--", label="Organisation B: deliberate formation")
    ax.set_title(title, fontsize=9.5); ax.set_xlabel("Years after adoption", fontsize=9)
    ax.tick_params(labelsize=8); ax.spines[["top", "right"]].set_visible(False)
axs[0].legend(fontsize=7.5, frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig(out + ".png", dpi=600); fig.savefig(out + ".pdf"); fig.savefig(out + ".svg")
# print key numbers
for k in ["perf", "E", "fail"]:
    print(k, "A:", [round(A[k][i], 2) for i in (0, 3, 6, 10, 15)], "B:", [round(B[k][i], 2) for i in (0, 3, 6, 10, 15)])
cross = next((t for t in yrs if A["fail"][t] > 1.5 * B["fail"][t] and t > 0), None); print("A fails >1.5x B from year", cross)
