# Field Calibrated Multisource Remote Sensing and Machine Learning for Peatland Groundwater Level Mapping in South Sumatra, Indonesia: 1-km composites, uncertainty layers, model coefficients, and processing scripts

Version 1.0.0

This deposit accompanies the article "Field Calibrated Multisource Remote Sensing and Machine Learning for Peatland Groundwater Level Mapping in South Sumatra, Indonesia" (Irfan, Iskandar, Nurkhakim, Ariani, Kurniawati, and Saputra; submitted to *Science of the Total Environment*; article DOI: 10.5281/zenodo.23008827).

It contains the modelled 1-km groundwater level (GWL) rasters for two representative windows in 2019 (wet: 1 to 13 April; dry: 13 to 25 November), the intermediate scene and tile rasters, the layers that quantify composite variability and bootstrap uncertainty, quality-assurance tables, the coefficients of the fitted Ridge regression, and the Google Earth Engine (GEE) scripts that apply the model. It does not contain the field observations (Section 8).

## 1\. Files in this record

Zenodo keeps at most 100 files per record and does not keep folders, so the primary products are individual files and the bulk material is packed in ZIP archives (the folder names inside the archives are those of the authors' analysis).

|File|Content|
|-|-|
|`README.md`|This file|
|`ridge\\\_model\\\_coefficients.csv`|Coefficients of the frozen Ridge model (Section 5)|
|`A09\\\_FINAL\\\_\\\*\\\_1KM\\\_KHG\\\_SUMSEL.tif` (4 files)|Primary product (Section 2)|
|`A09\\\_DRYING\\\_BOOTSTRAP\\\_\\\*.tif`, `A09\\\_PROBABILITY\\\_DRYING\\\_GT0\\\_1KM.tif`, `A09\\\_UNCERTAINTY\\\_\\\*.tif` (11 files)|Uncertainty layers (Section 4)|
|`UNCERTAINTY\\\_SUMMARY.csv`, `MODEL\\\_GENERALIZATION\\\_REFERENCE.csv`, `V208U\\\_RUN\\\_SUMMARY.txt`|Uncertainty tables and run summary|
|`01\\\_SCENE\\\_1KM.zip`|46 scene rasters at 1 km, in `WET/` and `DRY/` subfolders by tile|
|`02\\\_TILE\\\_MEDIAN.zip`|10 tile-median rasters at 1 km|
|`04\\\_QA.zip`|Grid metadata and quality-assurance tables|
|`05\\\_TABLES.zip`|Per-scene and per-tile statistics|
|`scripts.zip`|GEE scripts (Section 9)|

## 2\. Primary product

|File|Content|Unit|
|-|-|-|
|`A09\\\_FINAL\\\_GWL\\\_WET\\\_1KM\\\_KHG\\\_SUMSEL.tif`|Modelled GWL, wet window (1 to 13 April 2019)|m|
|`A09\\\_FINAL\\\_GWL\\\_DRY\\\_1KM\\\_KHG\\\_SUMSEL.tif`|Modelled GWL, dry window (13 to 25 November 2019)|m|
|`A09\\\_FINAL\\\_DRYING\\\_MAGNITUDE\\\_WET\\\_MINUS\\\_DRY\\\_1KM\\\_KHG\\\_SUMSEL.tif`|Decline D = GWL\_wet minus GWL\_dry; positive D means a deeper water table in the dry window|m|
|`A09\\\_FINAL\\\_GWL\\\_DRY\\\_MINUS\\\_WET\\\_1KM\\\_KHG\\\_SUMSEL.tif`|GWL\_dry minus GWL\_wet (equal to minus D; provided for convenience)|m|

GWL is expressed in metres relative to the peat surface: negative values mean the water table is below the surface, positive values mean water above the surface.

Grid (identical for all rasters in this record): EPSG:32748 (WGS 84 / UTM zone 48S); 1,000 m; 365 columns by 279 rows; bounds 257,000 to 622,000 m easting and 9,539,000 to 9,818,000 m northing; float32; NoData = -9999; band description `gwl\\\_pred\\\_m` (or the variable name for uncertainty layers). The analysis domain is the Peat Hydrological Units (KHG) of South Sumatra Province, 20,921 cells; cells outside the mask are NoData. Details: `COMMON\\\_GRID\\\_METADATA.json` in `04\\\_QA.zip`.

Summary statistics of the primary product (from `FINAL\\\_RASTER\\\_QA.csv` in `04\\\_QA.zip`; coverage of the domain is 100%):

|Layer|Median (m)|1st percentile (m)|99th percentile (m)|
|-|-|-|-|
|GWL wet|-0.089|-1.494|0.358|
|GWL dry|-0.826|-2.492|-0.312|
|Drying magnitude D|0.725|0.450|1.107|

D is positive in all 20,921 cells.

## 3\. How the composites were made

1. GEE applied the frozen Ridge model to each Sentinel-1A scene at 50-m support and exported one raster per scene and tile (`04\\\_spatial\\\_deployment/` in `scripts.zip`; 23 scenes per window across five tiles: T02\_SC, T03\_SE, T04\_NW, T05\_NC, T06\_NE).
2. Offline, each 50-m scene raster was aggregated to 1 km (`01\\\_SCENE\\\_1KM.zip`), the scenes of each tile and window were combined by median (`02\\\_TILE\\\_MEDIAN.zip`), and the tile medians were mosaicked and clipped to the KHG mask (the four primary files).

Scene file names follow `A09\\\_V206B\\\_<batch>\\\_<WET|DRY>\\\_<tile>\\\_<scene>\\\_O<relative orbit>\\\_<UTC acquisition time>\\\_PRIMARY\\\_1KM.tif`, for example `...\\\_B07\\\_DRY\\\_T02SC\\\_S01\\\_O098\\\_20191115T111607\\\_...` is scene 1 of batch B07, relative orbit 98, acquired on 2019-11-15 at 11:16:07 UTC. Tile-median files are named `A09\\\_V207\\\_<WET|DRY>\\\_<tile>\\\_MEDIAN\\\_1KM.tif`. The scene inventory and the tile counts are in `V206B\\\_SCENE\\\_INVENTORY.csv` and `V206B\\\_TILE\\\_COUNT\\\_AUDIT.csv` in `04\\\_QA.zip` (all tiles: expected scenes found).

The 50-m scene rasters are model-support inference only. Because GPM and SMAP predictors are coarse, the 1-km rasters are the primary scientific product, and the 50-m rasters should not be read as measured groundwater level at 50 m. The 50-m rasters are not part of this deposit.

## 4\. Uncertainty layers

|File|Content|Unit|
|-|-|-|
|`A09\\\_UNCERTAINTY\\\_WET\\\_MAD\\\_SIGMA\\\_1KM.tif`, `A09\\\_UNCERTAINTY\\\_DRY\\\_MAD\\\_SIGMA\\\_1KM.tif`|Robust spread of scene-level predictions in a cell: 1.4826 times the median absolute deviation|m|
|`A09\\\_UNCERTAINTY\\\_WET\\\_IQR\\\_1KM.tif`, `A09\\\_UNCERTAINTY\\\_DRY\\\_IQR\\\_1KM.tif`|Interquartile range of scene-level predictions|m|
|`A09\\\_UNCERTAINTY\\\_WET\\\_N\\\_SCENES\\\_1KM.tif`, `A09\\\_UNCERTAINTY\\\_DRY\\\_N\\\_SCENES\\\_1KM.tif`|Number of contributing scenes per cell (0 to 8; 0 where no scene contributes)|count|
|`A09\\\_DRYING\\\_BOOTSTRAP\\\_MEDIAN\\\_1KM.tif`, `...\\\_P05\\\_1KM.tif`, `...\\\_P95\\\_1KM.tif`|Median, 5th percentile, and 95th percentile of D from scene bootstrap|m|
|`A09\\\_DRYING\\\_BOOTSTRAP\\\_PI90\\\_WIDTH\\\_1KM.tif`|Width of the 90% bootstrap interval of D (P95 minus P05)|m|
|`A09\\\_PROBABILITY\\\_DRYING\\\_GT0\\\_1KM.tif`|Bootstrap probability that D is greater than 0|0 to 1|
|`UNCERTAINTY\\\_SUMMARY.csv`|Distribution statistics of each layer||
|`MODEL\\\_GENERALIZATION\\\_REFERENCE.csv`|Cross-validated error of the model, for context||
|`V208U\\\_RUN\\\_SUMMARY.txt`|Run summary||

Bootstrap: 500 resamples of the scenes within each window, with replacement (seed 20260909), computed for 20,890 of the 20,921 cells (99.852%). Median robust spread is 0.118 m (wet) and 0.124 m (dry); the median 90% interval width of D is 0.334 m; 99.895% of eligible cells have P(D>0) of at least 0.95.

These layers describe how much the result depends on the scenes that enter each composite. They are not prediction intervals for absolute GWL, and model generalisation error is reported separately (`MODEL\\\_GENERALIZATION\\\_REFERENCE.csv`). The two must not be combined into a pixelwise interval without further assumptions.

## 5\. Model coefficients: `ridge\\\_model\\\_coefficients.csv`

Ridge regression with alpha = 10, fitted at 50-m Sentinel-1 support. The file has 49 rows: the intercept and 48 model terms (index 0 to 47): 34 numeric predictors, 8 missing-value indicators, and 6 one-hot terms (Sentinel-1 pass direction: ascending, descending; relative orbit: 18, 98, 120, 171). Columns: `index`, `term`, `term\\\_type`, `coefficient`, `standardisation\\\_mean`, `standardisation\\\_scale`, `median\\\_imputation\\\_value`.

To reproduce a prediction: replace a missing numeric predictor by its `median\\\_imputation\\\_value` and set its missing indicator to 1; standardise each numeric predictor and indicator as (x minus `standardisation\\\_mean`) divided by `standardisation\\\_scale`; leave the one-hot terms unstandardised; predict GWL as the intercept plus the sum of coefficient times term. Predictor groups: antecedent rainfall from calibrated GPM IMERG V07 (accumulations over 1, 3, 7, 14, and 30 days; wet days; dry streak), SMAP L4 V8 hydrological state, seasonal terms (sine and cosine of day of year), and Sentinel-1A backscatter with past-only same-orbit change features. Units: rainfall in mm, backscatter in dB, SMAP surface temperature in K.

## 6\. Provenance and validation

The model was fitted to 1,133 GWL observations from eight core stations (2019 to 2023) and frozen before temporal testing and deployment. Cross-validated performance (see `MODEL\\\_GENERALIZATION\\\_REFERENCE.csv`): nested leave-one-station-out pooled RMSE 0.317 m, MAE 0.253 m, R2 0.461, bias -0.022 m (macro RMSE 0.296 m, macro R2 0.196); held-out-year R2 0.613; forward-chain R2 0.400. R2 was negative in 2020. Input products from Google Earth Engine: GPM IMERG V07 (`NASA/GPM\\\_L3/IMERG\\\_V07`), SMAP L4 V8 (`NASA/SMAP/SPL4SMGP/008`), and Sentinel-1 GRD (`COPERNICUS/S1\\\_GRD`).

## 7\. Intended use and limitations

* The rasters are regional hydrological indicators on a 1-km grid, not measurements at individual wells; they are unsuitable for parcel-level decisions.
* Transfer error is substantial and uneven among stations and years (Section 6). The 2019 layers cover two short windows and are not seasonal climatologies or a trend.
* The relationships were calibrated on eight stations in South Sumatra; use elsewhere needs independent recalibration and validation.
* The product estimates GWL only, not fire probability or carbon loss.

## 8\. Data and code not included

* The field GWL and rain-gauge observations belong to the BRGM/SIPALAGA monitoring network and are subject to the data provider's access and redistribution conditions; request them from the provider.
* The GEE scripts refer to private assets of the authors' GEE project (AOI boundary, station locations, export folder); the satellite inputs are public.
* \[Offline Python code for aggregation, median compositing, mosaicking, masking, and bootstrap: state here whether it is included in `scripts.zip` or available on request.]

## 9\. Scripts: `scripts.zip`

* `01\\\_predictor\\\_extraction/`: Sentinel-1 backscatter, SMAP anchoring, GPM IMERG extraction and calibrated rainfall features at the field stations.
* `02\\\_smap\\\_weekly\\\_composites/`: SMAP L4 weekly composite protocol and its QA versions.
* `03\\\_timestamp\\\_audit/`: field-to-satellite timestamp audit.
* `04\\\_spatial\\\_deployment/`: spatial application of the frozen model (development and parity tests; production manifest; ten production batches, five tiles by two windows).

Earlier versions are kept on purpose to document the QA history. The development repository is https://github.com/adsgeophysics/Penelitian\_Profesi.

## 10\. How to cite

Irfan, M., Iskandar, I., Nurkhakim, M.Y., Ariani, M., Kurniawati, N., Saputra, A.D., 2026. Peatland groundwater level composites, uncertainty layers, and Ridge model coefficients for South Sumatra, Indonesia \[dataset]. Zenodo. https://doi.org/\[Zenodo DOI]

Please also cite the accompanying article once published.

## 11\. Licence

Data, tables, and coefficient file: CC BY 4.0. Scripts: MIT.

## 12\. Funding and acknowledgements

This work was supported by Universitas Sriwijaya through the Professional Research Scheme (Penelitian Skema Unggulan Profesi) under the 2026 university budget \[Rector's Decree No. 0010/UN9.R/SK.R3.LPPM/2026, dated 12 June 2026; research contract No. 0207.45/UN9.LPPM/SB3.ADM/2026]. The authors acknowledge BRGM/SIPALAGA for maintaining peatland hydrometeorological monitoring in South Sumatra and the satellite-data providers supporting this study.

## 13\. Contact

Muhammad Irfan (corresponding author), Universitas Sriwijaya, muhammad\_irfan@unsri.ac.id

## 14\. Changelog

* 1.0.0: first release.

