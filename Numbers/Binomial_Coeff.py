
# ! In mathematics, the binomial coefficients are 
# ! the positive integers that occur as coefficients in the binomial theorem. 
# ! written as n!/(k!(n-k)!)

# Returns value of binomial coefficient 
def nCk(n, k): 
    C = [0 for i in range(0, k + 2)] 
   
    C[0] = 1; # nC0 is 1 
    for i in range(0, n + 1): 
       
        # Compute next row of pascal triangle 
        # using the previous row 
        for j in range(min(i, k), 0, -1): 
            C[j] = C[j] + C[j-1] 
       
    return C[k] 
   
# * Function to calculate number of triangle 
# * that can be formed
def counTriangles(n, m): 
    return (nCk(n, 3) - nCk(m, 3)) 
   
# driver code 
n = 7
m = 4
print (counTriangles(n, m)) 