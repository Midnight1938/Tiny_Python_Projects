# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
def file_Writer(name, num):
    file = open('GFG.txt', 'a')
    data = f"\n{name}:\t{num}"
    file.write(data)
    file.close()

N_Rec = int(input("Enter the amount of records: "))
i = 1
while i <= N_Rec:
    Name = str(input("Enter Name: "))
    try:
       Num = int(input("Enter Number: "))
    except ValueError:
        print("Enter numbers only")
    file_Writer(Name, Num)
    i+=i
    print("\nWritten\n")

