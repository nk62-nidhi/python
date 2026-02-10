str=input("enter string...>")
upper_count=0
lower_count=0
for i in str:
    if ("A"<=i<="Z"):
        upper_count+=1
    elif ("a"<=i<="z"):
        lower_count+=1
print("toatal lower count is",lower_count)
print("toatal upper count is",upper_count)