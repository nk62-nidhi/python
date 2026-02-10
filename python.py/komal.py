marks=float(input("enter a marks......>"))
if marks>0:
    if marks>90 and marks<=100:
        print("{} is distinction or A+ grade".format(marks))
    elif marks>80 and marks<=90:
        print("{} marks is A grade".format(marks))
    elif marks>70 and marks<=80:
        print("{} marks is B grade".format(marks))
    elif marks>60 and marks<=70:
        print("{} marks is C grade".format(marks))
    elif marks>50 and marks<=60:
        print("{} marks is D grade".format(marks))
    elif marks<50:
        print("{} marks is fail".format(marks))
    else:
        print("{} is invalid marks please enter valid marks".format(marks) )
else:
    print("please enter positive marks")
    
    