class A:
    def m(self):
        print("In Class1") 
       
class B(A):
    pass
 
class C(B):
    def m(self):
        print("In Class3")    
      
class D(C):
    pass      
 
obj = D()
obj.m()