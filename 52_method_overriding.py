class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
    
class shape2(shape):
    def __init__(self,x):
        self.x=x
        self.x=x
        super().__init__(x,x)
    def area(self):
        return 3.14*super().area()
    
obj1=shape2(5)
print(obj1.area())    
    
    
    