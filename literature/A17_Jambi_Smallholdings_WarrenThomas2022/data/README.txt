This Readme.txt file was generated on 2022-02-11 by Eleanor Warren-Thomas

GENERAL INFORMATION

1. Title of Dataset: No evidence for trade-offs between bird diversity, yield and water table depth on oil palm smallholdings: implications for tropical peatland landscape restoration.

2. Author Information
	Principal Investigator Contact Information
	Name: Eleanor Warren-Thomas
	Institution: Bangor University (formerly, University of York), UK
	Email: em.warren.thomas@gmail.com

3. Date of data collection (single date, range, approximate date): August 2018 - July 2019

4. Geographic location of data collection: Jambi province, Sumatra, Indonesia

5. Information about funding sources that supported the collection of the data: Research funding was provided by NERC/The Newton Fund, grant number NE/P014658/1. EWT was also supported by NERC-IIASA Fellowship NE/T009306/1. JL was supported by NERC Knowledge Exchange Fellowship NE/M006840/1-2. JAH was supported by NERC Innovation grant NE/R009597/1. 


SHARING/ACCESS INFORMATION

1. Links to publications that cite or use the data: https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2664.14135   

2. Recommended citation for this dataset: Warren-Thomas, E. et al. (2022), ‘No evidence for trade-offs between bird diversity, yield and water table depth on oil palm smallholdings: implications for tropical peatland landscape restoration’, Dryad, Dataset, https://doi.org/10.5061/dryad.rr4xgxd9v

DATA & FILE OVERVIEW

1. File List: 

	Rainfall.csv
		Rainfall recorded at each site (manual measures) in mm. Site names are decoded in Oil_palm_yields_predictors.csv

	Water_tables_loggers.csv
		Automated water table depth measurements taken at each site (raw data barometrically compensated using manual dip measures at time of installation for each sensor). Sudden drops in pressure on the sensors, sometimes ere accompanied by sudden changes in temperature, indicate removal of the sensor from the dipwell, and possible re-installation in a slightly different place e.g. due to resting on silt. 

	Oil_palm_yields_predictors.csv
		Oil palm yield, vegetation structure, water tables and environmental predictors (used in analysis of oil palm yields, vegetation and birds on oil palm farms). 
		**Contains mapping between Plot ID code and habitat, site and location.**

	Oil_palm_yields_predictors_description.csv
		Descriptors for the variables contained in Oil_palm_yields_predictors.csv

	Bird_species_list_within_50m.csv
		List of bird species recorded within 50m of all sampling plots. Habitat dependency columns populated following methods detailed in manuscript and supplementary material. **Contains mapping between species codes and full species names.**

	Bird_abundance_matrix_within_50m.csv
		Bird species abundance recorded during each repeat sample taken at each sampling plot, within 50m. Plot ID code is linked to habitat, site and location based on data in Oil_palm_yields_predictors.csv. Species codes are linked to full species names in Bird_species_list_within_50m.csv

	Bird_max_abundance_matrix_within_50m.csv
		Maximum bird species abundance recorded during any single sample taken at each sampling plot, within 50m. Plot ID code is linked to habitat, site and location based on data in Oil_palm_yields_predictors.csv. Species codes are linked to full species names in Bird_species_list_within_50m.csv

	Bird_max_diet_within_50m.csv
		Maximum abundance of birds within each diet group recorded during any single sample taken at each sampling plot, within 50m. Plot ID code is linked to habitat, site and location based on data in Oil_palm_yields_predictors.csv. Species codes are linked to full species names in Bird_species_list_within_50m.csv

	Bird_CWM_within_50m.csv
		Community-weighted mass of birds per plot (maximum abundance of each species found per plot * mass) following methods detailed in manuscript and supplementary material. Plot ID code is linked to habitat, site and location based on data in Oil_palm_yields_predictors.csv. Species codes are linked to full species names in Bird_species_list_within_50m.csv

2. Relationship between files, if important: 

Bird_species_list_within_50m.csv - Contains mapping between species codes and full species names, as used in Bird_abundance_matrix_within_50m.csv, Bird_max_abundance_matrix_within_50m.csv and Bird_max_diet_within_50m.csv

