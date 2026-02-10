list=eval(input('enter list.....>'))
count=0
list1=[]
for i in range(1,len(list)+1,1):
    if list[i]==list[i-1]:
        count+=1
        list1.append(i)
print("count of {} is {}".format(i,count))