str=input("enter string...>")
print(len(str))
str1=""
for i in str:
    if i!=" ":
        str1+=i
str=str1
print(str)
print(len(str))