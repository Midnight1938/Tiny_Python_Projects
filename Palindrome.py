def isPalindrome(s):
    s = s.upper()
    s = "".join(s.split())
    return "Palindrome Detected" if s == s[::-1] else "Not a Palindrome"
 
 
# ! Own input
s = "Repaper"
n = "Tester"

###Intro
print(" #############################", "\n", "##     Palindrome Check    ##", "\n", "#############################")


Asker = int(input("Prebuilt[1] or personal[2]? Choose 1 or 2: "))
if Asker == 1:
    print('Default Input That Is One: ', s)
    print(isPalindrome(s.upper()))
    print('Default Input That Isnt One: ', n)
    print(isPalindrome(n.upper()))
# * Check for own input #
elif Asker == 2:
    string = str(input("Enter your textline: "))
    print("User input is", string, '\n')
    print(isPalindrome(string.upper()))