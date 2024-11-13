        #1.simple function #
def fun():
    print("hello world")
    
def add(num1 :int ,num2:int):
    num3=num1+num2
    return num3

def evenodd(x):
    if(x%2==0):
        print("even")
    else:
        print("odd")
def sub(num1,num2):
    num3=num1-num2
    return num3

fun()
num1=5
num2=30
num3=90
num4=30
ans=add(num1,num2)
print(ans)
evenodd(28)
ans2=sub(num3,num4)
print(f"num3 ans num4 is : {ans2}")