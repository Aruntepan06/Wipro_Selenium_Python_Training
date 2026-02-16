import csv

#read
with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/data.csv","r")as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#write
with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/write.csv","w",newline="")as f:
    writer = csv.writer(f)
    writer.writerow(["A","B","C","D","E","F","G"])
    writer.writerow(["Arun", "3", "arujun", "D", "E", "F", "G"])

#append

with open("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/data.csv","a",newline="")as f:
   writer = csv.writer(f)
   writer.writerow(["Python","98","java","56"])
   writer.writerow(["subjects","teachers","Rooms","Staff"])