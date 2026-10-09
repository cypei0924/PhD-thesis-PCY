function del_CO2 = del_CO2_Model_DOM_Aug (p, x)

Conc = Along_Canal_Model_DOM_Aug (p,x);
del_CO2 = Conc(:,2)';

end
