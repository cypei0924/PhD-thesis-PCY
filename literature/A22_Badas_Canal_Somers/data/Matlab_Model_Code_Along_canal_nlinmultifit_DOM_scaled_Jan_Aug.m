%% Along_Canal_13C_nlinfit_DOM_Scaled_Jan_Aug
% Lauren Somers
% Mar 9, 2021
% This code fits a 1D model (in the form of differential equations solved numerically)
% of canal dissolved gas processes (advection, degassing, DOC oxidation, CH4 oxidation) to field observations of concentration and isotopic 
% ratios of of CO2 and CH4 along the Badas Canal. This code fits the model
% based on both datasets from January and August 2020. 

%% Clear and create isotope conversion function
clear;
clc;
% Define function to convert concentration and delta to Concentration of
% 12C and 13C (Peedee Belemnite 13C/12C = 0.01118)
del_to_ConcC12 = @(delta, Conc_t) (Conc_t)./((delta/1000 +1) * 0.01118 + 1);

%% Initial values of fitting parameters:
% Initial guess of fitting parameters:
% Order:  deep_coef_Jan ; B ; V_mic_coef ; V_atm_init  ; V_atm_slope ; k_DOC_Jan ; deep_coef_Aug ; k_DOC_Aug
% This is what they were: p = [-1.5; 0.97; 2; 0 ; 7.8537e-09; 2 ; -1.5; 4]';
p = [-1.5; 0.97; 2.8; 5.56806e-07 ; 1.4772245e-07; 1.55 ; -1.5; 5.3]';

%% Parameter Scaling:
%scaling = [10  1  1/10  10000000  10000000  1  10];
scaling = [1  1  1/10  10000000  10000000  1  1  1];
p=p.*scaling;

%% ***  Constants that are different in Jan and Aug ***

