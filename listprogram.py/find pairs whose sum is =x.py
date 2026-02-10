list=eval(input("enter list:"))
x=eval(input("enter a value..>"))
total_pair=0
for i in range(0,len(list),1):
    for j in range(i+1,len(list),1):
        if list[i]+list[j]==x  :
            total_pair+=1
            print((list[i],list[j]))
print("total pairs=",total_pair)