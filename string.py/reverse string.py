str=input('enter string...>')
n=len(str)
rev_str=''
for i in range(len(str)-1,-1,-1):
    rev_str+=str[i]
   

print("string is",rev_str)
if rev_str==str:
    print("it is a palindrome")
else:
    print("not palindrome")
#reve_str=" "
#for i in str:
    #reve_str=i+reve_str
    #print(reve_str,i)

#print(reve_str)