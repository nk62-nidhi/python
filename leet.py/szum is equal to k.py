arr=eval(input("enter arrays...>"))
k=int(input("enter a number...>"))
count=0
for i in range(1,len(arr)+1,1):
        if arr[i]+arr[i+1]==k:
            count+=1
print(count)