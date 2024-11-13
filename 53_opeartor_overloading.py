class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a+o.a
    
obj1=A(2)
obj2=A(2)
obj3=A("manjeet")
obj4=A("Bhai")

print(obj1+obj2)
print(obj3+obj4)

print(A.__add__(obj1,obj2))
print(A.__add__(obj3,obj4))

print(obj1.__add__(obj2))
print(obj3.__add__(obj4))