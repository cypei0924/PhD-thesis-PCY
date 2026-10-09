function [M_12gw, M_13gw, C_12gw, C_13gw] = GW_exp_fit(PT1_30W, deep_coef)
%GW_EXP_FIT Use an exponential function to describe the groundwater
%signature

% Resolution of interpolation: (how many points do you want to calculate
% the interpolation and beta function
res = 1000;
x_min = 0;
x_max = 5.7;

% define X
X = x_min : ((x_max-x_min)/res) : x_max;

% Get the beta distribution for the parameters:
y = exp(deep_coef.* X);
% calc area under curve:
area = trapz(X,y);
% Normalize the function so the area under the curve = 1
y_norm = y./area; 
% Check:
%trapz(X, y_norm)

% % Load observed data 
% PT1_30W_Jan = xlsread('/Users/laurensomers/Documents/Tropical Peatlands Research/Stable Carbon Isotope Analysis/13C-DIC_CH4-Jan_2020.xlsx',1);
% PT1_30W_Aug = xlsread('/Users/laurensomers/Documents/Tropical Peatlands Research/Stable Carbon Isotope Analysis/13C-DIC_CH4_Badas_Aug_2020',3);
% 
% % Fix issues with JAN field data
% PT1_30W_Jan(9:10,:) = []; % Remove duplicate values at d=3m
% PT1_30W_Jan = cat(1,PT1_30W_Jan (1,:),PT1_30W_Jan); % Duplicate data for most shallow point
% PT1_30W_Jan (1,1) = 0.1; % Make the depth of the most shallow point 0.1
% PT1_30W_Jan = cat(1, [0   0.0176   -11   2.68*10^(-6)    -47] ,PT1_30W_Jan);   % Make top point at d = 0 in equilibrium with atmosphere
% 
% % Fix issues with AUG field data
% PT1_30W_Aug = cat(1,PT1_30W_Aug , PT1_30W_Jan (10:15,:)); % Combine shallow pts from August and deep points from Jan
% PT1_30W_Aug = cat(1, [0   0.0176   -11   2.68*10^(-6)    -47] ,PT1_30W_Aug);   % Make top point at d = 0 in equilibrium with atmosphere
% 
% Convert to concentrations of 12C, 13C, 12M and 13M
del_to_ConcC12 = @(delta, Conc_t) (Conc_t)./((delta/1000 +1) * 0.01118 + 1);

% Convert concentrations and delta notation to concentrations
iso_30W (:,1) = PT1_30W (:,1); %Depth
iso_30W (:,2) = del_to_ConcC12 (PT1_30W(:,3),PT1_30W(:,2)); % C12
iso_30W (:,3) = PT1_30W(:,2) - iso_30W (:,2); % C13
iso_30W (:,4) = del_to_ConcC12 (PT1_30W(:,5),PT1_30W(:,4)); % M12
iso_30W (:,5) = PT1_30W(:,4) - iso_30W (:,4); % M13

% Perform interpolation on observed data:
int_30W (:,1) = [x_min:(x_max-x_min)/res:x_max]'; % Where to perform interpolation:
int_30W (:,2) = interp1 (iso_30W(:,1), iso_30W(:,2),int_30W(:,1));
int_30W (:,3) = interp1 (iso_30W(:,1), iso_30W(:,3),int_30W(:,1));
int_30W (:,4) = interp1 (iso_30W(:,1), iso_30W(:,4),int_30W(:,1));
int_30W (:,5) = interp1 (iso_30W(:,1), iso_30W(:,5),int_30W(:,1));

%multiply the beta distriution by the interpolation and take the area under the curve

% Calculate representative concentrations for groundwater:
C_12gw = trapz (X, (y_norm' .* int_30W (:,2)));
C_13gw = trapz (X, (y_norm' .* int_30W (:,3)));
M_12gw = trapz (X, (y_norm' .* int_30W (:,4)));
M_13gw = trapz (X, (y_norm' .* int_30W (:,5)));

end

