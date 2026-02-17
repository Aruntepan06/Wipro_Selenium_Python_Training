# Car class stores car details
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand      # assigning brand
        self.model = model      # assigning model
        self.price = price      # assigning price


# Student class checks pass or fail
class Student:
    def __init__(self, marks):
        self.marks = marks      # storing marks

    def get_grade(self):
        if self.marks >= 50:    # checking if marks >= 50
            return "Pass"
        else:
            return "Fail"


# BankAccount class handles deposit and withdraw
class BankAccount:
    def __init__(self, balance):
        self.balance = balance   # setting initial balance

    def deposit(self, amount):
        self.balance += amount   # adding money to balance

    def withdraw(self, amount):
        self.balance -= amount   # subtracting money from balance


# Employee class stores employee data
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name         # storing name
        self.id = emp_id         # storing id
        self.salary = salary     # storing salary


# Counter class counts number of objects created
class Counter:
    count = 0                    # class variable to count objects

    def __init__(self):
        Counter.count += 1       # increasing count when object created


# Company class with class variable
class Company:
    company_name = "ABC Pvt Ltd"   # common company name for all objects


# Validator class with static method
class Validator:
    @staticmethod
    def check_email(email):
        if "@" in email:         # checking if @ is present
            return True
        return False


# Inheritance example
class Vehicle:
    def start(self):
        print("Vehicle started")   # printing message


class Bike(Vehicle):
    pass                           # inheriting start() method


# Multilevel inheritance example
class Person:
    def speak(self):
        print("Person speaking")   # printing message


class Employee2(Person):
    pass                           # inherits from Person


class Manager(Employee2):
    pass                           # inherits from Employee2


# Encapsulation using private variable
class BankAccountPrivate:
    def __init__(self):
        self.__balance = 0        # private variable

    def set_balance(self, amount):
        self.__balance = amount   # updating balance

    def get_balance(self):
        return self.__balance     # returning balance


# Property decorator example
class SalaryEmployee:
    def __init__(self, salary):
        self.salary = salary      # calling setter method

    @property
    def salary(self):
        return self._salary       # returning salary

    @salary.setter
    def salary(self, value):
        if value < 0:             # checking negative salary
            print("Salary cannot be negative")
        else:
            self._salary = value  # setting salary


# Polymorphism example
class Circle:
    def area(self):
        print("Area of Circle")   # circle area method


class Rectangle:
    def area(self):
        print("Area of Rectangle")  # rectangle area method


# Operator overloading example
class Number:
    def __init__(self, value):
        self.value = value        # storing value

    def __add__(self, other):
        return self.value + other.value   # adding two objects


# Composition example
class Engine:
    def start(self):
        print("Engine started")   # engine start message


class CarWithEngine:
    def __init__(self):
        self.engine = Engine()    # creating Engine object inside Car


c = Car("Honda", "City", 1000000)
print(c.brand, c.model, c.price)

s = Student(60)
print(s.get_grade())

b = BankAccount(1000)
b.deposit(500)
b.withdraw(200)
print(b.balance)

e = Employee("Arun", 101, 50000)
print(e.name, e.id, e.salary)

a = Counter()
b2 = Counter()
print(Counter.count)

print(Company.company_name)

print(Validator.check_email("ja@gmail.com"))
print(Validator.check_email("test1gmail.com"))

bike = Bike()
bike.start()

m = Manager()
m.speak()

acc = BankAccountPrivate()
acc.set_balance(500)
print(acc.get_balance())

emp = SalaryEmployee(30000)
print(emp.salary)
emp.salary = -10
print(emp.salary)

c1 = Circle()
r1 = Rectangle()
c1.area()
r1.area()

n1 = Number(5)
n2 = Number(10)
print(n1 + n2)

car2 = CarWithEngine()
car2.engine.start()
