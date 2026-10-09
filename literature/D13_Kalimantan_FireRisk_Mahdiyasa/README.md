# D13: Kalimantan peatland fire-risk table (WT height, land cover, fires)

**Status:** Downloaded

**Data source:** [Zenodo 17907349](https://doi.org/10.5281/zenodo.17907349); licence CC-BY-4.0

**How the paper used the data:** No paper confirmed; the same author published peatland fire-risk models in 2025-2026 (e.g. Mahdiyasa et al. 2025, Ecological Informatics, 'Peatfr').

- No dates in the file: Water Table Height has only 340 distinct values, so it is a coarse gridded or modelled field sampled at about 0.009 deg (1 km) points, not a measurement.

## Files in `data/`

- `Kalimantan Tropical Peatland Data.csv`: Water Table Height (m), distance to human activities, land cover, fire occurrence. WTD: Yes (static): m; negative = below surface

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py D13`.
