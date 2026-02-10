n=int(input("enter a number...>"))
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(chr(64+j),end=" ")
    print()

print("new pattern1")
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(chr(64+j),end=" ")
    print()
print("new pattern2")
for i in range(1,n+1,1):
    for j in range(1,n+1-i,1):
            print(" ",end=" ")
    for k in range(1,i+1,1):
        print(chr(64+k),end=" ")
    print()