s1=input("Enter First String:")
s2=input("Enter Second String:")
output=''
i,j=0,0
while i<len(s1) or j<len(s2):
        if i<len(s1):
            output=output+s1[i]
            i+=1 
j=0          
while j<len(s2):
    if j<len(s2):
        output=output+s2[j]
        j+=1       
print(output)

print("by using for loop")
out1=""
for i in s1:
    out1+=i
for j in s2:
    out1+=j

print(out1)