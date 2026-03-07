import pandas as pd

# read excel sheet
df = pd.read_excel(io="/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/Openpyxl/Students.xlsx")

print(df)

#writing excel sheet
data = {
    "Name": ["Ram", "Ravi", "Sita"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

df.to_excel("output.xlsx", index=False,engine="openpyxl")

#read a specific coumn
df=pd.read_excel("output.xlsx",usecols=["Name"],engine="openpyxl")
print(df)

#read particular sheet
df=pd.read_excel("Students.xlsx",sheet_name="students",engine="openpyxl")
print(df)

# Writing Multiple Sheets

data1 = {
    "Product": ["Laptop", "Phone"],
    "Sales": [10, 20]
}

data2 = {
    "City": ["Delhi", "Mumbai"],
    "Customers": [200, 150]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

with pd.ExcelWriter(path="report.xlsx", engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name="Sales")
    df2.to_excel(writer, sheet_name="Customers")