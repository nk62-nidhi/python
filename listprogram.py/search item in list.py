list=eval(input("enter the list"))
x=eval(input("enter a number to search in list"))
n=1
for i in list:
    if x in list:
        n+=1
    print(f"{x} is present in list at index{n} ")
    break
    
for i in range(0,len(list),1):
    if x == list[i]:
        print(f"{x} is prsent in list at {i}")
