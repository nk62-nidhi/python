num=int(input("enter a number....>"))
a,b=0,1
print("fibonacci of 1 is {}".format(a))
print("fibonacci of 2 is {}".format(b))
for i in range(3,num+1,1):
    c=a+b
    a=b
    b=c
    print("fibonacci of {} is {}".format(i,c))