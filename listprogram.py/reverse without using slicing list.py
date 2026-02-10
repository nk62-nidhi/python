list=eval(input("enter list:"))
rev_list=[]
for i  in range(len(list)-1,-1,-1):
    rev_list.append(list[i])

print(rev_list)

list.reverse()
print(list)
x=len(list)
for i in range(x//2):
    swap=list[i]
    list[i] =list[x-i-1]
    list[x-i-1]=swap

print(list)

