bin=int(input("enter binary number...>"))
i=0
dec=0
while bin!=0:
    r=bin%10
    dec=r*pow(2,i)+dec
    bin=bin//10
    i+=1
print(dec)
print("decimal to binary..>")
dec=int(input("enter a number..>"))
i=0 
bin=0
while dec!=0:
    r=dec%2
    bin=bin*(10*i+1)+r
    dec=dec//2
    i+=1

print(bin)