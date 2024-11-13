                     #1.dir() method #
List=[1,2,3]
#print(dir(List))
#print(List.__add__)

                     #2.__dict__ method #
class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

obj=A("manjeet",20)
print(obj.__dict__)

                    #3.Help() method #
print(help(A))