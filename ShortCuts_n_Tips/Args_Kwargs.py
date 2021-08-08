def func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def func2(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)


args = [1, 3, 4]
kwargs = {"arg2": 2, "arg1": 1, "arg3": 3}

#* USing *Args ie Positional Argumennts
func1(args[0], args[1], args[2])
func1(*args)
print("\n")
func2(*kwargs)
func2(**kwargs)  ##* Sending in Values via keys. Similar to:
func2(arg2=2, arg1=1, arg3=3)
