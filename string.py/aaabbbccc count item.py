str=input("enter string...>")
print(len(str))
out=""
count=1
for i in range(len(str)-1):
    if  str[i]==str[i+1]:
        count+=1
    else:
        out+=str[i] + f"{count}"
        count=1

if count!=0:
    out+=str[i] + f"{count}"
print(out)


        