def Count(str):
    # ** Types of characters #
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
        elif str[i].islower():
            lower += 1
        elif str[i].isdigit():
            number += 1
        else:
            special += 1
    print('Upper case letters:', upper)
    print('Lower case letters:', lower)
    print('Number:', number)
    print('Special characters:', special)
    print('Alphabets:', upper+lower)


# * Example input #
str = "Thi5isMet35ing@codes"

# Driver Code
Asker = int(input("Prebuilt[1] or personal[2]? Choose 1 or 2: "))
if Asker == 1:
    print('default input is', str)
    Count(str)
# * Check for own input #
elif Asker == 2:
    str = input("Enter your textline: ")
    print("User input is", str)
    Count(str)

else:
    print("Had to choose one of the given ones")
