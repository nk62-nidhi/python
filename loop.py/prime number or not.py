num=int(input("enter a number to check....>"))
if num>1:
    for i in range(2,num,1):
        is_prime=True
        if num%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(f"{num} is prime number")
    else:
        print("not prime number")
else:
    print("invalid number ...")