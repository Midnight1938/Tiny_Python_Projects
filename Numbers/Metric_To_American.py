def l100kmtompg(liters):
    Ltr_per_Gal = 3.785411784
    Km_per_Mi = 1.6093472187
    return((100/Km_per_Mi) / (liters/Ltr_per_Gal))


def mpgtol100km(miles):
    Gal_per_Ltr = 0.2641720524
    Mi_per_Km = 0.6213699495
    return((100*Gal_per_Ltr) / (miles*Mi_per_Km))


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))