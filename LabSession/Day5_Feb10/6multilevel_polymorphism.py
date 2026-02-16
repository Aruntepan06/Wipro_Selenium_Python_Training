# LAB 3: Multilevel Inheritance with Polymorphism (Vehicle -> Car -> ElectricCar)

class Vehicle:
    def fuel_type(self):
        return "Unknown"


class Car(Vehicle):
    def fuel_type(self):
        return "Petrol/Diesel"


class ElectricCar(Car):
    def fuel_type(self):
        return "Electric"


v = Vehicle()
c = Car()
e = ElectricCar()

print(v.fuel_type())
print(c.fuel_type())
print(e.fuel_type())

# different references (same method name)
ref1 = ElectricCar()
ref2 = Car()
ref3 = Vehicle()

print(ref1.fuel_type())
print(ref2.fuel_type())
print(ref3.fuel_type())
