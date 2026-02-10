list=eval(input("enter tupple..>"))
rev_list=[]
for i  in range(len(list)-1,-1,-1):
    rev_list.append(list[i])

print(rev_list)
if rev_list==list:
    print("palindrome")
else:
    print("not palindrome")