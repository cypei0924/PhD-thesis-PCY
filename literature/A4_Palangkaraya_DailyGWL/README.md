# A4: Palangkaraya daily groundwater level (UF, DF)

**Status:** Downloaded

**Data source:** [figshare 22321129](https://doi.org/10.6084/m9.figshare.22321129.v1); licence CC BY 4.0

**Paper:** Hirano et al. 2014, Global Change Biology 21 (methods reference cited by the record), https://doi.org/10.1111/gcb.12653 (Accepted manuscript (Hokkaido Univ. repository))

> Data availability: Not applicable (the dataset post-dates the paper; the record cites it only for methods).

**Paper:** Hirano et al. 2012, Global Change Biology 18 (methods reference), https://doi.org/10.1111/j.1365-2486.2012.02793.x (Closed)

> Data availability: Not applicable.

**Paper:** Ohkubo, Hirano & Kusin 2023, Journal of Hydrology 620 (probable companion paper, inferred), https://doi.org/10.1016/j.jhydrol.2023.129523 (Free to read on ScienceDirect (bronze); blocks scripts)

> Data availability: Not read (ScienceDirect blocked). Link to this dataset is inferred from the same authors, sites and years, not confirmed.

**How the paper used the data:** GWL (distance between ground and water surface) was logged every 30 min with a water-level logger (Sensor Technik DL/N or Keller DCX-22) within 5 m of each tower (Hirano 2014 methods); this file gives daily means. The figshare record only cites the 2012/2014 methods papers. The 2013-2018 period matches Ohkubo et al. 2023 (J. Hydrol.), which studies transpiration and evaporation in these forests, but that link is my inference.

- These daily values are essentially the daily mean of A3's half-hourly GWL: mean absolute difference 0.2 cm (UF, 1461 days) and 1.2 cm (DF, 1618 days). Use A3 if you need sub-daily data or the DB site.

## Files in `data/`

- `DailyGWL.xlsx` (sheet UF): Year, DOY, GWL (m). 2015-01-01 to 2018-12-31, 1 d. WTD: Yes: m; negative = below peat surface
- `DailyGWL.xlsx` (sheet DF): Year, DOY, GWL (m). 2013-01-01 to 2017-06-06, 1 d. WTD: Yes: m; negative = below peat surface

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A4`.
