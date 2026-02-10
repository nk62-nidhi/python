#set is mutable but it's elements are immutable
collection=set()
collection.add(1)
collection.add(2)
collection.add(3)
print(collection)
collection1=set()
for i in range(1,11,1):
    if i%2==0:
        collection1.add(i)

#print(collection.remove(2))
#print(collection)
print(collection1)
#print(collection.clear())
#print(collection.pop())
print(collection.union(collection1))
print(collection.intersection(collection1))