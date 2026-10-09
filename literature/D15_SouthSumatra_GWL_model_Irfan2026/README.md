# D15: Modelled 1-km GWL maps for South Sumatra peat units, wet and dry windows 2019

**Status:** Downloaded

**Data source:** [Zenodo 23008826](https://doi.org/10.5281/zenodo.23008826); licence CC-BY-4.0 (scripts MIT)

**How the paper used the data:** A Ridge regression of Sentinel-1, GPM and SMAP predictors, calibrated on field GWL (BRGM SIPALAGA stations), was applied in Google Earth Engine to 23 scenes per window; scenes were aggregated to 1 km and median-composited. The accompanying article (Irfan et al., submitted to Science of the Total Environment) is not yet published.

- The SIPALAGA field data used for calibration are NOT included (provider's access conditions).
- Same research group as B9 (Irfan 2020/2023) and C42 (Khakim 2022).

## Files in `data/`

- `A09_FINAL_GWL_WET_1KM_KHG_SUMSEL.tif`: Modelled GWL, 1-13 April 2019 (m, EPSG:32748, 1 km). 2019-04-01 to 2019-04-13, composite. WTD: Yes (model): m; negative = below peat surface
- `A09_FINAL_GWL_DRY_1KM_KHG_SUMSEL.tif`: Modelled GWL, 13-25 November 2019. 2019-11-13 to 2019-11-25, composite. WTD: Yes (model): m; negative = below peat surface
- `A09_FINAL_DRYING_*.tif, A09_*UNCERTAINTY*.tif, A09_DRYING_BOOTSTRAP_*.tif, *.zip, *.csv, README.md`: Drying magnitude, bootstrap uncertainty, QA tables, model coefficients, GEE scripts. 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py D15`.
