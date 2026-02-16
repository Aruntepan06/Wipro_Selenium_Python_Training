#Generator → numbers from 1 to N
def numbers(n):
    for i in range(1, n+1):
        yield i


# using generator
for num in numbers(5):
    print(num)

#Generator → even numbers only
def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i


for num in even_numbers(10):
    print(num)
#Generator → read file line by line
def read_file(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()


# using generator
for line in read_file("/Users/arunkumartepan/PycharmProjects/PythonAdvancePrograming/LabSession/Dataformats/data.txt"):
    print(line)

#Generator → Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci(7):
    print(num)

#Generator → retry attempts (max 3 tries)
def retry_attempts():
    attempts = 1
    while attempts <= 3:
        yield f"Attempt {attempts}"
        attempts += 1


for attempt in retry_attempts():
    print(attempt)
