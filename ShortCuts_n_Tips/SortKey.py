lst = [[1, 2], [-2, 3], [-3, 4], [-4, 5], [-5, 6]]

lst.sort()
print(lst, "\n")

lst.sort(key=lambda x: x[1])  # lambda is a one lien anon function, we sort by the second element
print(lst)

lst.sort(key=lambda x: x[0] + x[1]) #
print(lst)

#* Like:
def sortFn(x):
    return x[1]
lst.sort(key=sortFn)
print("\n",lst)