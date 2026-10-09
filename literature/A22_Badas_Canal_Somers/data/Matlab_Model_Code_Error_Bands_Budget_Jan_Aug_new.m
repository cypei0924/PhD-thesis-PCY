%% Error_Bands_Budget_Jan_Aug
% Lauren Somers
% Mar 11, 2021
%
% This code takes the fitted parameters and thestandard deviations of
% parameters and performs a monte carlo simulation to calculate error bands
% and the budget components for both Jan and Aug datasets at Badas
%
% Before running this script run:
% Along_Canal_nlinmultifit_DOM_scaled_Jan_Aug.m to get the Sigma
% (Covariance) matrix

%% Generate realizations of the model parameters

n = 1000 + 2; % number of runs in the monte carlo simulation

% params should be the best  fit parameters from the 8 parameter fit (where D and k_DOC are allowed to be different in Jan and Aug):
p = (mvnrnd(params,Sigma, n))./scaling;

% Now make the first line the best fit scenario:
p(1,:) = params_US;

% And make the last line the best fit scenario (so it will be easy to plot
% stuff later)
p(1002,:) = params_US;

% Values of x at which to solve the ODEs:
solve_at = [0.01 1 2 3 4 5 10 20 30 40 50 100 200 300 457 500 600 700 800 900 1000 1500 2000 2500 3000 3500 4000 4600 4800 5070];
% Adjust the groundwater concentration:
q = qgw;

%% Create the variables that will be filled by the loop

% Jan:
C_Conc_pred_Jan = zeros (n,length(solve_at));
C_del_pred_Jan = zeros (n,length(solve_at));
M_Conc_pred_Jan = zeros (n,length(solve_at));
M_del_pred_Jan = zeros (n,length(solve_at));
budget_C_Jan = zeros (n,5);
budget_M_Jan = zeros (n,4);

% Aug:
C_Conc_pred_Aug = zeros (n,length(solve_at));
C_del_pred_Aug = zeros (n,length(solve_at));
M_Conc_pred_Aug = zeros (n,length(solve_at));
M_del_pred_Aug = zeros (n,length(solve_at));
budget_C_Aug = zeros (n,5);
budget_M_Aug = zeros (n,4);

%% THE LOOP: run the model using the inputs p

for i=1:n

% %%%%%%%%% January %%%%%%%%%%%%
deep_coef = p(i,1);  % Proportion of incoming groundwater that comes from below the canal
B = p(i,2); % Isotopic fractionation: methane oxidation reaction rate ratio: (13C rate)/(12C rate) Alison used alpha = 1.01 to 1.02 B=1/alpha
V_mic_coef = p(i,3); % coefficient to calculate V_mic based on V_atm.
V_atm_init = p(i,4);  % initial gas exchange velocity for CH4 METHANE!
V_atm_slope = p(i,5); % (1.2e-05)/500%1.1294e-05/1000; % Slope of V_atm * careful not to make it get too large or go negative
k_DOC = p(i,6);

qgw = q(1);

% Calculate groundwater concentrations

[M_12gw, M_13gw, C_12gw, C_13gw] = GW_exp_fit (PT1_30W_Jan, deep_coef);

% M_12gw = deep_coef *(deep_gw(3)) + (1 - deep_coef)*(shallow_gw(3,1));  
% M_13gw = deep_coef *(deep_gw(4)) + (1 - deep_coef)*(shallow_gw(4,1)); 
% C_12gw = deep_coef *(deep_gw(1)) + (1 - deep_coef)*(shallow_gw(1,1)); 
% C_13gw = deep_coef *(deep_gw(2)) + (1 - deep_coef)*(shallow_gw(2,1));

% Add the fraction of DOC that is 13DOC:
f=C_13DOC/(C_13DOC + C_12DOC); 

% %% Define and solve the differential equation system: 
% % dC_dx change inconcentration over change in distance is an array with
% % four functions linear increase in V_atm and Vmic k_DOC:  
% dC_dx = @ (x,Conc)    [1/(qgw*x) * (qgw * (M_12gw - Conc(1)) -     (V_mic_coef * (x*V_atm_slope + V_atm_init) * Conc(1) * w) - ((x*V_atm_slope + V_atm_init) *          (Conc(1)-M_12atm) * w));...
%                         1/(qgw*x) * (qgw * (M_13gw - Conc(2)) - (B * V_mic_coef * (x*V_atm_slope + V_atm_init) * Conc(2) * w) - ((x*V_atm_slope + V_atm_init) *          (Conc(2)-M_13atm) * w));...           
%                         1/(qgw*x) * (qgw * (C_12gw - Conc(3)) +      V_mic_coef * (x*V_atm_slope + V_atm_init) * Conc(1) * w -  ((x*V_atm_slope + V_atm_init) * 0.9667 * (Conc(3)-C_12atm) * w) + (x*V_atm_slope + V_atm_init) * k_DOC * (1-f));...
%                         1/(qgw*x) * (qgw * (C_13gw - Conc(4)) +  B * V_mic_coef * (x*V_atm_slope + V_atm_init) * Conc(2) * w -  ((x*V_atm_slope + V_atm_init) * 0.9667 * (Conc(4)-C_13atm) * w) + (x*V_atm_slope + V_atm_init) * k_DOC * f    )];                             
                    
dC_dx = @ (x,Conc)     [1/(qgw*x) * (qgw * (M_12gw - Conc(1)) -     (V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(1) * w) - ((x*qgw*1000*V_atm_slope + V_atm_init) *          (Conc(1)-M_12atm) * w));...
                        1/(qgw*x) * (qgw * (M_13gw - Conc(2)) - (B * V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(2) * w) - ((x*qgw*1000*V_atm_slope + V_atm_init) *          (Conc(2)-M_13atm) * w));...           
                        1/(qgw*x) * (qgw * (C_12gw - Conc(3)) +      V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(1) * w -  ((x*qgw*1000*V_atm_slope + V_atm_init) * 0.9667 * (Conc(3)-C_12atm) * w) + (x*qgw*1000*V_atm_slope + V_atm_init) * k_DOC * (1-f));...
                        1/(qgw*x) * (qgw * (C_13gw - Conc(4)) +  B * V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(2) * w -  ((x*qgw*1000*V_atm_slope + V_atm_init) * 0.9667 * (Conc(4)-C_13atm) * w) + (x*qgw*1000*V_atm_slope + V_atm_init) * k_DOC * f    )];                             

