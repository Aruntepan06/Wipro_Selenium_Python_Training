# LAB 1: Method Overriding with Inheritance (Runtime Polymorphism)

class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


# parent reference -> child object (runtime polymorphism)
emp = Employee(30000)
ref = Manager(30000, 7000)  # parent type reference possible in Python

print("Employee salary:", emp.calculate_salary())
print("Manager salary:", ref.calculate_salary())
