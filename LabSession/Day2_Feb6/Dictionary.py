# Create dictionary (roll no : name)
students = {
    101: "Arun",
    102: "Rahul",
    103: "Sita"
}

# Print dictionary
print("Dictionary:", students)


# Access value (existing key)
print("Existing key value:", students[101])

# Access value (non-existing key)
print("Non-existing key value:", students.get(1050))


# Update value of existing key
students[102] = "Amit"
print("After update:", students)


# Delete using del
del students[103]
print("After del:", students)

# Delete using pop()
students.pop(101)
print("After pop:", students)


# Find number of key–value pairs
print("Length:", len(students))


# Print only keys
print("Keys:", students.keys())

# Print only values
print("Values:", students.values())

# Print key–value pairs
print("Key-Value pairs:", students.items())
