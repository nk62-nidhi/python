list=eval(input("enter list:...>"))
n=int(input("enter index to delete ..>"))
list2=[]
for i in range(0,len(list),1):
    if i!=n:
        list2.append(list[i])
list=list2 
print(list2)