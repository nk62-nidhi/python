num=int(input("enter a number"))
for i in range(1,num+1,1):
    a=1
    for j  in range(1,i+1,1):
        print(a,end=" ") 
        a+=2
    print()