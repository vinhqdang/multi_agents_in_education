def build(ARGS):
    """Triple-difference and event study: young workers' employment in GenAI-exposed occupations, Australia (ABS EQ07a)."""
    import sys
    import numpy as np, pandas as pd, openpyxl
    import statsmodels.formula.api as smf
    
    eq07a, exposure_csv, codes_tsv, outdir = ARGS
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
    return df, ex
