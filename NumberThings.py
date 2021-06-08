##Fibbothing

nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

##Validity
if nterms <= 0:
	print("Positive integers please")
elif nterms == 1:
		print("Fibbonachi sequence upto {}:".format(nterms))
		print(n1)
else:
	print("Fibbonachi sequence: ")
	while count < nterms:
		print(n1)
		nth = n1 + n2
		#updating vals
		n1 = n2
		n2 = nth
		count += 1	

###---n natural number sum--###
number = int(input("Please enter number: "))

total = 0

for value in range(1, number+1):
	total = total+value

print("The sum of numbers from 0 to {0} is {1}".format(number, total))


###---Factorial--###
number = int(input("Please enter number: "))

factorial = 1

if number<0:
	print("No factorial for negatives")
elif number == 0:
	print("The factorial of 0 is 1")
else:
	for i in range(1, number+1):
		factorial = factorial*i
	print("The factorial of {0} is {1}".format(number, factorial))


###---Factorial--###
def Sum_Of_Digits(Number):
    Sum = 0
    while(Number > 0):
        Reminder = Number % 10
			print(Reminder)
        Sum = Sum + Reminder
			print(Sum)        
        Number = Number //10
    return Sum

Number = int(input("Please Enter any Number: "))
Sum = Sum_Of_Digits(Number)
print("\n Sum of the digits of Given Number = %d" %Sum)