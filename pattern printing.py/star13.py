n=int(input("enter a number.."))
for i in range(n,0,-1):
    for j in range(1,i+1,1):
        print(n+1-j,end=" ")
    print()