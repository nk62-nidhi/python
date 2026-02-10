a=eval(input("enter first number"))
b=eval(input("enter second number"))
def swap(x,y):
    swap=x
    x=y
    y=swap
    print("after swap a ={} and b={}".format(x,y))
    return x,y

print("a={} and b={}".format(a,b))
swap(a,b)


