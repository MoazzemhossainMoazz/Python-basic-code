class A:
    def display1(self):
        print("A class")

class B(A):
    def display2(self):
        print("B class")

class C(B):
    def display3(self):
        print("C class")

print("For class-C")
ob1 = C()
ob1.display1()
ob1.display2()
ob1.display3()

print("For class-B")
ob2 = B()
ob2.display1()
ob2.display2()

print("For class-A")
ob3 = A()
ob3.display1()




print("\n\nAnother way: ")

class X:
    def display1(self):
        print("Class-X")

class Y(X):
    def display2(self):
        super().display1()
        #print("\nC-Y")
        print("Class-Y")

class Z(Y):
    def display3(self):
        super().display1()
        super().display2()
        print("Class-Z")



obj1 = Z()
obj1.display3()

obj2 = Y()
obj2.display2()

obj3 = X()
obj3.display1()

print("\n\nAnother way: ")

class H:
    def display(self):
        print("Class-X")

class I:
    def display(self):
        print("Class-Y")

class J(H,I): #try class J(I,H)
    pass

object1 = J()
object1.display()