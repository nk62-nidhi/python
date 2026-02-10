n=int(input("enter a number.."))
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(chr((n+1-i)+64),end=" ")
    print()


print("second rectangle..")
n=int(input("enter a number.."))
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(chr((n+1-j)+64),end=" ")
    print()


