list=eval(input("enter list..>"))
x=eval(input("enter value to count item...>"))
n=eval(input("enter item to search index...>"))
m=eval(input("enter item to remove..>"))
print(list.count(x))
print("length is ",len(list))
print(list.index(n))
list.remove(m)
print(list)
list.append(10)
print(list)
list.insert(1,222)
print(list)
list2=[]
list2.extend(list)
print("list2=",list2)
print(list2.pop())
print(list2)



