day=input("enter day")
while type(day)!=int:
    try:
        day=int(day)
    except:
        day=input("please enter valid day..")
             
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thrusday")
    case _:
        print("not valid")