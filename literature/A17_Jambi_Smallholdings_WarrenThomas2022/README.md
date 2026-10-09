# A17: Oil palm smallholdings and Sungai Buluh protected forest, Jambi

**Status:** Downloaded

**Data source:** [Dryad](https://doi.org/10.5061/dryad.rr4xgxd9v); licence CC0-1.0

**Paper:** Warren-Thomas et al. 2022, Journal of Applied Ecology 59, https://doi.org/10.1111/1365-2664.14135 (Open; downloaded to paper/)

> Data availability: 'Data available via the Dryad Digital Repository https://doi.org/10.5061/dryad.rr4xgxd9v.'

**How the paper used the data:** Water tables were read manually every fortnight (August 2018 - August 2019) in a dipwell at each of 41 smallholder oil palm plots (3 sites) and 21 plots in the adjacent Sungai Buluh Peat Protection Forest; four LevelSCOUT loggers (15 min) in one dipwell per site were a sense-check. Plot indices (12-month mean, max depth, number of readings below 40 cm) were tested as predictors of bird diversity, vegetation structure and oil palm yield. Mean water tables were -52 to -3 cm on farms and -3 to +15 cm in the forest; no trade-off between wetness and yield or birds was detected.

- Coordinates are not given in the files or the paper (map only); the study area is in Jambi, next to the Sungai Buluh Peat Protection Forest.
- The README warns that sudden pressure drops mean a sensor was lifted out of the dipwell; the -210 cm minima in every logger series are such artefacts and should be removed.
- The per-plot manual summaries are in Oil_palm_yields_predictors.csv for 33 farms (the paper's yield models also used n = 33); the raw fortnightly readings and the forest plots' manual data are not in the dataset.
- Dryad blocks scripts (bot check and a token for its API); the files were saved with a headless browser.

## Files in `data/`

- `Water_tables_loggers.csv` (Site = Forest): Logger depth to water (cm) and water temperature. 2018-08-28 02:00 to 2019-07-14 14:15, 15 min. WTD: Yes: cm; negative = below peat surface (column ..._neg)
- `Water_tables_loggers.csv` (Site = Site 1): As above. 2018-09-08 01:43 to 2019-07-14 14:13, 15 min. WTD: Yes: cm; negative = below peat surface
- `Water_tables_loggers.csv` (Site = Site 2): As above. 2018-08-28 02:00 to 2019-07-14 14:15, 15 min. WTD: Yes: cm; negative = below peat surface
- `Water_tables_loggers.csv` (Site = Site 3): As above. 2018-09-10 01:05 to 2019-07-14 14:05, 15 min. WTD: Yes: cm; negative = below peat surface
- `Oil_palm_yields_predictors.csv`: Per-plot WT summaries from fortnightly manual readings (Wat_min/max/mean/SD_cm, n = 24 readings), yield, vegetation, management. 2018-08 to 2019-08, fortnightly (summarised). 
- `Rainfall.csv`: Daily manual rainfall (mm). 
- `README.txt`: Dataset README (variables, sensor notes). 
- `Bird_*.csv (5 files), Oil_palm_yields_predictors_description.csv`: Bird counts, species list, traits; variable descriptions. 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A17`.
