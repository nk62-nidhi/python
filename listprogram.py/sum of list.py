list=eval(input("enter list:"))
sum=0
product=1
for i in range(0,len(list),1):
    product*=list[i]
    sum+=list[i]
print("product is",product)
print("sum of list is",sum)