list=eval(input("enter list....>"))
def element(list,index):
    if index==len(list):
        return
    print(list[index],end=" ")
    element(list,index+1)


element(list,0)
