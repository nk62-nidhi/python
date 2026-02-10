n1=float(input("enter first no...>"))
n2=float(input("enter second no...>"))
n3=float(input("enter third no...>"))
n4=float(input("enter fourth no...>"))

if n1>n2 and n1>n3 and n1>n4:
    print(f"{n1} is greater")
elif n2>n3 and n2>n4:
    print(f"{n2} is greater")
elif n3>n4:
    print(f"{n3} is greater")
else:
    print(f"{n4} is greater")