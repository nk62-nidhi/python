list=eval(input("enter list..>"))
for i in range(0,len(list)-1,1):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            swap=list[i]
            list[i]=list[j]
            list[j]=swap

print(list)