class person:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    
obj1=person("raj",200000)
print(obj1.name)
print(obj1.salary)

string="john-30000"
obj2=person.fromstr(string)
print(obj2.name)
print(obj2.salary)