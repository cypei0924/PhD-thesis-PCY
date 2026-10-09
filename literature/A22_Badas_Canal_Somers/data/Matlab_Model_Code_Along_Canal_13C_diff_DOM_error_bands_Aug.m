%% Along_Canal_13C_diff
% Lauren Somers
% Oct 7, 2020
% Simulates concentration of 12C- and 13C- CO2 and CH4 along the Badas Canal numerically using differential equations.
%
%THIS SCRIPT TAKES THE STANDARD DEVIATIONS FROM THE 4 PARAMERTER RUN AND
%APPLIES THEM TO THE 6 PARAMETER MODEL...SO IT'S KEEPING ALL 6 PARAMETERS
%AND THE BEST 6 parameter FIT WE HAVE BUT IT'S MAKING THE ERROR BANDS AND BARS
%BASED ON THE 2 PARAMETERS HAVING 0 STANDARD DEVIATION...SO THERE IS NO
%ERROR CONTRIBUTED FROM D AND VI
%
% Wondered if the answers are different enough that this matters? Yes it makes ~3-4% difference to the budget so we're going to code it out
%
% Before running this script run
% Along_Canal_nlinmultifit_DOM_scaled.m to get the sigma from that

%% Generate realizations of the model parameters
% n = 1000 + 1; % number of runs in the monte carlo simulation
n=1;
% % params should be the best  fit parameters from the 6 parameter fit:
% % p =   [-0.0020     0.9693    1.9665    1.6712e-7      1.7688e-08    0.5277];
% params = [0.1080     0.9791    5.0390    2.7808e-6      5.5702e-08    1.8928] .* scaling;
% p = (mvnrnd(params,Sigma, n))./scaling;

% If the 

% Now make the first line the best fit scenario:
%p(1,:) = [0.1080     0.9791    5.0390    2.7808e-6      5.5702e-08    1.8928];
p =   [1.001     0.9687    1.8589    1.1031e-5      4.0615e-07    2.156];

%% Define inputs

% Define function to convert delta to Concentration 12C and 13C - Peedee Belemnite 13C/12C = 0.01118
del_to_ConcC12 = @(delta, Conc_t) (Conc_t)/((delta/1000 +1) * 0.01118 + 1);

