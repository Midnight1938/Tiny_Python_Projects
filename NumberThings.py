
#%%
###---n natural number sum--###
number = int(input("Please enter number: "))

total = 0

for value in range(1, number+1):
	total = total+value

print("The sum of numbers from 0 to {0} is {1}".format(number, total))