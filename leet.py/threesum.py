list=eval(input("enter list:"))
triplet=0
for i in range(0,len(list),1):
    for j in range(i+1,len(list),1):
        for k in range(j+1 ,len(list),1):
                if list[i]+list[j]+list[k]==0 :
                    triplet+=1
                    print((list[i],list[j],list[k]))

print("triplet is",triplet)