% Calculate the inital values
tp = qgw*M_12gw+V_atm_init*w*M_12atm;
bt = qgw+V_atm_init*V_mic_coef*w+V_atm_init*w;
M_12_init = tp/bt;

%Calculate initial values for M_13
tp = qgw*M_13gw+V_atm_init*w*M_13atm;
bt = qgw+V_atm_init*V_mic_coef*B*w+V_atm_init*w;
M_13_init = tp/bt;

%Calculate initial values for C_12
tp = (qgw * C_12gw) + (V_mic_coef * M_12_init * w * V_atm_init) + (0.9667*V_atm_init*C_12atm*w) + (k_DOC*V_atm_init*(1-f));
bt = qgw + 0.9667*V_atm_init*w;
C_12_init = tp/bt;

%Calculate initial values for C_13
tp = (qgw * C_13gw) + (V_mic_coef* B * M_13_init * w * V_atm_init) + (0.9667*V_atm_init*C_13atm*w) + (k_DOC*V_atm_init*f);
bt = qgw + 0.9667*V_atm_init*w;
C_13_init = tp/bt;

%Set initial values
y0 = [M_12_init; M_13_init; C_12_init; C_13_init];

% Solve the ODE:
%[x,y] = ode23(odefun,xspan,y0)
[x,Conc] = ode23(dC_dx,solve_at,y0);

% Parse the isotopolog concentrations
M_12 = Conc (:,1);
M_13 = Conc (:,2);
C_12 = Conc (:,3);
C_13 = Conc (:,4);

% Convert output to delta notation (Peedee Belemnite 13C/12C = 0.01118)
M_del_pred_Jan(i,:) = (((M_13./M_12)/0.01118)-1)*1000;
C_del_pred_Jan(i,:) = (((C_13./C_12)/0.01118)-1)*1000;
% Convert to total concentration
M_Conc_pred_Jan(i,:) = M_12 + M_13;
C_Conc_pred_Jan(i,:) = C_12 + C_13;

% Calculate the budget components
% Calculate fluxes:
advection_C = ones(length(x),1) * qgw * (C_12gw + C_13gw);
oxidation_C = (V_atm_slope .* x * qgw * 1000 + V_atm_init)'.* V_mic_coef .* (M_Conc_pred_Jan(i,:)) * w ;
degassing_C = 0.9667 .* (V_atm_slope .* x * qgw * 1000 + V_atm_init)' .* ((C_Conc_pred_Jan(i,:)) - (C_12atm + C_13atm)) .* w ;
DOC_C = k_DOC .* (V_atm_slope .* x * qgw * 1000 + V_atm_init);
advection_M = ones(length(x),1) * qgw * (M_12gw + M_13gw);
oxidation_M = (V_atm_slope .* x * qgw * 1000 + V_atm_init)' .* (V_mic_coef .* (M_Conc_pred_Jan(i,:)) .* w) ;
degassing_M = (V_atm_slope .* x * qgw * 1000 + V_atm_init)' .* ((M_Conc_pred_Jan(i,:)) - (M_12atm + M_13atm)) .* w ;

%Total up the fluxes to make gas budgets
advection_C_t = qgw * x(end) * (C_12gw + C_13gw); % CO2 coming into the canal in mmol/s  
fluvial_C = qgw * x(end) *(C_Conc_pred_Jan(i,end)); % CO2 leaving the canal with streamflow mmol/s 
oxidation_C_t = trapz(x,oxidation_C);
degassing_C_t = trapz(x,degassing_C);
DOC_C_t = trapz(x,DOC_C);

%CH4:
advection_M_t = qgw * x(end) * (M_12gw + M_13gw); % CH4 coming into the canal in mol/s  
fluvial_M = qgw * x(end) *(M_Conc_pred_Jan(i,end)); % CH4 leaving the canal with streamflow mol/s 
oxidation_M_t = trapz(x,oxidation_M); % CH4 leaving the canal from oxidation mol/s 
degassing_M_t = trapz(x,degassing_M); % CH4 leaving the canal from degassing mol/s 

% Record the CO2 budget [advection, DOC  oxidation degassing   fluvial]
budget_C_Jan (i,:) = [advection_C_t   DOC_C_t    oxidation_C_t       degassing_C_t   fluvial_C];
% Record the CH4 budget [advection   oxidation  degassing   fluvial]
budget_M_Jan (i,:) = [advection_M_t     oxidation_M_t   degassing_M_t   fluvial_M];


% %%%%%%%%% August %%%%%%%%%%%%

deep_coef = p(i,7);  % Proportion of incoming groundwater that comes from below the canal
B = p(i,2); % Isotopic fractionation: methane oxidation reaction rate ratio: (13C rate)/(12C rate) Alison used alpha = 1.01 to 1.02 B=1/alpha
V_mic_coef = p(i,3); % coefficient to calculate V_mic based on V_atm.
V_atm_init = p(i,4);  % initial gas exchange velocity for CH4 METHANE!
V_atm_slope = p(i,5); % (1.2e-05)/500%1.1294e-05/1000; % Slope of V_atm * careful not to make it get too large or go negative
k_DOC = p(i,8);

qgw = q(2);

PT1_30W = PT1_30W_Aug;

% Calculate groundwater concentrations

[M_12gw, M_13gw, C_12gw, C_13gw] = GW_exp_fit (PT1_30W_Aug, deep_coef);

% % Calculate groundwater concentrations
% M_12gw = deep_coef *(deep_gw(3)) + (1 - deep_coef)*(shallow_gw(3,2));  
% M_13gw = deep_coef *(deep_gw(4)) + (1 - deep_coef)*(shallow_gw(4,2)); 
% C_12gw = deep_coef *(deep_gw(1)) + (1 - deep_coef)*(shallow_gw(1,2)); 
% C_13gw = deep_coef *(deep_gw(2)) + (1 - deep_coef)*(shallow_gw(2,2));

