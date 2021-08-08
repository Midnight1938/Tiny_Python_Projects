x = [[1,2],3]*5
print(x)

##* Inline/Ternatry Conditions
x = 1 if 2>3 else 0
print(bool(x), "\n")

#* IN C++ 
#! x = 2>3 ? 1:0 

##* ZIP
names = ['Jim', 'Jam', 'Jane', 'June', 'Jin']
ages = [23,25,22,30,12]
eyeColour = ['Blue', 'Green', 'Yellow', 'Brown', 'Honey']

print(list(zip(names, ages, eyeColour)))
##? In case of extra elements, it simply skips the extra values

for name, age, eye in zip(names, ages, eyeColour):
    if age>20:
        print(f"{name}: {eye} eyes")
print("\n")

## Zip with Ternary
for name, age, eye in zip(names, ages, eyeColour):
    print(name, ":\tis eligible") if age>20 else print(name, ":\tis inelegible")