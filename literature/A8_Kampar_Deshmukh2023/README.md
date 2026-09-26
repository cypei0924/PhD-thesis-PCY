# A8: Kampar Peninsula Acacia plantation / degraded / intact, Riau

**Status:** Downloaded

**Data source:** [Zenodo 7500659 (index link)](https://doi.org/10.5281/zenodo.7500659), [Zenodo 7728463 (cited in the paper)](https://doi.org/10.5281/zenodo.7728463); licence CC-BY-4.0

**Paper:** Deshmukh et al. 2023, Nature 616, https://doi.org/10.1038/s41586-023-05860-9 (Hybrid OA (CC-BY); also in PMC (PMC10132972))

> Data availability: "All data that support the findings of this study are archived on Zenodo at 10.5281/zenodo.7728463."

**How the paper used the data:** GWL loggers (Solinst Levelogger 3001, every 30 min, perforated PVC anchored in clay): 4 around the plantation tower, 1 at the degraded site, 6 at the intact site; annual means average 11, 4 and 15 locations. GWL is the main explanatory variable for CO2, CH4 and N2O across the three land covers, and the paper places its sites on literature GWL-flux relationships (Fig. 3, ED Fig. 3c). ED Fig. 2a shows daily intact-site GWL (mean of 3 piezometers spanning 12 km) against the 90-day mean of rainfall minus ET.

- Two Zenodo versions are kept: data/ holds 7500659 (the index link), data/zenodo_7728463_v03/ the version the paper cites. The daily GWL series is identical in both; v03 expands the diel ET panels of ED Fig. 2.
- Only the intact-site GWL is published as a daily series; plantation and degraded-site GWL appear only as annual means (ED Table 2 in the paper).
- Fig. 1 file gives the Acacia tower at 0 30'57"N, 102 02'11"E, about 70 km west of the other towers although the paper describes one landscape; check against the paper's Fig. 1 before using it.

## Files in `data/`

- `Deshmukh_ED_Fig. 2.xlsx` (Panel a (identical in zenodo_7728463_v03/)): Daily GWL and 90-day (rain - ET). 2017-06-01 to 2022-05-30, 1 d. WTD: Yes: m; negative = below peat surface
- `Deshmukh_ED_Fig. 2.xlsx` (Panels b, c): Diel ET in dry and wet season. 
- `Deshmukh_ED_Fig. 1.xlsx`: Daily cumulative net CO2 and CH4 with uncertainty. 2016-10-01 to 2022-05-31, 1 d. 
- `Deshmukh_ED_Fig. 3.xlsx`: Quarterly soil N2O; literature GWL vs N2O. WTD: Yes (literature site means)
- `Deshmukh_Fig. 1.xlsx`: Coordinates (DMS): intact 0.3952 N 102.7645 E; degraded 0.6995 N 102.7933 E; Acacia 0.5159 N 102.0364 E (see note). 
- `Deshmukh_Fig. 2.xlsx`: GHG balance table. 
- `Deshmukh_Fig. 3.xlsx`: GWL vs net CO2 and CH4 from eddy-covariance studies. WTD: Yes (site means)

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A8`.
