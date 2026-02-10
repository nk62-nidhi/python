str=input("enter string.....>")
lower_case=""
for i in str:
    if ("a"<=i<="z"):
        lower_case+= chr(ord(i)-32)
    else:
        lower_case+=i
print(lower_case)