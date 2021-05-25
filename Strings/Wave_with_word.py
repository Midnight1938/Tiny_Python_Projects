# ! Wave your word
word = input("Enter the word: ")
# enter word
print(word)
for i in range(1, len(word)+1):
    print(word[:i])
for i in range(1, len(word)+1):
    print(word[:-i])
