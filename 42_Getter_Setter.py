                      # 1.Getter method #
class raj:
    def __init__(self,val):
        self.value=val
        
    def show(self):
        print(f"value is: {self.value}")
        
   # @property
    def ten_value(self):
        return 10*self.value

obj=raj(10)
print(obj.ten_value())
obj.show()

           
 