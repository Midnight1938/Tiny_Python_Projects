import Len_N_Mas_Conv.Mass.Mass_Conv as MasCnv
import Len_N_Mas_Conv.Length.Len_Conv as LenCnv

Taken_mil = 30
Taken_km = LenCnv.mil2km(Taken_mil)
Taken_in = 20
Taken_ft = LenCnv.in2ft(Taken_in)

print("Values of Miles in Km is ",LenCnv.Mile_in_Km)
print("Values of Feet in inches is ",LenCnv.Ft_in_In)

print(f"""\n{Taken_mil} Miles in Km is {LenCnv.mil2km(Taken_mil)}
{Taken_km} Km in Miles is {LenCnv.km2mile(Taken_km)}

{Taken_in} inches in Feet is {LenCnv.in2ft(Taken_in)}
{Taken_ft} feet in Inches is {LenCnv.ft2in(Taken_ft)}""")


Taken_Kg = 30
Taken_Ton = MasCnv.kgtoton(Taken_Kg)
Taken_Pnd = MasCnv.kgtolbs(Taken_Kg)

print(f"""\n1 Kg is {MasCnv.Kg_in_ton} Ton and {MasCnv.Kg_in_lbs} lbs.

{Taken_Kg} is {MasCnv.kgtolbs(Taken_Kg)} lbs, and {MasCnv.kgtoton(Taken_Kg)}

{Taken_Ton} is {MasCnv.tontokg(Taken_Ton)} Kg
{Taken_Pnd} is {MasCnv.lbstokg(Taken_Pnd)} Kg""")
