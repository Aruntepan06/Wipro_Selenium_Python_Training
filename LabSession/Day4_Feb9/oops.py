# 1) Circle: area + perimeter
import math
from datetime import date
from abc import ABC, abstractmethod

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius * self.radius,2)

    def perimeter(self):
        return round(2 * math.pi * self.radius,2)


# 2) Person: name, country, dob + age
class Person:
    def __init__(self, name, country, dob):  # dob = date(YYYY,MM,DD)
        self.name = name
        self.country = country
        self.dob = dob

    def age(self):
        today = date.today()
        years = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            years -= 1
        return years


# 3) Shape parent + subclasses (circle, triangle, square)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class ShapeCircle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# 4) Vehicle parent + Bus child (inherits all)
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def info(self):
        print(self.brand, self.wheels)

class Bus(Vehicle):
    pass


# 5) Vehicle class without any variables and methods
class VehicleEmpty:
    pass


# ---- sample run ----
c = Circle(5)
print(c.area())
print(c.perimeter())

p = Person("Arun", "India", date(2003, 7, 6))
print(p.age())

t = Triangle(3, 4, 5)
print(t.area())
print(t.perimeter())

b = Bus("Tata", 6)
b.info()
