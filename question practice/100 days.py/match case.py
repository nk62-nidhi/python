x=float(input("enter a number.."))
match x:
    case 0:
        print(f"{x} is 0")
    case 1:
        print(f"{x} is 1")
    case 2:
        print(f"{x} is 2")
    case 3:
        print(f"{x} is 3")
    case _:
        print(x)