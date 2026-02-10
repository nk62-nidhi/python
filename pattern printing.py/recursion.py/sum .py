num=int(input("enter number..>"))
def sum(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n + sum(n-1)

print(sum(num))