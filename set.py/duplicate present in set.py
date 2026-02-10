set=eval(input("enter set...>"))
l=[]
for i in set:
    if i!=l:
        l.append(i)
set=l
print(set)