% %% Define and solve the differential equation system: 
% % dC_dx change inconcentration over change in distance is an array with
% % four functions linear increase in V_atm and Vmic k_DOC:  
% dC_dx = @ (x,Conc)    [1/(qgw*x) * (qgw * (M_12gw - Conc(1)) -     (V_mic_coef * (x*V_atm_slope + V_atm_init) * Conc(1) * w) - ((x*V_atm_slope + V_atm_init) *          (Conc(1)-M_12atm) * w));...
%                         1/(qgw*x) * (qgw * (M_13gw - Conc(2)) - (B * V_mic_coef * (x*V_atm_slope + V_atm_init) * Conc(2) * w) - ((x*V_atm_slope + V_atm_init) *          (Conc(2)-M_13atm) * w));...           
%                         1/(qgw*x) * (qgw * (C_12gw - Conc(3)) +      V_mic_coef * (x*V_atm_slope + V_atm_init) * Conc(1) * w -  ((x*V_atm_slope + V_atm_init) * 0.9667 * (Conc(3)-C_12atm) * w) + (x*V_atm_slope + V_atm_init) * k_DOC * (1-f));...
%                         1/(qgw*x) * (qgw * (C_13gw - Conc(4)) +  B * V_mic_coef * (x*V_atm_slope + V_atm_init) * Conc(2) * w -  ((x*V_atm_slope + V_atm_init) * 0.9667 * (Conc(4)-C_13atm) * w) + (x*V_atm_slope + V_atm_init) * k_DOC * f    )];                             
                    
dC_dx = @ (x,Conc)     [1/(qgw*x) * (qgw * (M_12gw - Conc(1)) -     (V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(1) * w) - ((x*qgw*1000*V_atm_slope + V_atm_init) *          (Conc(1)-M_12atm) * w));...
                        1/(qgw*x) * (qgw * (M_13gw - Conc(2)) - (B * V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(2) * w) - ((x*qgw*1000*V_atm_slope + V_atm_init) *          (Conc(2)-M_13atm) * w));...           
                        1/(qgw*x) * (qgw * (C_12gw - Conc(3)) +      V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(1) * w -  ((x*qgw*1000*V_atm_slope + V_atm_init) * 0.9667 * (Conc(3)-C_12atm) * w) + (x*qgw*1000*V_atm_slope + V_atm_init) * k_DOC * (1-f));...
                        1/(qgw*x) * (qgw * (C_13gw - Conc(4)) +  B * V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(2) * w -  ((x*qgw*1000*V_atm_slope + V_atm_init) * 0.9667 * (Conc(4)-C_13atm) * w) + (x*qgw*1000*V_atm_slope + V_atm_init) * k_DOC * f    )];                             

% Calculate the inital values
tp = qgw*M_12gw+V_atm_init*w*M_12atm;
bt = qgw+V_atm_init*V_mic_coef*w+V_atm_init*w;
M_12_init = tp/bt;

%Calculate initial values for M_13
tp = qgw*M_13gw+V_atm_init*w*M_13atm;
bt = qgw+V_atm_init*V_mic_coef*B*w+V_atm_init*w;
M_13_init = tp/bt;

%Calculate initial values for C_12
tp = (qgw * C_12gw) + (V_mic_coef * M_12_init * w * V_atm_init) + (0.9667*V_atm_init*C_12atm*w) + (k_DOC*V_atm_init*(1-f));
bt = qgw + 0.9667*V_atm_init*w;
C_12_init = tp/bt;

%Calculate initial values for C_13
tp = (qgw * C_13gw) + (V_mic_coef* B * M_13_init * w * V_atm_init) + (0.9667*V_atm_init*C_13atm*w) + (k_DOC*V_atm_init*f);
bt = qgw + 0.9667*V_atm_init*w;
C_13_init = tp/bt;

%Set initial values
y0 = [M_12_init; M_13_init; C_12_init; C_13_init];

% Solve the ODE:
%[x,y] = ode23(odefun,xspan,y0)
[x,Conc] = ode23(dC_dx,solve_at,y0);

% Parse the isotopolog concentrations
M_12 = Conc (:,1);
M_13 = Conc (:,2);
C_12 = Conc (:,3);
C_13 = Conc (:,4);

% Convert output to delta notation (Peedee Belemnite 13C/12C = 0.01118)
M_del_pred_Aug(i,:) = (((M_13./M_12)/0.01118)-1)*1000;
C_del_pred_Aug(i,:) = (((C_13./C_12)/0.01118)-1)*1000;
% Convert to total concentration
M_Conc_pred_Aug(i,:) = M_12 + M_13;
C_Conc_pred_Aug(i,:) = C_12 + C_13;

% Calculate the budget components
% Calculate fluxes:
advection_C = ones(length(x),1) * qgw * (C_12gw + C_13gw);
oxidation_C = (V_atm_slope .* x * qgw * 1000 + V_atm_init)'.* V_mic_coef .* (M_Conc_pred_Aug(i,:)) * w ;
degassing_C = 0.9667 .* (V_atm_slope .* x * qgw * 1000 + V_atm_init)' .* ((C_Conc_pred_Aug(i,:)) - (C_12atm + C_13atm)) .* w ;
DOC_C = k_DOC .* (V_atm_slope .* x * qgw * 1000 + V_atm_init);
advection_M = ones(length(x),1) * qgw * (M_12gw + M_13gw);
oxidation_M = (V_atm_slope .* x * qgw * 1000 + V_atm_init)' .* (V_mic_coef .* (M_Conc_pred_Aug(i,:)) .* w) ;
degassing_M = (V_atm_slope .* x * qgw * 1000 + V_atm_init)' .* ((M_Conc_pred_Aug(i,:)) - (M_12atm + M_13atm)) .* w ;

%Total up the fluxes to make gas budgets
advection_C_t = qgw * x(end) * (C_12gw + C_13gw); % CO2 coming into the canal in mmol/s  
fluvial_C = qgw * x(end) *(C_Conc_pred_Aug(i,end)); % CO2 leaving the canal with streamflow mmol/s 
oxidation_C_t = trapz(x,oxidation_C);
degassing_C_t = trapz(x,degassing_C);
DOC_C_t = trapz(x,DOC_C);

