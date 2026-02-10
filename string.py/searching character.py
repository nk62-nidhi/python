str=input("enter string.....>")
x=input("enetr character to search..>")
print(len(str))
a=0
for i in range(0,len(str),1):
     if x==str[i]:
        print(" {} is present in at position {}".format(x,a))
     a+=1     