# variables = used to store the data
# instance variables - global variables at class level
# local variables - inside the method only

# instance variables example

class Student:
    #class variable
    school="st. Joseph Convent"  #class variables
    def __init__(self, name, marks):
        self.name = name      # Instance variables
        self.marks = marks

    def show(self):
        school_city= "banglore"   #Local variable
        print(self.name, self.marks)
        print(school_city)
        print(self.school)


s1 = Student(name="Harsha", marks=85)
s2 = Student(name="Amit", marks=90)

s1.show()
s2.show()
