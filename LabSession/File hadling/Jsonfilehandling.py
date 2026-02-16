import json

#reading the J_son file

with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/employee.json",'r') as f:
    data = json.load(f)
    print(data)
    print(data['name'])

with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/nested.json",'r')as f:
    data = json.load(f)

    email=data["user"]["profile"]["email"]
    print(email)

    #writing using dumpmethod()
    data={
        "name": "Harsha",
        "role": "Tester",
        "experience": 5,
        "skills": ["Python", "Automation", "API"]
    }

with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/writeJson.json",'w')as f:

    json.dump(data,f)



#modify the data
#step 1(read)
import json

# Step 1 — Read
with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/modify.json", "r") as f:
    data = json.load(f)

# Step 2 — Update
data["experience"] = 6

# Step 3 — Write
with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/modify.json", "w") as f:
    json.dump(data, f, indent=4)
