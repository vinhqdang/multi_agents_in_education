# Japan LFS employment by occupation x age, 2015 to 2026Q3

Source: Statistics Bureau of Japan (MIC), Labour Force Survey (労働力調査, LFS), downloaded from e-Stat on 2026-11-14. Everything here is published tabulated data. Nothing is imputed. The 10-year age groups in the annual file are sums of published 5-year cells.

**Unit: `employed_10k` = employed persons in units of 10,000 (万人), rounded to integers as published.** "-" in the source (no sample observation) is stored as 0.

## Files

| file | content |
|---|---|
| `jp_panel.csv` | **Annual (calendar-year average), 2015-2025.** 37 occupation categories plus the total: 12 JSOC major groups and the 25 LFS sub-groups under them (11 sub-groups for 2015, see caveats). 5-year ages 15-19 to 60-64, 65+, 65-69, 70-74, 70+, 75+; 10-year groups 15-24 to 55-64 derived from the 5-year cells; total. Sex: total, male, female. |
| `jp_panel_quarterly.csv` | **Quarterly, 2015Q1-2026Q3 (47 quarters).** 12 JSOC major groups plus the total, by published 10-year ages 15-24, 25-34, 35-44, 45-54, 55-64, 65+, total, and the memo item "15-24 of which enrolled in school" (`15-24_in_school`). Sex: total, male, female. |
| `jp_panel_overlap_2015census_basis.csv` | The same tables on the older 2015-Census population basis for 2018-2021 (annual) and 2018Q1-2021Q4 (quarterly). Use only to check the population-benchmark revision; they are not part of the main series. |
| `jp_isco_map.csv` | Each occupation code mapped to its JSOC-2009 middle groups and to ISCO-08 major and sub-major groups, with a one-line justification. |
| `jp_sources.csv` | Every downloaded table: statInfId, table number, period, e-Stat collection, download URL. |

Columns in the panels: `period` (YYYY or YYYY-Qn), `occupation_code`, `occupation_name_en`, `age_group`, `employed_10k`, `sex`, `occupation_name_ja`, `occupation_level` (total/major/sub), `parent_code`, `age_level` (total / 5yr / 10yr / 10yr_derived / 65plus / 65plus_detail / memo), `pop_benchmark`, `bench_link_factor`, `source_table`, `statInfId`.

To get non-overlapping cells, filter on `age_level`:
- Annual 10-year scheme: `10yr_derived` + `65plus`.
- Annual 5-year scheme: `5yr` + `65plus`.
- Quarterly: `10yr` + `65plus`.

The finest non-overlapping annual occupation set has 31 cells:
- the 6 major groups that have no sub-groups: A, F, G, I, J, L
- the 25 sub-groups: B1-B4, C1-C3, D1-D3, E1-E5, H1-H7, K1-K3

## Source tables

### Annual: 基本集計 第II-A表「年齢階級，職業別就業者数」

LFS Basic Tabulation, Table II-A, "Employed persons by age group and occupation". It is published annually only and does not exist in the monthly or quarterly releases.

- 2018-2025, 2020 Census basis. e-Stat > 労働力調査（公表資料、時系列結果など）> 結果原表 > 基本集計 > 年次. statInfIds:
  - 2018 000032173998
  - 2019 000032174146
  - 2020 000032174222
  - 2021 000032173850
  - 2022 000040008573
  - 2023 000040137572
  - 2024 000040243373
  - 2025 000040403942
- 2016-2017, 2015 Census basis. e-Stat > 労働力調査（旧基準：2015年国勢調査を基準とした結果）> 結果原表 > 基本集計 > 年次. statInfIds:
  - 2016 000031534426
  - 2017 000031667362
  - The 2018-2021 overlap on this basis is in the overlap file: 000031789368, 000031905262, 000032045562, 000032164193.
- 2015: no II-A table exists for 2015. The panel uses 労働力調査年報 2015, 第I-B-7表「年齢階級，職業別就業者数（実数及び構成比）」 (Annual Report 2015, Table I-B-7, "Employed persons by age group and occupation"), statInfId 000031415887. It is on the 2010 Census basis, as originally published, and its oldest age group is 65+.

### Quarterly: 詳細集計 第II-1表

「従業上の地位・雇用形態・雇用契約期間・産業・職業，年齢階級・配偶関係・世帯の種類・世帯主との続き柄・教育・従業者規模別就業者数」 (LFS Detailed Tabulation, Table II-1, "Employed persons by employment status, industry and occupation x age, marital status, household, education and enterprise size"). Only the occupation x age block is extracted, for all employed persons.

- 2018Q1-2026Q3, 2020 Census basis. e-Stat > 労働力調査（公表資料、時系列結果など）> 結果原表 > 詳細集計 > 四半期.
- 2015Q4-2017Q4, 2015 Census basis, from the 旧基準 collection. The 2018Q1-2021Q4 overlap on this basis is in the overlap file.
- 2015Q1-Q3, 2010 Census basis, as originally published.
- All statInfIds are in `jp_sources.csv`.

### Other sources

- Download URL pattern: `https://www.e-stat.go.jp/stat-search/file-download?statInfId=<id>&fileKind=0` (Excel).
- Listing pages: `https://www.e-stat.go.jp/stat-search/files?toukei=00200531&tstat=000001226583` (current) and `...&tstat=000001226703` (2015 Census basis).
- Category contents: LFS 産業・職業分類表 (Annual Report appendix 付8, "Industry and occupation classification table"), statInfId 000040199044 (PDF).
- JSOC 2009 item list: https://www.soumu.go.jp/main_content/000587432.csv

## Classification: no occupation break, 2015-2026Q3

The LFS has used the Japan Standard Occupational Classification (JSOC, 日本標準職業分類), December 2009 revision, from January 2011 results onward. It still did at the latest release (2026Q3).

