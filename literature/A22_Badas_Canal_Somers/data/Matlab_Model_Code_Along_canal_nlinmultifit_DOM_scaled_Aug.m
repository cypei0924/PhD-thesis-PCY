%% Along_Canal_13C_nlinfit_DOM_Scaled
% Lauren Somers
% Jan 19, 2021
% Fits input parameters to match field observations of concentration of 12C- and 13C- CO2 
% and CH4 along the Badas Canal numerically using differential equations.
% Now includes oxidation of DOC and scaling of parameters!

%% Clear and load function
clear;
clc;
% Define function to convert delta to Concentration 12C and 13C - Peedee Belemnite 13C/12C = 0.01118
del_to_ConcC12 = @(delta, Conc_t) (Conc_t)./((delta/1000 +1) * 0.01118 + 1);

%% Initial values of fitting parameters:

% Initial guess of fitting parameters:
% Order:  deep_coef ; B ; V_mic_coef ; V_atm_init  ; V_atm_slope ; k_DOC ()
p = [0.1; 0.98; 2; 0 ; 7.8537e-09; 1]'; 
% generate random starting guesses:
%p = low + rand(5,1).*(high-low);

%% Parameter Scaling:
scaling = [10  1  1/10  10000000  10000000  1];
p=p.*scaling;
%p(4) = p(4) + 1;

