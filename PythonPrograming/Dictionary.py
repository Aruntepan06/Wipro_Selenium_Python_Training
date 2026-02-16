range={
    1:"india",2:"Netherland",3:"Australia"

}

print(range)
#tuples
# my_dict = {(1,2): ("One", "Two")}
# print(my_dict)
my_dict = {1: "four", 2: "two", 3: "three"}
print(my_dict)

my_dict = {1: "four", 2: "two", 3: "three", 1: "one"}
print(my_dict)


student = {
    "name": "Arun",
    "age": 22,
    "course": "Python"
}
#pop
student.pop("age")
print(student)
#upadate
student.update({"age": 22, "city": "Jaipur"})
print(student)

#keys
print(student.keys())
#values()
print(student.values())
#popitem()
student.popitem()
print(student)
#copy
new_student = student.copy()
print(new_student)


 #Dict inside the List:

employees = [
    {"id": 1, "name": "Harsha", "role": "QA"},
    {"id": 2, "name": "Anil", "role": "Dev"},
    {"id": 3, "name": "Ravi", "role": "Manager"}
]

print(employees[0])
print(employees[0]["name"])

for emp in employees:
    print(emp["name"], emp["role"])

employees.append({"id": 4, "name": "Sita", "role": "Tester"})
print(employees)

employees.pop(0)
print(employees)

