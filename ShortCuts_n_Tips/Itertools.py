import itertools

lst1= [1,2,3,4,5,6,7,8]
print(list(itertools.accumulate(lst1))) # Like Fractal

lst2 = ['A','B','C','D','E']
print(list(itertools.chain(lst1,lst2)))

Show = [1,0,0,1,1]
print(list(itertools.compress(lst2,Show)))