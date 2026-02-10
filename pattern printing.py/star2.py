num=int(input("enter a number"))
for i in range(1,num+1,1):
    for j in range(num+1-i,0,-1):
        print(j,end=" ")
    print()
    

print("new pattern staring from 1 to n")
for i in range(num,0,-1):
    for j in range(1,i+1,1):
        print(j,end="")
    print()