# object type
print(len("python"))      # string
print(len([1, 2, 3]))     # list
print(len({1, 2, 3}))     # set

# input arguments no of arguments / data types

# usage
class calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


c = calculator()
print(c.add(5))
print(c.add(a=5, b=10.5))
print(c.add(a=5, b=10, c=15))

#runtime polymosrphism supported
#acheving mehtod overriding

# usage
class Animal:
    def sound(self):
        print("Animal makes sound")


# usage
class Dog(Animal):
    # usage
    def sound(self):
        print("dog barks")


a = Dog()
a.sound
# usage
class Animal:
    def sound(self):
        print("Animal makes sound")


# usage
class Dog(Animal):
    # usage
    def sound(self):
        print("dog barks")


a = Dog()
a.sound()
