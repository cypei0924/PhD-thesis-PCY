%% Along_Canal_13C_diff
% Lauren Somers
% Oct 7, 2020
% Simulates concentration of 12C- and 13C- CO2 and CH4 along the Badas Canal numerically using differential equations.
%
% Before running this script run
% Along_Canal_nlinmultifit_DOM_scaled.m to get the sigma from that

%% Load the model results and budgets 

% January 2020
load('/Users/laurensomers/Documents/Tropical Peatlands Research/Stable Carbon Isotope Analysis/Along_Canal/Jan_fit_budget.mat')
Canal_data_Jan = xlsread ('/Users/laurensomers/Documents/Tropical Peatlands Research/Stable Carbon Isotope Analysis/13C-DIC_CH4-Jan_2020.xlsx',7);

% August 2020
load('/Users/laurensomers/Documents/Tropical Peatlands Research/Stable Carbon Isotope Analysis/Along_Canal/Aug_2020/Aug_fit_budget.mat')
Canal_data_Aug = xlsread ('/Users/laurensomers/Documents/Tropical Peatlands Research/Stable Carbon Isotope Analysis/13C-DIC_CH4_Badas_Aug_2020.xlsx',1);
Canal_data_deep_Aug = xlsread ('/Users/laurensomers/Documents/Tropical Peatlands Research/Stable Carbon Isotope Analysis/13C-DIC_CH4_Badas_Aug_2020.xlsx',2);
x_obs_Aug = Canal_data_Aug(:,1);

%% Plot the concentrations with confidence bands:
figure

%Jan
subplot (4,2,1)
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,2),'bo');
ylabel ('DIC Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x_Jan,C_Conc_mean_Jan,'r')
hold on
plot(x_Jan (10:23), C_Conc_pred_high_Jan(10:23),':r')
hold on
plot(x_Jan (10:23), C_Conc_pred_low_Jan(10:23),':r');
xlim([0 5100]);
ylim([0 1.3]);
title('January 2020');

subplot (4,2,3)
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,3),'bo');
ylabel ('delta ^1^3C DIC (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x_Jan,C_del_mean_Jan,'r')
hold on
plot(x_Jan(10:23) , C_del_pred_high_Jan(10:23),':r')
hold on
plot(x_Jan(10:23) , C_del_pred_low_Jan(10:23),':r');
xlim([0 5100]);
ylim([-29 -17]);

subplot (4,2,5)
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,4),'bo');
ylabel ('CH_4 Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x_Jan,M_Conc_mean_Jan,'r')
hold on
plot(x_Jan(10:23) , M_Conc_pred_high_Jan(10:23),':r')
hold on
plot(x_Jan(10:23) , M_Conc_pred_low_Jan(10:23),':r');
xlim([0 5100]);
ylim([0 0.12]);

subplot (4,2,7)
plot (Canal_data_Jan (:,1),Canal_data_Jan (:,5),'bo');
ylabel ('delta ^1^3C CH4 (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x_Jan,M_del_mean_Jan,'r')
hold on
plot(x_Jan(10:23) , M_del_pred_high_Jan(10:23),':r')
hold on
plot(x_Jan(10:23) , M_del_pred_low_Jan(10:23),':r');
xlim([0 5100]);
ylim([-74 -40])

% Aug
subplot (4,2,2)
plot (Canal_data_deep_Aug (:,1),Canal_data_deep_Aug (:,3),'co');
hold on
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,3),'bo');
ylabel ('DIC Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x_Aug,C_Conc_mean_Aug,'r')
hold on
plot(x_Aug (1:23), C_Conc_pred_high_Aug(1:23),':r')
hold on
plot(x_Aug (1:23), C_Conc_pred_low_Aug(1:23),':r');
xlim([0 5100]);
ylim([0 1.3]);
legend('Measured (deep)','Measured (shallow)','Modeled','95% Confidence Interval');
title('August 2020')

subplot (4,2,4)
plot (Canal_data_deep_Aug (:,1),Canal_data_deep_Aug (:,4),'co');
hold on
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,4),'bo');
ylabel ('delta ^1^3C DIC (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x_Aug,C_del_mean_Aug,'r')
hold on
plot(x_Aug(1:23) , C_del_pred_high_Aug(1:23),':r')
hold on
plot(x_Aug(1:23) , C_del_pred_low_Aug(1:23),':r');
xlim([0 5100]);
ylim([-29 -17]);

subplot (4,2,6)
plot (Canal_data_deep_Aug (:,1),Canal_data_deep_Aug (:,5),'co');
hold on
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,5),'bo');
ylabel ('CH_4 Concentration (mM)');
xlabel ('Distance downstream (m)');
hold on
plot (x_Aug,M_Conc_mean_Aug,'r')
hold on
plot(x_Aug(1:23) , M_Conc_pred_high_Aug(1:23),':r')
hold on
plot(x_Aug(1:23) , M_Conc_pred_low_Aug(1:23),':r');
xlim([0 5100]);
ylim([0 0.12]);

