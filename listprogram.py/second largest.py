list=eval(input("enter list:"))
smax=0
max=0
for i in range(0,len(list),1):
    if max<list[i]:
        max=list[i]
    

for i in range(0,len(list),1):
    if smax<list[i] and smax<max and max!=list[i]:
        smax=list[i]
print("second max",smax)


