# ye koi jaruri nhi hh ki user hamesha int hi value hi de or agar humlog data mangvate hh server to to uske error se liye bhi try and except ka use karte h
#error se bachne ke liye


# a=input("enter the number..")
# print(f"multiplication table of {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)}*{i}={int(a)*i}")
# except :
#     print("please enter valid number")

#print("some imp code of line")

try:
    num=int(input("enter an integer"))
    a=[1,2,3]
    print(a[num])
except ValueError:
    print("number enter is not integers")
except IndexError:
    print("index error")

