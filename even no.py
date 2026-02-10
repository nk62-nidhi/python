num= int(input("enter a range.....>"))
for i in range(2,num+1,2):
    print(i)
print("by using if function print odd number")
for i in range(1,num+1,1):
    if i%2!=0:
        print(i)