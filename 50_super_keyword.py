class parent:
    def parentmethod(self):
        print("Hii manjeet")

class child(parent):
    def childmethod(self):
        print("hii arjun")
        super().parentmethod()

obj=child()
obj.childmethod()