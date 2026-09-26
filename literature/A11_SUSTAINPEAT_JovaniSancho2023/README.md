# A11: 48 smallholder plots (SUSTAINPEAT), Selangor and West/Central Kalimantan

**Status:** Downloaded

**Data source:** [Nottingham repository doi:10.17639/nott.7296](https://doi.org/10.17639/nott.7296); licence CC-BY-4.0

**Paper:** Jovani-Sancho et al. 2023, Global Change Biology 29, https://doi.org/10.1111/gcb.16747 (Hybrid OA (CC-BY); accepted version on NERC NORA)

> Data availability: "The data that support the findings of this study are openly available in the Nottingham Research Data Management Repository at https://doi.org/10.17639/nott.7296."

**How the paper used the data:** WTD was read manually in a perforated PVC dipwell (2 m long, 1.5 m in the peat) next to each plot at every monthly gas-sampling visit. It was a fixed effect in mixed models of CH4 and N2O, and was used to fit an exponential CH4-WTD model (net CH4 emission starts around WTD -25 to -30 cm) and sigmoidal/linear N2O-WTD models; Fig. 2 shows seasonal WTD by land use.

- Plot coordinates are not published (only region names and a map); regions: NS = North Selangor, SS = South Selangor, WK = West Kalimantan, CK = Central Kalimantan.
- Two sampling methods are mixed in the file: 'vial' (static chambers, GC) and 'LGR' (dynamic chamber, Los Gatos).

## Files in `data/`

- `CH4_and_N2O_emissions_SUSTAINPEAT_data_paper.xlsx` (sheet data (codes in sheet metadata)): CH4, N2O (ug m-2 h-1), air T, soil T10, WTD, total dissolved N. 2018-03-21 to 2019-04-01, Monthly visits (20-32 dates per region). WTD: Yes: cm; negative = below peat surface

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A11`.
