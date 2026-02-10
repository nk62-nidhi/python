str=input("enetr string:")
longest=""
current=""
for ch in str:
    if ch not in current:
        current+=ch
    else:
        index=0
        while current[index]!=ch:
            index+=1
        current=current[index+1]+ch

    if len(current)>len(longest):
        longest=current

print("longest substring..",longest)
print("length:",len(longest))
