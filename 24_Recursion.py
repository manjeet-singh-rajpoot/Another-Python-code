             # fibonacci series#
def fibo(n):
    if(n<=1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=10

if(n<=0):
    print("Invalid")
else:
    print("Fibonacci series: ")
for i in range(n):
    print(fibo(i))
    
         # factorial program#
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
print(f"fact(5) is : {fact(5)}")
    
        