Oil_palm_yields_predictors.csv - Contains mapping between Plot ID code and habitat, site and location, as used in Bird_abundance_matrix_within_50m.csv, Bird_max_abundance_matrix_within_50m.csv and Bird_max_diet_within_50m.csv

3. Additional related data collected that was not included in the current data package: latitude/longitude of all farms, not included to retain privacy of study participant data

4. Are there multiple versions of the dataset? No
	


METHODOLOGICAL INFORMATION

1. Description of methods used for collection/generation of data: 

Very detailed data collection methodology is provided in this publication:  https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2664.14135 - please email the lead author using the details above, if you are unable to access the paper. 

2. Methods for processing the data: 

 - species names in bird surveys were standardised, and fly-through or fly-over records were removed
 - records outside of a 50m radius from the sampling points were removed
 - the method for calculation of abundance and community-weighted mass are given in the publication  https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2664.14135   
 - manual water table and vegetation data had no post-processing beyond calculation of means and SD for measures repeated within plots (these are clearly indicated by _Mean or _SD variable names), and calculation of the inverse value of understorey density
 - water table logger data was barometrically compensated through the use of an above-ground atmospheric pressure sensor (subtraction of the air pressure from the water pressure records) following the protocol of the LevelScout sensor guidelines

3. Instrument- or software-specific information needed to interpret the data: 

All data is provided as csv files - no specific software or instrument needed

4. People involved with sample collection, processing, analysis and/or submission: 

Eleanor Warren-Thomas1,2,3, Fahmuddin Agus4, Panji Gusti Akbar5, Merry Crowson6, Keith C. Hamer7, Bambang Hariyadi8, Jenny A. Hodgson9, Winda D. Kartika8, Mailys Lopes6, Jennifer M. Lucey10, Dedy Mustaqim8, Nathalie Pettorelli6, Asmadi Saad11, Widia Sari8, Gita Sukma8, Lindsay C. Stringer1,12,13, Caroline Ward1,13, Jane K. Hill1 

1 Leverhulme Centre for Anthropocene Biodiversity, Department of Biology, University of York, York, YO10 5DD, UK
2 School of Natural Sciences, Bangor University, Bangor, LL57 2DG, UK 
3 Biodiversity and Natural Resources Program, International Institute for Applied Systems Analysis (IIASA), Laxenburg, Austria
4 Indonesian Center for Agricultural Land Resources Research and Development, Bogor 16124, Indonesia
5 Birdpacker, Batu, East Java, Indonesia 65331
6 Institute of Zoology, Zoological Society of London, London, NW1 4RY, UK 
7 School of Biology, Faculty of Biological Sciences, University of Leeds, Leeds, LS2 9JT, UK
8 Biology Education Program, Faculty of Education and Teacher Training, Jambi University, Jambi, Indonesia 
9 Department of Evolution, Ecology and Behaviour, University of Liverpool, Liverpool, L69 7ZB, UK
10 Department of Zoology, University of Oxford, Oxford, OX1 3SZ, UK
11 Faculty of Agriculture, Jambi University, Jambi, Indonesia
12 Department of Environment and Geography, University of York, York, YO10 5DD, UK
13 School of Earth and Environment, University of Leeds, Leeds, LS2 9JT, UK

DATA-SPECIFIC INFORMATION FOR: Bird_abundance_matrix_within_50m.csv

1. Number of variables: 4

2. Number of cases/rows: 1800

3. Variable List: 

Plot_ID	- location of survey
Repeat - repeat visit number (1-4)
Species_code - bird species identification code
Abundance - number of birds recorded

4. Missing data codes: 
None used

5. Specialized formats or other abbreviations used: 
Plot_ID and Species_code are translated to habitat/location and full species name in Oil_palm_yields_predictors.csv and Bird_species_list_within_50m.csv respectively

DATA-SPECIFIC INFORMATION FOR: Bird_CWM_within_50m.csv

1. Number of variables: 2

2. Number of cases/rows: 62

3. Variable List: 

