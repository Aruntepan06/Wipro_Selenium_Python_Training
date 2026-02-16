# LAB 4: Operator Overloading (+ and >) with BankAccount

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

    def __gt__(self, other):
        return self.balance > other.balance

    def __str__(self):
        return f"BankAccount(balance={self.balance})"


a1 = BankAccount(5000)
a2 = BankAccount(8000)

total = a1 + a2
print("Total:", total)

print("a2 > a1:", a2 > a1)
print("a1 > a2:", a1 > a2)
