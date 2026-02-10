num1=float(input("enter first number..."))
num2=float(input("enter second number..."))
num3=float(input("enter third number..."))
def greatest(a,b,c):
    if a>b and a>c:
        print(f"{a} is gretest")
    elif b>c:
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")
greatest(num1,num2,num3)
