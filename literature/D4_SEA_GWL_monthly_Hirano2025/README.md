# D4: Monthly GWL, NEE and peat decomposition by province and land use, 2011-2020 (your D4)

**Status:** Downloaded

**Data source:** [figshare 30761072 (Hirano 2025)](https://doi.org/10.6084/m9.figshare.30761072); licence CC BY 4.0

**Paper:** Hirano et al. 2025, AGU Advances 6, https://doi.org/10.1029/2025AV001861 (Open access, but the publisher blocked the download; abstract only)

> Data availability: Not read; the figshare record (T. Hirano, December 2025) matches the paper's scope (CO2 and CH4 from SE Asian peatlands, GWL from satellite antecedent precipitation).

**How the paper used the data:** The paper estimates spatio-temporal GWL from satellite antecedent precipitation and uses GWL-flux relations to compute net CO2 and CH4 emissions of about 180,000 km2 of SE Asian peatland under undrained forest, drained forest and plantation (abstract and press release).

- Values are modelled province means, not measurements: one sheet per variable and land use (Precipitation; GWL_, NEECO2_, NEECH4_, SoilRH_ for UndrainedPSF, DrainedPSF and MP), columns = 13 Indonesian provinces, 13 Malaysian states and Brunei.
- figshare blocks scripts; the file was saved with a headless browser.

## Files in `data/`

- `MonthlyData250816.xlsx` (GWL_UndrainedPSF): Monthly GWL (m). 2011-01 to 2020-12, 1 month. WTD: Yes (model): m; negative = below peat surface
- `MonthlyData250816.xlsx` (GWL_DrainedPSF): Monthly GWL (m). 2011-01 to 2020-12, 1 month. WTD: Yes (model): m; negative = below peat surface
- `MonthlyData250816.xlsx` (GWL_MP): Monthly GWL (m). 2011-01 to 2020-12, 1 month. WTD: Yes (model): m; negative = below peat surface
- `MonthlyData250816.xlsx` (Precipitation, NEECO2_*, NEECH4_*, SoilRH_*): Monthly precipitation; NEE CO2 (Mg CO2 ha-1 month-1), NEE CH4, soil heterotrophic respiration. 2011-01 to 2020-12, 1 month. 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py D4`.
