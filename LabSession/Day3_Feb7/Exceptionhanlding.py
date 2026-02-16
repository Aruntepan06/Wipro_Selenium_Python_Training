# import json
#
# try:
#     with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/employee.json", 'r') as f:
#         data = json.load(f)
#         print(data)
#         print(data['name'])
#
# except FileNotFoundError:
#     print("employee.json file not found")
#
#
#
# try:
#     with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/nested.json", 'r') as f:
#         data = json.load(f)
#
#         email = data["user"]["profile"]["email"]
#         print(email)
#
# except FileNotFoundError:
#     print("nested.json file not found")
#
#
#
# data = {
#     "name": "Harsha",
#     "role": "Tester",
#     "experience": 5,
#     "skills": ["Python", "Automation", "API"]
# }
#
# try:
#     with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/writeJson.json", 'w') as f:
#         json.dump(data, f, indent=4)
#         print("Data written successfully")
#
# except FileNotFoundError:
#     print("Path not found while writing JSON")
#
#
#
#
# try:
#     with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/modify.json", "r") as f:
#         data = json.load(f)
#
#     # Step 2 — Update
#     data["experience"] = 6
#
#     # Step 3 — Write
#     with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/modify.json", "w") as f:
#         json.dump(data, f, indent=4)
#
#     print("JSON modified successfully")
#
# except FileNotFoundError:
#     print("modify.json file not found")


# Q2; handle ivalid input

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input! Please enter a valid number.")


#q3

import random
import string

char = random.choice(string.ascii_letters)
print("Random Character:", char)

length = 5
rand_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
print("Random String:", rand_string)


n = int(input("Enter fixed length: "))
fixed_string = ''.join(random.choice(string.ascii_letters) for _ in range(n))
print("Fixed Length String:", fixed_string)
