n=int(input('enter a number.'))
for i in range(1,n+1,1):
    for j in range(n-i,0,-1):
        print(" ",end=' ')
    for k in range(1,i+1,1):
        print("*",end=" ")
    for l in range(1,i,1):
        print("*",end=' ')
    print()