from typing import ChainMap


x = []

for i in range(20 + 1):
    x.append(i)

print(x)
##? A Better way:
x = [i for i in range(20 + 1)]
print(x)
x = [i for i in range(20 + 1) if i % 2 == 0]  #? Even only
print("\n",x)

x= [[3 for _ in range(4)] for _ in range(8)] ##?? We can use an underscore if we dont need an iterator
print("\n",x)

x = (i for i in "Hello there")
print("\n",tuple(x))

Word = "Hello I am making stuff"
x = {char: Word.count(char) for char in set(Word)} #? Character frequency in a sentence
print("\n",x)