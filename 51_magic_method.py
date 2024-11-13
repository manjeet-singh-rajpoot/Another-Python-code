                   #1.__repr__ method #
class string:
    def __init__(self,string):
     self.string=string
     
    def __repr__(self):
        return "object: {}".format(self.string)
    
# if __name__=="__main__":
#     obj1=string("manjeet")
#     print(obj1.show())
    
             #2.__add__ method#
             
    def __add__(self,other):
        return self.string+other
    
if __name__=="__main__":
    obj1=string("manjeet")
    print(repr(obj1))
    print(obj1+"geeks")
    