#!/bin/bash
S=${S:-.}  # working directory for downloads
for y in 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026; do
  yy=${y:2:2}
  for m in jan apr jul oct; do
    mm=$m; if [ "$y$m" = "2025oct" ]; then mm=nov; fi
    out=$S/data_us/agg/${y}_${mm}.csv
    [ -s "$out" ] && continue
    raw=$S/data_us/raw/${mm}${yy}pub.dat.gz
    for t in 1 2 3; do curl -sfL -m 900 -o "$raw" "https://www2.census.gov/programs-surveys/cps/datasets/$y/basic/${mm}${yy}pub.dat.gz" && break; sleep $((t*5)); done
    if [ -s "$raw" ]; then python3 -I $S/us_scripts/cps_agg.py "$raw" "$out" && echo "ok $y $mm"; else echo "FAIL $y $mm"; fi
    rm -f "$raw"
  done
done
echo DONE