%CH4:
advection_M_t = qgw * x(end) * (M_12gw + M_13gw); % CH4 coming into the canal in mol/s  
fluvial_M = qgw * x(end) *(M_Conc_pred_Aug(i,end)); % CH4 leaving the canal with streamflow mol/s 
oxidation_M_t = trapz(x,oxidation_M); % CH4 leaving the canal from oxidation mol/s 
degassing_M_t = trapz(x,degassing_M); % CH4 leaving the canal from degassing mol/s 

% Record the CO2 budget [advection, DOC  oxidation degassing   fluvial]
budget_C_Aug (i,:) = [advection_C_t   DOC_C_t    oxidation_C_t       degassing_C_t   fluvial_C];
% Record the CH4 budget [advection   oxidation  degassing   fluvial]
budget_M_Aug (i,:) = [advection_M_t     oxidation_M_t   degassing_M_t   fluvial_M];

end

%% Calculate the confidence bands on the concentrations lines 2:end are the randoms

%JAN
C_Conc_pred_low_Jan  = prctile(C_Conc_pred_Jan(2:end,:),2.5);
C_Conc_pred_high_Jan = prctile(C_Conc_pred_Jan(2:end,:),97.5);
C_Conc_mean_Jan = C_Conc_pred_Jan(1,:);

C_del_pred_low_Jan  = prctile(C_del_pred_Jan(2:end,:),2.5);
C_del_pred_high_Jan = prctile(C_del_pred_Jan(2:end,:),97.5);
C_del_mean_Jan = C_del_pred_Jan(1,:);

M_Conc_pred_low_Jan  = prctile(M_Conc_pred_Jan(2:end,:),2.5);
M_Conc_pred_high_Jan = prctile(M_Conc_pred_Jan(2:end,:),97.5);
M_Conc_mean_Jan = M_Conc_pred_Jan(1,:);

M_del_pred_low_Jan  = prctile(M_del_pred_Jan(2:end,:),2.5);
M_del_pred_high_Jan = prctile(M_del_pred_Jan(2:end,:),97.5);
M_del_mean_Jan = M_del_pred_Jan(1,:);

%AUG
C_Conc_pred_low_Aug  = prctile(C_Conc_pred_Aug(2:end,:),2.5);
C_Conc_pred_high_Aug = prctile(C_Conc_pred_Aug(2:end,:),97.5);
C_Conc_mean_Aug = C_Conc_pred_Aug(1,:);

C_del_pred_low_Aug  = prctile(C_del_pred_Aug(2:end,:),2.5);
C_del_pred_high_Aug = prctile(C_del_pred_Aug(2:end,:),97.5);
C_del_mean_Aug = C_del_pred_Aug(1,:);

M_Conc_pred_low_Aug  = prctile(M_Conc_pred_Aug(2:end,:),2.5);
M_Conc_pred_high_Aug = prctile(M_Conc_pred_Aug(2:end,:),97.5);
M_Conc_mean_Aug = M_Conc_pred_Aug(1,:);

M_del_pred_low_Aug  = prctile(M_del_pred_Aug(2:end,:),2.5);
M_del_pred_high_Aug = prctile(M_del_pred_Aug(2:end,:),97.5);
M_del_mean_Aug = M_del_pred_Aug(1,:);

%% Load the observed data 

% January 2020
Canal_data_Jan = xlsread ('/Users/laurensomers/Documents/Research/Badas Methane/Stable Carbon Isotope Analysis/13C-DIC_CH4-Jan_2020.xlsx',7);

% August 2020
Canal_data_Aug = xlsread ('/Users/laurensomers/Documents/Research/Badas Methane/Stable Carbon Isotope Analysis/13C-DIC_CH4_Badas_Aug_2020.xlsx',1);
Canal_data_deep_Aug = xlsread ('/Users/laurensomers/Documents/Research/Badas Methane/Stable Carbon Isotope Analysis/13C-DIC_CH4_Badas_Aug_2020.xlsx',2);
x_obs_Aug = Canal_data_Aug(:,1);

%% Calculate the upstream and downstrem bounds (June 2022)

%Jan:
% Parse parameters:
deep_coef = params_US(1);  % Proportion of incoming groundwater that comes from below the canal
B = params_US(2); % Isotopic fractionation: methane oxidation reaction rate ratio: (13C rate)/(12C rate) Alison used alpha = 1.01 to 1.02 B=1/alpha
V_mic_coef = params_US(3); % coefficient to calculate V_mic based on V_atm.
V_atm_init = params_US(4);  % initial gas exchange velocity for CH4 METHANE!
V_atm_slope = params_US(5); % (1.2e-05)/500%1.1294e-05/1000; % Slope of V_atm * careful not to make it get too large or go negative
k_DOC = params_US(6);
qgw = q(1);
[M_12gw, M_13gw, C_12gw, C_13gw] = GW_exp_fit (PT1_30W_Jan, deep_coef);

%Calc initial conditions
M_12_init_Jan = (qgw*M_12gw+V_atm_init*w*M_12atm)/(qgw+V_atm_init*V_mic_coef*w+V_atm_init*w);
M_13_init_Jan = (qgw*M_13gw+V_atm_init*w*M_13atm)/(qgw+V_atm_init*V_mic_coef*B*w+V_atm_init*w);
C_12_init_Jan = ((qgw * C_12gw) + (V_mic_coef * M_12_init * w * V_atm_init) + (0.9667*V_atm_init*C_12atm*w) + (k_DOC*V_atm_init*(1-f)))/(qgw + 0.9667*V_atm_init*w);
C_13_init_Jan = ((qgw * C_13gw) + (V_mic_coef* B * M_13_init * w * V_atm_init) + (0.9667*V_atm_init*C_13atm*w) + (k_DOC*V_atm_init*f))/(qgw + 0.9667*V_atm_init*w);

% Convert initial condition to concentration and delta notation (Peedee Belemnite 13C/12C = 0.01118)
M_del_init_Jan = (((M_13_init_Jan/M_12_init_Jan)/0.01118)-1)*1000;
C_del_init_Jan = (((C_13_init_Jan/C_12_init_Jan)/0.01118)-1)*1000;
% Convert to total concentration
M_Conc_init_Jan = M_12_init_Jan + M_13_init_Jan;
C_Conc_init_Jan = C_12_init_Jan + C_13_init_Jan;

