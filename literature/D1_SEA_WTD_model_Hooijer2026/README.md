# D1: SE Asia forested-peatland WTD model maps

**Status:** Downloaded

**Data source:** [Mendeley Data 69mbg22fxf](https://doi.org/10.17632/69mbg22fxf); licence CC BY 4.0

**Paper:** Hooijer & Vernimmen 2026, Scientific Reports, https://doi.org/10.1038/s41598-026-64641-2 (Gold OA (CC-BY); also PMC13503653)

> Data availability: "The rainfall and WTD maps presented in this paper are available online in GIS format (https://doi.org/10.17632/69mbg22fxf). ... updated maps can be shared by the authors upon reasonable request."

**How the paper used the data:** A simple water-balance model driven by GPM IMERG satellite rainfall produces 25 years of indicative daily WTD for forested peat, calibrated on four long-term records: Sarawak (Busman et al. 2023, 8 y), Riau (A8, 6 y), Central Kalimantan (A3, 16 y) and South Sumatra (C1, 5 y). Daily results are summarised into maps of hydrological regime (annual mean and minimum WTD, days below -0.5 m) to discuss variable WTD targets for restoration.

- The published files are 10 summary GeoTIFFs, not daily grids; the index's 'daily, ~25 y' describes the model, not the download.

## Files in `data/`

- `Fig4a_WTD_annual_mean.tif`: Annual mean WTD (m); EPSG:4326, 243 x 135 cells, 2797 peat cells. 2000 to 2024, 0.1 deg grid. WTD: Yes: m; negative = below peat surface
- `Fig4b_WTD_min_overall_2000_2024.tif`: Minimum WTD over 2000-2024 (m). 2000 to 2024, 0.1 deg grid. WTD: Yes: m; negative = below peat surface
- `Fig4c_WTD_annual_mean_min.tif`: Mean annual minimum WTD (m). 2000 to 2024, 0.1 deg grid. WTD: Yes: m; negative = below peat surface
- `Fig4d_WTD_annual_mean_days_below_min0p5m.tif`: Mean days per year with WTD below -0.5 m. 2000 to 2024, 0.1 deg grid. 
- `Fig4e_WTD_longest_period_overall_wtd_below_0p5m_2000_2024.tif`: Longest period with WTD below -0.5 m (days). 2000 to 2024, 0.1 deg grid. 
- `Fig2a-e_GPM_*.tif (5 files)`: GPM IMERG rainfall statistics (annual mean/min, 91-day minimum, dry-period length). 2000 to 2024, 0.1 deg grid. 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py D1`.
