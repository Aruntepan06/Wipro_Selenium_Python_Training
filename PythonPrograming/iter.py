numbers = [10, 20, 30, 40]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

fruits = ["apple", "banana", "mango"]

it = iter(fruits)

for i in it:
    print(i)

def even_numbers():
    n = 0
    while True:
        n += 2
        yield n

it = iter(even_numbers())

print(next(it))  # 2
print(next(it))  # 4
print(next(it))  # 6
print(next(it))  # 8

def get_input():
    return input("Enter value: ")

for value in iter(get_input, "quit"):
    print("You entered:", value)

print("Loop ended")
