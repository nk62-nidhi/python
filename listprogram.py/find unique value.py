list=eval(input("enter list.....>"))
n=len(list)
for i in range(0,n,1):
    flag=False
    for j in range(i+1,n,1):
        if list[i]==list[j]:
            flag=True
flag=False
print(list[i])
    