subplot (4,2,8)
plot (Canal_data_deep_Aug (:,1),Canal_data_deep_Aug (:,6),'co');
hold on
plot (Canal_data_Aug (:,1),Canal_data_Aug (:,6),'bo');
ylabel ('delta ^1^3C CH4 (permil)')
xlabel ('Distance downstream (m)');
hold on
plot (x_Aug,M_del_mean_Aug,'r')
hold on
plot(x_Aug(1:23) , M_del_pred_high_Aug(1:23),':r')
hold on
plot(x_Aug(1:23) , M_del_pred_low_Aug(1:23),':r');
xlim([0 5100]);
ylim([-74 -40])


%% Plot the budget with error bars:

figure
subplot(1,2,1)            
Jan_num = [0.85  1.85  2.85  3.85  4.85]
Aug_num = [1.15  2.13  3.15  4.15  5.15]
C_chart_Jan = bar(Jan_num,budget_C_mean_Jan, 0.3)
hold on
C_Chart_Aug = bar(Aug_num,budget_C_mean_Aug,0.3)     
hold on
er_Jan = errorbar(Jan_num,  budget_C_mean_Jan,  budget_C_high_delta_Jan ,  budget_C_low_delta_Jan);  
er_Jan.Color = [0 0 0];                            
er_Jan.LineStyle = 'none'; 
hold on
er_Aug = errorbar(Aug_num,  budget_C_mean_Aug,  budget_C_high_delta_Aug ,  budget_C_low_delta_Aug);       
er_Aug.Color = [0 0 0];                            
er_Aug.LineStyle = 'none';           
xticks([1 2 3 4 5]);
cats_C = categorical({'Advection into canal','Fluvial export','CH_4 oxidation to CO_2','Degassing','DOC oxidation'});          
xticklabels(cats_C);
xtickangle(45)
title('CO2 budget')

subplot(1,2,2)            
Jan_num = [0.85  1.85  2.85  3.85]
Aug_num = [1.15  2.13  3.15  4.15]
M_chart_Jan = bar(Jan_num,budget_M_mean_Jan, 0.3)
hold on
M_Chart_Aug = bar(Aug_num,budget_M_mean_Aug,0.3)     
hold on
er_Jan = errorbar(Jan_num,  budget_M_mean_Jan,  budget_M_high_delta_Jan ,  budget_M_low_delta_Jan);  
er_Jan.Color = [0 0 0];                            
er_Jan.LineStyle = 'none'; 
hold on
er_Aug = errorbar(Aug_num,  budget_M_mean_Aug,  budget_M_high_delta_Aug ,  budget_M_low_delta_Aug);       
er_Aug.Color = [0 0 0];                            
er_Aug.LineStyle = 'none'; 
cats_M = categorical({'Advection into canal','Fluvial export','CH_4 oxidation to CO_2','Degassing'});          
xticks([1 2 3 4]);
xticklabels(cats_M);
xtickangle(45)
title('CH4 budget')