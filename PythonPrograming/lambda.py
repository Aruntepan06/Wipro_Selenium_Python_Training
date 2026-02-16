check = lambda n: "Even" if n % 2 == 0 else "Odd"

print(check(10))  # Even
print(check(7))   # Odd


max=lambda a,b: a if a>b else b
print(max(1,2))

nums = [-5, 10, -3, 7, 0, 2]

pos=list(filter(lambda n: n>0, nums))
print(pos)


data = ["hello", "", "world", "", "python"]
nonempty = list(filter(lambda n: n!="", data))
print(nonempty)


from functools import reduce
#multiply
nums=[10,20,30,40]
print("the prod is: ",reduce(lambda x,y:x*y,nums))
#max val
nums=[10,20,30,40]
print("The max val is: ",reduce(lambda x,y:x if x>y else y,nums))
#min val
nums=[10,20,30,40]
print("The min val is: ",reduce(lambda x,y:x if x<y else y,nums))

# sorting
marks = {"A": 75, "B": 90, "C": 60}

sorted_marks = dict(
    sorted(marks.items(), key=lambda x: x[1])
)

print(sorted_marks)

data = [(1, 3), (4, 1), (2, 2)]

sorteddata = sorted(data, key=lambda x: x[0])

print(sorteddata)
