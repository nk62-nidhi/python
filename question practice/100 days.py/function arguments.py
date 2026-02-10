#  default arguments  in function is keyword argument
def add(b=10,a=9):
    sum=a-b
    return sum
sum=add
print(add())
print(sum())
# function arguments type
# 1. positonanl arguments
# 2.keyword arguments
# 3.varible length arguments
# 4.requried arguments
#Requried arguments
def average(a,b,c=1):
    print("the average is",(a+b+c)/3)
#average(b=9)
average(5,6)
# take  varible length arguments arguments as a tupple
def average(*numbers):
    print(type (numbers))
    sum=0
    for i in numbers:
        sum+=i
    print("average is",sum/len(numbers))
average(5,6,4,7,8,9)
#arbitary arguments
def name(**name):
    print(type(name))
    print("hello",name["fname"],name["lname"],name["mname"])

name(mname="nidhi",lname="sneha",fname="riyansh")
