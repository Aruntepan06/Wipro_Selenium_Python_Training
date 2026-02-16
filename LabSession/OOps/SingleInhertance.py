# single inheritance
# Parent ---> child class - properties from parent class are acquired to child class

# parent class
class Employee:
    def __init__(self, name, empid):
        self.name = name
        self.empid = empid

    def empdetails(self):
        print(self.name, self.empid)


# child class
class Manager(Employee):
    def approve_leave(self):
        print("leave approved")

m=Manager("arujun", "123456")
m.empdetails() #from parent class
m.approve_leave() #from child class

class SavingsAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:", self.balance)


class ChildAccount(SavingsAccount):
    def addinterest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print("Interest added:", interest)

    def show_balance(self):
        print("Current Balance:", self.balance)


a = ChildAccount()

a.deposit(1000)      # deposit
a.addinterest(10)    # add interest
a.show_balance()     # show final balance
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def book_title(self):
        return f"{self.title}"

    def book_price(self):
        return f"{self.price}"

    def book_author_only(self):
        return f"{self.author}"


B = Book("Avatar", "James", "4000")

print(B.book_title())
print(B.book_price())
print(B.book_author_only())

# Q2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
        self.perimeter = 2 * (length + width)

r = Rectangle(10, 5)

print("Area:", r.area)
print("Perimeter:", r.perimeter)
