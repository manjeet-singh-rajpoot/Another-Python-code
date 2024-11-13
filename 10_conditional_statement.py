r=int(input("enter rupees: "))
if(r==1000):
    print("5 GB")
elif(r==2000):
    print("10 GB")
elif(r==3000):
    print("15 GB")
    
    print("now advance data is free: please print 2-100 rupees  ")
    b=int(input("enter again rupees: "))
    if(b<=100):
        print("2 GB")
    else:
        print("please do not print more than 100 rupees")
else:
    print("does not available above 3000 rupess data")
    print("please enter 1000-2000-3000 rupees data")