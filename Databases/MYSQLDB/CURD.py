import mysql.connector

# create th connection to my Sql data abse
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123"
)

# connection.cursor() is a method used in Python database drivers (like sqlite3, psycopg2, mysql-connector)
# to create a cursor object from an established database connection.

cursor = connection.cursor()
print("Connected successfully")

# create database
cursor.execute("CREATE DATABASE IF NOT EXISTS school")
connection.commit()

# Now reconnect with database:
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="school"
    )

cursor = connection.cursor()
print("Connected successfully")

# create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    studentid INT AUTO_INCREMENT PRIMARY KEY,
    studentname VARCHAR(50),
    subject VARCHAR(50),
    marks INT
)
''')

connection.commit()

# Insert Data
query = "INSERT INTO students (studentname, subject, marks) VALUES (%s, %s, %s)"
values = ("John", "Math", 85)

cursor.execute(query, values)
connection.commit()

# Insert multiple records
students_data = [
    ("Ravi", "Science", 90),
    ("Sneha", "Math", 78),
    ("Kiran", "Science", 88)
]

cursor.executemany(query, students_data)
connection.commit()

# read data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# update the data
cursor.execute("UPDATE students SET marks=95 WHERE studentname='John'")
connection.commit()

# delete data
cursor.execute("DELETE FROM students WHERE studentname ='Sneha'")
connection.commit()