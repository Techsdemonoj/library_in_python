# #Constrant in scipy: scipy is more focused on 
# scientific implimentations, it provides may built in scientific
# constrants: helpful in data science 


# Printing the constant value of PI:
from scipy import constants
print(constants.pi) # 3.141592653589793


# Constrants unit: all list of unit under the constrant can be seen with dir() fuction
from scipy import constants
print(dir(constants))



# MOST USED UNIT CATEGORIES: Metric,Binary,Mass, Angle,Time,Length,
#                  Presuure,Volume,Speed,Temperature,Energy,Power.

# Metric (SI) Prefixes:
from scipy import constants
print("yotta = ",constants.yotta)  # 1e+24
print("zetta = ",constants.zetta)  # 1e+21
print("exa = ",constants.exa)      # 1e+18
print("peta = ",constants.peta)    # 1000000000000000.0
print("tera = ",constants.tera)    # 1000000000000.0
print("giga = ",constants.giga)    # 1000000000.0
print("mega = ",constants.mega)    # 1000000.0
print("kilo = ",constants.kilo)    # 1000.0
print("hecto = ",constants.hecto)  # 100.0
print("deka = ",constants.deka)    # 10.0
print("deci = ",constants.deci)    # 0.1
print("centi = ",constants.centi)  # 0.01
print("milli = ",constants.milli)  # 0.001
print("micro = ",constants.micro)  # 1e-06
print("nano = ",constants.nano)    # 1e-09
print("pico = ",constants.pico)    # 1e-12
print("femto = ",constants.femto)  # 1e-15
print("atto = ",constants.atto)    # 1e-18
print("zepto = ",constants.zepto)  # 1e-21


# Binary Prefixes:
from scipy import constants
print("kibi = ",constants.kibi) # 1024
print("mebi = ",constants.mebi) # 1048576
print("gibi = ",constants.gibi) # 1073741824
print("tebi = ",constants.tebi) # 1099511627776
print("pebi = ",constants.pebi) # 1125899906842624
print("exbi = ",constants.exbi) # 1152921504606846976
print("zebi = ",constants.zebi) # 1180591620717411303424
print("yobi = ",constants.yobi) # 1208925819614629174706176


# Mass Prefixes:
from scipy import constants
print("gram = ",constants.gram)                     # 0.001
print("metric_ton = ",constants.metric_ton)         # 1000.0
print("grain = ",constants.grain)                   # 6.479891e-05
print("lb = ",constants.lb)                         # 0.45359236999999997
print("pound = ",constants.pound)                   # 0.45359236999999997
print("oz = ",constants.oz)                         # 0.028349523124999998
print("ounce = ",constants.ounce)                   # 0.028349523124999998
print("stone = ",constants.stone)                   # 6.3502931799999995
print("long_ton = ",constants.long_ton)             # 1016.0469088
print("short_ton = ",constants.short_ton)           # 907.1847399999999
print("troy_ounce = ",constants.troy_ounce)         # 0.031103476799999998
print("troy_pound = ",constants.troy_pound)         # 0.37324172159999996
print("carat = ",constants.carat)                   # 0.0002
print("atomic_mass = ",constants.atomic_mass)       # 1.6605390666e-27
print("m_u = ",constants.m_u)                       # 1.6605390666e-27
print("u = ",constants.u)                           # 1.6605390666e-27


# Angle Prefixes:
from scipy import constants
print("degree = ",constants.degree)             # 0.017453292519943295
print("arcmin = ",constants.arcmin)             # 0.0002908882086657216
print("arcminute = ",constants.arcminute)       # 0.0002908882086657216
print("arcsec = ",constants.arcsec)             # 4.84813681109536e-06
print("arcsecond = ",constants.arcsecond)       # 4.84813681109536e-06


# Time Prefixes:
from scipy import constants
print("minute = ",constants.minute)             # 60.0
print("hour = ",constants.hour)                 # 3600.0
print("day = ",constants.day)                   # 86400.0
print("week = ",constants.week)                 # 604800.0
print("year = ",constants.year)                 # 31536000.0
print("Julian_year = ",constants.Julian_year)   # 31557600.0
print("light_year = ",constants.light_year)     # 9460730472580800.0


