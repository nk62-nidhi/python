def fun():
    try:
        a=[1,3,2,4]
        i=int(input("enter index.."))
        print(a[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("i am always occured")
fun()
#koi file ko close karna hh to finaaly ke ooo likh sakte hh
#print(" i am always occured") ka use karte to ye excutes to hota but function me work nhi karta