"""Triple-difference and event study: young workers' employment in GenAI-exposed occupations, Australia (ABS EQ07a)."""
import sys
import numpy as np, pandas as pd, openpyxl
import statsmodels.formula.api as smf

eq07a, exposure_csv, codes_tsv, outdir = sys.argv[1:5]
codes = dict(l.rstrip("\n").split("\t")[::-1] for l in open(codes_tsv))
rows = []
ws = openpyxl.load_workbook(eq07a, read_only=True)["Data 1"]
for i, r in enumerate(ws.iter_rows(values_only=True)):
    if i < 4 or r[0] is None or r[3] not in codes:
        continue
    rows.append((r[0], r[2], codes[r[3]], (r[4] or 0) + (r[5] or 0), (r[6] or 0) + (r[7] or 0)))
df = pd.DataFrame(rows, columns=["date", "age", "occ", "emp", "hours"])
df = df.groupby(["date", "age", "occ"], as_index=False)[["emp", "hours"]].sum()   # sum over sex
ex = pd.read_csv(exposure_csv, dtype={"submajor": str}).rename(columns={"submajor": "occ"})
df = df.merge(ex[["occ", "exposure"]], on="occ")
df = df[(df.date >= "2015-01-01")]
df["t"] = df.date.dt.strftime("%Y-%m")
df["year"] = df.date.dt.year
df["post"] = (df.date >= "2023-01-01").astype(int)          # first observation after ChatGPT release (30 Nov 2022) is Feb 2023
agemap = {"15-24 years": "15-24", "25-34 years": "25-34", "35-44 years": "35-54", "45-54 years": "35-54",
          "55-64 years": "55+", "65 years and over": "55+"}
df["ageg"] = df.age.map(agemap)
df = df.groupby(["date", "t", "year", "post", "ageg", "occ", "exposure"], as_index=False)[["emp", "hours"]].sum()
# standardised exposure (employment-weighted across occupations)
w = ex.set_index("occ").emp2019_weight
mu = np.average(ex.exposure, weights=w); sd = np.sqrt(np.average((ex.exposure - mu) ** 2, weights=w))
df["expz"] = (df.exposure - mu) / sd
base = df[df.year == 2019].groupby(["ageg", "occ"]).emp.mean().rename("w19")
df = df.merge(base, on=["ageg", "occ"])
df = df[df.emp > 0]
df["lemp"] = np.log(df.emp); df["lhrs"] = np.log(df.hours.clip(lower=1e-6))
df["cell"] = df.occ + "_" + df.ageg; df["occ_t"] = df.occ + "_" + df.t; df["age_t"] = df.ageg + "_" + df.t
out = []
def gapdata(sub, young, ref, y):
    p = sub[sub.ageg.isin([young, ref])].pivot_table(index=["occ", "t", "date", "year", "post", "expz"], columns="ageg", values=[y, "w19"]).dropna()
    g = pd.DataFrame({"gap": p[(y, young)] - p[(y, ref)], "w": p[("w19", young)]}).reset_index()
    return g
def fit(sub, y, young, ref="35-54", label=""):
    g = gapdata(sub, young, ref, y)
    g["dd"] = g.expz * g.post
    m = smf.wls("gap ~ dd + C(occ) + C(t)", data=g, weights=g.w).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(g.occ)[0]})
    out.append((label, young, ref, y, m.params["dd"], m.bse["dd"], m.pvalues["dd"], int(m.nobs)))
    return m
for young in ["15-24", "25-34"]:
    fit(df, "lemp", young, label="main")
    fit(df, "lhrs", young, label="hours")
    fit(df[df.date < "2025-01-01"], "lemp", young, label="sample to 2024")
    fit(df, "lemp", young, ref="55+", label="reference 55+")
    s2 = df[df.date >= "2018-01-01"]; fit(s2, "lemp", young, label="sample from 2018")
pl = df[df.date < "2022-11-01"].copy(); pl["post"] = (pl.date >= "2019-01-01").astype(int)
for young in ["15-24", "25-34"]:
    fit(pl, "lemp", young, label="placebo 2019")
res = pd.DataFrame(out, columns=["spec", "young", "ref", "outcome", "coef", "se", "p", "n"])
res.to_csv(f"{outdir}/ddd_results.csv", index=False)
print(res.round(4).to_string(index=False))

ev = []
for young in ["15-24", "25-34"]:
    g = gapdata(df, young, "35-54", "lemp"); terms = []
    for yr in range(2015, 2027):
        if yr == 2022: continue
        g[f"e{yr}"] = g.expz * (g.year == yr); terms.append(f"e{yr}")
    m = smf.wls("gap ~ " + " + ".join(terms) + " + C(occ) + C(t)", data=g, weights=g.w).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(g.occ)[0]})
    for yr in range(2015, 2027):
        ev.append((young, yr, 0.0 if yr == 2022 else m.params[f"e{yr}"], 0.0 if yr == 2022 else m.bse[f"e{yr}"]))
ev = pd.DataFrame(ev, columns=["young", "year", "coef", "se"]); ev.to_csv(f"{outdir}/event_study.csv", index=False)
print(ev.round(4).to_string(index=False))

# descriptive: young share of employment in top vs bottom exposure terciles
ex["terc"] = pd.qcut(ex.exposure, 3, labels=["Low", "Middle", "High"])
dd = df.merge(ex[["occ", "terc"]], on="occ")
desc = dd.groupby(["date", "terc", "ageg"], observed=True).emp.sum().unstack("ageg")
desc["share1524"] = desc["15-24"] / desc.sum(axis=1); desc["share2534"] = desc["25-34"] / desc[["15-24","25-34","35-54","55+"]].sum(axis=1)
desc.reset_index().to_csv(f"{outdir}/young_share_by_tercile.csv", index=False)
dr = desc.reset_index(); dr = dr[dr.date.isin(pd.to_datetime(["2019-11-01","2022-11-01","2025-11-01","2026-02-01"]))]
print(dr[["date","terc","share1524","share2534"]].to_string(index=False))
