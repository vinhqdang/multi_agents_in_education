"""Map Census 2010 and 2018 occupation codes to SOC minor groups and Eloundou et al. (2024) GPT-4 beta exposure."""
import sys, re, collections
import openpyxl, xlrd, pandas as pd
xw18, xw10, elo, out = sys.argv[1:5]
e = pd.read_csv(elo)
e["minor"] = e["O*NET-SOC Code"].str[:4]          # e.g. '43-3'
expo = e.groupby("minor").dv_rating_beta.mean()
rows = []
wb = openpyxl.load_workbook(xw18, read_only=True)
for r in wb["2018 Census Occ Code List"].iter_rows(values_only=True):
    code, soc = (str(r[2]).strip() if r[2] else ""), (str(r[3]).strip() if r[3] else "")
    if re.fullmatch(r"\d{4}", code) and re.match(r"\d{2}-\d", soc):
        rows.append(("2018", code, soc[:4]))
b = xlrd.open_workbook(xw10)
for sh in b.sheets():
    for i in range(sh.nrows):
        r = [str(x).strip() for x in sh.row_values(i)]
        for j in range(len(r) - 1):
            c = r[j].split(".")[0]
            if re.fullmatch(r"\d{4}", c) and j + 1 < len(r) and re.match(r"\d{2}-\d", r[j + 1]):
                rows.append(("2010", c, r[j + 1][:4]))
m = pd.DataFrame(rows, columns=["scheme", "occ", "minor"]).drop_duplicates(["scheme", "occ"])
m["exposure"] = m.minor.map(expo)
print(m.groupby("scheme").agg(n=("occ", "size"), mapped=("exposure", lambda s: s.notna().sum())), file=sys.stderr)
m.to_csv(out, index=False)
print(expo.sort_values().tail(8).round(3).to_string(), file=sys.stderr)
print(expo.sort_values().head(5).round(3).to_string(), file=sys.stderr)
