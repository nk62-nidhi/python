n=int(input('enter a number'))
count=0
r=0
rev=0
i=0
sum=0
num=n
while n!=0:
    r=n%10
    n=n//10
    count+=1
    i+=1
    rev=rev*10+r
    sum+=r
print("reverse is {}:".format(rev))
if rev==num:
    print("it is palindrome:")
else:
    print("not palindrome")
print("count is :{} and sum is {} ".format(count,sum))
 