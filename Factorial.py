def factorialFun(n):
    if n<0:
        return None
    if n<2:
        return 1
    
    product = 1 
    for i in range(2, n+1):
        product *= i
    return product
    
for n in range(1,6):
    print('{}! has factorial value: {}'.format(n, factorialFun(n)))