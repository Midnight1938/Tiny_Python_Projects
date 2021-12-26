
##***Values***##
Kg_in_ton = round(0.0011023113109244, 3)
Kg_in_lbs = 2.20462

##***Conversions***##
def  kgtoton(kg):
    return round(kg*Kg_in_ton, 2)

def tontokg(ton) :
    return round(ton/Kg_in_ton, 2)

def  kgtolbs (kg):
    return round(kg*Kg_in_lbs, 2)

def  lbstokg(pnd):
    return round(pnd/Kg_in_lbs, 2)