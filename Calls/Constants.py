# Constants to call in other python files

R = 8.314  # J/mol*K
Na = 6.022E23  # atoms/mol
kb = 8.6173303E-5  # eV/K(atom?)
Jto_eV = 6.242E18  # joule * this = eV


# Bulk Diffusivity Prefactor
D0 = 8.33E9 * 1E-18  # nm^2/s -> m2/s

# Bulk Vacancy Migration Energy
EmB = 3.61  # eV

# GB/Surface Boundary Layer Thickness
delta = 0.5 * 1E-9  # nm -> m
deltas = 0.5 * 1E-9  # nm -> m

# surfaceEnergy = 19.7 * 1.60218E-19  # J/nm2

# UO2 Density
UO2density = 10.97  # g/cm^3

# UO2 Molar Mass
molar_mass = 270.03  # g/mol

# Molar volume
V_m = (molar_mass / UO2density) * 1E-2 ** 3  # cm^3/mol -> m3/mol

# GB Diffusivity Weight
wgb = 3E7

# Mobility Prefactor
M0 = 2.14E-7  # m4/Js

# Mobility Activation Energy
Q = 290000  # J/mol

# Surface Diffusivity Prefactor
Ds0 = 54  # m2/s

# Surface Vacancy Migration Energy
Em = 108 * 4184  # J/mol - 452 kJ/mol

# GG Model Parameters
Rst = 2.8  # Stereological parameter - 1 is random, 2.8 is from the matlab code from Tonks
dist = 0.2  # lognormal distribution of pores -- stdev(radius) = 0.2*avg_radius
