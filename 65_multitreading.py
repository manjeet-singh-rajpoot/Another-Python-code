                                #1.program #
import threading
import time
def fun(s):
    print(f"function for sleeping : {s}")
    time.sleep(s)


print("Main 1: ")
time1=time.perf_counter()
fun(3)
fun(2)
fun(1)
time2=time.perf_counter()
L=time2-time1
print(L)

print("Main2: ")
time3=time.perf_counter()
t1=threading.Thread(target=fun,args=[3])
t2=threading.Thread(target=fun,args=[2])
t3=threading.Thread(target=fun,args=[1])

t1.start()
t2.start()
t3.start()
time4=time.perf_counter()
L2=time4-time3
print(L2)