% Constants ********************
qgw = 0.0000572; %(incoming groundwater per unit length of canal (m^2/s)
w = 10; % Width of the canal (m)

%Atmospheric equilibrium concentrations:
M_atm = 2.68*10^(-6); % aqueous concentration of CH4 in equilibrium with atmosphere (mM)
delta_M_atm = -47; % isotope ratio for atmospheric methane
M_12atm = del_to_ConcC12 (delta_M_atm,M_atm); % Aqueous concentration of 12CH4 that would be in equilibrium with atmosphere (mM)
M_13atm = M_atm - M_12atm;
C_atm = 0.0176; % aqueous concentration of CO2 in equilibrium with atmosphere (mM)
delta_C_atm = -11; % isotope ratio for atmospheric methane
C_12atm = del_to_ConcC12 (delta_C_atm,C_atm);
C_13atm = C_atm - C_12atm;

% DOC conversion to CO2
C_DOC = 0.283; % Concentration of CO2 produced by degradation of DOC (mM) 
delta_C_DOC = -29.67; % From Gandois, 2014, d13C of DOC
C_12DOC = del_to_ConcC12 (delta_C_DOC,C_DOC);
C_13DOC = C_DOC - C_12DOC;
f=C_13DOC/(C_13DOC + C_12DOC); 

%% Concentration of incoming groundwater 

% Define array of shallow groudnwater concentrations:
% Average shallow gw is at a depth of 0.8325m. See Sept 29 word doc. for more details
shallow_gw(1) = del_to_ConcC12(-16.74,0.982); %C12-DIC
shallow_gw(2) = 0.982 - shallow_gw(1); %13C-DIC
shallow_gw(3) = del_to_ConcC12(-75.9,0.129); % 12C-CH4 
shallow_gw(4) = 0.129 - shallow_gw(3); %13C-CH4

% Deep gw is currently represented by the point directly below the canal *
% Subject to change when we get the CH4 data from the D1 point.
deep_gw(1) = del_to_ConcC12(-0.01,2.80); %C12-DIC
deep_gw(2) = 2.80 - deep_gw(1); %13C-DIC
deep_gw(3) = del_to_ConcC12(-70.09,0.5641); % 12C-CH4 
deep_gw(4) = 0.5641 - deep_gw(3); %13C-CH4

%% Use a loops to run the model over and over in Monte Carlo simulation
% Make the variables we want to get out

C_Conc_pred = zeros (n,25);
C_del_pred = zeros (n,25);
M_Conc_pred = zeros (n,25);
M_del_pred = zeros (n,25);

budget_C = zeros (n,5);
budget_M = zeros (n,4);

%% THE LOOP

for i=1:n
    
deep_coef = p(i,1);  % Proportion of incoming groundwater that comes from below the canal
B = p(i,2); % Isotopic fractionation: methane oxidation reaction rate ratio: (13C rate)/(12C rate) Alison used alpha = 1.01 to 1.02 B=1/alpha
V_mic_coef = p(i,3); % coefficient to calculate V_mic based on V_atm.
V_atm_init = p(i,4);  % initial gas exchange velocity for CH4 METHANE!
V_atm_slope = p(i,5); % (1.2e-05)/500%1.1294e-05/1000; % Slope of V_atm * careful not to make it get too large or go negative
k_DOC = p(i,6);

% Calculate groundwater concentrations
M_12gw = deep_coef *(deep_gw(3)) + (1 - deep_coef)*(shallow_gw(3));  
M_13gw = deep_coef *(deep_gw(4)) + (1 - deep_coef)*(shallow_gw(4)); 
C_12gw = deep_coef *(deep_gw(1)) + (1 - deep_coef)*(shallow_gw(1)); 
C_13gw = deep_coef *(deep_gw(2)) + (1 - deep_coef)*(shallow_gw(2));

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

% Initial instructions for solving the ODE:
% x_init = 1;  % First point to solve for
% x_fin = 5070;  % last point (culvert)
solve_at = [1 10 20 30 40 50 100 200 300 400 500 600 700 800 900 1000 1500 2000 2500 3000 3500 4000 4600 4800 5070];

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

M_12 = Conc (:,1);
M_13 = Conc (:,2);
C_12 = Conc (:,3);
C_13 = Conc (:,4);

% Convert output to delta notation (Peedee Belemnite 13C/12C = 0.01118)
delta_13CH4(i,:) = (((M_13./M_12)/0.01118)-1)*1000;
delta_13CO2(i,:) = (((C_13./C_12)/0.01118)-1)*1000;
% Convert to total concentration
Conc_CH4(i,:) = M_12 + M_13;
Conc_CO2(i,:) = C_12 + C_13;

% and then also do the budget over and over

% Calculate fluxes:
advection_C = ones(length(x),1) * qgw * (C_12gw + C_13gw);
oxidation_C = (V_atm_slope .* x * qgw * 1000 + V_atm_init)'.* V_mic_coef .* (Conc_CH4(i,:)) * w ;
degassing_C = 0.9667 .* (V_atm_slope .* x * qgw * 1000 + V_atm_init)' .* ((Conc_CO2(i,:)) - (C_12atm + C_13atm)) .* w ;
DOC_C = k_DOC .* (V_atm_slope .* x * qgw * 1000 + V_atm_init);
advection_M = ones(length(x),1) * qgw * (M_12gw + M_13gw);
oxidation_M = (V_atm_slope .* x * qgw * 1000 + V_atm_init)' .* (V_mic_coef .* (Conc_CH4(i,:)) .* w) ;
degassing_M = (V_atm_slope .* x * qgw * 1000 + V_atm_init)' .* ((Conc_CH4(i,:)) - (M_12atm + M_13atm)) .* w ;

%Total up the fluxes to make gas budgets
advection_C_t = qgw * x(end) * (C_12gw + C_13gw); % CO2 coming into the canal in mmol/s  
fluvial_C = qgw * x(end) *(Conc_CO2(i,end)); % CO2 leaving the canal with streamflow mmol/s 
oxidation_C_t = trapz(x,oxidation_C);
degassing_C_t = trapz(x,degassing_C);
DOC_C_t = trapz(x,DOC_C);

%CH4:
advection_M_t = qgw * x(end) * (M_12gw + M_13gw); % CH4 coming into the canal in mol/s  
fluvial_M = qgw * x(end) *(Conc_CH4(i,end)); % CH4 leaving the canal with streamflow mol/s 
oxidation_M_t = trapz(x,oxidation_M); % CH4 leaving the canal from oxidation mol/s 
degassing_M_t = trapz(x,degassing_M); % CH4 leaving the canal from degassing mol/s 

% Record the CO2 budget [advection,fluvial,oxidation, degassing, DOC]
budget_C (i,:) = [advection_C_t   fluvial_C  oxidation_C_t  degassing_C_t  DOC_C_t];
% Record the CH4 budget [advection,fluvial,oxidation, degassing, DOC]
budget_M (i,:) = [advection_M_t   fluvial_M  oxidation_M_t  degassing_M_t];

end

%% Calculate the confidence bands on the concentrations lines 2:end are the randoms

C_Conc_pred_low  = prctile(Conc_CO2(2:end,:),2.5);
C_Conc_pred_high = prctile(Conc_CO2(2:end,:),97.5);
C_Conc_mean = Conc_CO2(1,:);

C_del_pred_low  = prctile(delta_13CO2(2:end,:),2.5);
C_del_pred_high = prctile(delta_13CO2(2:end,:),97.5);
C_del_mean = delta_13CO2(1,:);

M_Conc_pred_low  = prctile(Conc_CH4(2:end,:),2.5);
M_Conc_pred_high = prctile(Conc_CH4(2:end,:),97.5);
M_Conc_mean = Conc_CH4(1,:);

M_del_pred_low  = prctile(delta_13CH4(2:end,:),2.5);
M_del_pred_high = prctile(delta_13CH4(2:end,:),97.5);
M_del_mean = delta_13CH4(1,:);

%% Plot the concentrations with confidence bands:

Canal_data = xlsread ('/Users/laurensomers/Documents/Tropical Peatlands Research/Stable Carbon Isotope Analysis/13C-DIC_CH4_Badas_Aug_2020.xlsx',1);
Canal_data_deep = xlsread ('/Users/laurensomers/Documents/Tropical Peatlands Research/Stable Carbon Isotope Analysis/13C-DIC_CH4_Badas_Aug_2020.xlsx',2);
x_obs = Canal_data(:,1);

figure
subplot (2,2,1)
plot (Canal_data_deep (:,1),Canal_data_deep (:,3),'co');
hold on
plot (Canal_data (:,1),Canal_data (:,3),'bo');
ylabel ('DIC Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x,Conc_CO2(1,:),'r')
hold on
plot(x (1:23), C_Conc_pred_high(1:23),':r')
hold on
plot(x (1:23), C_Conc_pred_low(1:23),':r');
xlim([0 5100]);
ylim([0 1.3]);

subplot (2,2,2)
plot (Canal_data_deep (:,1),Canal_data_deep (:,4),'co');
hold on
plot (Canal_data (:,1),Canal_data (:,4),'bo');
ylabel ('delta ^1^3C DIC (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x,delta_13CO2(1,:),'r')
hold on
plot(x(1:23) , C_del_pred_high(1:23),':r')
hold on
plot(x(1:23) , C_del_pred_low(1:23),':r');
xlim([0 5100]);
ylim([-29 -17]);

subplot (2,2,3)
plot (Canal_data_deep (:,1),Canal_data_deep (:,5),'co');
hold on
plot (Canal_data (:,1),Canal_data (:,5),'bo');
ylabel ('CH_4 Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x,Conc_CH4(1,:),'r')
hold on
plot(x(1:23) , M_Conc_pred_high(1:23),':r')
hold on
plot(x(1:23) , M_Conc_pred_low(1:23),':r');
xlim([0 5100]);

subplot (2,2,4)
plot (Canal_data_deep (:,1),Canal_data_deep (:,6),'co');
hold on
plot (Canal_data (:,1),Canal_data (:,6),'bo');
ylabel ('delta ^1^3C CH4 (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x,delta_13CH4(1,:),'r')
hold on
plot(x(1:23) , M_del_pred_high(1:23),':r')
hold on
plot(x(1:23) , M_del_pred_low(1:23),':r');
legend('Measured (shallow)','Measured (deep)','Modeled','95% Confidence Interval');
xlim([0 5100]);
ylim([-74 -47])

%% Get 95% CI bands on the budget

% CO2 [advection,fluvial,oxidation, degassing, DOC]
budget_C_low = (prctile(budget_C(2:end,:),2.5).* [1 -1 1 -1 1]).* 1000;
budget_C_high = (prctile(budget_C(2:end,:),97.5).* [1 -1 1 -1 1]).*1000;
budget_C_mean = (budget_C(1,:) .* [1 -1 1 -1 1]).*1000;

%Methane [advection,fluvial,oxidation, degassing]
budget_M_low = (prctile(budget_M(2:end,:),2.5) .* [1 -1 -1 -1]).*1000;
budget_M_high = (prctile(budget_M(2:end,:),97.5) .* [1 -1 -1 -1]).*1000;
budget_M_mean = (budget_M(1,:).* [1 -1 -1 -1]).*1000;

%Calculate the deltas for the error bars:
budget_C_high_delta = budget_C_high - budget_C_mean;
budget_C_low_delta = budget_C_mean - budget_C_low;

%Calculate the deltas for the error bars:
budget_M_high_delta = budget_M_high - budget_M_mean
budget_M_low_delta = budget_M_mean - budget_M_low;

% What are the percentages of the budget (for the text)
% The best-fit numbers:
C_in = budget_C_mean(1) + budget_C_mean(3) + budget_C_mean(5)
C_out = budget_C_mean(2) + budget_C_mean(4)
M_in = budget_M_mean(1)

% Percentage of CO2 inputs
budget_C_mean (1) / C_in % advection
budget_C_mean (3) / C_in % CH4 oxidation
budget_C_mean (5) / C_in % DOC oxidation
% Percentage of CO2 outputs
budget_C_mean (2) / C_out % fluvial
budget_C_mean(4) / C_out % degassing
% Percentage of CH4 outputs
budget_M_mean (2) /M_in %Fluvial
budget_M_mean (3) /M_in %oxidaion
budget_M_mean (4) /M_in %degasing

% Make a table with budget #s and %:
Source_sink_C = {'CO2 advection';'CO2 fluvial export';'CH4 oxidation';'CO2 degassing';'DOC oxidation'};
Var_names = {'Mean';'low';'high'}
Source_sink_M = {'CH4 advection';'CH4 fluvial export';'CH4 oxidation';'CH4 degassing'};

budget_table_C = table(budget_C_mean',budget_C_low',budget_C_high','RowNames',Source_sink_C,'VariableNames',Var_names)
budget_table_M = table(budget_M_mean',budget_M_low',budget_M_high','RowNames',Source_sink_M,'VariableNames',Var_names)

%% Save the bar chart plotting stuff to be combined with the Jan bars:
% First change name to include Aug:
budget_C_mean_Aug = budget_C_mean;
budget_C_high_delta_Aug = budget_C_high_delta;
budget_C_low_delta_Aug = budget_C_low_delta;
budget_M_mean_Aug = budget_M_mean;
budget_M_high_delta_Aug = budget_M_high_delta;
budget_M_low_delta_Aug = budget_M_low_delta;

C_Conc_pred_low_Aug  = C_Conc_pred_low;
C_Conc_pred_high_Aug = C_Conc_pred_high;
C_del_pred_low_Aug  = C_del_pred_low;
C_del_pred_high_Aug = C_del_pred_high;
M_Conc_pred_low_Aug  = M_Conc_pred_low;
M_Conc_pred_high_Aug = M_Conc_pred_high;
M_del_pred_low_Aug  = M_del_pred_low;
M_del_pred_high_Aug = M_del_pred_high;
x_Aug = x;

C_Conc_mean_Aug = Conc_CO2(1,:);
C_del_mean_Aug = delta_13CO2(1,:);
M_Conc_mean_Aug = Conc_CH4(1,:);
M_del_mean_Aug = delta_13CH4(1,:);

save ('Aug_fit_budget.mat','budget_C_mean_Aug','budget_C_high_delta_Aug','budget_C_low_delta_Aug','budget_M_mean_Aug','budget_M_high_delta_Aug','budget_M_low_delta_Aug',...
    'C_Conc_pred_low_Aug','C_Conc_pred_high_Aug','C_del_pred_low_Aug','C_del_pred_high_Aug','M_Conc_pred_low_Aug','M_Conc_pred_high_Aug','M_del_pred_low_Aug','M_del_pred_high_Aug',...
    'x_Aug','C_Conc_mean_Aug','C_del_mean_Aug','M_Conc_mean_Aug','M_del_mean_Aug')

%% Plot the budget with error bars:

figure
subplot(1,2,1)
cats = categorical({'Advection into canal','Fluvial export','CH_4 oxidation to CO_2','Degassing','DOC oxidation'});
C_chart = bar(cats,budget_C_mean,'Facecolor','flat');
C_chart.CData(1,:) = [0.1 0.3 0.6];
C_chart.CData(2,:) = [0.3 0.8 0.8];
C_chart.CData(3,:) = [0.9 0.5 0.2];
C_chart.CData(4,:) = [0.9 0.2 0.2];
C_chart.CData(5,:) = [0.9 0.8 0.2];
hold on
er = errorbar(cats,budget_C_mean,...
                   budget_C_high_delta,...
                   budget_C_low_delta);    
er.Color = [0 0 0];                            
er.LineStyle = 'none'; 
title('Canal CO_2 Budget');
ylabel('Total input or output (mMol/s)');

subplot(1,2,2)
cats = categorical({'Advection into canal','Fluvial export','CH_4 oxidation to CO_2','Degassing'});
M_chart = bar(cats,budget_M_mean,'Facecolor','flat');
title('Canal CH_4 Budget');
ylabel('Total input or output (mMol/s)');
M_chart.CData(1,:) = [0.1 0.3 0.6];
M_chart.CData(2,:) = [0.3 0.8 0.8];
M_chart.CData(3,:) = [0.9 0.2 0.2];
M_chart.CData(4,:) = [0.9 0.8 0.2];
hold on
er = errorbar(cats,budget_M_mean,...
                   budget_M_high_delta,...
                   budget_M_low_delta);    
er.Color = [0 0 0];                            
er.LineStyle = 'none'; 