%Calc downstream condition:
M_12_inf_Jan = M_12atm/(1+V_mic_coef);
M_13_inf_Jan = M_13atm/(1+(B*V_mic_coef));
C_12_inf_Jan = C_12atm + (V_mic_coef*M_12atm)/(0.9667*(1+V_mic_coef)) + ((k_DOC*(1-f))/(0.9667*w));
C_13_inf_Jan = C_13atm + ((V_mic_coef*B*M_13atm)/(0.9667*(1+B*V_mic_coef)))+((k_DOC*f)/(0.9667*w));

% Convert downstream condition to concentration and delta notation (Peedee Belemnite 13C/12C = 0.01118)
M_del_inf_Jan = (((M_13_inf_Jan/M_12_inf_Jan)/0.01118)-1)*1000;
C_del_inf_Jan = (((C_13_inf_Jan/C_12_inf_Jan)/0.01118)-1)*1000;
% Convert to total concentration
M_Conc_inf_Jan = M_12_inf_Jan + M_13_inf_Jan;
C_Conc_inf_Jan = C_12_inf_Jan + C_13_inf_Jan;

%Aug:
deep_coef = params_US(7);  % Proportion of incoming groundwater that comes from below the canal
B = params_US(2); % Isotopic fractionation: methane oxidation reaction rate ratio: (13C rate)/(12C rate) Alison used alpha = 1.01 to 1.02 B=1/alpha
V_mic_coef = params_US(3); % coefficient to calculate V_mic based on V_atm.
V_atm_init = params_US(4);  % initial gas exchange velocity for CH4 METHANE!
V_atm_slope = params_US(5); % (1.2e-05)/500%1.1294e-05/1000; % Slope of V_atm * careful not to make it get too large or go negative
k_DOC = params_US(8);
qgw = q(2);
[M_12gw, M_13gw, C_12gw, C_13gw] = GW_exp_fit (PT1_30W_Aug, deep_coef);

M_12_init_Aug = (qgw*M_12gw+V_atm_init*w*M_12atm)/(qgw+V_atm_init*V_mic_coef*w+V_atm_init*w);
M_13_init_Aug = (qgw*M_13gw+V_atm_init*w*M_13atm)/(qgw+V_atm_init*V_mic_coef*B*w+V_atm_init*w);
C_12_init_Aug = ((qgw * C_12gw) + (V_mic_coef * M_12_init * w * V_atm_init) + (0.9667*V_atm_init*C_12atm*w) + (k_DOC*V_atm_init*(1-f)))/(qgw + 0.9667*V_atm_init*w);
C_13_init_Aug = ((qgw * C_13gw) + (V_mic_coef* B * M_13_init * w * V_atm_init) + (0.9667*V_atm_init*C_13atm*w) + (k_DOC*V_atm_init*f))/(qgw + 0.9667*V_atm_init*w);

% Convert initial condition to concentration and delta notation (Peedee Belemnite 13C/12C = 0.01118)
M_del_init_Aug = (((M_13_init_Aug/M_12_init_Aug)/0.01118)-1)*1000;
C_del_init_Aug = (((C_13_init_Aug/C_12_init_Aug)/0.01118)-1)*1000;
% Convert to total concentration
M_Conc_init_Aug = M_12_init_Aug + M_13_init_Aug;
C_Conc_init_Aug = C_12_init_Aug + C_13_init_Aug;

%Downstream (x approaches infinity):
%Calc downstream condition:
M_12_inf_Aug = M_12atm/(1+V_mic_coef);
M_13_inf_Aug = M_13atm/(1+(B*V_mic_coef));
C_12_inf_Aug = C_12atm + (V_mic_coef*M_12atm)/(0.9667*(1+V_mic_coef)) + ((k_DOC*(1-f))/(0.9667*w));
C_13_inf_Aug = C_13atm + ((V_mic_coef*B*M_13atm)/(0.9667*(1+B*V_mic_coef)))+((k_DOC*f)/(0.9667*w));

% Convert downstream condition to concentration and delta notation (Peedee Belemnite 13C/12C = 0.01118)
M_del_inf_Aug = (((M_13_inf_Aug/M_12_inf_Aug)/0.01118)-1)*1000;
C_del_inf_Aug = (((C_13_inf_Aug/C_12_inf_Aug)/0.01118)-1)*1000;
% Convert to total concentration
M_Conc_inf_Aug = M_12_inf_Aug + M_13_inf_Aug;
C_Conc_inf_Aug = C_12_inf_Aug + C_13_inf_Aug;


%% Plot the concentrations with confidence bands:
figure

%Jan
subplot (4,2,5)
x2 = [x(1:28); flipud(x(1:28))]
inBetween = [C_Conc_pred_low_Jan(1:28)'; flipud(C_Conc_pred_high_Jan(1:28)')];
fill(x2, inBetween, [0.9 0.9 0.9],'LineStyle','none');
hold on
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,2),'b.',MarkerSize=18);
ylabel ('DIC Concentration (mM)');
xlabel ('Distance downstream (m)');
plot (x,C_Conc_mean_Jan,'k:',LineWidth=2)
%plot(x (15:28), C_Conc_pred_high_Jan(15:28),':r')
%plot(x (15:28), C_Conc_pred_low_Jan(15:28),':r');
yline(C_Conc_init_Jan)
yline(C_Conc_inf_Jan)
xlim([0 5100]);
ylim([0 1.3]);


subplot (4,2,7)
x2 = [x(1:28); flipud(x(1:28))]
inBetween = [C_del_pred_low_Jan(1:28)'; flipud(C_del_pred_high_Jan(1:28)')];
fill(x2, inBetween, [0.9 0.9 0.9],'LineStyle','none');
hold on
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,3),'b.',MarkerSize=18);
ylabel ('\delta^1^3C-DIC (‰)')
xlabel ('Distance downstream (m)');
plot (x,C_del_mean_Jan,'k:',LineWidth=2)
%plot(x(15:28) , C_del_pred_high_Jan(15:28),':r')
%plot(x(15:28) , C_del_pred_low_Jan(15:28),':r');
yline(C_del_init_Jan)
yline(C_del_inf_Jan)
xlim([0 5100]);
ylim([-29 -17]);

