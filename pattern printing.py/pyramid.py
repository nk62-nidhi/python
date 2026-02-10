n=int(input("enter a number....>"))
ml=n//2+1
nsp=n//2
nst=1
for i in range(1,n+1,1):
    for j in range(1,nsp+1,1):
        print("",end=" ")
    for k in range(1,nst+1,1):
        print(k,end=" ")
    if i<ml:
        nsp-=1
        nst+=1
    else:
        nsp+=1
        nst-=1
    print()