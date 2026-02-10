list=[1,2,1,3,5,4]
largest=1
for i in range(0,len(list),1):
    if largest<list[i]:
        largest=list[i]

print(largest)