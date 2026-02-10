str=input("enter string....>")
sub=input("enter substring...>")
flag=False
pos=-1
n=len(str)
while True:
        pos=str.find(sub,pos+1,n)
        if pos==-1:
            break
        print("found at index",pos)
        flag=True
if flag==False:
    print("not found")