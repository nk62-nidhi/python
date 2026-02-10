len=float(input("enter a length....>"))#here len is a variable
bre=float(input("enter a breath....>")) #here breath is a varaible
area_rectange=len*bre
perimeter_rectangle=2*(len+bre)
if area_rectange> perimeter_rectangle:
    print(f"{area_rectange:.2f} area of rectangle is greater than perimeter of rectangle {perimeter_rectangle:.2f}:" )
else:
    print(f"{ perimeter_rectangle:.2f} perimeter of rectangle is greater than {area_rectange:.2f}:" )