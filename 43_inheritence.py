class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"name1 : {self.name}")
        print(f"id1 : {self.id} ")
    
class employee2(employee):
     def display(self):
        print(f"name2 : {self.name}")
        print(f"id2 : {self.id} ")


obj1=employee("harshit",400)
obj2=employee2("raj",410)

obj1.show()
obj2.display()
    