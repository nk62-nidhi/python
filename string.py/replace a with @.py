str=input("enter string.....>")
result=""
for i in str:
    if i=="a":
        result+="@"
    else:
        result+=i
print(result)