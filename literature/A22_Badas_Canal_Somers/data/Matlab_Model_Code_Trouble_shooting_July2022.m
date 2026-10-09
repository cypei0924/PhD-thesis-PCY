

solve_at = [0.01 1 2 3 4 5 10 20 30 40 50 100 200 300 457 500 600 700 800 900 1000 1500 2000 2500 3000 3500 4000 4600 4800 5000 6000 7000 8000 9000 9500 9800 100000 110000 120000 130000 140000 150000 160000 170000 180000 190000 200000 220000 230000 240000 250000 260000 270000 280000 290000 300000 400000 500000 1000000 10000000];
solve_at = [0.01:100:1000000];


%M_atm = 2.68*10^(-6); % aqueous concentration of CH4 in equilibrium with atmosphere (mM)
M_atm = 2.68*10^(-3); % aqueous concentration of CH4 in equilibrium with atmosphere (mM)
delta_M_atm = -47; % isotope ratio for atmospheric methane
M_12atm = del_to_ConcC12 (delta_M_atm,M_atm); % Aqueous concentration of 12CH4 that would be in equilibrium with atmosphere (mM)
M_13atm = M_atm - M_12atm;


% %%%%%%%%% January %%%%%%%%%%%%
deep_coef = params_US(1);  % Proportion of incoming groundwater that comes from below the canal
B = params_US(2); % Isotopic fractionation: methane oxidation reaction rate ratio: (13C rate)/(12C rate) Alison used alpha = 1.01 to 1.02 B=1/alpha
V_mic_coef = params_US(3); % coefficient to calculate V_mic based on V_atm.
V_atm_init = params_US(4);  % initial gas exchange velocity for CH4 METHANE!
V_atm_slope = params_US(5); % (1.2e-05)/500%1.1294e-05/1000; % Slope of V_atm * careful not to make it get too large or go negative
k_DOC = params_US(6);

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
M_12_Jan = Conc (:,1);
M_13_Jan = Conc (:,2);
C_12_Jan = Conc (:,3);
C_13_Jan = Conc (:,4);

% Convert output to delta notation (Peedee Belemnite 13C/12C = 0.01118)
M_del_pred_Jan = (((M_13_Jan./M_12_Jan)/0.01118)-1)*1000
C_del_pred_Jan = (((C_13_Jan./C_12_Jan)/0.01118)-1)*1000
% Convert to total concentration
M_Conc_pred_Jan = M_12_Jan + M_13_Jan
C_Conc_pred_Jan = C_12_Jan + C_13_Jan

R=(V_mic_coef+1)/(B*V_mic_coef+1)
R=(B*V_mic_coef+1)/(V_mic_coef+1)
del = ((R/0.01118)-1)*1000

% %%%%%%%%% August %%%%%%%%%%%%

deep_coef = params_US(7);  % Proportion of incoming groundwater that comes from below the canal
B = params_US(2); % Isotopic fractionation: methane oxidation reaction rate ratio: (13C rate)/(12C rate) Alison used alpha = 1.01 to 1.02 B=1/alpha
V_mic_coef = params_US(3); % coefficient to calculate V_mic based on V_atm.
V_atm_init = params_US(4);  % initial gas exchange velocity for CH4 METHANE!
V_atm_slope = params_US(5); % (1.2e-05)/500%1.1294e-05/1000; % Slope of V_atm * careful not to make it get too large or go negative
k_DOC = params_US(8);

qgw = q(2);

PT1_30W = PT1_30W_Aug;

% Calculate groundwater concentrations

[M_12gw, M_13gw, C_12gw, C_13gw] = GW_exp_fit (PT1_30W_Aug, deep_coef);


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
M_12_Aug = Conc (:,1);
M_13_Aug = Conc (:,2);
C_12_Aug = Conc (:,3);
C_13_Aug = Conc (:,4);

% Convert output to delta notation (Peedee Belemnite 13C/12C = 0.01118)
M_del_pred_Aug = (((M_13_Aug./M_12_Aug)/0.01118)-1)*1000;
C_del_pred_Aug = (((C_13_Aug./C_12_Aug)/0.01118)-1)*1000;
% Convert to total concentration
M_Conc_pred_Aug = M_12_Aug + M_13_Aug;
C_Conc_pred_Aug = C_12_Aug + C_13_Aug;

figure
subplot(4,1,1)
plot(solve_at, M_Conc_pred_Jan, solve_at, M_Conc_pred_Aug)

subplot(4,1,2)
plot(solve_at,M_del_pred_Jan,solve_at,M_del_pred_Aug)

subplot(4,1,3)
plot(solve_at,M_12_Jan,solve_at,M_12_Aug)

subplot(4,1,4)
plot(solve_at,M_13_Jan,solve_at,M_13_Aug)