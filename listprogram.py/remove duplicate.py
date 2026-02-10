list=[1,2,3,1,2,3,4]
unique=[]
for i in list:
    found=False
    for j in unique:
        if i==j:
            found=True
            break
    if not found:
        unique.append(i)

print("original list:",list)
print("without duplicate:",unique)

