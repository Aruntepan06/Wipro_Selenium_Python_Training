#Exception Handling:

try:
    a = int(input("Enter the number"))
    b = int(input("Enter the number"))
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")


# Generic Expression

try:
    a=5/10
except Exception as e:
    print(e)

#Runs only if no exception occurs
else:
    print("Division Successful")

#mandaroty code
finally:
    print("close the browser")

#customs exception create a own exception
age=int(input("Enter your age: "))
if age>18:
    raise ValueError("age must be less than or equal to 18")