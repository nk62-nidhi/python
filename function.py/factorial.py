n=int(input("enter a number"))
def fact(x):
    fact=1
    for i in range(1,x+1,1):
        fact*=i
    print(fact)
    return fact
factorial=fact(n)
print("factorial is ",factorial)