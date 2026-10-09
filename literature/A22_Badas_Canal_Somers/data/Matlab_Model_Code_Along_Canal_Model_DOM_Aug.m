function Conc = Along_Canal_Model_DOM_Aug (p, X)

% Load the constants so the function can use them
load('Along_canal_inputs.mat');

% Fitting parameters:
% Scale parameters
p = p./scaling;

% deep_coef_Jan ; B ; V_mic ; V_atm_init ; V_atm_slope ; k_DOC ; deep_coef_Aug
deep_coef = p(7);
B = p(2);
V_mic_coef = p(3);
V_atm_init = p(4);
V_atm_slope = p(5);
k_DOC = p(8);

qgw = qgw(2);

% Calculate f, the fraction of DOC that is 13DOC
f=C_13DOC/(C_13DOC + C_12DOC); 

% Calculate groundwater concentrations
[M_12gw, M_13gw, C_12gw, C_13gw] = GW_exp_fit (PT1_30W_Aug, deep_coef);

% M_12gw = deep_coef *(deep_gw(3,2)) + (1 - deep_coef)*(shallow_gw(3,2));  
% M_13gw = deep_coef *(deep_gw(4,2)) + (1 - deep_coef)*(shallow_gw(4,2)); 
% C_12gw = deep_coef *(deep_gw(1,2)) + (1 - deep_coef)*(shallow_gw(1,2)); 
% C_13gw = deep_coef *(deep_gw(2,2)) + (1 - deep_coef)*(shallow_gw(2,2));

%Define the differential equation with increasing V_atm, V_mic and k_DOM
dC_dx = @ (x,Concen)    [1/(qgw*x) * (qgw * (M_12gw - Concen(1)) -     (V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Concen(1) * w) - ((x*qgw*1000*V_atm_slope + V_atm_init) *          (Concen(1)-M_12atm) * w));...
                         1/(qgw*x) * (qgw * (M_13gw - Concen(2)) - (B * V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Concen(2) * w) - ((x*qgw*1000*V_atm_slope + V_atm_init) *          (Concen(2)-M_13atm) * w));...           
                         1/(qgw*x) * (qgw * (C_12gw - Concen(3)) +      V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Concen(1) * w -  ((x*qgw*1000*V_atm_slope + V_atm_init) * 0.9667 * (Concen(3)-C_12atm) * w) + (x*qgw*1000*V_atm_slope + V_atm_init) * k_DOC * (1-f));...
                         1/(qgw*x) * (qgw * (C_13gw - Concen(4)) +  B * V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Concen(2) * w -  ((x*qgw*1000*V_atm_slope + V_atm_init) * 0.9667 * (Concen(4)-C_13atm) * w) + (x*qgw*1000*V_atm_slope + V_atm_init) * k_DOC * f    )];                             

% dC_dx = @ (x,Concen)    [1/(qgw*x) * (qgw * (M_12gw - Concen(1)) -     (V_mic_coef * (x*V_atm_slope + V_atm_init) * Concen(1) * w) - ((x*V_atm_slope + V_atm_init) *          (Concen(1)-M_12atm) * w));...
%                          1/(qgw*x) * (qgw * (M_13gw - Concen(2)) - (B * V_mic_coef * (x*V_atm_slope + V_atm_init) * Concen(2) * w) - ((x*V_atm_slope + V_atm_init) *          (Concen(2)-M_13atm) * w));...           
%                          1/(qgw*x) * (qgw * (C_12gw - Concen(3)) +      V_mic_coef * (x*V_atm_slope + V_atm_init) * Concen(1) * w -  ((x*V_atm_slope + V_atm_init) * 0.9667 * (Concen(3)-C_12atm) * w) + (x*V_atm_slope + V_atm_init) * k_DOC * (1-f));...
%                          1/(qgw*x) * (qgw * (C_13gw - Concen(4)) +  B * V_mic_coef * (x*V_atm_slope + V_atm_init) * Concen(2) * w -  ((x*V_atm_slope + V_atm_init) * 0.9667 * (Concen(4)-C_13atm) * w) + (x*V_atm_slope + V_atm_init) * k_DOC * f    )];                             
                         
