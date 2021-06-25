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