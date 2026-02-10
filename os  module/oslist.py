#to calculate how many folders are present in data folder we used listdir()function
import os
folders=os.listdir('data')
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))



#use more os module suggest by harry bhai
print(os.getcwd())
os.chdir("/users")
print(os.getcwd)