subplot (5,2,1)
x2 = [x(1:28); flipud(x(1:28))]
inBetween = [M_Conc_pred_low_Jan(1:28)'; flipud(M_Conc_pred_high_Jan(1:28)')];
fill(x2, inBetween, [0.9 0.9 0.9],'LineStyle','none');
hold on
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,4),'b.',MarkerSize=18);
ylabel ('CH_4 Concentration (mM)');
xlabel ('Distance downstream (m)');
plot (x,M_Conc_mean_Jan,'k:',LineWidth=2)
%plot(x(15:28) , M_Conc_pred_high_Jan(15:28),':r')
%plot(x(15:28) , M_Conc_pred_low_Jan(15:28),':r');
yline(M_Conc_init_Jan)
yline(M_Conc_inf_Jan)
xlim([0 5100]);
ylim([0 0.1]);
title('January 2020');


subplot (4,2,3)
x2 = [x(1:28); flipud(x(1:28))]
inBetween = [M_del_pred_low_Jan(1:28)'; flipud(M_del_pred_high_Jan(1:28)')];
fill(x2, inBetween, [0.9 0.9 0.9],'LineStyle','none');
hold on
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,5),'b.',MarkerSize=18);
ylabel ('\delta^1^3C-CH_4 (‰)')
xlabel ('Distance downstream (m)');
plot (x,M_del_mean_Jan,'k:',LineWidth=2)
%plot(x(15:28) , M_del_pred_high_Jan(15:28),':r')
%plot(x(15:28) , M_del_pred_low_Jan(15:28),':r');
yline(M_del_init_Jan)
yline(M_del_inf_Jan)
xlim([0 5100]);
ylim([-74 -40])

% Aug
subplot (4,2,6)
x2 = [x(1:28); flipud(x(1:28))]
inBetween = [C_Conc_pred_low_Aug(1:28)'; flipud(C_Conc_pred_high_Aug(1:28)')];
fill(x2, inBetween, [0.9 0.9 0.9],'LineStyle','none');
hold on
%plot (Canal_data_deep_Aug (:,1),Canal_data_deep_Aug (:,3),'co');
plot (Canal_data_deep_Aug (:,1),Canal_data_deep_Aug (:,3),'Color','b','Marker','o','Linestyle','none');
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,3),'b.',MarkerSize=18);
%ylabel ('DIC Concentration (mM)');
%xlabel ('Distance downstream (m)');
plot (x,C_Conc_mean_Aug,'k:',LineWidth=2)
%plot(x (1:28), C_Conc_pred_high_Aug(1:28),':r')
%plot(x (1:28), C_Conc_pred_low_Aug(1:28),':r');
yline(C_Conc_init_Aug);
yline(C_Conc_inf_Aug);
xlim([0 5100]);
ylim([0 1.3]);


subplot (4,2,8)
x2 = [x(1:28); flipud(x(1:28))]
inBetween = [C_del_pred_low_Aug(1:28)'; flipud(C_del_pred_high_Aug(1:28)')];
fill(x2, inBetween, [0.9 0.9 0.9],'LineStyle','none');
hold on
plot (Canal_data_deep_Aug (:,1),Canal_data_deep_Aug (:,4),'b','Marker','o','Linestyle','none');
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,4),'b.',MarkerSize=18);
%ylabel ('\delta^1^3C-DIC (‰)')
%xlabel ('Distance downstream (m)');
plot (x,C_del_mean_Aug,'k:',LineWidth=2)
%plot(x(1:28) , C_del_pred_high_Aug(1:28),':r')
%plot(x(1:28) , C_del_pred_low_Aug(1:28),':r');
yline(C_del_init_Aug)
yline(C_del_inf_Aug)
xlim([0 5100]);
ylim([-29 -17]);

subplot (4,2,2)
x2 = [x(1:28); flipud(x(1:28))]
inBetween = [M_Conc_pred_low_Aug(1:28)'; flipud(M_Conc_pred_high_Aug(1:28)')];
fill(x2, inBetween, [0.9 0.9 0.9],'LineStyle','none');
hold on
plot (Canal_data_deep_Aug (:,1),Canal_data_deep_Aug (:,5),'bo','Linestyle','none');
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,5),'b.','Markersize',16);
%ylabel ('CH_4 Concentration (mM)');
%xlabel ('Distance downstream (m)');
plot (x,M_Conc_mean_Aug,'k:',LineWidth=2)
%plot(x(1:28) , M_Conc_pred_high_Aug(1:28),':r')
%plot(x(1:28) , M_Conc_pred_low_Aug(1:28),':r');
yline(M_Conc_init_Aug)
yline(M_Conc_inf_Aug)
xlim([0 5100]);
ylim([0 0.1]);
title('August 2020')
legend('95% Confidence Envelope','Measured (deep)','Measured (shallow)','Best fit');

subplot (4,2,4)

x2 = [x(1:28); flipud(x(1:28))]
inBetween = [M_del_pred_low_Aug(1:28)'; flipud(M_del_pred_high_Aug(1:28)')];
fill(x2, inBetween, [0.9 0.9 0.9],'LineStyle','none');
hold on
plot (Canal_data_deep_Aug (:,1),Canal_data_deep_Aug (:,6),'bo','Linestyle','none');
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,6),'b.','MarkerSize',18);
%ylabel ('\delta^1^3C-CH_4 (‰)')
%xlabel ('Distance downstream (m)');
plot (x,M_del_mean_Aug,'k:',LineWidth=2)
%plot(x(1:28) , M_del_pred_high_Aug(1:28),':r')
%plot(x(1:28) , M_del_pred_low_Aug(1:28),':r');
yline(M_del_init_Aug)
yline(M_del_inf_Aug)
xlim([0 5100]);
ylim([-74 -40])

%% Now plot the fluxes along the canal for the best fit scenario

% Calculate fluxes:
% January:

