           #1.default arguments#
def myfun(x,y=50):
    print("x :",x)
    print("y :",y)
        
myfun(10)

          #2.keyword arguments#
def student(firstname,lastname):
    print(firstname,lastname)

student(firstname="raj",lastname="singh")
student(lastname="singh",firstname="raj")

       #3.positional arguments #
def nemeage(name,age):
    print("I am ",name)
    print("My age is ",age)

print("Case 1: ")
nemeage("shivam",29)
print("case2: ")
nemeage(29,"raj")
      
      #4.Arbitary keywords #
      #A.non keyword arguments#
def myfun2(*argv):
    for i in argv:
        print(i)
        
myfun2("hello","welcome","to","raj")

     #B.keyword arguments #
# def myfun3(**kwargs):
#     for key,val in kwargs.items():
#         print("%S==%s"%(key,val))
        
# myfun3(first="raj",mid="singh",last="rajpoot")

    #5.Docstring in function call#
def multi(num1,num2):
    num3=num1+num2
    return num3
    
num1=20
num2=40
ans4=multi(num1,num2)
print(ans4.__doc__)
     
     #6.Function within function#
def f1():
    s="I love you "
    def f2():
        print(s)
    f2()
f1()

   #7.recursive program in function#
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))
        
   

