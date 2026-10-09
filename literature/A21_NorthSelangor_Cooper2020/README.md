# A21: North Selangor forest-to-oil-palm conversion stages, GHG and WT, Malaysia

**Status:** Downloaded (part of the data)

**Data source:** [Nature Communications supplementary files](https://doi.org/10.1038/s41467-020-14298-w); licence CC BY 4.0

**Paper:** Cooper et al. 2020, Nature Communications 11, https://doi.org/10.1038/s41467-020-14298-w (Open; downloaded to paper/)

> Data availability: 'All data are available on request from the authors. The source data underlying Figs. 1-3 are provided as a Source Data file; additional data are in Supplementary Data 1 file.'

**How the paper used the data:** CO2, CH4 and N2O fluxes in four conversion stages (secondary forest, drained forest, young and mature oil palm) in North Selangor Peat Swamp Forest; sampling repeated three times in the 2014 wet season (Oct-Dec; annual fluxes from Nov-Dec 2014), 150 sampling points at 20 sites. Water table was read in dipwells at each plot at the time of gas sampling and used to test whether WT explained the fluxes; monthly WT over two years at two secondary-forest locations is described but not published. Conversion raised CO2 and N2O and lowered CH4.

- Plot coordinates are not given in the paper.
- Cooper2020_SourceData.xlsx 'Basic data' and Cooper2020_SupplementaryData1.xlsx hold the same plot table (not byte-identical); 'Water Table / cm Time 1' has 20 values ('PLUS 10' = +10 cm).

## Files in `data/`

- `Cooper2020_SourceData.xlsx` (Basic data): Per-sampling GHG means, soil moisture/temperature; WT at sampling time (Time 1); Fig. 1-2 data. 2014-10 to 2014-12, per sampling (5 per class). WTD: Yes: cm; negative = below peat surface (single readings)
- `Cooper2020_SupplementaryData1.xlsx`: Same plot table as 'Basic data'. WTD: Yes (as above)

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A21`.
