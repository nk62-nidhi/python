str=input("enter a string.....>")
for i in range(0,len(str),1):
    if i==0 or i==len(str)-1:
        print(str[i])