marks=[12,49,69,89,99,12]
# index=0
# for mark in marks:
#     print(mark)
#     if (index==3):
#         print("harry,awesome!")
#     index+=1

# for easy we use enumarate function

for index ,mark in enumerate(marks,start=1):
    print(mark,index)
    if index==3:
     print("hello good   ")




#enumerate function is built in function in python that allows you to loop over a sequence and get the index And value of each elemenin the sequence at same time