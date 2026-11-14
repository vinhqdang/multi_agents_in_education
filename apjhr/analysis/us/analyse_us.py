"""US replication with CPS: log employment gap young vs 35-54 within SOC minor group, by GenAI exposure (Eloundou et al. beta)."""
import sys, glob, os
import numpy as np, pandas as pd
import statsmodels.formula.api as smf
aggdir, expo_csv, outdir = sys.argv[1:4]
mon = {"jan": 1, "apr": 4, "jul": 7, "oct": 10, "nov": 11}
ex = pd.read_csv(expo_csv, dtype={"occ": str})
ex["occ"] = ex.occ.str.zfill(4)
frames = []
for f in sorted(glob.glob(os.path.join(aggdir, "*.csv"))):
    y, m = os.path.basename(f)[:-4].split("_")
    d = pd.read_csv(f, dtype={"occ": str}); d["occ"] = d.occ.str.zfill(4)
    scheme = "2010" if int(y) < 2020 else "2018"
    d = d.merge(ex[ex.scheme == int(scheme)] if ex.scheme.dtype != object else ex[ex.scheme == scheme], on="occ", how="inner")
    d["date"] = pd.Timestamp(int(y), mon[m], 1)
    frames.append(d)
df = pd.concat(frames)
df = df.groupby(["date", "minor", "ageg"], as_index=False).agg(emp=("emp", "sum"), exposure=("exposure", "first"))
df = df[df.exposure.notna()]
df["year"] = df.date.dt.year; df["t"] = df.date.dt.strftime("%Y-%m")
df["post"] = (df.date >= "2023-01-01").astype(int)
w19 = df[df.year == 2019].groupby("minor").emp.sum()
e = df.drop_duplicates("minor").set_index("minor").exposure
mu = np.average(e, weights=w19.reindex(e.index).fillna(0)); sd = np.sqrt(np.average((e - mu) ** 2, weights=w19.reindex(e.index).fillna(0)))
df["expz"] = (df.exposure - mu) / sd
print(f"US exposure mean {mu:.3f} sd {sd:.3f}; minor groups {df.minor.nunique()}; periods {df.t.nunique()}")
base = df[df.year == 2019].groupby(["minor", "ageg"]).emp.mean().rename("w19")
df = df.merge(base, on=["minor", "ageg"])
df = df[df.emp > 0]; df["lemp"] = np.log(df.emp)
def gap(young, ref="35-54", sub=None):
    s = df if sub is None else sub
    p = s[s.ageg.isin([young, ref])].pivot_table(index=["minor", "t", "date", "year", "post", "expz"], columns="ageg", values=["lemp", "w19"]).dropna()
    return pd.DataFrame({"gap": p[("lemp", young)] - p[("lemp", ref)], "w": p[("w19", young)]}).reset_index()
rows = []
def est(g, formula, term, label, young):
    m = smf.wls(formula, data=g, weights=g.w).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(g.minor)[0]})
    rows.append((label, young, m.params[term], m.bse[term], m.pvalues[term], int(m.nobs), g.minor.nunique()))
ev = []
for young in ["22-25", "26-30"]:
    g = gap(young); g["dd"] = g.expz * g.post
    g["dd2324"] = g.expz * ((g.date >= "2023-01-01") & (g.date < "2025-01-01")); g["dd25"] = g.expz * (g.date >= "2025-01-01")
    est(g, "gap ~ dd + C(minor) + C(t)", "dd", "post x exposure", young)
    est(g, "gap ~ dd2324 + dd25 + C(minor) + C(t)", "dd2324", "2023-24 x exposure", young)
    est(g, "gap ~ dd2324 + dd25 + C(minor) + C(t)", "dd25", "2025-26 x exposure", young)
    g["trend"] = g.year - 2017 + (g.date.dt.month - 1) / 12; g["pretr"] = g.expz * g.trend
    est(g, "gap ~ dd2324 + dd25 + pretr + C(minor) + C(t)", "dd25", "2025-26 x exposure, with exposure trend", young)
    pl = g[g.date < "2022-11-01"].copy(); pl["dd"] = pl.expz * (pl.date >= "2019-07-01")
    est(pl, "gap ~ dd + C(minor) + C(t)", "dd", "placebo mid-2019", young)
    terms = []
    for yr in range(2017, 2027):
        if yr == 2022: continue
        g[f"e{yr}"] = g.expz * (g.year == yr); terms.append(f"e{yr}")
    m = smf.wls("gap ~ " + " + ".join(terms) + " + C(minor) + C(t)", data=g, weights=g.w).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(g.minor)[0]})
    for yr in range(2017, 2027):
        ev.append((young, yr, 0.0 if yr == 2022 else m.params[f"e{yr}"], 0.0 if yr == 2022 else m.bse[f"e{yr}"]))
r = pd.DataFrame(rows, columns=["spec", "young", "coef", "se", "p", "n", "clusters"]); r.to_csv(f"{outdir}/us_results.csv", index=False)
pd.DataFrame(ev, columns=["young", "year", "coef", "se"]).to_csv(f"{outdir}/us_event_study.csv", index=False)
print(r.round(4).to_string(index=False)); print(pd.DataFrame(ev, columns=["young", "year", "coef", "se"]).round(4).to_string(index=False))
