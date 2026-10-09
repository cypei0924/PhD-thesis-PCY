# A34: Bengkalis Island coastal peat: channel water level, surveys, weather (Riau)

**Status:** Downloaded (part of the data)

**Data source:** [Zenodo 19159832](https://doi.org/10.5281/zenodo.19159832); licence CC-BY-4.0

**Paper:** Kagawa et al. 2026, Biogeosciences 23, https://doi.org/10.5194/bg-23-2119-2026 (Open; downloaded to paper/)

> Data availability: 'The data for this paper is made available online at https://doi.org/10.5281/zenodo.19159833 (Kagawa et al., 2026).' (19159833 and 19159832 are two DOIs of the same Zenodo record.)

**How the paper used the data:** Estimates particulate organic carbon export to the sea from coastal erosion and peat mass movements (PMMs, peat landslides) on Bengkalis Island, using RTK-GNSS surveys, peat cores, DTMs and satellite land-cover series. A HOBO U-20 logger in a PVC well recorded the CHANNEL water level behind a weir at WP1 (1 December 2014 - 31 January 2015): the level fell from 9.124 m to 7.896 m within 10 minutes on 27 December 2014, dating the weir breach that triggered a PMM.

- WP1 is a waterway (channel) gauge, not a peat dipwell, and its values are ELEVATIONS (m above the survey datum; weir crest 9.00 m), not depths. No peat water-table series is in the dataset.
- The 2013 water-level survey and RTK files use UTM 48N; the transect lies at about 1.59-1.61 N, 102.02 E (north-west coast).
- Zenodo rate-limited this container: 8 of 33 files (metadata, carbon stocks, peat mass movement area-volume, vegetation and wind-wave tables) are missing; run `python3 download_data.py A34` locally. The partial error pages were renamed *.FAILED_403.html (git-ignored).
- Same island as C35 (Sutikno 2026) and the B9 SESAME station at Dompas.

## Files in `data/`

- `Water_level_WP1.csv`: Channel water level (m, elevation). 2014-12-01 00:00 to 2015-01-31 23:50, 10 min. 
- `Water_level_24-08-2013.csv`: UTM N, E and water-level elevation (m) on one day. 2013-08-24 to 2013-08-24, one survey. 
- `Precipitation_Selat_Baru.csv`: Daily precipitation (mm). 2014-12-01 to 2015-01-31, 1 d. 
- `RTK_GNSS_*.csv (7), elevations of DTM.csv, peat core analysis_P1-P4.csv`: Ground elevations 2013-2016, DTM profile, peat properties. 
- `Perapat Tunggal_2018/2021_10minutes_csv.csv, Selatbaru_2018/2021_10minutes_csv.csv, Meteorological observations.csv`: 10-min wind; monthly max wind and rainfall 2018-2021. 2018-01 to 2021-12, . 
- `Cumulative coastline retreat..., Landsat/Sentinel NDVI tables, vegetation-cover series`: Remote-sensing tables. 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A34`.
