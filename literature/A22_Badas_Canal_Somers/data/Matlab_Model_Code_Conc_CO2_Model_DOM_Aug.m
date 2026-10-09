function Conc_CO2 = Conc_CO2_Model_DOM_Aug (p, x)

Conc = Along_Canal_Model_DOM_Aug (p,x);
Conc_CO2 = Conc(:,1)';

end

