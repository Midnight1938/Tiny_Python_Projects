Secret_Word, Special_Hide = str(input("Secret Word: ")), str(input("Potential place: "))
print('Hiden place: ', Special_Hide)
print('Secret word: ',Secret_Word)
Special_Hide = list(Special_Hide.upper())
Secret_Word = list(Secret_Word.upper()) 

result =  all(elem in Special_Hide for elem in Secret_Word)
if result:
    print('\n', "Yes, Secret_Word is hidden")    
else :
    print('\n', "No, Secret_Word is not here")