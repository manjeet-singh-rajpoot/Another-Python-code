class A:
    def m(self):
        print("In Class1") 
       
class B(A):
    pass
 
class C(A):
    def m(self):
        print("In Class3")    
      
class D(B,C):
    pass      
 
obj = D()
obj.m()