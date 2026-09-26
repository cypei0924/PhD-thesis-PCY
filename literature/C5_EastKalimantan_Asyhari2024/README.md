# C5: Muara Siran undrained peatland, East Kalimantan

**Status:** Downloaded (part of the data)

**Data source:** [Zenodo 10427000](https://doi.org/10.5281/zenodo.10427000); licence CC-BY-4.0

**Paper:** Asyhari et al. 2024, Scientific Reports 14, https://doi.org/10.1038/s41598-024-62233-6 (Gold OA (CC-BY); also PMC11106321)

> Data availability: "All data that support the findings of this study are archived on 10.5281/zenodo.10427000."

**How the paper used the data:** CO2 and CH4 chamber fluxes (10 chambers per site, about 3 visits a month) with water level read manually at each chamber at the same time; an hourly Keller DCX-22 logger at each plot centre and a river logger (Siran River) track continuous water levels (Fig. 2). Water level is used to explain flux seasonality, e.g. CH4 rising as water fell from >1 m above the surface (Dec 2022) to near the surface (Jan 2023).

- The index rated C5 as 'figures only'; the paper's Data availability points to this Zenodo record.
- The hourly logger series of Fig. 2 are not in the archive.
- Site codes in the file are PPSF and DPSF; the paper text uses PPSF and SPSF.
- Sign: positive WaterDepth_cm = water above the peat surface (inferred from the flooding >1 m described in the paper).

## Files in `data/`

- `GHG_Flux_Data.xlsx` (sheet All Data): WaterDepth_cm, CO2 and CH4 flux (Mg CO2(e) ha-1 yr-1). 2022-10-27 to 2023-09-23, ~3 visits/month (36 dates). WTD: Yes: cm; + = above surface (inferred)
- `GHG_Flux_Data.xlsx` (sheet All Data): as above. 2022-10-27 to 2023-09-23, ~3 visits/month (36 dates). WTD: Yes: as above

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py C5`.