%qgw = [0.0000489  0.0000572]; %(incoming groundwater per unit length of
%canal (m^2/s). Updated to below values with improvement of stream gauging data
qgw = [0.0000489  0.0000611]; %(incoming groundwater per unit length of canal (m^2/s) for January and August datasets respectively

% Load porewater concentrations
PT1_30W_Jan = xlsread('/Users/laurensomers/Documents/Research/Badas Methane/Stable Carbon Isotope Analysis/13C-DIC_CH4-Jan_2020.xlsx',1);
PT1_30W_Aug = xlsread('/Users/laurensomers/Documents/Research/Badas Methane/Stable Carbon Isotope Analysis/13C-DIC_CH4_Badas_Aug_2020',3);

% Fix issues with JAN field data
PT1_30W_Jan(9:10,:) = []; % Remove duplicate values at d=3m
PT1_30W_Jan = cat(1,PT1_30W_Jan (1,:),PT1_30W_Jan); % Duplicate data for most shallow point
PT1_30W_Jan (1,1) = 0.1; % Make the depth of the most shallow point 0.1
PT1_30W_Jan = cat(1, [0   0.0176   -11   2.68*10^(-6)    -47] ,PT1_30W_Jan);   % Make top point at d = 0 in equilibrium with atmosphere

% Fix issues with AUG field data
PT1_30W_Aug = cat(1,PT1_30W_Aug , PT1_30W_Jan (10:15,:)); % Combine shallow pts from August and deep points from Jan
PT1_30W_Aug = cat(1, [0   0.0176   -11   2.68*10^(-6)    -47] ,PT1_30W_Aug);   % Make top point at d = 0 in equilibrium with atmosphere

% shallow_gw(1,1) = del_to_ConcC12(-20.1248,0.4002); %C12-DIC
% shallow_gw(2,1) = 0.4002 - shallow_gw(1,1); %13C-DIC
% shallow_gw(3,1) = del_to_ConcC12(-67.4044,0.0459); % 12C-CH4 
% shallow_gw(4,1) = 0.0459 - shallow_gw(3,1); %13C-CH4
% 
% %August:
% shallow_gw(1,2) = del_to_ConcC12(-19.3532,0.6568); %C12-DIC
% shallow_gw(2,2) = 0.6568 - shallow_gw(1,2); %13C-DIC
% shallow_gw(3,2) = del_to_ConcC12(-76.7505,0.0537); % 12C-CH4 
% shallow_gw(4,2) = 0.0537 - shallow_gw(3,2); %13C-CH4


%% *** Constants that are the same in Jan and Aug ***
% Define the constants in an array that the function can use.

%Deep groundwater concentrations

% New Data
% deep_gw(1,1) = del_to_ConcC12(-2.7121,2.3089); %C12-DIC
% deep_gw(2,1) = 2.3089 - deep_gw(1,1); %13C-DIC
% deep_gw(3,1) = del_to_ConcC12(-71.7026,0.3325); % 12C-CH4 
% deep_gw(4,1) = 0.3325 - deep_gw(3,1); %13C-CH4
% 
% deep_gw(:,2) = deep_gw(:,1);
% deep_gw(1,2) = del_to_ConcC12(-0.01,2.80); %C12-DIC
% deep_gw(2,2) = 2.80 - deep_gw(1,2); %13C-DIC
% deep_gw(3,2) = del_to_ConcC12(-70.09,0.4); % 12C-CH4 
% deep_gw(4,2) = 0.4 - deep_gw(3,2); %13C-CH4

w = 10; % Width of the canal (m)

% DOC isotopic characteristics
C_DOC = 0.283; % Concentration of CO2 produced by degradation of DOC (mM) 
delta_C_DOC = -29.67; % From Gandois, 2014, d13C of DOC
C_12DOC = del_to_ConcC12 (delta_C_DOC,C_DOC);
C_13DOC = C_DOC - C_12DOC;

%Atmospheric equilibrium concentrations:
M_atm = 2.68*10^(-6); % aqueous concentration of CH4 in equilibrium with atmosphere (mM)
delta_M_atm = -47; % isotope ratio for atmospheric methane
M_12atm = del_to_ConcC12 (delta_M_atm,M_atm); % Aqueous concentration of 12CH4 that would be in equilibrium with atmosphere (mM)
M_13atm = M_atm - M_12atm;
C_atm = 0.0176; % aqueous concentration of CO2 in equilibrium with atmosphere (mM)
delta_C_atm = -11; % isotope ratio for atmospheric methane
C_12atm = del_to_ConcC12 (delta_C_atm,C_atm);
C_13atm = C_atm - C_12atm;


%% Load field observations:

Canal_data = xlsread ('/Users/laurensomers/Documents/Research/Badas Methane/Stable Carbon Isotope Analysis/13C-DIC_CH4-Jan_2020.xlsx',7);
Canal_data_Jan = Canal_data(2:(end-1),:); % Cut off the first and last points for fitting 
x_obs_Jan = Canal_data_Jan(:,1);

Canal_data = xlsread ('/Users/laurensomers/Documents/Research/Badas Methane/Stable Carbon Isotope Analysis/13C-DIC_CH4_Badas_Aug_2020.xlsx',1);
Canal_data_Aug = Canal_data (1:(end-1),:); % Cut off the last point for fitting
x_obs_Aug = Canal_data_Aug(:,1);

% Optimize for conc and delta instead of concentrations of isotopologs
Conc_obs_d_Jan = Canal_data_Jan(:, 2:5); % Observed concentraitons in conc and delta
Conc_obs_d_Aug = Canal_data_Aug(:, 3:6); % Observed concentraitons in conc and delta

% Scale the observed values (dependent variables)
Conc_obs_d_Jan_sc (:,1) = (Conc_obs_d_Jan (:,1) - min(Conc_obs_d_Jan(:,1)))/(max(Conc_obs_d_Jan(:,1)) - min(Conc_obs_d_Jan(:,1)));
Conc_obs_d_Jan_sc (:,2) = (Conc_obs_d_Jan (:,2) - min(Conc_obs_d_Jan(:,2)))/(max(Conc_obs_d_Jan(:,2)) - min(Conc_obs_d_Jan(:,2)));
Conc_obs_d_Jan_sc (:,3) = (Conc_obs_d_Jan (:,3) - min(Conc_obs_d_Jan(:,3)))/(max(Conc_obs_d_Jan(:,3)) - min(Conc_obs_d_Jan(:,3)));
Conc_obs_d_Jan_sc (:,4) = (Conc_obs_d_Jan (:,4) - min(Conc_obs_d_Jan(:,4)))/(max(Conc_obs_d_Jan(:,4)) - min(Conc_obs_d_Jan(:,4)));

Conc_obs_d_Aug_sc (:,1) = (Conc_obs_d_Aug (:,1) - min(Conc_obs_d_Aug(:,1)))/(max(Conc_obs_d_Aug(:,1)) - min(Conc_obs_d_Aug(:,1)));
Conc_obs_d_Aug_sc (:,2) = (Conc_obs_d_Aug (:,2) - min(Conc_obs_d_Aug(:,2)))/(max(Conc_obs_d_Aug(:,2)) - min(Conc_obs_d_Aug(:,2)));
Conc_obs_d_Aug_sc (:,3) = (Conc_obs_d_Aug (:,3) - min(Conc_obs_d_Aug(:,3)))/(max(Conc_obs_d_Aug(:,3)) - min(Conc_obs_d_Aug(:,3)));
Conc_obs_d_Aug_sc (:,4) = (Conc_obs_d_Aug (:,4) - min(Conc_obs_d_Aug(:,4)))/(max(Conc_obs_d_Aug(:,4)) - min(Conc_obs_d_Aug(:,4)));

% Define solver weights - curretly all points are equally weighted and observations are scaled:
% weights = ones(size(Conc_obs_d));
% weights_cell = {weights(:,1)',weights(:,2)',weights(:,3)',weights(:,4)'};

% Save the inputs so that the model function can load them
%save ('Along_canal_inputs.mat','qgw','w','M_12atm','M_13atm','C_12atm','C_13atm','shallow_gw','deep_gw','Conc_obs_d_Jan_sc','Conc_obs_d_Aug_sc','C_12DOC','C_13DOC','scaling') % The observations are used for re-scaling in the function

save ('Along_canal_inputs.mat','qgw','w','M_12atm','M_13atm','C_12atm','C_13atm','PT1_30W_Jan','PT1_30W_Aug','Conc_obs_d_Jan','Conc_obs_d_Aug','C_12DOC','C_13DOC','scaling'); % The observations are used for re-scaling in the function

%% Optimize the fitting parameters to match field data:

%Make cell array inputs
% Put model functions in cell array:
mdl_cell = {@Conc_CO2_Model_DOM_Jan,  @del_CO2_Model_DOM_Jan,  @Conc_CH4_Model_DOM_Jan,  @del_CH4_Model_DOM_Jan,... %Models for Jan
            @Conc_CO2_Model_DOM_Aug,  @del_CO2_Model_DOM_Aug,  @Conc_CH4_Model_DOM_Aug,  @del_CH4_Model_DOM_Aug}; % Models for Aug (only difference is where to solve diff equation)

% Put observations in cell array:        
Conc_obs_d_cell = {Conc_obs_d_Jan_sc(:,1)' , Conc_obs_d_Jan_sc(:,2)' , Conc_obs_d_Jan_sc(:,3)' , Conc_obs_d_Jan_sc(:,4)',...
                   Conc_obs_d_Aug_sc(:,1)' , Conc_obs_d_Aug_sc(:,2)' , Conc_obs_d_Aug_sc(:,3)' , Conc_obs_d_Aug_sc(:,4)'};

x_obs_cell = {x_obs_Jan',x_obs_Jan',x_obs_Jan',x_obs_Jan',...
              x_obs_Aug',x_obs_Aug',x_obs_Aug',x_obs_Aug'};

%Fit parameters using non-linear regression function nlinmultifit:
% [params,resid,J,Sigma,mse,errorparam,rubustw] = nlinmultifit(x_obs_cell , Conc_obs_d_cell, mdl_cell, p , 'Weights' , weights_cell);
[params,resid,J,Sigma,mse,errorparam,rubustw] = nlinmultifit(x_obs_cell , Conc_obs_d_cell, mdl_cell, p);


%% Get the confidence intervals on fitted parameters
% returns 95% CI

ci = nlparci(params,resid,'jacobian',J);

%% Calculate and plot the model output and confidence interval
[C_Conc_pred_sc_Jan,C_CI_sc] = nlpredci(@Conc_CO2_Model_DOM_Jan,x_obs_Jan',params,resid,'Covar',Sigma);
C_Conc_pred_Jan = C_Conc_pred_sc_Jan .* (max(Conc_obs_d_Jan(:,1)) - min(Conc_obs_d_Jan(:,1))) + min(Conc_obs_d_Jan(:,1));
C_CI_high_Jan = (C_Conc_pred_sc_Jan + C_CI_sc) .* (max(Conc_obs_d_Jan(:,1)) - min(Conc_obs_d_Jan(:,1))) + min(Conc_obs_d_Jan(:,1));
C_CI_low_Jan = (C_Conc_pred_sc_Jan - C_CI_sc) .* (max(Conc_obs_d_Jan(:,1)) - min(Conc_obs_d_Jan(:,1))) + min(Conc_obs_d_Jan(:,1));

figure
subplot (4,2,1)
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,2),'bo');
ylabel ('DIC Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x_obs_Jan,C_Conc_pred_Jan,'r')
hold on
plot(x_obs_Jan , C_CI_high_Jan,':r')
hold on
plot(x_obs_Jan , C_CI_low_Jan,':r');
legend('Measured','Modeled','95% Confidence Interval');

[C_del_pred_sc_Jan,Cd_CI_sc] = nlpredci(@del_CO2_Model_DOM_Jan,x_obs_Jan',params,resid,'Covar',Sigma);
C_del_pred_Jan = C_del_pred_sc_Jan * (max(Conc_obs_d_Jan(:,2)) - min(Conc_obs_d_Jan(:,2))) + min(Conc_obs_d_Jan(:,2));
Cd_CI_high_Jan = (C_del_pred_sc_Jan + Cd_CI_sc) .* (max(Conc_obs_d_Jan(:,2)) - min(Conc_obs_d_Jan(:,2))) + min(Conc_obs_d_Jan(:,2));
Cd_CI_low_Jan = (C_del_pred_sc_Jan - Cd_CI_sc) .* (max(Conc_obs_d_Jan(:,2)) - min(Conc_obs_d_Jan(:,2))) + min(Conc_obs_d_Jan(:,2));

subplot (4,2,3)
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,3),'bo');
ylabel ('delta ^1^3C DIC (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x_obs_Jan,C_del_pred_Jan,'r')
hold on
plot(x_obs_Jan , Cd_CI_high_Jan,':r')
hold on
plot(x_obs_Jan , Cd_CI_low_Jan,':r');

[M_Conc_pred_sc_Jan,M_CI_sc] = nlpredci(@Conc_CH4_Model_DOM_Jan,x_obs_Jan',params,resid,'Covar',Sigma);
M_Conc_pred_Jan = M_Conc_pred_sc_Jan * (max(Conc_obs_d_Jan(:,3)) - min(Conc_obs_d_Jan(:,3))) + min(Conc_obs_d_Jan(:,3));
M_CI_high_Jan = (M_Conc_pred_sc_Jan + M_CI_sc) .* (max(Conc_obs_d_Jan(:,3)) - min(Conc_obs_d_Jan(:,3))) + min(Conc_obs_d_Jan(:,3));
M_CI_low_Jan = (M_Conc_pred_sc_Jan - M_CI_sc) .* (max(Conc_obs_d_Jan(:,3)) - min(Conc_obs_d_Jan(:,3))) + min(Conc_obs_d_Jan(:,3));

subplot (4,2,5)
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,4),'bo');
ylabel ('CH_4 Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x_obs_Jan,M_Conc_pred_Jan,'r')
hold on
plot(x_obs_Jan , M_CI_high_Jan,':r')
hold on
plot(x_obs_Jan , M_CI_low_Jan,':r');

[M_del_pred_sc_Jan,Md_CI_sc] = nlpredci(@del_CH4_Model_DOM_Jan,x_obs_Jan',params,resid,'Covar',Sigma);
M_del_pred_Jan = M_del_pred_sc_Jan * (max(Conc_obs_d_Jan(:,4)) - min(Conc_obs_d_Jan(:,4))) + min(Conc_obs_d_Jan(:,4));
Md_CI_high_Jan = (M_del_pred_sc_Jan + Md_CI_sc) .* (max(Conc_obs_d_Jan(:,4)) - min(Conc_obs_d_Jan(:,4))) + min(Conc_obs_d_Jan(:,4));
Md_CI_low_Jan  = (M_del_pred_sc_Jan - Md_CI_sc) .* (max(Conc_obs_d_Jan(:,4)) - min(Conc_obs_d_Jan(:,4))) + min(Conc_obs_d_Jan(:,4));

subplot (4,2,7)
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,5),'bo');
ylabel ('delta ^1^3C CH4 (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x_obs_Jan,M_del_pred_Jan,'r')
hold on
plot(x_obs_Jan , Md_CI_high_Jan,':r')
hold on
plot(x_obs_Jan , Md_CI_low_Jan,':r');

% AUGUST

[C_Conc_pred_sc_Aug,C_CI_sc] = nlpredci(@Conc_CO2_Model_DOM_Aug,x_obs_Aug',params,resid,'Covar',Sigma);
C_Conc_pred_Aug = C_Conc_pred_sc_Aug .* (max(Conc_obs_d_Aug(:,1)) - min(Conc_obs_d_Aug(:,1))) + min(Conc_obs_d_Aug(:,1));
C_CI_high_Aug = (C_Conc_pred_sc_Aug + C_CI_sc) .* (max(Conc_obs_d_Aug(:,1)) - min(Conc_obs_d_Aug(:,1))) + min(Conc_obs_d_Aug(:,1));
C_CI_low_Aug = (C_Conc_pred_sc_Aug - C_CI_sc) .* (max(Conc_obs_d_Aug(:,1)) - min(Conc_obs_d_Aug(:,1))) + min(Conc_obs_d_Aug(:,1));

subplot (4,2,2)
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,3),'bo');
ylabel ('DIC Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x_obs_Aug,C_Conc_pred_Aug,'r')
hold on
plot(x_obs_Aug , C_CI_high_Aug,':r')
hold on
plot(x_obs_Aug , C_CI_low_Aug,':r');

[C_del_pred_sc_Aug,Cd_CI_sc] = nlpredci(@del_CO2_Model_DOM_Aug,x_obs_Aug',params,resid,'Covar',Sigma);
C_del_pred_Aug = C_del_pred_sc_Aug * (max(Conc_obs_d_Aug(:,2)) - min(Conc_obs_d_Aug(:,2))) + min(Conc_obs_d_Aug(:,2));
Cd_CI_high_Aug = (C_del_pred_sc_Aug + Cd_CI_sc) .* (max(Conc_obs_d_Aug(:,2)) - min(Conc_obs_d_Aug(:,2))) + min(Conc_obs_d_Aug(:,2));
Cd_CI_low_Aug = (C_del_pred_sc_Aug - Cd_CI_sc) .* (max(Conc_obs_d_Aug(:,2)) - min(Conc_obs_d_Aug(:,2))) + min(Conc_obs_d_Aug(:,2));

subplot (4,2,4)
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,4),'bo');
ylabel ('delta ^1^3C DIC (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x_obs_Aug,C_del_pred_Aug,'r')
hold on
plot(x_obs_Aug , Cd_CI_high_Aug,':r')
hold on
plot(x_obs_Aug , Cd_CI_low_Aug,':r');

[M_Conc_pred_sc_Aug,M_CI_sc] = nlpredci(@Conc_CH4_Model_DOM_Aug,x_obs_Aug',params,resid,'Covar',Sigma);
M_Conc_pred_Aug = M_Conc_pred_sc_Aug * (max(Conc_obs_d_Aug(:,3)) - min(Conc_obs_d_Aug(:,3))) + min(Conc_obs_d_Aug(:,3));
M_CI_high_Aug = (M_Conc_pred_sc_Aug + M_CI_sc) .* (max(Conc_obs_d_Aug(:,3)) - min(Conc_obs_d_Aug(:,3))) + min(Conc_obs_d_Aug(:,3));
M_CI_low_Aug = (M_Conc_pred_sc_Aug - M_CI_sc) .* (max(Conc_obs_d_Aug(:,3)) - min(Conc_obs_d_Aug(:,3))) + min(Conc_obs_d_Aug(:,3));

subplot (4,2,6)
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,5),'bo');
ylabel ('CH_4 Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x_obs_Aug,M_Conc_pred_Aug,'r')
hold on
plot(x_obs_Aug , M_CI_high_Aug,':r')
hold on
plot(x_obs_Aug , M_CI_low_Aug,':r');

[M_del_pred_sc_Aug,Md_CI_sc] = nlpredci(@del_CH4_Model_DOM_Aug,x_obs_Aug',params,resid,'Covar',Sigma);
M_del_pred_Aug = M_del_pred_sc_Aug * (max(Conc_obs_d_Aug(:,4)) - min(Conc_obs_d_Aug(:,4))) + min(Conc_obs_d_Aug(:,4));
Md_CI_high_Aug = (M_del_pred_sc_Aug + Md_CI_sc) .* (max(Conc_obs_d_Aug(:,4)) - min(Conc_obs_d_Aug(:,4))) + min(Conc_obs_d_Aug(:,4));
Md_CI_low_Aug  = (M_del_pred_sc_Aug - Md_CI_sc) .* (max(Conc_obs_d_Aug(:,4)) - min(Conc_obs_d_Aug(:,4))) + min(Conc_obs_d_Aug(:,4));

subplot (4,2,8)
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,6),'bo');
ylabel ('delta ^1^3C CH4 (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x_obs_Aug,M_del_pred_Aug,'r')
hold on
plot(x_obs_Aug , Md_CI_high_Aug,':r')
hold on
plot(x_obs_Aug , Md_CI_low_Aug,':r');


%% Error metrics

% Convert covariance matrix to correlation matrix
Correlation = corrcov(Sigma); % Does the covariance matrix need to be unscaled somehow?

% % Calc residuals
residuals_abs_Jan = Conc_obs_d_Jan - [C_Conc_pred_Jan' , C_del_pred_Jan', M_Conc_pred_Jan' , M_del_pred_Jan'];
residuals_abs_Aug = Conc_obs_d_Aug - [C_Conc_pred_Aug' , C_del_pred_Aug', M_Conc_pred_Aug' , M_del_pred_Aug'];
 
params_US = params./scaling %Unscale the parameters
ci_US (1,:) = ci(:,1)./scaling' %Unscale the 95 % confidence interval
ci_US (2,:) = ci(:,2)./scaling' %Unscale the 95 % confidence interval
std_dev_abs = sqrt(diag(Sigma))./scaling' % Unscaled parameter std devs?
sse_scaled = sum(resid.^2) % Sum of square errors weighted
%sse_abs = sum(residuals_abs.^2)
RMSE_abs_Jan = sqrt(mean(residuals_abs_Jan.^2)) % These are the true RMSE
RMSE_abs_Aug = sqrt(mean(residuals_abs_Aug.^2)) % These are the true RMSE
%nRMSE = RMSE_abs./(range(Conc_obs_d))
