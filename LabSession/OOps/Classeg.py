class Student:
    studentname="ravi"
    studentID=677887
    def DisplayStudentdetails(self):
        print(self.studentname)
        print(self.studentID)


#creats the obj of the class
a=Student()
a.DisplayStudentdetails()

#wac to create class of employee

class Employee:
    def employeeDetails(self):
        self.Employeename="ravi"
        self.employeeID=677887
        self.empdept="QEA"
    def DisplayEmployeedetails(self):
        print(self.Employeename)
        print(self.employeeID)
        print(self.empdept)

a=Employee()
a.employeeDetails()
a.DisplayEmployeedetails()