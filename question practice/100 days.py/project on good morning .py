import time
t=time.strftime('%H:%M:%S')
# print(recenttime)
recenttime=int(time.strftime('%H'))
# print(recenttime)
# recenttime=int(time.strftime('%M'))
# print(recenttime)
# recenttime=int(time.strftime('%S'))
# print(recenttime)
# if time<12:0:0:
#     print("good morning")
name= input("enter your name ..")
if(recenttime>4 and recenttime<=12):
    print(f"good morning {name} {t}")
elif(recenttime>12 and recenttime<=15):
    print(f"good afternoon {name} {t}")
elif (recenttime>15 and recenttime<=17):
    print(f"good evening {name} {t}")
else:
    print(f"good night {name} {t}")