"""Robustness checks for the Australian triple-difference."""
import sys
import numpy as np, pandas as pd
import statsmodels.formula.api as smf
sys.path.insert(0, ".")
from build_panel import build
df, ex = build(sys.argv[1:5])
w = ex.set_index("occ").emp2019_weight
mu = np.average(ex.exposure, weights=w); sd = np.sqrt(np.average((ex.exposure - mu) ** 2, weights=w))
print(f"exposure mean {mu:.3f}, sd {sd:.3f}, min {ex.exposure.min():.3f}, max {ex.exposure.max():.3f}")
def gap(young, ref="35-54", y="lemp"):
    p = df[df.ageg.isin([young, ref])].pivot_table(index=["occ", "t", "date", "year", "post", "expz"], columns="ageg", values=[y, "w19"]).dropna()
    g = pd.DataFrame({"gap": p[(y, young)] - p[(y, ref)], "w": p[("w19", young)]}).reset_index()
    g["trend"] = (g.date.dt.year - 2015) + (g.date.dt.month - 1) / 12
    return g
rows = []
def est(g, formula, term, label, young):
    m = smf.wls(formula, data=g, weights=g.w).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(g.occ)[0]})
    rows.append((label, young, m.params[term], m.bse[term], m.pvalues[term], int(m.nobs)))
for young in ["15-24", "25-34"]:
    g = gap(young)
    g["dd"] = g.expz * g.post
    g["dd25"] = g.expz * (g.date >= "2025-01-01")
    g["dd2324"] = g.expz * ((g.date >= "2023-01-01") & (g.date < "2025-01-01"))
    # 2. timing split
    est(g, "gap ~ dd2324 + dd25 + C(occ) + C(t)", "dd2324", "2023-24 x exposure", young)
    est(g, "gap ~ dd2324 + dd25 + C(occ) + C(t)", "dd25", "2025-26 x exposure", young)
    # 3. pre-trend extrapolation: fit exposure-specific trend on 2018-2022, test deviation
    g18 = g[g.date >= "2018-01-01"].copy(); g18["pretr"] = g18.expz * g18.trend
    est(g18, "gap ~ dd2324 + dd25 + pretr + C(occ) + C(t)", "dd25", "2025-26 x exposure, from 2018 with exposure trend", young)
    est(g18, "gap ~ dd2324 + dd25 + C(occ) + C(t)", "dd25", "2025-26 x exposure, from 2018", young)
r = pd.DataFrame(rows, columns=["spec", "young", "coef", "se", "p", "n"])
r.to_csv(sys.argv[4] + "/robustness.csv", index=False)
print(r.round(4).to_string(index=False))
