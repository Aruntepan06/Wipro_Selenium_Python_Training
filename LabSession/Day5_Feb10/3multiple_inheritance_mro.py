# LAB 6: Multiple Inheritance and MRO (Diamond Structure)

class A:
    def show(self):
        print("A show")


class B(A):
    def show(self):
        print("B show")


class C(A):
    def show(self):
        print("C show")


class D(B, C):
    pass


d = D()
d.show()  # which one runs depends on MRO

print("MRO:", [cls.__name__ for cls in D.mro()])
