class raj:
    companyname="Apple"
    def __init__(self,name):
        self.name=name
   
    def show(self):
        print("name : ",self.name)
        print("company name: ",self.companyname)
        
    @classmethod
    def changecompanyname(cls,newname):
        cls.companyname=newname

obj=raj("manjeet")
obj.show()

obj2=raj("raj")
obj2.changecompanyname("tesla")
obj2.show()
         
        
        