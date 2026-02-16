#Q1
def check_range(n, start, end):
    if n >= start and n <= end:
        print("Number is within the range")
    else:
        print("Number is outside the range")


check_range(25, 10, 50)



#Q2
def print_even():
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)


print_even()


# Q3
def sum_1_to_100():
    total = 0
    for i in range(1, 101):
        total += i
    print("Sum =", total)

sum_1_to_100()

#q4
for i in range(1, 101):
    if i % 5 == 0:
        print(i)
#q5
lst = list(range(50, 101, 5))
print(lst)
#q6
for i in range(1, 11):
    print(i * i)
#q7
for i in range(-10, 11):
    print(i)

