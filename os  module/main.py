import os
# if( not os.path.exists("data")):
#     os.mkdir("data")
# remane folder 
for i in range(0,100):
    #os.mkdir(f"data/day{i+1}")
    os.rename(f"data/day{i+1}",f"data/tutorial{i+1}")

#mkdir is used for create folders or rename is used fro rename folder


