tups = (1, 2, 3, 4)
lst = [2, 3, 4, "What"]
stringss = "This is a string"
diction = {1: "a", 2: "b", 3: "c"}

Cordinates = [4, 5]

##* Multiple Assignments
width, height = 40, 60
print(f"Current Width and height: {width, height}")
width, height = height, width
print(f"Width and Height Switched: {width, height}")

##* Siple way to assign variables
##! Remember that
z, x, c, v = tups
print(z, x, c, v)
z, x, c, v = lst
print(z, x, c, v)

x, y = Cordinates
print(f"{[x,y]}")

a, b = diction.values()
c, d = diction.keys()
print(f"{a,b} are the values, {c,d} the kays")
