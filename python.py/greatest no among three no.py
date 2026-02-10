num1=float(input("enter a first number..."))
num2=float(input("enter second number.....>"))
num3=float(input("enter a third number...."))

if num1>num2 and num1>num3:

    print("{} is greater than num2 {} and num3 {}".format(num1,num2,num3))

elif num2>num3:

    print("{} is greater than num1{} and num3{}".format(num2,num1,num3))

elif num3>num1:

    print("{} is greater than num1 {} and num2 {}".format(num3,num1,num2))
