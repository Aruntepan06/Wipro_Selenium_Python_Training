# descriptor - control the access of the object data attributes
# __get__()
# __set__()
# __delete__()

# usage
class Desc:
    def __get__(self, instance, owner):
        print("getting the value ")
        return 10


# usage
class Test:
    x = Desc()


t = Test()
print(t.x)

# this non-data descriptor uses only __get__ descriptor
# data descriptor uses

class myDesc:
    def __get__(self, instance, owner):
       return instance.value

    def __set__(self, instance, value):
        print("setting the value ")
        instance.value = value



class Test:
    x = myDesc()
    t.Test = Test()
    t.x =1000
    print(t.x)

# delete
class Name:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        instance._name = value

    def __delete__(self, instance):
        print("Deleting name")
        del instance._name


# usage
class Person:
    name = Name()


p = Person()
p.name = "Arun"
del p.name
