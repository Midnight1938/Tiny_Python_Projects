
def Fibbonachi(nterms):
    Fibb_Lst = []
    count, n1, n2 = 0, 0, 1
    
    if nterms <= 0:
        print("Positive integers please")
    elif nterms == 1:
            print("Fibbonachi sequence upto {}:".format(nterms))
            print(n1)
    else:
        print("Fibbonachi sequence: ")
        while count < nterms:
            Fibb_Lst.append(n1)
            nth = n1 + n2
            #updating vals
            n1 = n2
            n2 = nth
            count += 1	
        print(Fibb_Lst)

def recur_fibo(n):
    
    if n <= 1:
       return n
    elif n <= 0:
        print("Plese enter a positive integer")
    else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


Rec_fibo_series = []
def main():
    nterms = int(input("How many terms? "))
    
    Fibbonachi(nterms)

    for i in range(0,nterms):
        Rec_fibo_series.append(recur_fibo(i))
    print("Recursive Series:\n", Rec_fibo_series)
	

if __name__ == "__main__":
    main()