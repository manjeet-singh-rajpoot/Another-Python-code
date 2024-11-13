                #1.default constructor #
class raj:
    def __init__(self):
        self.name="Raj"
        
    def print(self):
        print(self.name)

obj=raj()
obj.print()

              #2.parametrize constructor#
class maj:
    first=0
    second=0
    ans=0
    def __init__(self,f,s):
        self.first=f
        self.second=s
        
    def display(self):
        print("first num: ",self.first)
        print("second num: ",self.second)
        
    def display1(self):
        print("ans is : ",self.first+self.second)
        
obj2=maj(10,20)
obj2.display()
obj2.display1()