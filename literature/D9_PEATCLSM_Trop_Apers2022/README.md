# D9: PEATCLSM_Trop simulations 2000-2019, SE Asia part (your D2)

**Status:** Downloaded (part of the data)

**Data source:** [Zenodo 6011689](https://doi.org/10.5281/zenodo.6011689); licence CC-BY-4.0

**Paper:** Apers et al. 2022, JAMES 14, https://doi.org/10.1029/2021MS002784 (Open; downloaded to paper/)

> Data availability: 'Groundwater level and eddy covariance data used for evaluation are available at the sources indicated in Table B1. Full simulation output is accessible on a Zenodo data repository (Apers et al., 2022).'

**How the paper used the data:** NASA GEOS Catchment model (CLSM) and its natural and drained tropical peat versions (PEATCLSM_Trop,Nat/Drain) run at 9 km (EASEv2) for 2000-2019 over SE Asia, the Congo Basin and Central/South America; simulated water level zbar was evaluated against the water-level sites of Table B1 (B5, B13, C15-C18, C48, C59 and INDEX A1-A3).

- Only the SE Asia (SEA) 20-year mean and standard deviation maps were downloaded (about 15 MB each). The daily image stacks daily_images_PEATSEA_N/_D and _CLSMSEA (7.1-7.3 GB each) exceed the 5 GB limit and were not fetched; the Congo (CO) and South America (CSA) files were skipped.
- Each file holds 23 variables; zbar (m, negative downwards) is the water level. 39,525 peat cells on a 266 x 643 grid, 11.4 S - 7.4 N, 95.0-154.9 E. Read with GDAL/rasterio as netcdf:<file>:zbar.
- PEATCLSM_Trop-Simulations_doc.pdf (data description) is in data/ but not committed (PDF).

## Files in `data/`

- `daily_mean_PEATSEA_N.nc`: 20-year mean of 23 land-surface variables incl. zbar. 2000-01-01 to 2019-12-31, 20-year mean. WTD: Yes (model): m; negative = below peat surface
- `daily_mean_PEATSEA_D.nc`: As above. 2000-01-01 to 2019-12-31, 20-year mean. WTD: Yes (model): m; negative = below peat surface
- `daily_mean_CLSMSEA.nc`: As above. 2000-01-01 to 2019-12-31, 20-year mean. WTD: Yes (model): m; negative = below peat surface
- `daily_std_PEATSEA_N.nc, daily_std_PEATSEA_D.nc, daily_std_CLSMSEA.nc`: 20-year standard deviation of the same variables. 2000-01-01 to 2019-12-31, 20-year SD. WTD: Yes (model, SD)

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py D9`.
