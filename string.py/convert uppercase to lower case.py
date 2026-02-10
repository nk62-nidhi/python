str=input("enter uppercase string.....>")
lower_case=""
for i in str:
    if ("A"<=i<="Z"):
        lower_case+= chr(ord(i)+32)
    else:
        lower_case+=i
print(lower_case)



