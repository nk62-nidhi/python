def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))#strip method is used for remove unwanted word
    print(n)

l=input("enter list..>")
x=input("enter word to delete..>")
rem(l,x)