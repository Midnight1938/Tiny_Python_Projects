def Count(stru):
    # ** Types of characters #
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(stru)):
        if stru[i].isupper():
            upper += 1
        elif stru[i].islower():
            lower += 1
        elif stru[i].isdigit():
            number += 1
        else:
            special += 1
    print('Upper case letters:', upper)
    print('Lower case letters:', lower)
    print('Number:', number)
    print('Special characters:', special)
    print('Alphabets:', upper+lower)


# * Example input #
string = "Thi5isMet35ing@codes"

# Driver Code
Asker = int(input("Prebuilt[1] or personal[2]? Choose 1 or 2: "))
if Asker == 1:
    print('\nDefault input is', string)
    Count(string)
# * Check for own input #
elif Asker == 2:
    string = str(input("Enter your textline: "))
    print("\nUser input is", string)
    Count(string)

else:
    print("Had to choose one of the given ones")