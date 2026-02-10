name=input("enter your username..>")

if len(name) <=10  or "a"<= name >="z" or "A"<= name >="Z":
        print("valid username",name)

else:
        print("not valid",name)

#else:
    #print("please enter only character..>")