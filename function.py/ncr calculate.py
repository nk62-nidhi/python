n=int(input("enter the value of n....>"))
def fact(x):
    fact=1
    for i in range(1,x+1,1):
        fact*=i
    return fact
def ncr(i,j):
    ncr=fact(i)//(fact(j)*fact(i-j))
    return ncr
for i in range(0,n+1,1):
    for j in range(0,i+1,1):
        combination =ncr(i,j)
        print(combination,end=" ")
    print()





