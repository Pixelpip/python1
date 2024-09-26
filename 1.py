
def fact(n):
    if(n==1):
        return 1
    return fact(n-1)*n


n=int(input("enter the number to find factorial of:"))


print(fact(n))