advection_C_Jan = ones(length(x),1) * q(1) * (C_12gw + C_13gw);
oxidation_C_Jan = (V_atm_slope .* x * q(1) * 1000 + V_atm_init)'.* V_mic_coef .* (M_Conc_pred_Jan(1002,:)) * w ;
degassing_C_Jan = 0.9667 .* (V_atm_slope .* x * q(1) * 1000 + V_atm_init)' .* ((C_Conc_pred_Jan(1002,:)) - (C_12atm + C_13atm)) .* w ;
DOC_C_Jan = k_DOC .* (V_atm_slope .* x * q(1) * 1000 + V_atm_init);
advection_M_Jan = ones(length(x),1) * q(1) * (M_12gw + M_13gw);
oxidation_M_Jan = (V_atm_slope .* x * q(1) * 1000 + V_atm_init)' .* (V_mic_coef .* (M_Conc_pred_Jan(1002,:)) .* w) ;
degassing_M_Jan = (V_atm_slope .* x * q(1) * 1000 + V_atm_init)' .* ((M_Conc_pred_Jan(1002,:)) - (M_12atm + M_13atm)) .* w ;

% August:
advection_C_Aug = ones(length(x),1) * q(2) * (C_12gw + C_13gw);
oxidation_C_Aug = (V_atm_slope .* x * q(2) * 1000 + V_atm_init)'.* V_mic_coef .* (M_Conc_pred_Aug(1002,:)) * w ;
degassing_C_Aug = 0.9667 .* (V_atm_slope .* x * qgw * 1000 + V_atm_init)' .* ((C_Conc_pred_Aug(1002,:)) - (C_12atm + C_13atm)) .* w ;
DOC_C_Aug = k_DOC .* (V_atm_slope .* x * q(2) * 1000 + V_atm_init);
advection_M_Aug = ones(length(x),1) * q(2) * (M_12gw + M_13gw);
oxidation_M_Aug = (V_atm_slope .* x * q(2) * 1000 + V_atm_init)' .* (V_mic_coef .* (M_Conc_pred_Aug(1002,:)) .* w) ;
degassing_M_Aug = (V_atm_slope .* x * q(2) * 1000 + V_atm_init)' .* ((M_Conc_pred_Aug(1002,:)) - (M_12atm + M_13atm)) .* w ;

figure
subplot (1,2,1)

plot(x,advection_M_Jan,'-b')
hold on
plot(x,advection_M_Aug,'-.b')
plot(x,-oxidation_M_Jan,'-k')
plot(x,-oxidation_M_Aug,'-.k')
plot(x,-degassing_M_Jan,'-r')
plot(x,-degassing_M_Aug,'-.r')
xlim([0 5070]);
%legend('Advection-Jan','Advection-Aug','CH_4 oxidation-Jan','CH_4 oxidation-Aug','Degassing-Jan','Degassing-Aug')
ylabel('CH_4 input or output (mol/s)')
xlabel ('Distance along canal (m)')
set (gca,'Ydir','reverse')

subplot (1,2,2)

plot(x,advection_C_Jan,'-b')
hold on
plot(x,advection_C_Aug,'-.b')
plot(x,oxidation_M_Jan,'-k')
plot(x,oxidation_M_Aug,'-.k')
plot(x,-degassing_C_Jan,'-r')
plot(x,-degassing_C_Aug,'-.r')
plot(x,DOC_C_Jan,'-g','Color',[0.2 0.8 0.2])
plot(x,DOC_C_Aug,'-.g','Color',[0.2 0.8 0.2])
xlim([0 5070]);

legend('Advection-Jan','Advection-Aug','CH_4 oxidation-Jan','CH_4 oxidation-Aug','Degassing-Jan','Degassing-Aug','DOC oxidation-Jan','DOC oxidation-Aug');
ylabel('DIC input or output (mol/s)')
xlabel ('Distance along canal (m)')
set (gca,'Ydir','reverse')


%% %% Get 95% CI bands on the budget

% Jan:
% CO2 [advection, DOC  oxidation degassing   fluvial]
budget_C_low_Jan = (prctile(budget_C_Jan(2:end,:),2.5).* [1 1 1 -1 -1]).* 1000;
budget_C_high_Jan = (prctile(budget_C_Jan(2:end,:),97.5).* [1 1 1 -1 -1]).*1000;
budget_C_mean_Jan = (budget_C_Jan(1,:) .* [1 1 1 -1 -1]).*1000;

%Methane [advection   oxidation  degassing   fluvial]
budget_M_low_Jan = (prctile(budget_M_Jan(2:end,:),2.5) .* [1 -1 -1 -1]).*1000;
budget_M_high_Jan = (prctile(budget_M_Jan(2:end,:),97.5) .* [1 -1 -1 -1]).*1000;
budget_M_mean_Jan = (budget_M_Jan(1,:).* [1 -1 -1 -1]).*1000;

%Calculate the deltas for the error bars:
budget_C_high_delta_Jan = budget_C_high_Jan - budget_C_mean_Jan;
budget_C_low_delta_Jan = budget_C_mean_Jan - budget_C_low_Jan;

%Calculate the deltas for the error bars:
budget_M_high_delta_Jan = budget_M_high_Jan - budget_M_mean_Jan
budget_M_low_delta_Jan = budget_M_mean_Jan - budget_M_low_Jan;

% What are the percentages of the budget (for the text)
% The best-fit numbers:
C_in = budget_C_mean_Jan(1) + budget_C_mean_Jan(2) + budget_C_mean_Jan(3)
C_out = budget_C_mean_Jan(4) + budget_C_mean_Jan(5)
M_in = budget_M_mean_Jan(1)

% Percentage of CO2 inputs
budget_C_mean_Jan (1) / C_in % advection
budget_C_mean_Jan (2) / C_in % DOC oxidation
budget_C_mean_Jan (3) / C_in % CH4 oxidation
% Percentage of CO2 outputs
budget_C_mean_Jan (4) / C_out % degassing
budget_C_mean_Jan(5) / C_out % fluvial
% Percentage of CH4 outputs
budget_M_mean_Jan (2) /M_in % oxidatoin
budget_M_mean_Jan (3) /M_in % degassing
budget_M_mean_Jan (4) /M_in % fluvial

% Make a table with budget #s and %:
% CO2 [advection, DOC  oxidation degassing   fluvial]
Source_sink_C = {'CO2 advection';'DOC oxidation';'CH4 oxidation';'CO2 degassing';'CO2 fluvial export'};
Var_names = {'Mean';'low';'high'}
Source_sink_M = {'CH4 advection';'CH4 oxidation';'CH4 degassing';'CH4 fluvial export'};

