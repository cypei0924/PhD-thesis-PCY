%% Along_Canal_13C_diff
% Lauren Somers
% Oct 7, 2020
% Simulates concentration of 12C- and 13C- CO2 and CH4 along the Badas Canal numerically using differential equations.

%% Define inputs

clear;
clc;

% Define function to convert delta to Concentration 12C and 13C - Peedee Belemnite 13C/12C = 0.01118
del_to_ConcC12 = @(delta, Conc_t) (Conc_t)/((delta/1000 +1) * 0.01118 + 1);

% Unknowns (tuning parameters) ********************
p =   [0.0216     0.9707    2.1506    1.0287e-6      1.9496e-07    1.5756];

deep_coef = p(1);  % Proportion of incoming groundwater that comes from below the canal
B = p(2); % Isotopic fractionation: methane oxidation reaction rate ratio: (13C rate)/(12C rate) Alison used alpha = 1.01 to 1.02 B=1/alpha
V_mic_coef = p(3); % coefficient to calculate V_mic based on V_atm.
V_atm_init = p(4);  % initial gas exchange velocity for CH4 METHANE!
V_atm_slope = p(5); % (1.2e-05)/500%1.1294e-05/1000; % Slope of V_atm * careful not to make it get too large or go negative
k_DOC = p(6);