% Calculate the inital values
tp = qgw*M_12gw+V_atm_init*w*M_12atm;
bt = qgw+V_atm_init*V_mic_coef*w+V_atm_init*w;
M_12_init = tp/bt;

%Calculate initial values for M_13
tp = qgw*M_13gw+V_atm_init*w*M_13atm;
bt = qgw+V_atm_init*V_mic_coef*B*w+V_atm_init*w;
M_13_init = tp/bt;

%Calculate initial values for C_12
% tp = qgw*C_12gw+0.9667*V_atm_init*w*C_12atm;
% bt = qgw-V_mic_coef*V_atm_init*w + 0.9667*V_atm_init*w;
tp = (qgw * C_12gw) + (V_mic_coef * M_12_init * w * V_atm_init) + (0.9667*V_atm_init*C_12atm*w) + (k_DOC*V_atm_init*(1-f));
bt = qgw + 0.9667*V_atm_init*w;
C_12_init = tp/bt;

%Calculate initial values for C_13
% tp = qgw*C_13gw+0.9667*V_atm_init*w*C_13atm;
% bt = qgw-V_mic_coef*B*V_atm_init*w + 0.9667*V_atm_init*w;
tp = (qgw * C_13gw) + (V_mic_coef* B * M_13_init * w * V_atm_init) + (0.9667*V_atm_init*C_13atm*w) + (k_DOC*V_atm_init*f);
bt = qgw + 0.9667*V_atm_init*w;
C_13_init = tp/bt;

y0 = [M_12_init; M_13_init; C_12_init; C_13_init];

% Set values of x to solve differential equation at
x_calc_init = [0.01;1;2;3;4;5;10;20;30;40;50;100;200;300];
%x_calc = [x_calc_init ; x_obs];
X = X';
x_calc = [x_calc_init ; X(2:end)];

% Solve the ODE at certain values of x:
[~,Conc_a] = ode45(dC_dx , x_calc , y0); %[x,y] = ode23(odefun,xspan,y0)
%[Conc_a] = ode45(dC_dx , x_calc , y0); %[x,y] = ode23(odefun,xspan,y0)

Conc_a([2:length(x_calc_init)],:) = []; % Delete the spin-up
%Conc_a = Conc_a ((length(x_calc_init)+1):end,:); 

%% Convert back to Conc and delta (comment out if not using)
M_12 = Conc_a (:,1);
M_13 = Conc_a (:,2);
C_12 = Conc_a (:,3);
C_13 = Conc_a (:,4);

% Convert output to delta notation (Peedee Belemnite 13C/12C = 0.01118)
delta_13CH4 = (((M_13./M_12)/0.01118)-1)*1000;
delta_13CO2 = (((C_13./C_12)/0.01118)-1)*1000;
% Convert to total concentration
Conc_CH4 = M_12 + M_13;
Conc_CO2 = C_12 + C_13;

%Re-scale the simulated concentrations using the observed conentrations
Conc_CO2_sc = (Conc_CO2 - min(Conc_obs_d_Aug(:,1)))/(max(Conc_obs_d_Aug(:,1)) - min(Conc_obs_d_Aug(:,1)));
delta_13CO2_sc = (delta_13CO2 - min(Conc_obs_d_Aug(:,2)))/(max(Conc_obs_d_Aug(:,2)) - min(Conc_obs_d_Aug(:,2)));
Conc_CH4_sc = (Conc_CH4 - min(Conc_obs_d_Aug(:,3)))/(max(Conc_obs_d_Aug(:,3)) - min(Conc_obs_d_Aug(:,3)));
delta_13CH4_sc = (delta_13CH4 - min(Conc_obs_d_Aug(:,4)))/(max(Conc_obs_d_Aug(:,4)) - min(Conc_obs_d_Aug(:,4)));

%Report back:
Conc = [Conc_CO2_sc delta_13CO2_sc Conc_CH4_sc delta_13CH4_sc];

%Report back:
%Conc = [Conc_CO2 delta_13CO2 Conc_CH4 delta_13CH4];

% Don't let V_atm_init be negative:
if p(4)<0
    Conc = ones(size(Conc));
end 

end