budget_table_C_Jan = table(budget_C_mean_Jan',budget_C_low_Jan',budget_C_high_Jan','RowNames',Source_sink_C,'VariableNames',Var_names)
budget_table_M_Jan = table(budget_M_mean_Jan',budget_M_low_Jan',budget_M_high_Jan','RowNames',Source_sink_M,'VariableNames',Var_names)

% AUG:
% CO2 [advection, DOC  oxidation degassing   fluvial]
budget_C_low_Aug = (prctile(budget_C_Aug(2:end,:),2.5).* [1 1 1 -1 -1]).* 1000;
budget_C_high_Aug = (prctile(budget_C_Aug(2:end,:),97.5).* [1 1 1 -1 -1]).*1000;
budget_C_mean_Aug = (budget_C_Aug(1,:) .* [1 1 1 -1 -1]).*1000;

%Methane [advection   oxidation  degassing   fluvial]
budget_M_low_Aug = (prctile(budget_M_Aug(2:end,:),2.5) .* [1 -1 -1 -1]).*1000;
budget_M_high_Aug = (prctile(budget_M_Aug(2:end,:),97.5) .* [1 -1 -1 -1]).*1000;
budget_M_mean_Aug = (budget_M_Aug(1,:).* [1 -1 -1 -1]).*1000;

%Calculate the deltas for the error bars:
budget_C_high_delta_Aug = budget_C_high_Aug - budget_C_mean_Aug;
budget_C_low_delta_Aug = budget_C_mean_Aug - budget_C_low_Aug;

%Calculate the deltas for the error bars:
budget_M_high_delta_Aug = budget_M_high_Aug - budget_M_mean_Aug
budget_M_low_delta_Aug = budget_M_mean_Aug - budget_M_low_Aug;

% What are the percentages of the budget (for the text)
% The best-fit numbers:
C_in = budget_C_mean_Aug(1) + budget_C_mean_Aug(2) + budget_C_mean_Aug(3)
C_out = budget_C_mean_Aug(4) + budget_C_mean_Aug(5)
M_in = budget_M_mean_Aug(1)

% Percentage of CO2 inputs
budget_C_mean_Aug (1) / C_in % advection
budget_C_mean_Aug (2) / C_in % DOC oxidation
budget_C_mean_Aug (3) / C_in % CH4 oxidation
% Percentage of CO2 outputs
budget_C_mean_Aug (4) / C_out % degassing
budget_C_mean_Aug(5) / C_out % fluvial
% Percentage of CH4 outputs
budget_M_mean_Aug (2) /M_in %oxidation
budget_M_mean_Aug (3) /M_in %degassing
budget_M_mean_Aug (4) /M_in %Fluvial

% Make a table with budget #s and %:
% CO2 [advection, DOC  oxidation degassing   fluvial]
Source_sink_C = {'CO2 advection';'DOC oxidation';'CH4 oxidation';'CO2 degassing';'CO2 fluvial export'};
Var_names = {'Mean';'low';'high'}
Source_sink_M = {'CH4 advection';'CH4 oxidation';'CH4 degassing';'CH4 fluvial export'};

budget_table_C_Aug = table(budget_C_mean_Aug',budget_C_low_Aug',budget_C_high_Aug','RowNames',Source_sink_C,'VariableNames',Var_names)
budget_table_M_Aug = table(budget_M_mean_Aug',budget_M_low_Aug',budget_M_high_Aug','RowNames',Source_sink_M,'VariableNames',Var_names)

%% Plot Budget bar charts with error bars

figure
subplot(1,2,2)            
Jan_num = [0.8  1.8  2.8  3.8  4.8]
Aug_num = [1.2  2.2  3.2  4.2  5.2]
C_chart_Jan = bar(Jan_num,budget_C_mean_Jan, 0.4)
hold on
C_Chart_Aug = bar(Aug_num,budget_C_mean_Aug,0.4)     
hold on
er_Jan = errorbar(Jan_num,  budget_C_mean_Jan,  budget_C_high_delta_Jan ,  budget_C_low_delta_Jan);  
er_Jan.Color = [0 0 0];                            
er_Jan.LineStyle = 'none'; 
hold on
er_Aug = errorbar(Aug_num,  budget_C_mean_Aug,  budget_C_high_delta_Aug ,  budget_C_low_delta_Aug);       
er_Aug.Color = [0 0 0];                            
er_Aug.LineStyle = 'none';           
xticks([1 2 3 4 5]);
cats_C = categorical({'Advection into canal','DOC oxidation','CH_4 oxidation to CO_2','Degassing','Fluvial export'});          
xticklabels(cats_C);
xtickangle(45)
title('CO_2 budget')
% CO2 [advection, DOC  oxidation degassing   fluvial]
ylim([-1100 1100])
ylabel('Input or output (mMol/s)')

subplot(1,2,1)            
Jan_num = [0.8  1.8  2.8  3.8]
Aug_num = [1.2  2.2  3.2  4.2]
M_chart_Jan = bar(Jan_num,budget_M_mean_Jan, 0.4)
hold on
M_Chart_Aug = bar(Aug_num,budget_M_mean_Aug,0.4)     
hold on
er_Jan = errorbar(Jan_num,  budget_M_mean_Jan,  budget_M_high_delta_Jan ,  budget_M_low_delta_Jan);  
er_Jan.Color = [0 0 0];                            
er_Jan.LineStyle = 'none'; 
hold on
er_Aug = errorbar(Aug_num,  budget_M_mean_Aug,  budget_M_high_delta_Aug ,  budget_M_low_delta_Aug);       
er_Aug.Color = [0 0 0];                            
er_Aug.LineStyle = 'none'; 
cats_M = categorical({'Advection into canal','CH_4 oxidation to CO_2','Degassing','Fluvial export'});          
xticks([1 2 3 4]);
xticklabels(cats_M);
xtickangle(45)
title('CH_4 budget')
legend('January 2020','August 2020')
ylim([-35 35])
ylabel('Input or output (mMol/s)')

