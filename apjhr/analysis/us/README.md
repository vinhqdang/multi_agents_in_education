# United States comparison (Current Population Survey)

Inputs (public):
- CPS basic monthly public-use files, January, April, July and October 2017–2026 (November 2025 replaces October 2025, which was not released): https://www2.census.gov/programs-surveys/cps/datasets/
- Census occupation code lists and 2010/2018 crosswalks with SOC codes: https://www2.census.gov/programs-surveys/demo/guidance/industry-occupation/
- GenAI exposure by O*NET-SOC occupation (GPT-4 rated beta), Eloundou et al. (2024): https://github.com/openai/GPTs-are-GPTs (data/occ_level.csv)

Steps: `fetch_all.sh` downloads each month and runs `cps_agg.py` (employed persons, composite weight, by Census occupation code × age group; positions from the record layouts: age 122–123, labour force status 180–181, occupation 860–863, weight 846–855). `build_us_exposure.py` maps Census codes to SOC minor groups (95) and averages exposure. `analyse_us.py` estimates the same specification as the Australian analysis with ages 22–25 and 26–30 against 35–54, standard errors clustered by SOC minor group.

January 2024 was distributed as a zip archive and was processed by extracting the .dat file and passing it to `cps_agg.py`.
