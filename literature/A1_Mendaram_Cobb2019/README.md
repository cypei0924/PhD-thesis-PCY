# A1: Mendaram peat dome (undrained), Brunei

**Status:** Downloaded

**Data source:** [PANGAEA collection](https://doi.org/10.1594/PANGAEA.908215); licence CC-BY-4.0

**Paper:** Cobb & Harvey 2019, Water Resources Research 55, https://doi.org/10.1029/2019WR025411 (Open (publisher author manuscript); Wiley blocks scripts, open in a browser)

> Data availability: Not read (Wiley blocked automated access). The PANGAEA README states the collection is the data used in this paper.

**How the paper used the data:** Four piezometers (Solinst Levelogger Edge, barometrically corrected, screened 1.30-1.45 m) logged water level every 20 min for a year, together with throughfall from four tipping-bucket gauges. Combined with the peat-surface Laplacian from the flowtube geometry, the water-level and throughfall series were used to fit hillslope-scale hydraulic conductivity (transmissivity) and specific yield as functions of water-table height, for a 'scalar' model that treats a peatland subcatchment as one storage unit. The fitted K and Sy knots are published as PANGAEA 908209 and 908210.

- The PANGAEA metadata query lists only 4 children; the 4 water-level series (908201, 908206-908208) were found from the collection page and added.
- README_Brunei_peat_swamp_data.pdf (dataset documentation, CC-BY) is downloaded but not committed because PDFs are git-ignored; download_data.py fetches it.

## Files in `data/`

- `PANGAEA_908201.tab`: Water level WL (m). 2012-02-06 22:20 to 2013-01-30 02:40, 20 min. WTD: Yes: m relative to the peat-surface datum of Cobb et al. 2017; + = above surface
- `PANGAEA_908206.tab`: Water level WL (m). 2012-02-06 22:20 to 2013-01-30 02:40, 20 min. WTD: Yes: as above
- `PANGAEA_908207.tab`: Water level WL (m). 2012-02-06 22:20 to 2013-01-30 02:40, 20 min. WTD: Yes: as above
- `PANGAEA_908208.tab`: Water level WL (m). 2012-02-06 22:20 to 2013-01-30 02:40, 20 min. WTD: Yes: as above
- `PANGAEA_908214.tab`: Throughfall intensity (mm/h). 2012-02-06 22:20 to 2013-01-30 02:40, 20 min. 
- `PANGAEA_908209.tab`: Hydraulic conductivity K(WL) knots with 95% CI. 
- `PANGAEA_908210.tab`: Specific yield Sy(WL) knots with 95% CI. 
- `PANGAEA_908211.tab`: Flowtube area vs integrated normal gradient. 
- `README_Brunei_peat_swamp_data.pdf`: Dataset README (not committed; PDF). 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A1`.
