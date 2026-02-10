list=[]
for i in range(1,11,1):
    list.append(i**2)
i=0
while i!=10 :
    print(f"{i} postion {list[i]}")
    i+=1
tuple=tuple(list)
x=int(input("enter number..>"))
i=1
while i!=len(tuple):
    if x==tuple[i]:
        print(f"{x} is present at {i}")
        i+=1
    else:
        print("searching.....")
        i+=1

   
    
    
    

