
a=int(input("first number"))
op=input("enter operator")
b=int(input("second number"))

match op:
    case "+":
        result=a+b
    case "-":
        result=a-b
    case "*":
        result=a*b
    case "/":
        result=a/b

    case "//":
        result=a//b

    case "**":
        result=a**b
    case "%":
        result=a%b
print(result)