# A2: Mendaram water table + chamber CO2, Brunei

**Status:** Downloaded

**Data source:** [Zenodo 3245335](https://doi.org/10.5281/zenodo.3245335); licence CC-BY-4.0

**Paper:** Hoyt et al. 2019, Global Change Biology 25, https://doi.org/10.1111/gcb.14702 (Preprint on HAL (hal-02333558) and DSpace@MIT; both block scripts, open in a browser)

> Data availability: Not read (full text blocked). The Zenodo record is titled 'Supplement to: Hoyt et al. (2019)'.

**How the paper used the data:** Automated chambers (root-cut to 30 cm, in sun and shade) measured peat CO2 efflux hourly. Mean daily heterotrophic respiration (Rhet) was linearly related to water-table depth and small and constant under flooding. That Rhet-WTD relationship, plus a DOC-WTD relationship, was applied to a 3-year, 20-min water-table record (Feb 2012 - Feb 2015) to upscale annual carbon export (Fig. 3). Period 1 (Jul-Nov 2012) data are in Fig. 2/S1, Period 2 (Nov 2013 - Mar 2014) in Figs. 4, 5, S2.

- Site coordinates are not given in the files; the chambers are on the same Mendaram dome as A1 (about 4.37 N, 114.35 E).
- Zip archives are committed as downloaded; unzip them locally (the cloud copy was unpacked only for inspection).

## Files in `data/`

- `Data_Period_1_CO2Flux_WT_AirTemp_Rainfall.zip` (WaterTable_Period_1a.csv): WaterTable_Period_1a.csv: WT at chamber-measurement times. 2012-07-13 16:37 to 2012-08-05 14:37, 1 h. WTD: Yes: m; negative = below peat surface
- `Data_Period_1_CO2Flux_WT_AirTemp_Rainfall.zip` (WaterTable_Period_1b.csv): WaterTable_Period_1b.csv. 2012-08-07 10:00 to 2012-11-23 23:40, 20 min. WTD: Yes: m; negative = below peat surface
- `Data_Period_1_CO2Flux_WT_AirTemp_Rainfall.zip` (CO2flux_Chamber*.csv (6 files)): Hourly CO2 flux (umol m-2 s-1); 1a: chambers 1, 4 (13 Jul - 5 Aug 2012); 1b: chambers 1-4 (7 Aug - 23 Nov 2012; ch. 2 ends 8 Oct). 2012-07-13 to 2012-11-23, 1 h. 
- `Data_Period_1_CO2Flux_WT_AirTemp_Rainfall.zip` (DailyMeans_Period_1b.csv): Daily means of CO2 flux, air T and WT (day of year 219-327, 2012). 2012-08-06 to 2012-11-22, 1 d. WTD: Yes (daily mean)
- `Data_Period_1_CO2Flux_WT_AirTemp_Rainfall.zip` (AirTemp_Period_1extended.csv, RainDepth_Period_1.csv): Air temperature (10 min, 6 Jun 2012 - 21 Feb 2013); rain depth (10 min, 13 Jul - 23 Nov 2012). 2012-06-06 to 2013-02-21, 10 min. 
- `Data_Period_2_PeatTemp_AirTemp_WT.zip` (WaterTable_Period_2.csv): WaterTable_Period_2.csv. 2013-11-23 15:20 to 2014-03-23 14:00, 20 min. WTD: Yes: m; negative = below peat surface
- `Data_Period_2_PeatTemp_AirTemp_WT.zip` (AirTemp_Period_2.csv, PeatTemperature_Tidbits_Period_2.csv): Air temperature (20 min); peat temperature at surface/10/25 cm, sun and shade (10 min). 2013-11-24 to 2014-03-23, 10-20 min. 
- `Flux_Upscaling.zip` (UpscalingTimeseries_3yrs.csv): UpscalingTimeseries_3yrs.csv: WT + modelled Rhet (hollows, dome) + DOC export. 2012-02-06 12:00 to 2015-02-06 11:40, 20 min. WTD: Yes: m; negative = below peat surface
- `Flux_Upscaling.zip` (Rhet_WT_Upscaling_Relationship.csv, DOC_WT_Upscaling_Relationship.csv): Rhet-WT and DOC-WT relationships used for upscaling (WT -0.4 to 0.2 m). 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A2`.
