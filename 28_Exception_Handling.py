                #1.program#
amount=10000
if(amount>2999):
 print("error")

                #2.zerodivisionError#
marks=1000
a=marks/0
print(a)
               #3.typeError#
                
x=5
y="hello"
z=x+y
print(z)

              #4.program #
a=[1,2,3]
try:
    print("second element: ",a[1])
    print("fourth element: ",a[3])
except:
    print("An Error occurs")
            
            #5.catching specific exception#
def fun(a):
    if(a<4):
        b=a/(a-3)
        print("Value of b is : ",b)
try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("Zero dividion error")
except NameError:
    print('NameError')
      
         #6.Finally Keyword #
try:
    k=5//0
    print(k)
except ZeroDivisionError:
    print("Cant divide by Zero")
finally:
    print("This will be always execute")
    
    
      #7.Raise keyword #
x=int(input("Enter num b/w 2 & 7: "))
if(x<2 or x>7):
    raise ValueError("value should be b/w 2 & 7")



    
    
        
