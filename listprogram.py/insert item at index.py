list=eval(input("enter list:..>"))
list.append(0)
print(list)
print(len(list))
pos=int(input("enter index to insert list item..>"))
x=eval(input("enter item...>"))
for i in range(len(list)-1,pos,-1):
    list[i]=list[i-1]
list[pos]=x

print(list)
print(len(list))