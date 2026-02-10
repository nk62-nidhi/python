list1=[0,3,1]
list2=[2,5,4]
list=list1+list2
print(list)
for i in range(0,len(list),1):
    for j in range(i+1,len(list),1):
        if list[i]>list[j]:
            swap=list[i]
            list[i]=list[j]
            list[j]=swap
print(list)