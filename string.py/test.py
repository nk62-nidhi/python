for i in range(1,10):
    for j in range(1,10):
        if j%2==0:
          break
    print(i,j)
    if i%2==0:
        print("second is",i,j)