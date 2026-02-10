str=input("enter string...>")
unique={}
for i in str:
        if i in unique :
            unique[i]= unique[i]+1
        else:
          unique[i]=1
for key in unique:
    print(key,unique[key])
    




