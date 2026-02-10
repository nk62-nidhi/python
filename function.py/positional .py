

a,b,c=10,20,30
#def add(a,b):
    #print(a+b)
#add(10,20,30)
def add(a=100,b=20):
    return a+b

print("addition is....",add(a,b))
print("addition is....",add())
print("addition is....",add(a))
print("addition is....",add(a,b,c))

