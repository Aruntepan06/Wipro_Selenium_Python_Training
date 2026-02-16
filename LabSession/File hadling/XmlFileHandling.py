import xml.etree.ElementTree as ET

# Load XML file
tree = ET.parse("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/employee.xml")
root = tree.getroot()

# Print root tag
print("Root Tag:", root.tag)

# Print first child tag
print("First Child Tag:", root[0].tag)

# Print attributes of first child
print("First Child Attributes:", root[0].attrib)

# Fetch all employee ids
print("\nEmployee IDs:")
for employee in root.findall("employee"):
    emp_id = employee.get("id")
    print(emp_id)




# Create root element
new_root = ET.Element("employees")

# Employee 1
emp1 = ET.SubElement(new_root, "employee", id="101")
ET.SubElement(emp1, "name").text = "Harsha"
ET.SubElement(emp1, "role").text = "Tester"
ET.SubElement(emp1, "experience").text = "5"

# Employee 2
emp2 = ET.SubElement(new_root, "employee", id="102")
ET.SubElement(emp2, "name").text = "Amit"
ET.SubElement(emp2, "role").text = "Developer"
ET.SubElement(emp2, "experience").text = "3"

# Write new XML to file
new_tree = ET.ElementTree(new_root)
ET.indent(tree, space="    ")

new_tree.write(
    "/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/WriteXml.xml",
    encoding="utf-8",
    xml_declaration=True
)

print("\nNew XML file created successfully ✅")



# Load XML to update
tree = ET.parse(
    "/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/updating.xml"
)
root = tree.getroot()

# Update experience of employee id = 101
for emp in root.findall("employee"):
    if emp.get("id") == "101":
        exp = emp.find("experience")
        if exp is not None:
            exp.text = "16"

# Save updated XML
ET.indent(tree, space="    ")
tree.write(
    "/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/updating.xml",
    encoding="utf-8",
    xml_declaration=True
)


