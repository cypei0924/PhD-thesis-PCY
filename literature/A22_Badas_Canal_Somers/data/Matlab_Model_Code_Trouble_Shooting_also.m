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

% Simple concentration:
M_Conc_Jan = M_atm/(1+V_mic_coef)
C_Conc_Jan = C_atm + (V_mic_coef*M_atm)/(0.9667*(1+V_mic_coef)) + k_DOC/(0.9667*w)

% Now back to more complicated
M_12_inf_Jan = M_12atm/(V_mic_coef+1)
M_13_inf_Jan = M_13atm/((V_mic_coef*B)+1)
M_del_inf_Jan = (((M_13_inf_Jan/M_12_inf_Jan)/0.01118)-1)*1000

% Convert downstream condition to concentration and delta notation (Peedee Belemnite 13C/12C = 0.01118)
M_del_inf_Jan = (((M_13_inf_Jan/M_12_inf_Jan)/0.01118)-1)*1000;
C_del_inf_Jan = (((C_13_inf_Jan/C_12_inf_Jan)/0.01118)-1)*1000;
% Convert to total concentration
M_Conc_inf_Jan = M_12_inf_Jan + M_13_inf_Jan;
C_Conc_inf_Jan = C_12_inf_Jan + C_13_inf_Jan;




% Why do the fitted models trend towards different numbers? Identical
% equations
% Jan:
1/(qgw*x) * (qgw * (M_13gw - Conc(2)) - (B * V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(2) * w) - ((x*qgw*1000*V_atm_slope + V_atm_init) *          (Conc(2)-M_13atm) * w));... 
% Aug:
1/(qgw*x) * (qgw * (M_13gw - Conc(2)) - (B * V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(2) * w) - ((x*qgw*1000*V_atm_slope + V_atm_init) *          (Conc(2)-M_13atm) * w));...     

% KMic is the same in Jan and Aug. M atm is the same in january and
% august...right?



% Take the limit of the function another way:
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
