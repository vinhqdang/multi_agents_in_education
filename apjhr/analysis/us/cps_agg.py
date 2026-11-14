"""Aggregate one CPS basic monthly file (fixed width, gz) to weighted employment by occupation code x age group."""
import gzip, sys, collections
src, dst = sys.argv[1:3]
agg = collections.defaultdict(float)
def ageg(a):
    if a < 16: return None
    return "16-21" if a <= 21 else "22-25" if a <= 25 else "26-30" if a <= 30 else "31-34" if a <= 34 else "35-54" if a <= 54 else "55+"
with gzip.open(src, "rt", encoding="latin-1") as f:
    for line in f:
        if len(line) < 863: continue
        try:
            age = int(line[121:123]); lf = int(line[179:181]); occ = line[859:863].strip(); w = int(line[845:855]) / 1e4
        except ValueError:
            continue
        if lf not in (1, 2) or not occ or occ.startswith("-"): continue
        g = ageg(age)
        if g and w > 0: agg[(occ, g)] += w
with open(dst, "w") as o:
    o.write("occ,ageg,emp\n")
    for (occ, g), v in sorted(agg.items()): o.write(f"{occ},{g},{v:.1f}\n")
