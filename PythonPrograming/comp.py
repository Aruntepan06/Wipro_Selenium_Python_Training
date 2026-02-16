# square of a number
sqs = [x**2 for x in range(1, 6)]
print(sqs)


# with the condition
evennumbers = [x for x in range(10) if x % 2 == 0]
print(evennumbers)


# dict comprehension — increase by 10%
salary = {"A": 50000, "B": 60000, "C": 70000}

updated_sal = {k: v + 0.1 * v for k, v in salary.items()}
print(updated_sal)


# filtering of dict
employees = {
    "Harsha": "ACTIVE",
    "Amit": "INACTIVE",
    "Ravi": "ACTIVE"
}

active_employees = {k: v for k, v in employees.items() if v == "ACTIVE"}
print(active_employees)

# set comprehensions
sqs = {x**2 for x in range(1, 6)}
print(sqs)


# with the condition
evennumbers = {x for x in range(10) if x % 2 == 0}
print(evennumbers)

