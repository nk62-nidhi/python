str=input('enter your name.....>')
print(len(str))
count=0
for i in str:
    count+=1
print("length of string is ..",count)
count=0
for i in str:
    if i=="$":
        count+=1
print("occurence is...",count)
print(str.count("$"))