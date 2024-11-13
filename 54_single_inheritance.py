class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"name: {self.name}")
        print(f"name: {self.age}")
        
class child(parent):
    def __init__(self,name,age):
        self.name=name
        self.age=age
       
    def display(self):
        print("name: ",self.name)
        print("age: ",self.age)

obj=child("manjeet",20)
obj.display()
