
##***Values***##
Mile_in_Km = 1.609344
Ft_in_In = 12


##***Conversions***##
def mil2km(mile):
    return mile*Mile_in_Km

def km2mile(km):
    return round(km/Mile_in_Km, 3)

def in2ft(inch):
    return inch*Ft_in_In

def ft2in(ft):
    return round(ft/Ft_in_In, 3)