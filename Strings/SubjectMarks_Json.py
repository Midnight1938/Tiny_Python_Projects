import json
Stud_Nm = input("Enter your name: ")

Sub_Name_lst = []
Sub_Marks_lst = []

Num_Sub = int(input('Enter the number of subjects you have: '))
i = 0
while i in range(Num_Sub):
    Sub_Name = str(input('Enter name of subject: '))
    Sub_Name_lst.append(Sub_Name)
    Sub_Mrks = float(input('Enter marks for {0}'.format(Sub_Name)))
    Sub_Marks_lst.append(Sub_Mrks)
    i += 1

Stud_Dict = dict(zip(Sub_Name_lst, Sub_Marks_lst))

print('For {0} --> \n'.format(Stud_Nm))
for key, value in Stud_Dict.items():
    print(key, ' : ', value)

print('\n pretty printing: ')
print(json.dumps(Stud_Dict, indent=2))
