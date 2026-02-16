# default methods - built in methods, user defined methods - method name, method body

# parameterized methods
# it allows the same method to behave differently for different inputs

# parameterized methods (multiple usage)

class Calculator:
    def add(self, a, b):
        print(a + b)

c = Calculator()

c.add(a=10, b=20)
c.add(a=5, b=7)

#default parameter
class Test:
    def run(self,browser="chrome"):
        print("the browser:", browser)

test = Test()
test.run()
test.run("Firefox")
# *args parameterized methods

class Numbers:
    def total(self, *args):
        print(sum(args))

n = Numbers()

n.total(10, 20, 30)
n.total(10)
n.total(10, 60)
