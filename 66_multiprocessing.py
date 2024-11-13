import multiprocessing

def square(num):
    print("squre is: {}".format(num*num))
def cube(num):
    print("cube is: {}".format(num*num*num))

if __name__=="__main__":
    p1=multiprocessing.Process(target=square,args=(10,))
    p2=multiprocessing.Process(target=cube,args=(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
