# Australian evidence: generative AI exposure and young workers' employment

All inputs are public. Raw files are not stored here; download them as below.

| Input | Source |
|---|---|
| `EQ07a.xlsx`: employed persons by age, ANZSCO sub-major group and sex, quarterly, Aug 1986 to Feb 2026 | ABS, Labour Force, Australia, Detailed (March 2026 release): https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia-detailed/mar-2026/EQ07a.xlsx |
| `EQ08.xlsx`: employed persons by ANZSCO unit group (used for 2019 employment weights) | same release, `EQ08.xlsx` |
| `corr.xls`: ANZSCO v1.2 to ISCO-08 correspondence | ABS cat. 1220.0, ANZSCO 2013 v1.2, "ANZSCO Correspondence to ISCO-08 v2.xls" |
| `ilo.json`: generative AI task exposure scores by ISCO-08 4-digit occupation | ILO Working Paper 140 (Gmyrek et al., 2025), data at https://pgmyrek.github.io/2025_GenAI_scores_ISCO08/output_data.json |

Steps:
1. `build_exposure.py ilo.json corr.xls EQ08.xlsx exposure_submajor.csv`: ISCO-08 occupation exposure = mean task score; mapped to ANZSCO 6-digit occupations (mean over matched ISCO unit groups), averaged to 4-digit unit groups, then employment-weighted (2019) to 43 sub-major groups.
2. `analyse_au.py EQ07a.xlsx exposure_submajor.csv submajor_codes.tsv .`: outcome is the log employment gap between a young age group and ages 35–54 within occupation and quarter (equivalent to a triple difference with occupation × quarter fixed effects); regressed on standardised exposure × post-November-2022, with occupation and quarter fixed effects, weighted by 2019 young employment, standard errors clustered by occupation (43 clusters). Also an event study by year (2022 = reference), a 2019 placebo and alternative specifications.
3. `robust_au.py` (same arguments): timing split (2023–24 vs 2025–26) and exposure-specific pre-trends.
4. `plot_event.py event_study.csv figure3`.

Results files: `ddd_results.csv`, `robustness.csv`, `event_study.csv`, `young_share_by_tercile.csv`.

## Japan

`japan/` holds the Japanese panel built from the Labour Force Survey (Statistics Bureau of Japan, e-Stat), the definition-based mapping of Japanese occupation groups to ISCO-08 sub-major groups (`jp_isco_map.csv`; no official detailed correspondence exists), sources (`jp_sources.csv`, `README_data.md`) and `analyse_jp.py`, which applies the same design to annual data for 2018–2025 (single 2020 census population basis), 30 occupation groups.

## Three-country figure

`plot_three.py us/us_event_study.csv event_study.csv japan/jp_event_study.csv ../figure2` produces Figure 2.

Note: earlier runs also tried occupation-specific linear trends for Australia; these were numerically unstable with 43 clusters and are not reported.
