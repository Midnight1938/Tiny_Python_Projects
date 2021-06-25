BASE_Fract = [1, 1]

def factorialFn(n):
    if n < len(BASE_Fract):
        return BASE_Fract[n]

    last = len(BASE_Fract) - 1
    total = BASE_Fract[last]
    for i in range(last + 1, n + 1):
        total *= i
        BASE_Fract.append(total)
    return total

def Combinn(n,r):
    return factorialFn(n)/(factorialFn(r)*(factorialFn(n-r)))

def main():
    # TODO Human Imput: n = int(input("Total number of objects: "))
    # TODO Human Imput: r = int(input("Number of choosing objects: "))
    n = 17
    r = 2

    print('''{}! has factorial value: {}
And the Combination value is {}'''.format(n, factorialFn(n), Combinn(n,r)))

if __name__ == "__main__":
    main()