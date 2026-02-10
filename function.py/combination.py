   
n=int(input("enter the value of n....>"))
r=int(input("enter the value of r:..>"))
def fact(x):
    fact=1
    for i in range(1,x+1,1):
        fact=fact*i
    return fact

ncr=fact(n)/(fact(r)*fact(n-r))
print(ncr)
