# A3: Palangkaraya UF / DF / DB flux towers, Central Kalimantan

**Status:** Downloaded

**Data source:** [figshare (link given in the paper)](https://figshare.com/s/6aefe20137486d0a6f62); licence CC BY 4.0

**Paper:** Hirano et al. 2024, Communications Earth & Environment 5:221, https://doi.org/10.1038/s43247-024-01387-7 (Gold OA (CC-BY); nature.com shows a bot check to scripts, open in a browser)

> Data availability: "The CO2 flux, meteorology, and groundwater level data that support the findings of this study are available on figshare [https://figshare.com/s/6aefe20137486d0a6f62]."

**How the paper used the data:** GWL was measured at a hollow next to each tower. The paper uses it (1) as a driver when gap-filling half-hourly NEE (marginal distribution sampling for daytime, a GWL look-up table for night-time), (2) to relate annual NEE, RE and GPP to annual mean GWL and to compare ENSO-drought, normal and wet years, and (3) to back-estimate monthly NEE from the 1997 canal excavation onward, using GWL estimated from a nearby record (Takahashi site, since 1993) and NEE-GWL regressions.

- UF and DF GWL columns contain no missing values over 15 years, so they are probably gap-filled; the paper does not say.
- Coordinates are from Hirano 2024; Hirano et al. 2014 gives DF as 2.35 S, 114.14 E instead of 114.04 E.
- Flux columns (fNEE, fGPP, fRE) end in 2017; environmental data continue to Dec 2019 (UF) and Jan 2017 (DB).

## Files in `data/`

- `CO2 flux data.zip` (UF_fluxdata230802.csv): Half-hourly fNEE, fGPP, fRE, H, LE, radiation, PPFD, T, RH, VPD, GWL, precipitation. 2004-07-10 00:30 to 2019-12-11 12:00, 30 min. WTD: Yes: m; negative = below peat surface (hollow)
- `CO2 flux data.zip` (DF_fluxdata230802.csv): as UF. 2001-11-28 00:30 to 2017-06-06 11:00, 30 min. WTD: Yes: m; negative = below peat surface (hollow)
- `CO2 flux data.zip` (DB_fluxdata230802.csv): as UF. 2004-04-17 00:00 to 2017-01-01 00:00, 30 min. WTD: Yes: m; negative = below peat surface (hollow)
- `CO2 flux data.zip` (Annual CO2 fluxes.csv): Annual precipitation, mean GWL, RE, GPP, NEE, GPP0, Gs,ref per site. 2002 to 2017, 1 year. WTD: Yes (annual mean)

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A3`.
