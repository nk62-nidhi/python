num=int(input("enter a number... to print factorial...>"))
fact=1
for i in range (1,num+1,1):
    fact*=i
print("factorial of {} is = {}".format(num,fact))