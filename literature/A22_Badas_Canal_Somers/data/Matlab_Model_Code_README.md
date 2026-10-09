# Badas_Methane
Mathematical model (in Matlab) that simulates methane and carbon dioxide dynamics in a tropical peatland drainage canal. These codes are shared as part of the submission process of an academic journal article. Accompanying field data for these codes is available from Hydroshare: https://www.hydroshare.org/resource/3953b24e0238467980a226c72cfc360e/![image](https://user-images.githubusercontent.com/25670782/185951389-1cd57b28-ca48-4a7f-91d5-79bf5b4fb84e.png)

The inital commit contains two main matlab scripts and a number of supporting functions:

<b> Along_canal_nlimmultifit_DOM_scaled_Jan_Aug.m </b> 
This file fits the mathematical model of methane and carbon dioxide concentrations and stable carbon isotopes to field data.

<b> Error_Bands_Budget_Jan_Aug_new.m </b>  
This script takes the best fit simulation and runs a monte-carlo error propagation routine and then makes budget plots that are in the manuscript. 

Supporting functions:

<b> GW_exp_fit.m </b>
This is a function called by the above codes that fits the depth of groundwater contribution to the canal based on field data.

<b> "del and Conc" functions </b>
These eight functions contain our mathematical models for concentration and delta 13 C.

<b> nlinmultifit.m </b>
This is the fitting function used for this project, written by matlab contributor, Chen Avinadav which I can no longer find online. It is a wrapper for nlinfit which alows non-linear regression to multiple datasets.
