num=int(input("enter a number.."))
i=2
while i!=num:
    is_prime=False
    if num%i==0:
        is_prime=True
        break
    i+=1
if is_prime==False:
    print(f" {num} is prime number") 
elif num==2:
    print(f"{num} prime number")    
else:
    print(f" {num} is  not prime number.")

    
