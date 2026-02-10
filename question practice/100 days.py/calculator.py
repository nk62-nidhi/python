while True:
    a=float(input())
    n=input()
    b=float(input())
   
    match n:
        case "+":
            print(f"= {(a+b)}") 
        case "-":
            print(f"= {a-b}")
        case "*":
            print(f"={a*b}")
        case "/":
            print(f"= {a/b}")
        case "**":
            print(f"= {a**b}")
        case "%":
            print(f"= {a%b}")
        case "_":
            print("invalid choice enter valid choice.")
