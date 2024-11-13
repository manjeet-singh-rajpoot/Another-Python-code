class person:     #public modifier #
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print("name: ",self.name)
        print("id: ",self.id)

obj1=person("raj",100)
obj1.show()

               #private modifier #
class raj:
    def __init__(self,__name,__id):
        self.__name=__name
        self.__id=__id
    def display(self):
        print("name: ",self.__name)
        print("id: ", self.__id)
obj2=raj("raj",200)
obj2.display()
             
             #protected modifier #
class kapil:
    def __init__(self,_name,_id):
        self._name=_name
        self._id=_id
    def display(self):
        print("name: ",self._name)
        print("id: ", self._id)
obj2=kapil("kapil",300)
obj2.display()

          