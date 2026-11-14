"""Build GenAI exposure for ANZSCO v1.2 sub-major groups from the ILO (Gmyrek et al., 2025) ISCO-08 task scores."""
import json, re, sys, collections
import xlrd, openpyxl
ilo_json, corr_xls, eq08, out_csv = sys.argv[1:5]

# 1. ISCO-08 4-digit exposure = mean of task scores
d = json.load(open(ilo_json))
isco = {}
def walk(n):
    m = re.match(r"(\d{4}) - ", n["name"])
    if m and "children" in n:
        scores = [float(re.match(r"\(\s*([\d.]+)\s*\)", c["name"]).group(1)) for c in n["children"] if re.match(r"\(\s*[\d.]+\s*\)", c["name"])]
        if scores:
            isco[m.group(1)] = (sum(scores) / len(scores), n.get("risk", ""))
        return
    for c in n.get("children", []):
        walk(c)
walk(d)
print("ISCO unit groups with scores:", len(isco), file=sys.stderr)

# 2. ANZSCO 6-digit -> ISCO-08 unit groups (ABS correspondence, Table 1)
sh = xlrd.open_workbook(corr_xls).sheet_by_index(1)
anz = collections.defaultdict(set)
for i in range(sh.nrows):
    r = sh.row_values(i)
    a, c = str(r[0]).split(".")[0].strip(), str(r[2]).split(".")[0].strip()
    if re.fullmatch(r"\d{6}", a) and re.fullmatch(r"\d{4}", c):
        anz[a].add(c)
occ = {}
for a, cs in anz.items():
    v = [isco[c][0] for c in cs if c in isco]
    if v:
        occ[a] = sum(v) / len(v)
print("ANZSCO occupations mapped:", len(occ), "of", len(anz), file=sys.stderr)

# 3. Unit group (4-digit) = mean of its occupations; weights = average employment 2019 from EQ08
unit = collections.defaultdict(list)
for a, v in occ.items():
    unit[a[:4]].append(v)
unit = {u: sum(v) / len(v) for u, v in unit.items()}
wb = openpyxl.load_workbook(eq08, read_only=True)
ws = wb["Data 1"]
w = collections.defaultdict(float); n = collections.defaultdict(int)
hdr = None
for r in ws.iter_rows(values_only=True):
    if hdr is None:
        if r and r[0] == "Mid-quarter month":
            hdr = r
        continue
    if r[0] is None or r[0].year != 2019:
        continue
    code = re.match(r"(\d{4})", str(r[3]))
    if code:
        w[code.group(1)] += (r[4] or 0)
print("EQ08 header:", hdr[:6], file=sys.stderr)

# 4. Sub-major (2-digit) = employment-weighted mean of unit groups
sub = collections.defaultdict(lambda: [0.0, 0.0])
for u, v in unit.items():
    wt = w.get(u, 0.0)
    if wt > 0:
        sub[u[:2]][0] += v * wt; sub[u[:2]][1] += wt
with open(out_csv, "w") as f:
    f.write("submajor,exposure,emp2019_weight\n")
    for s, (num, den) in sorted(sub.items()):
        f.write(f"{s},{num/den:.4f},{den:.1f}\n")
print("sub-major groups:", len(sub), file=sys.stderr)
