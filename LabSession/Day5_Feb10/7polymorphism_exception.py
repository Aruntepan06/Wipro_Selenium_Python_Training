# LAB 7: Polymorphism with Exception Handling (Method Overriding)

class Calculator:
    def divide(self, a, b):
        return a / b


class SafeCalculator(Calculator):
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"


c1 = Calculator()
c2 = SafeCalculator()

print("Calculator:", c2.divide(10, 2))
print("SafeCalculator:", c2.divide(10, 0))
