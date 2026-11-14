"""Japan (LFS annual Table II-A, 2018-2025, single 2020 census population basis): same design as Australia/US."""
import sys, json, re, collections
import numpy as np, pandas as pd
import statsmodels.formula.api as smf
panel, isco_map, ilo_json, outdir = sys.argv[1:5]
# ISCO-08 sub-major (2-digit) exposure = mean of 4-digit occupation means
d = json.load(open(ilo_json)); occ4 = {}
def walk(n):
    m = re.match(r"(\d{4}) - ", n["name"])
    if m and "children" in n:
        s = [float(re.match(r"\(\s*([\d.]+)\s*\)", c["name"]).group(1)) for c in n["children"] if re.match(r"\(\s*[\d.]+\s*\)", c["name"])]
        if s: occ4[m.group(1)] = sum(s) / len(s)
        return
    for c in n.get("children", []): walk(c)
walk(d)
sub = collections.defaultdict(list)
for k, v in occ4.items(): sub[k[:2]].append(v)
sub = {k: sum(v) / len(v) for k, v in sub.items()}
mp = pd.read_csv(isco_map, dtype=str)
leaf = ["A","B1","B2","B3","B4","C1","C2","C3","D1","D2","D3","E1","E2","E3","E4","E5","F","G","H1","H2","H3","H4","H5","H6","H7","I","J","K1","K2","K3"]
mp = mp[mp.occupation_code.isin(leaf)].copy()
mp["exposure"] = mp.isco08_submajor.apply(lambda s: np.mean([sub[x.zfill(2)] for x in s.split(";") if x.zfill(2) in sub]))
p = pd.read_csv(panel, dtype={"occupation_code": str})
p = p[(p.sex == "total") & p.occupation_code.isin(leaf) & p.period.between(2018, 2025)]
p["ageg"] = p.age_group.map({"15-24": "15-24", "25-34": "25-34", "35-44": "35-54", "45-54": "35-54"})
p = p[p.ageg.notna()].groupby(["period", "occupation_code", "ageg"], as_index=False).employed_10k.sum()
df = p.merge(mp[["occupation_code", "occupation_name_en", "exposure"]], on="occupation_code").rename(columns={"occupation_code": "occ", "period": "year", "employed_10k": "emp"})
w19 = df[df.year == 2019].groupby("occ").emp.sum(); e = df.drop_duplicates("occ").set_index("occ").exposure
mu = np.average(e, weights=w19[e.index]); sd = np.sqrt(np.average((e - mu) ** 2, weights=w19[e.index]))
df["expz"] = (df.exposure - mu) / sd; df["post"] = (df.year >= 2023).astype(int)
print(f"Japan: {df.occ.nunique()} occupations, exposure mean {mu:.3f} sd {sd:.3f}")
print(df.drop_duplicates("occ").sort_values("exposure", ascending=False)[["occ","occupation_name_en","exposure"]].head(6).round(3).to_string(index=False))
base = df[df.year == 2019].groupby(["occ", "ageg"]).emp.mean().rename("w19"); df = df.merge(base, on=["occ", "ageg"])
df = df[df.emp > 0]; df["lemp"] = np.log(df.emp)
rows, ev = [], []
for young in ["15-24", "25-34"]:
    q = df[df.ageg.isin([young, "35-54"])].pivot_table(index=["occ", "year", "post", "expz"], columns="ageg", values=["lemp", "w19"]).dropna()
    g = pd.DataFrame({"gap": q[("lemp", young)] - q[("lemp", "35-54")], "w": q[("w19", young)]}).reset_index()
    g["dd"] = g.expz * g.post; g["dd25"] = g.expz * (g.year >= 2025); g["dd2324"] = g.expz * g.year.isin([2023, 2024])
    for f, term, lab in [("gap ~ dd + C(occ) + C(year)", "dd", "post x exposure"),
                         ("gap ~ dd2324 + dd25 + C(occ) + C(year)", "dd2324", "2023-24 x exposure"),
                         ("gap ~ dd2324 + dd25 + C(occ) + C(year)", "dd25", "2025 x exposure")]:
        m = smf.wls(f, data=g, weights=g.w).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(g.occ)[0]})
        rows.append((lab, young, m.params[term], m.bse[term], m.pvalues[term], int(m.nobs), g.occ.nunique()))
    terms = []
    for yr in range(2018, 2026):
        if yr == 2022: continue
        g[f"e{yr}"] = g.expz * (g.year == yr); terms.append(f"e{yr}")
    m = smf.wls("gap ~ " + " + ".join(terms) + " + C(occ) + C(year)", data=g, weights=g.w).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(g.occ)[0]})
    for yr in range(2018, 2026):
        ev.append((young, yr, 0.0 if yr == 2022 else m.params[f"e{yr}"], 0.0 if yr == 2022 else m.bse[f"e{yr}"]))
r = pd.DataFrame(rows, columns=["spec", "young", "coef", "se", "p", "n", "clusters"]); r.to_csv(f"{outdir}/jp_results.csv", index=False)
pd.DataFrame(ev, columns=["young", "year", "coef", "se"]).to_csv(f"{outdir}/jp_event_study.csv", index=False)
mp.to_csv(f"{outdir}/jp_exposure.csv", index=False)
print(r.round(4).to_string(index=False)); print(pd.DataFrame(ev, columns=["young","year","coef","se"]).round(4).to_string(index=False))
