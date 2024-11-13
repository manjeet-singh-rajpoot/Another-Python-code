class A:
    def m():
        print("class A")
class B(A):
    def m():
        print("class B")
class C(A):
    def m():
        print("class C")
class D(B,C):
    def m():
        print("Class D")

D.m()