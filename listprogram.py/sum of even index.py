list=eval(input("enetr list:"))
print( "length is",len(list))
sum_even=0
sum_odd=0
for i in range(0,len(list),1):
    print(list[i])
    if list[i]%2==0:
        sum_even+=list[i]
    else:
        sum_odd+=list[i]
    resultant=sum_even+sum_odd
print("sum of even index is :",sum_even)
print("sum of odd index is:",sum_odd)
print("resultant is:",resultant)
