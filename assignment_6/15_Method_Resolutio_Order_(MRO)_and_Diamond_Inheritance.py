class A:
    @staticmethod
    def show()->str:
        print("show from A")


class B(A):
    def show(self):
        print("show from B")

class C(A):
    def show(self):
        print("show from C")

class D(B, C):
   pass


d = D()
d.show()
print(D.__mro__)


