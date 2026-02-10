sub1=int(input("enter your physics marks...>"))
sub2=int(input("enter your physics marks...>"))
sub3=int(input("enter your physics marks...>"))
total_percentage=(sub1+sub2+sub3)/300*100
if sub1>=33 and sub2>=33 and sub3>=33 and total_percentage>=40 :
    print("student pass")
    print("and total percentage is ",total_percentage)
else:
    print("fail",total_percentage)

