# list=[i*i for i in range(10)]
# print(list)
# list1=[j*j for j in range(15) if j%2==0]
# print(list1)
name=["aaruhi","nidhi","komal","laddo","hiii","hello"]
name_hostel=[item for item in name if (len(item)>4)]
print(name_hostel)