- A 6th revision of JSOC was presented to the Statistics Commission's standards subcommittee in October 2026 (総務省「日本標準職業分類の変更について」, 第21回統計基準部会 資料3, https://www.soumu.go.jp/main_content/001094895.pdf). It has not yet been applied to any LFS release.
- The 37 column headings are identical in every year, 2016-2025.
- **There is no occupation classification break in these files.** A break should be expected when the LFS adopts the new JSOC, probably a few years from now.

The LFS occupation categories are the 12 JSOC major groups plus 25 LFS-specific groupings of JSOC middle groups (listed in `jp_isco_map.csv`). The LFS application of JSOC middle groups 49-51 (生産設備制御・監視従事者, "production equipment control and monitoring workers") is not stated in the LFS classification table. I assumed 49→H1, 50→H2 and 51→H3, following census practice.

**Detail limit:** the finest occupation x age cross available from public LFS tables is:
- annual: 37 categories (major groups plus about 25 aggregated sub-groups) by 5-year ages;
- quarterly or monthly: the 12 major groups by 10-year ages, from the detailed tabulation.

No public LFS table crosses JSOC middle (74 groups) or minor (329 groups) occupations with age. The monthly basic tables show occupation and age only as separate margins, never crossed.

Finer occupation x age data exist only in:
- the Population Census (2015, 2020; 2025 occupation results not yet released);
- the Employment Status Survey (Oct 2017, Oct 2022, i.e. before ChatGPT).

Neither gives a post-Nov-2022 time series.

## Population-benchmark breaks

LFS estimates are benchmarked to census-based population estimates. The files use three bases:

| periods | basis |
|---|---|
| 2015 annual and 2015Q1-Q3 | 2010 Census |
| 2016-2017 annual and 2015Q4-2017Q4 | 2015 Census |
| 2018 onward | 2020 Census, the current official series, revised back to 2018 when the switch was made in 2022 |

The 2015 to 2020 Census switch is age-specific. Ratios of the 2020 basis to the 2015 basis for total employment in 2018, both sexes:

| age | ratio |
|---|---|
| 15-24 | 0.998 |
| 25-34 | 1.009 |
| 35-44 | 1.006 |
| 45-54 | 1.005 |
| 55-64 | 1.003 |
| 65+ | 0.999 |

These differences widen by 2021: 0.995 for 15-24 and 1.017 for 25-34. The revision moves young vs prime-age levels by about 1-2%, which is the same order as the effects being tested.

`bench_link_factor` is the ratio for each sex x age group, taken from the 2018 overlap: annual 2018, or the sum of 2018Q1-Q4 for the quarterly file. Its values:
- 1 for 2020-basis rows;
- the ratio for 2015-basis rows; multiply `employed_10k` by it for an approximate splice;
- empty for 2010-basis rows (no overlap is available).

**For the post-Nov-2022 test, use 2018 onward (a single basis): 2018-2022 annual or 2018Q1-2022Q4 as the pre-period.**

## Caveats

1. **Rounding and sampling.** Cells are integers in units of 10,000. Many youth cells are small: for example, accountancy clerks aged 15-24 are 6-8 (60-80 thousand people). Changes of ±1 are rounding noise, and published sums do not add exactly. In checks, sub-groups vs major, ages vs total, majors vs total and male + female vs total all agree within ±6 (±4 in most). The derived 10-year cells carry up to ±1 extra rounding error.
2. **Two different samples.** The quarterly Table II-1 comes from the LFS detailed tabulation, which uses the special questionnaire given to about a quarter of the sample. It is noisier than the annual Table II-A and differs slightly in level (for example, 2025Q1 total 6,764 vs 2025 annual average 6,828). Do not mix the two series in one regression without a source fixed effect.
3. **2015 annual differences.** The 2015 row comes from the Annual Report table and differs from the other years in three ways:
   - It has no "not classifiable" (L) column, so the majors sum to 40-92 less than the total.
   - It has no 65-69/70+ split.
   - It is on the 2010 Census basis.
4. **Students.** Youth employment in Japan is dominated by students working part-time (アルバイト), concentrated in sales and service occupations. The quarterly memo item `15-24_in_school` lets you exclude students. The annual table has no such split.
5. **JSOC vs ISCO-08.** JSOC does not separate professionals from associate professionals. It also places shop and restaurant owner-managers in sales and service rather than managers, and clerical work is broader than ISCO 4. Exposure scores built on ISCO or SOC must therefore be cross-walked through `jp_isco_map.csv`, which is approximate.
6. **ISCO mapping source.** I found no official detailed JSOC 2009 to ISCO-08 concordance. MIC publishes only an approximate major-group comparison: 「日本標準職業分類（平成9年時点、平成21年基準）及び国際標準職業分類の分類項目比較表」 (comparison of JSOC 1997 and 2009 items with ISCO-08), https://www.soumu.go.jp/main_content/000394426.pdf. The sub-major mappings in `jp_isco_map.csv` were made **by definition**, from the JSOC middle-group contents and the ISCO-08 group definitions.
7. **Period definitions.** Annual figures are calendar-year averages of monthly estimates. Quarterly figures are averages of three months (Q1 = Jan-Mar). The data are not seasonally adjusted, so use same-quarter comparisons or quarter fixed effects.

## Reproduction

Scripts are in `../../jp_scripts/` and are run with `python3 -I`:
- `crawl.sh`: e-Stat listing pages
- `index.py`: table index
- `build.py`: parse the Excel files
- `validate.py`: consistency checks
- `finalize.py`: write the panels
- `isco_map.py`: write the ISCO map

The raw Excel files are in `../dl/<collection>_<table>_<statInfId>/`.
