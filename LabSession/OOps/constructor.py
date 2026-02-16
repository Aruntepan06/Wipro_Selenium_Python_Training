#constructor-first function of the class when an obj of the class is created
#syntax   --init__()
#we can paramatrize the constructor
class Student:

    def __init__(self):
        print("Constructor is called")

    def addsum(self):
        print("Adding 2 numbers")

s1 = Student()
s1.addsum()

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Employee name: ", self.name)
        print("Salary: ", self.salary)


e1=employee("raju", 5000)
e1.display()


#using * arguments in constructor
#constructor overloading is supported by *args
#we can pass any number of parameter to the constructor using *args

class Numbers:
    def __init__(self, *args):
        self.values = args

n=Numbers(1,2,3)
print(n.values)
m=Numbers(11,22)
print(m.values)
n1=Numbers(7)
print(n1.values)


 #parents and child constructors
 #using the super keyword for accessing parent constructor data

class Parent:
    def __init__(self):
        print("I am a parent class")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("I am a child class")


c = Child()