Plot_ID	- location of survey
Total_weighted_mass - abundance-weighted mass of all bird species per plot (maximum abundance of each bird species recorded during any one repeat visit to each plot, multiplied by species mass in Handbook of Birds of the World (del Hoyo, J. et al. (2017) Handbook of the Birds of the World Alive. Lynx Edicions, Barcelona. Available at: http://www.hbw.com (Accessed: 17 March 2017), summed over all species. 

4. Missing data codes: 
None used

5. Specialized formats or other abbreviations used: 
Plot_ID is translated to habitat/location in Oil_palm_yields_predictors.csv

DATA-SPECIFIC INFORMATION FOR: Bird_max_abundance_matrix_within_50m.csv

1. Number of variables: 3

2. Number of cases/rows: 962

3. Variable List: 

Plot_ID	- location of survey
Species_code - bird species identification code
Max_abun - maximum number of birds recorded on any single repeat visit to the plot

4. Missing data codes: 
None used

5. Specialized formats or other abbreviations used: 
Plot_ID and Species_code are translated to habitat/location and full species name in Oil_palm_yields_predictors.csv and Bird_species_list_within_50m.csv respectively

DATA-SPECIFIC INFORMATION FOR: Bird_max_diet_within_50m.csv

1. Number of variables: 3

2. Number of cases/rows: 2542

3. Variable List: 

Plot_ID	- location of survey
Diet - one of five diet groups based on the Elton Traits database variable “Diet-5Cat” according to their predominant diets (Wilman, H. et al. (2014) ‘EltonTraits 1.0 : Species-level foraging attributes of the world’s birds and mammals’, Ecology, 95(7), p. 2027.)
Max_abun - sum of maximum number of birds per species recorded on any single repeat visit to the plot in each diet cateogry

4. Missing data codes: 
None used

5. Specialized formats or other abbreviations used: 
Plot_ID translated to habitat/location and full species name in Oil_palm_yields_predictors.csv and Bird_species_list_within_50m.csv respectively

DATA-SPECIFIC INFORMATION FOR: Bird_species_list_within_50m.csv

1. Number of variables: 7

2. Number of cases/rows: 125

3. Variable List: 

Species	- English species names of bird
Scientific_name	- Latin species name of bird
Species_code - species code used in all other datasets
IUCN - IUCN threat status of each species at time of study
Dependence_EWT	- habitat dependence of each species (note below)
Dependence_strict - yes/no if bird species is strictly forest dependent	
Range - range size of species

Note: Habitat dependence classification based on IUCN species accounts and the Handbook of Birds of the World (del Hoyo et al., 2017; IUCN, 2019). Classed as follows: “Forest” if thought to be found only in primary forest, secondary forest or disturbed forest; “High_tree” if also found in plantations adjacent to forest, but does not persist in plantations; “Generalist” if found in both forest and non-forest habitats; “Open” if found in non-forest habitats (grassland, paddy, urban, etc).

4. Missing data codes: 
None used

5. Specialized formats or other abbreviations used: 
IUCN threat status uses the standard abbreviations from the IUCN Red list.

DATA-SPECIFIC INFORMATION FOR: Oil_palm_yields_predictors.csv

1. Number of variables: 82

2. Number of cases/rows: 34

3. Variable List: 

A full list of variable definitions is provided in a separate CSV file Oil_palm_yields_predictors_description.csv

4. Missing data codes: 
"NA"

5. Specialized formats or other abbreviations used: 
None used

DATA-SPECIFIC INFORMATION FOR: Rainfall.csv

1. Number of variables: 3

2. Number of cases/rows: 705

3. Variable List: 

Site - name of site (translation of site names is in Oil_palm_yields_predictors.csv)
Date - DD-MM-YYYY
Rainfall_mm - millimetres of rainfall recorded

4. Missing data codes: 
None used

5. Specialized formats or other abbreviations used: 
None used

DATA-SPECIFIC INFORMATION FOR: Water_tables_loggers.csv

1. Number of variables: 7

2. Number of cases/rows: 120782

3. Variable List: 

Recording_no - index
Date_Time - YYYY-MM-DDTHH:MM:SSZ
Temperature	- recorded water temperature in degrees centrigradee
Pressure_cm_H2O	- water pressure of logger in cmH2O
Depth_to_water_cm_H2O - calculated distance between ground and water surface based on water pressure on logger, calibrated with atmospheric pressure nearby, in centimetres
Site - site location name
Depth_to_water_cm_H2O_neg - inverse of depth to water i.e. negative values indicate water table is below ground, positive values indicate it is above ground

4. Missing data codes: 
None used

5. Specialized formats or other abbreviations used: 
None used