# Length Prefixes (change in meter) :
from scipy import constants
print("inch = ",constants.inch)                             # 0.0254
print("foot = ",constants.foot)                             # 0.30479999999999996
print("yard = ",constants.yard)                             # 0.9143999999999999
print("mile = ",constants.mile)                             # 1609.3439999999998       
print("mil = ",constants.mil)                               # 2.5399999999999997e-05
print("pt = ",constants.pt)                                 # 0.00035277777777777776
print("point = ",constants.point)                           # 0.00035277777777777776
print("survey_foot = ",constants.survey_foot)               # 0.3048006096012192
print("survey_mile = ",constants.survey_mile)               # 1609.3472186944373
print("nautical_mile = ",constants.nautical_mile)           # 1852.0
print("fermi = ",constants.fermi)                           # 1e-15
print("angstrom = ",constants.angstrom)                     # 1e-10
print("micron = ",constants.micron)                         # 1e-06
print("au = ",constants.au)                                 # 149597870700.0
print("astronomical_unit = ",constants.astronomical_unit)   # 149597870700.0
print("light_year = ",constants.light_year)                 # 9460730472580800.0
print("parsec = ",constants.parsec)                         # 3.085677581491367e+16


# Presuure Prefixes (change in pascal) :
from scipy import constants
print("atm = ",constants.atm)               # 101325.0
print("atmosphere = ",constants.atmosphere) # 101325.0
print("bar = ",constants.bar)               # 100000.0
print("torr = ",constants.torr)             # 133.32236842105263
print("mmHg = ",constants.mmHg)             # 133.32236842105263
print("psi = ",constants.psi)               # 6894.757293168361


# Volume Prefixes(change in cubic meter) :
from scipy import constants
print("liter = ",constants.liter)                       # 0.001
print("litre = ",constants.litre)                       # 0.001
print("gallon = ",constants.gallon)                     # 0.0037854117839999997
print("gallon_US = ",constants.gallon_US)               # 0.0037854117839999997
print("gallon_imp = ",constants.gallon_imp)             # 0.00454609
print("fluid_ounce = ",constants.fluid_ounce)           # 2.9573529562499998e-05
print("fluid_ounce_imp = ",constants.fluid_ounce_imp)   # 2.84130625e-05
print("fluid_ounce_US = ",constants.fluid_ounce_US)     # 2.9573529562499998e-05
print("barrel = ",constants.barrel)                     # 0.15898729492799998
print("bbl = ",constants.bbl)                           # 0.15898729492799998


# Spped Prefixes (metre per second):
from scipy import constants
print("kmh = ",constants.kmh)                           # 0.2777777777777778
print("mph = ",constants.mph)                           # 0.44703999999999994
print("mach = ",constants.mach)                         # 340.5   
print("speed_of_sound = ",constants.speed_of_sound)     # 340.5
print("knot = ",constants.knot)                         # 0.5144444444444445


#Temperature Prefixes(chnage in kelvin) :
from scipy import constants
print("zero_Celsius = ",constants.zero_Celsius)             # 273.15
print("degree_Fahrenheit = ",constants.degree_Fahrenheit)   # 0.5555555555555556


# Energy Prefixes (Change in jouls) :
from scipy import constants
print("eV = ",constants.eV)                        #1.602176634e-19
print("electron_volt = ",constants.electron_volt)  #1.602176634e-19
print("calorie = ",constants.calorie)              #4.184
print("calorie_th = ",constants.calorie_th)        #4.184
print("calorie_IT = ",constants.calorie_IT)        #4.1868
print("erg = ",constants.erg)                      #1e-07
print("Btu = ",constants.Btu)                      #1055.05585262
print("Btu_th = ",constants.Btu_th)                #1054.3502644888888
print("Btu_IT = ",constants.Btu_IT)                #1055.05585262
print("ton_TNT = ",constants.ton_TNT)              #4184000000.0


#Power Prefixes (change in Newton) :
from scipy import constants
print("dyn = ",constants.dyn)                       # 1e-05
print("dyne = ",constants.dyne)                     # 1e-05
print("lbf = ",constants.lbf)                       # 4.4482216152605
print("pound_force = ",constants.pound_force)       # 4.4482216152605
print("kgf = ",constants.kgf)                       # 9.80665
print("kilogram_force = ",constants.kilogram_force) # 9.80665















































