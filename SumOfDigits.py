def Sum_Of_Digits(Number):
    Sum = 0
    while(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        Number = Number //10
    return Sum


Number = int(input("Please Enter any Number: "))
Sum = Sum_Of_Digits(Number)
print("\n Sum of the digits of Given Number = %d" %Sum)

str = "Amazing World of Python"
print(str.find("y"))