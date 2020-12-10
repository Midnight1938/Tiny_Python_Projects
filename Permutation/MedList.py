MedList = []
Numbers = int(input("Enter the amount of numbers you have: "))
i = 0
while i <= Numbers:
    Nummer = int(input("Enter Number: "))
    MedList.append(Nummer)
    i += 1
    
MedList.sort()
mid = len(MedList) // 2
res = (MedList[mid] + MedList[~mid]) / 2
print("Median of MedList is {}".format(res))
    