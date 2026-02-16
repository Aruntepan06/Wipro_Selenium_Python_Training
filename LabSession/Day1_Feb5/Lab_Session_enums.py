# Q1:
list(enumerate(['a', 'b', 'c']))

#OUTPUT=[(0, 'a'), (1, 'b'), (2, 'c')]

#Q2
for i, v in enumerate([10, 20, 30]):
    print(i, v)
#OUTPUT= 0 10
       # 1 20
       #2 30
#Q3
colors = ['red', 'green', 'blue']

for i, v in enumerate(colors, start=1):
    print(i, v)
#output:
# 1 red
# 2 green
# 3 blue

#Q4
list(enumerate("PYTHON", start=1))
#output:
# [(1, 'P'), (2, 'Y'), (3, 'T'), (4, 'H'), (5, 'O'), (6, 'N')]


#Q5
nums = [10, 20, 30, 40, 50, 60]

for i, v in enumerate(nums):
    if v == 50:
        print(i)
#Output 4

#Q6
for i, n in enumerate(range(10, 60, 10)):
    print(i, n)
for i, v in enumerate(data):
    print(i, v)

    #output
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50

#Q7
for i, v in enumerate(data):
    print(i, v)

#Q8
items = ['a', 'b', 'c']
for i in enumerate(items):
    print(i)

    #Output:
    # (0, 'a')
# (1, 'b')
# (2, 'c')

#Q9
list(enumerate([], start=5))
#output: []   Nothing to iterate

#10
for i, v in enumerate([100, 200, 300], start=-1):
    print(i, v)
#output:
# -1 100
# 0 200
# 1 300

# Q11
i, v = enumerate(['x', 'y', 'z'])
#Error occurs enumerate() returns an iterator, not two values.
#correct way
for i, v in enumerate(['x','y','z']):
    print(i, v)

#Q12
# Explain the difference:
# enumerate(data)
#eg: data = ['a', 'b', 'c']
# list(enumerate(data))
#output: [(0, 'a'), (1, 'b'), (2, 'c')]


# enumerate(data, start=1)
#eg data = ['a', 'b', 'c']
# list(enumerate(data, start=1))
#output: [(1, 'a'), (2, 'b'), (3, 'c')]