% Constants ********************
qgw = 0.0000489; %(incoming groundwater per unit length of canal (m^2/s)
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
shallow_gw(1) = del_to_ConcC12(-16.8664,0.5284); %C12-DIC
shallow_gw(2) = 0.5284 - shallow_gw(1); %13C-DIC
shallow_gw(3) = del_to_ConcC12(-68.9517,0.08902); % 12C-CH4 
shallow_gw(4) = 0.08902 - shallow_gw(3); %13C-CH4

% Deep gw is currently represented by the point directly below the canal *
% Subject to change when we get the CH4 data from the D1 point.
deep_gw(1) = del_to_ConcC12(-0.01,2.80); %C12-DIC
deep_gw(2) = 2.80 - deep_gw(1); %13C-DIC
deep_gw(3) = del_to_ConcC12(-70.09,0.5941); % 12C-CH4 
deep_gw(4) = 0.5941 - deep_gw(3); %13C-CH4

% Calculate groundwater concentrations
M_12gw = deep_coef *(deep_gw(3)) + (1 - deep_coef)*(shallow_gw(3));  
M_13gw = deep_coef *(deep_gw(4)) + (1 - deep_coef)*(shallow_gw(4)); 
C_12gw = deep_coef *(deep_gw(1)) + (1 - deep_coef)*(shallow_gw(1)); 
C_13gw = deep_coef *(deep_gw(2)) + (1 - deep_coef)*(shallow_gw(2));

% %% Define and solve the differential equation system: 
% % dC_dx change inconcentration over change in distance is an array with
% % four functions linear increase in V_atm and Vmic k_DOC:  
dC_dx = @ (x,Conc)     [1/(qgw*x) * (qgw * (M_12gw - Conc(1)) -     (V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(1) * w) - ((x*qgw*1000*V_atm_slope + V_atm_init) *          (Conc(1)-M_12atm) * w));...
                        1/(qgw*x) * (qgw * (M_13gw - Conc(2)) - (B * V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(2) * w) - ((x*qgw*1000*V_atm_slope + V_atm_init) *          (Conc(2)-M_13atm) * w));...           
                        1/(qgw*x) * (qgw * (C_12gw - Conc(3)) +      V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(1) * w -  ((x*qgw*1000*V_atm_slope + V_atm_init) * 0.9667 * (Conc(3)-C_12atm) * w) + (x*qgw*1000*V_atm_slope + V_atm_init) * k_DOC * (1-f));...
                        1/(qgw*x) * (qgw * (C_13gw - Conc(4)) +  B * V_mic_coef * (x*qgw*1000*V_atm_slope + V_atm_init) * Conc(2) * w -  ((x*qgw*1000*V_atm_slope + V_atm_init) * 0.9667 * (Conc(4)-C_13atm) * w) + (x*qgw*1000*V_atm_slope + V_atm_init) * k_DOC * f    )];                             
                   
% Initial instructions for solving the ODE:
x_init = 1;  % First point to solve for
x_fin = 5070;  % last point (culvert)

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
[x,Conc] = ode23(dC_dx,[x_init x_fin],y0);

M_12 = Conc (:,1);
M_13 = Conc (:,2);
C_12 = Conc (:,3);
C_13 = Conc (:,4);

% Convert output to delta notation (Peedee Belemnite 13C/12C = 0.01118)
delta_13CH4 = (((M_13./M_12)/0.01118)-1)*1000;
delta_13CO2 = (((C_13./C_12)/0.01118)-1)*1000;
% Convert to total concentration
Conc_CH4 = M_12 + M_13;
Conc_CO2 = C_12 + C_13;


%% Plot the fluxes along the canal and in total

% Calculate fluxes:
advection_C = ones(length(x),1) * qgw * (C_12gw + C_13gw);
oxidation_C = (V_atm_slope .* x * qgw*1000 + V_atm_init).* V_mic_coef .* (M_12 + M_13) * w ;
degassing_C = 0.9667 .* (V_atm_slope .* x * qgw*1000 + V_atm_init) .* ((C_12 + C_13) - (C_12atm + C_13atm)) .* w ;
DOC_C = k_DOC .* (V_atm_slope .* x * qgw*1000 + V_atm_init);
advection_M = ones(length(x),1) * qgw * (M_12gw + M_13gw);
oxidation_M = (V_atm_slope .* x * qgw*1000 + V_atm_init) .* V_mic_coef .* (M_12 + M_13) .* w ;
degassing_M = (V_atm_slope .* x * qgw*1000 + V_atm_init) .* ((M_12 + M_13) - (M_12atm + M_13atm)) .* w ;

figure 
subplot (2,1,1)
plot (x , advection_C, 'Color',[0.1 0.3 0.6],'LineWidth',2,'LineStyle','-.'); 
hold on
plot (x, oxidation_C, 'Color',[0.3 0.8 0.8],'LineWidth',2,'LineStyle','-'); 
hold on
plot (x, -degassing_C,'Color',[0.9 0.2 0.2],'LineWidth',2,'LineStyle','--'); 
hold on
plot (x,  DOC_C,  'Color'    ,[0.9 0.2 0.8],'LineWidth',2,'LineStyle','--');
legend('CO2 incoming with groudwater (Mol/m)','CO2 produced from CH4 oxidation (Mol/m)','CO2 degassing (Mol/m)','CO2 from DOC (Mol/m)')
ylabel('Mol of CO2 per meter length of canal')
xlabel('length along canal (m)')
title('CO2 entering/leaving the canal per unit length')

% + CH4 incoming with groudwater - CH4 oxidized to CO2 - amount of CH4 degassing
subplot (2,1,2)
plot (x , advection_M, 'Color',[0.1 0.3 0.6],'LineWidth',2,'LineStyle','-.'); 
hold on
plot (x, -oxidation_M, 'Color',[0.3 0.8 0.8],'LineWidth',2,'LineStyle','-'); 
hold on
plot (x, -degassing_M,'Color',[0.9 0.2 0.2],'LineWidth',2,'LineStyle','--'); 
ylabel('mMol of CH4 per meter length of canal')
xlabel('length along canal (m)')
legend ('CH4 incoming with groudwater (mMol/m)','CH4 oxidized to CO2 (mMol/m)','CH4 degassing (mMol/m)')
title('CH4 entering/leaving the canal per unit length')

% Sum oxidation, degassing, groundwater inputs and canal export:
% CO2:
advection_C_t = qgw * x(end) * (C_12gw + C_13gw); % CO2 coming into the canal in mmol/s  
fluvial_C = qgw * x(end) *(C_12(end)+C_13(end)); % CO2 leaving the canal with streamflow mmol/s 
oxidation_C_t = trapz(x,oxidation_C);
degassing_C_t = trapz(x,degassing_C);
DOC_C_t = trapz(x,DOC_C);

%CH4:
advection_M_t = qgw * x(end) * (M_12gw + M_13gw); % CH4 coming into the canal in mol/s  
fluvial_M = qgw * x(end) *(M_12(end)+M_13(end)); % CH4 leaving the canal with streamflow mol/s 
oxidation_M_t = trapz(x,oxidation_M); % CH4 leaving the canal from oxidation mol/s 
degassing_M_t = trapz(x,degassing_M); % CH4 leaving the canal from degassing mol/s 

% Print out this stuff to make it easier to put in paper
degassing_flux = degassing_M_t * 16 * 3600*24*365 * (1/(x(end)*w)) % in g of CH4/m^2/yr
degassing_flux_units = degassing_M_t * 16 * 3600 * 24 * (10000/(x(end)*w)) % in g of CH4/ha/d

% Percentage of CO2 inputs
advection_C_t / (advection_C_t + oxidation_C_t + DOC_C_t)
DOC_C_t / (advection_C_t + oxidation_C_t + DOC_C_t)
oxidation_C_t / (advection_C_t + oxidation_C_t + DOC_C_t)
% Percentage of CO2 outputs
degassing_C_t/(degassing_C_t + fluvial_C)
fluvial_C/(degassing_C_t + fluvial_C)
% Percentage of CH4 outputs
fluvial_M/advection_M_t
oxidation_M_t/advection_M_t
degassing_M_t/advection_M_t

%% Plot with error bars:
figure
subplot(1,2,1)
cats = categorical({'Advection into canal','Fluvial export','CH_4 oxidation to CO_2','Degassing','DOC oxidation'});
C_chart = bar(cats,[advection_C_t , -fluvial_C , oxidation_C_t , -degassing_C_t, DOC_C_t],'Facecolor','flat');
C_chart = bar(cats,[advection_C_t , -fluvial_C , oxidation_C_t , -degassing_C_t, DOC_C_t],'Facecolor','flat');
C_chart.CData(1,:) = [0.1 0.3 0.6];
C_chart.CData(2,:) = [0.3 0.8 0.8];
C_chart.CData(3,:) = [0.9 0.5 0.2];
C_chart.CData(4,:) = [0.9 0.2 0.2];
C_chart.CData(5,:) = [0.9 0.8 0.2];
title('Canal CO_2 Budget');
% er = errorbar(cats,[advection_C_t , -fluvial_C , oxidation_C_t , -degassing_C_t, DOC_C_t],...
%                    [(advection_C_t_sd) , fluvial_C_t_sd , oxidation_C_t_sd , degassing_C_t_sd, DOC_C_t_sd],...
%                    [(advection_C_t_sd) , fluvial_C_t_sd , oxidation_C_t_sd , degassing_C_t_sd, DOC_C_t_sd]);    
% er.Color = [0 0 0];                            
% er.LineStyle = 'none'; 
% title('Canal CO_2 Budget');
% ylabel('Total input or output (Mol/s)');

subplot(1,2,2)
cats = categorical({'Advection into canal','Fluvial export','CH_4 oxidation to CO_2','Degassing'});
M_chart = bar(cats,[advection_M_t , -fluvial_M , -oxidation_M_t , -degassing_M_t],'Facecolor','flat');
title('Canal CH_4 Budget');
ylabel('Total input or output (Mol/s)');
M_chart.CData(1,:) = [0.1 0.3 0.6];
M_chart.CData(2,:) = [0.3 0.8 0.8];
M_chart.CData(3,:) = [0.9 0.2 0.2];
M_chart.CData(4,:) = [0.9 0.8 0.2];
% hold on
% er = errorbar(cats,[advection_M_t , -fluvial_M , -oxidation_M_t , -degassing_M_t],...
%                    [advection_M_t_sd , fluvial_M_t_sd , oxidation_M_t_sd , degassing_M_t_sd],...
%                    [advection_M_t_sd , fluvial_M_t_sd , oxidation_M_t_sd , degassing_M_t_sd]);    
% er.Color = [0 0 0];                            
% er.LineStyle = 'none'; 


%% Plot simulated and observed concentrations and delta 13C

% Load measured profiles
Canal_data = xlsread ('/Users/laurensomers/Documents/Tropical Peatlands Research/Stable Carbon Isotope Analysis/13C-DIC_CH4-Jan_2020.xlsx',7);

% Plot
figure
subplot (4,1,1)
plot (Canal_data (:,1),Canal_data (:,2),'ob');
ylabel ('DIC Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x,Conc_CO2,'-r');
% hold on
% plot(Canal_data (2:12,1),C_CI_high,':r', Canal_data (2:12,1),C_CI_low,':r');
legend ('Measured','Modeled');

subplot (4,1,2)
plot (Canal_data (:,1),Canal_data (:,3),'ob');
ylabel ('delta ^1^3C DIC (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x,delta_13CO2,'-r');
% hold on
% plot(Canal_data (2:12,1),Cd_CI_high,':r', Canal_data (2:12,1),Cd_CI_low,':r');
%legend ('Measured','Modeled'); %,'Groundwater');

subplot (4,1,3)
plot (Canal_data (:,1),Canal_data (:,4),'ob');
ylabel ('CH4 Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x,Conc_CH4,'-r');
% hold on
% plot(Canal_data (2:12,1),M_CI_high,':r', Canal_data (2:12,1),M_CI_low,':r');
%legend ('Measured','Modeled','95% Confidence Interval');

subplot (4,1,4)
plot (Canal_data (:,1),Canal_data (:,5),'ob');
ylabel ('delta ^1^3C CH4 (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x,delta_13CH4,'-r');
% hold on
% plot(Canal_data (2:12,1),Md_CI_high,':r', Canal_data (2:12,1),Md_CI_low,':r');
%legend ('Measured','Modeled');%'Groundwater');

