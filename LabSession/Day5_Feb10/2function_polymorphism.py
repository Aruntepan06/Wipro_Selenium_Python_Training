# LAB 2: Polymorphism Using Function Arguments

class Dog:
    def speak(self):
        print("Dog says: Woof")


class Cat:
    def speak(self):
        print("Cat says: Meow")


class Cow:
    def speak(self):
        print("Cow says: Moo")


def animal_sound(obj):
    obj.speak()


animal_sound(Dog())
animal_sound(Cat())
animal_sound(Cow())
