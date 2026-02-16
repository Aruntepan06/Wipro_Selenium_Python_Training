from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# Step 1 — Filter even numbers
even_nums = list(filter(lambda x: x % 2 == 0, nums))

# Step 2 — Square them
squares = list(map(lambda x: x*x, even_nums))

# Step 3 — Find sum
total = reduce(lambda a, b: a + b, squares)

print("Even numbers:", even_nums)
print("Squares:", squares)
print("Sum:", total)

from functools import reduce

salaries = [25000, 40000, 32000, 18000]

# Filter salaries > 30000
filtered = list(filter(lambda x: x > 30000, salaries))

#  Add 10% hike
hiked = list(map(lambda x: x * 1.10, filtered))

# Total payout
total = reduce(lambda a, b: a + b, hiked)

print("Filtered Salaries:", filtered)
print("After Hike:", hiked)
print("Total Payout:", total)


#Question1

# Example list of tuples
data = [(2, 5), (1, 3), (4, 1), (3, 2)]

# Sort by second element
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)

#Question2
from datetime import datetime

# Current date & time
now = datetime.now()

# Lambda functions
get_year  = lambda x: x.year
get_month = lambda x: x.month
get_date  = lambda x: x.day
get_time  = lambda x: x.time()

print("Year :", get_year(now))
print("Month:", get_month(now))
print("Date :", get_date(now))
print("Time :", get_time(now))



#Question3
# Given dictionaries
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

# Concatenate
new_dict = {**dict1, **dict2, **dict3}

print(new_dict)
