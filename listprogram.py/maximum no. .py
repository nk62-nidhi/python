list=eval(input("enter list:"))
max=1
for i in range(0,len(list),1):
    if max<list[i]:
        max=list[i]
print("maximum is:",max)


min=list[0]
for i in range(0,len(list),1):
    if min>list[i]:
        min=list[i]
print("minimum is:",min)