%% Constants ********************
% Define the constants in an array that the function can use.
qgw = 0.0000572; %(incoming groundwater per unit length of canal (m^2/s)
w = 4; % Width of the canal (m)

% DOC conversion to CO2
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

% Shallow and deep groudnwater concentrations:
shallow_gw(1) = del_to_ConcC12(-16.74,0.982); %C12-DIC
shallow_gw(2) = 0.982 - shallow_gw(1); %13C-DIC
shallow_gw(3) = del_to_ConcC12(-75.9,0.129); % 12C-CH4 
shallow_gw(4) = 0.129 - shallow_gw(3); %13C-CH4

%Deep is currestly represented by the point directly below the canal*
%Subject to change when we get the CH4 data from the D1 point.
deep_gw(1) = del_to_ConcC12(-0.01,2.80); %C12-DIC
deep_gw(2) = 2.80 - deep_gw(1); %13C-DIC
deep_gw(3) = del_to_ConcC12(-70.09,0.5941); % 12C-CH4 
deep_gw(4) = 0.5941 - deep_gw(3); %13C-CH4

%% Load field observations:

Canal_data = xlsread ('/Users/laurensomers/Documents/Tropical Peatlands Research/Stable Carbon Isotope Analysis/13C-DIC_CH4_Badas_Aug_2020.xlsx',1);
Canal_data = Canal_data(1:(end-1),:);
x_obs = Canal_data(:,1);

% Optimize for conc and delta instead of concentrations of isotopologs
Conc_obs_d = Canal_data(:, 3:6); % Observed concentraitons in conc and delta
%Conc_obs_d = Canal_data(1:end-1, 3:6); % Observed concentraitons in conc and delta

% % % % Convert concentration and delt to concentrations:
% Conc_obs_i (:,1) = del_to_ConcC12 (Canal_data(:,5) , Canal_data(:,4)); % 12-CH4
% Conc_obs_i (:,2) = Canal_data (:,4) - Conc_obs_i(:,1); %13-CH4
% Conc_obs_i (:,3) = del_to_ConcC12 (Canal_data(:,3) , Canal_data(:,2)); %12-CO2
% Conc_obs_i (:,4) = Canal_data (:,2) - Conc_obs_i(:,3);  %13-CO2

% Scale the observed values (dependent variables)
Conc_obs_d_sc (:,1) = (Conc_obs_d (:,1) - min(Conc_obs_d(:,1)))/(max(Conc_obs_d(:,1)) - min(Conc_obs_d(:,1)));
Conc_obs_d_sc (:,2) = (Conc_obs_d (:,2) - min(Conc_obs_d(:,2)))/(max(Conc_obs_d(:,2)) - min(Conc_obs_d(:,2)));
Conc_obs_d_sc (:,3) = (Conc_obs_d (:,3) - min(Conc_obs_d(:,3)))/(max(Conc_obs_d(:,3)) - min(Conc_obs_d(:,3)));
Conc_obs_d_sc (:,4) = (Conc_obs_d (:,4) - min(Conc_obs_d(:,4)))/(max(Conc_obs_d(:,4)) - min(Conc_obs_d(:,4)));

% Define solver weights:
weights = ones(size(Conc_obs_d));

% %weighted by 1/the range of observed values
% weights(:,1) = 1/(max(Conc_obs_d(:,1)) - min(Conc_obs_d(:,1)));
% weights(:,2) = abs(1/(max(Conc_obs_d(:,2)) - min(Conc_obs_d(:,2))));
% weights(:,3) = 1/(max(Conc_obs_d(:,3)) - min(Conc_obs_d(:,3)));
% weights(:,4) = abs(1/(max(Conc_obs_d(:,4)) - min(Conc_obs_d(:,4))));

weights_cell = {weights(:,1)',weights(:,2)',weights(:,3)',weights(:,4)'};

% Save the inputs so that the function can load them
%save ('Along_canal_inputs.mat','qgw','w','M_12atm','M_13atm','C_12atm','C_13atm','shallow_gw','deep_gw','x_obs','Conc_obs_d','C_12DOC','C_13DOC')
save ('Along_canal_inputs.mat','qgw','w','M_12atm','M_13atm','C_12atm','C_13atm','shallow_gw','deep_gw','Conc_obs_d','Conc_obs_d_sc','C_12DOC','C_13DOC','scaling')
%% Optimize the fitting parameters to match field data:

%Make cell array inputs
mdl_cell = {@Conc_CO2_Model_DOM,  @del_CO2_Model_DOM,  @Conc_CH4_Model_DOM,  @del_CH4_Model_DOM};
%Conc_obs_d_cell = {Conc_obs_d(:,1)' , Conc_obs_d(:,2)' , Conc_obs_d(:,3)' , Conc_obs_d(:,4)'};
Conc_obs_d_cell = {Conc_obs_d_sc(:,1)' , Conc_obs_d_sc(:,2)' , Conc_obs_d_sc(:,3)' , Conc_obs_d_sc(:,4)'};
x_obs_cell = {Canal_data(:,1)',Canal_data(:,1)',Canal_data(:,1)',Canal_data(:,1)'};

%Fit parameters:
%params = nlinfit( x_obs, Conc_obs , @Model , p );
%params = lsqcurvefit (@Model , p , x_obs , Conc_obs_w , low , high );
%[params,resnorm,residual,exitflag,output,lambda,jacobian] = lsqcurvefit (@Model , p , x_obs , Conc_obs_w , low , high);
[params,resid,J,Sigma,mse,errorparam,rubustw] = nlinmultifit(x_obs_cell , Conc_obs_d_cell, mdl_cell, p , 'Weights' , weights_cell);

%% Get the confidence intervals on fitted parameters
% returns 95% CI

ci = nlparci(params,resid,'jacobian',J);

% %% Calculate and plot the model output and confidence interval
% [C_Conc_pred,C_CI] = nlpredci(@Conc_CO2_Model_DOM,x_obs',params,resid,'Covar',Sigma);
% 
% figure
% subplot (4,1,1)
% plot (Canal_data (:,1),Canal_data (:,2),'bo');
% ylabel ('DIC Concentration (mM)');
% xlabel ('Distance downstream (m)');
% hold on
% plot (x_obs,C_Conc_pred,'r')
% hold on
% plot(x_obs , C_Conc_pred-C_CI,':r')
% hold on
% plot(x_obs , C_Conc_pred+C_CI,':r');
% 
% [C_del_pred,Cd_CI] = nlpredci(@del_CO2_Model_DOM,x_obs',params,resid,'Covar',Sigma);
% 
% subplot (4,1,2)
% plot (Canal_data (:,1),Canal_data (:,3),'bo');
% ylabel ('delta ^1^3C DIC (permil)')
% xlabel ('Distance downstream (m)');
% hold on
% plot (x_obs,C_del_pred,'r')
% hold on
% plot(x_obs , C_del_pred-Cd_CI,':r')
% hold on
% plot(x_obs , C_del_pred+Cd_CI,':r');
% 
% [M_Conc_pred,M_CI] = nlpredci(@Conc_CH4_Model_DOM,x_obs',params,resid,'Covar',Sigma);
% 
% subplot (4,1,3)
% plot (Canal_data (:,1),Canal_data (:,4),'bo');
% ylabel ('CH_4 Concentration (mM)');
% xlabel ('Distance downstream (m)');
% hold on
% plot (x_obs,M_Conc_pred,'r')
% hold on
% plot(x_obs , M_Conc_pred-M_CI,':r')
% hold on
% plot(x_obs , M_Conc_pred+M_CI,':r');
% 
% [M_del_pred,Md_CI] = nlpredci(@del_CH4_Model_DOM,x_obs',params,resid,'Covar',Sigma);
% 
% subplot (4,1,4)
% plot (Canal_data (:,1),Canal_data (:,5),'bo');
% ylabel ('delta ^1^3C CH4 (permil)')
% xlabel ('Distance downstream (m)');
% hold on
% plot (x_obs,M_del_pred,'r')
% hold on
% plot(x_obs , M_del_pred-Md_CI,':r')
% hold on
% plot(x_obs , M_del_pred+Md_CI,':r');
% legend('Measured','Modeled','95% Confidence Interval');

%% Calculate and plot the model output and confidence interval
[C_Conc_pred_sc,C_CI_sc] = nlpredci(@Conc_CO2_Model_DOM,x_obs',params,resid,'Covar',Sigma);
C_Conc_pred = C_Conc_pred_sc .* (max(Conc_obs_d(:,1)) - min(Conc_obs_d(:,1))) + min(Conc_obs_d(:,1));
C_CI_high = (C_Conc_pred_sc + C_CI_sc) .* (max(Conc_obs_d(:,1)) - min(Conc_obs_d(:,1))) + min(Conc_obs_d(:,1));
C_CI_low = (C_Conc_pred_sc - C_CI_sc) .* (max(Conc_obs_d(:,1)) - min(Conc_obs_d(:,1))) + min(Conc_obs_d(:,1));

figure
subplot (4,1,1)
plot (Canal_data (:,1),Canal_data (:,3),'bo');
ylabel ('DIC Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x_obs,C_Conc_pred,'r')
hold on
plot(x_obs , C_CI_high,':r')
hold on
plot(x_obs , C_CI_low,':r');

[C_del_pred_sc,Cd_CI_sc] = nlpredci(@del_CO2_Model_DOM,x_obs',params,resid,'Covar',Sigma);
C_del_pred = C_del_pred_sc * (max(Conc_obs_d(:,2)) - min(Conc_obs_d(:,2))) + min(Conc_obs_d(:,2));
Cd_CI_high = (C_del_pred_sc + Cd_CI_sc) .* (max(Conc_obs_d(:,2)) - min(Conc_obs_d(:,2))) + min(Conc_obs_d(:,2));
Cd_CI_low = (C_del_pred_sc - Cd_CI_sc) .* (max(Conc_obs_d(:,2)) - min(Conc_obs_d(:,2))) + min(Conc_obs_d(:,2));

subplot (4,1,2)
plot (Canal_data (:,1),Canal_data (:,4),'bo');
ylabel ('delta ^1^3C DIC (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x_obs,C_del_pred,'r')
hold on
plot(x_obs , Cd_CI_high,':r')
hold on
plot(x_obs , Cd_CI_low,':r');

[M_Conc_pred_sc,M_CI_sc] = nlpredci(@Conc_CH4_Model_DOM,x_obs',params,resid,'Covar',Sigma);
M_Conc_pred = M_Conc_pred_sc * (max(Conc_obs_d(:,3)) - min(Conc_obs_d(:,3))) + min(Conc_obs_d(:,3));
M_CI_high = (M_Conc_pred_sc + M_CI_sc) .* (max(Conc_obs_d(:,3)) - min(Conc_obs_d(:,3))) + min(Conc_obs_d(:,3));
M_CI_low = (M_Conc_pred_sc - M_CI_sc) .* (max(Conc_obs_d(:,3)) - min(Conc_obs_d(:,3))) + min(Conc_obs_d(:,3));

subplot (4,1,3)
plot (Canal_data (:,1),Canal_data (:,5),'bo');
ylabel ('CH_4 Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x_obs,M_Conc_pred,'r')
hold on
plot(x_obs , M_CI_high,':r')
hold on
plot(x_obs , M_CI_low,':r');

[M_del_pred_sc,Md_CI_sc] = nlpredci(@del_CH4_Model_DOM,x_obs',params,resid,'Covar',Sigma);
M_del_pred = M_del_pred_sc * (max(Conc_obs_d(:,4)) - min(Conc_obs_d(:,4))) + min(Conc_obs_d(:,4));
Md_CI_high = (M_del_pred_sc + Md_CI_sc) .* (max(Conc_obs_d(:,4)) - min(Conc_obs_d(:,4))) + min(Conc_obs_d(:,4));
Md_CI_low = (M_del_pred_sc - Md_CI_sc) .* (max(Conc_obs_d(:,4)) - min(Conc_obs_d(:,4))) + min(Conc_obs_d(:,4));

subplot (4,1,4)
plot (Canal_data (:,1),Canal_data (:,6),'bo');
ylabel ('delta ^1^3C CH4 (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x_obs,M_del_pred,'r')
hold on
plot(x_obs , Md_CI_high,':r')
hold on
plot(x_obs , Md_CI_low,':r');
legend('Measured','Modeled','95% Confidence Interval');

save ('Prediction_Intervals.mat','C_Conc_pred','C_CI_high','C_CI_low','C_del_pred','Cd_CI_high','Cd_CI_low','M_Conc_pred','M_CI_high','M_CI_low','M_del_pred','Md_CI_high','Md_CI_low');

%% Error metrics

% Convert covariance matrix to correlation matrix
Correlation = corrcov(Sigma); % Does the covariance matrix need to be unscaled somehow?

% Un-scale residuals
residuals_abs = [resid(1:11) .* (max(Conc_obs_d(:,1)) - min(Conc_obs_d(:,1))) ... 
                resid(12:22) .* (max(Conc_obs_d(:,2)) - min(Conc_obs_d(:,2))) ...
                resid(23:33) .* (max(Conc_obs_d(:,3)) - min(Conc_obs_d(:,3))) ...
                resid(34:44) .* (max(Conc_obs_d(:,4)) - min(Conc_obs_d(:,4))) ]; 
% residuals = residuals_w./sqrt(weights) % These are the unweighted (true) residuals

params_US = params./scaling %Unscale the parameters
ci_US (1,:) = ci(:,1)./scaling' %Unscale the 95 % confidence interval
ci_US (2,:) = ci(:,2)./scaling' %Unscale the 95 % confidence interval
std_dev_abs = sqrt(diag(Sigma))./scaling' % Unscaled parameter std devs?
sse_scaled = sum(resid.^2) % Sum of square errors weighted
sse_abs = sum(residuals_abs.^2)
RMSE_abs = sqrt(mean(residuals_abs.^2)) % These are the true RMSE
