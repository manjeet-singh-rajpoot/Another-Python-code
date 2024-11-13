          #1.instance variable#
class Car: 
    def __init__(self, brand, model): 
        # Instance attributes 
        self.brand = brand 
        self.model = model 
  
# Creating instances of the Car class 
car1 = Car("Toyota", "Camry") 
car2 = Car("Honda", "Civic") 
  
# Accessing instance attributes 
print(f"{car1.brand} {car1.model}")   
print(f"{car2.brand} {car2.model}")   


          #2.class variable#
class MyClass: 
    class_attribute = "I am a class attribute"
  
# Accessing class attribute 
print(MyClass.class_attribute)  
  
# Modifying class attribute 
MyClass.class_attribute = "New value for class attribute"
print(MyClass.class_attribute)   