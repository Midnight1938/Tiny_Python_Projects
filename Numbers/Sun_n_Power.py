
def Sum_N(N):
    answer = (N*(N+1))/2
    print(answer)

def Power_Madgik(a,b):
    return a**b

def main():
    # TODO: Human Inpt:: X = int(input("Enter a Number: "))
    # TODO: Human Inpt:: Y = int(input("Enter Power: "))
    X = 17
    Y = 2
    print("\n{} to the power {} is {}".format(X,Y,Power_Madgik(X,Y)))

if __name__ == "__main__":
    main()