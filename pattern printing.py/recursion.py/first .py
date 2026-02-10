num=int(input('enter a value..>'))
def count(num):
    if num==0:
        return
    print(num)
    count(num-1)
    print(num)
   
count(num)