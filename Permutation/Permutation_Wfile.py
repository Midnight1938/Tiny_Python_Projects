from itertools import permutations
f = open('Permutation.txt', 'a')
List = []
e = 0
string = ''

##---ENTRIES---##
Range = int(input("Enter how many numbers there are: "))
span = int(input("How many numbers should it span? "))

for i in range(Range):
    num = str(input("Enter the numbers: "))
    string += num

print(string)
perms = [''.join(p) for p in permutations(string, span)]

perms.sort()
print("The list is: \n", perms)
print("\n There are {} total possibilities".format(len(perms)))