time=float(input("enter time.."))
if time>0:
    if time<12:
        print("good morning.")
    elif(time>12 and time<=2):
        print("good afternooon sir")
    elif(time>2 and time<7):
        print("good evening")
    else:
        print("good night")