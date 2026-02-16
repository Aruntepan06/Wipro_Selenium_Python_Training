# Q1 Custom iterator → prints numbers from 1 to 5
class Numbers:
    def __init__(self):
        self.num = 1          # starting value

    def __iter__(self):
        return self           # return iterator object

    def __next__(self):
        if self.num <= 5:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration


# using iterator
obj = Numbers()

for i in obj:
    print(i)

# Q2:Iterator class → returns next even number
class EvenNumbers:
    def __init__(self, limit):
        self.num = 2          # first even number
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            x = self.num
            self.num += 2
            return x
        else:
            raise StopIteration


# use iterator
obj = EvenNumbers(10)

for i in obj:
    print(i)


# Q3 explain

# _iter__()
#
# Called when iterator starts
#
# Returns the iterator object itself
#
# Used in for loop initialization
#
#  __next__()
#
# Returns the next value
#
# Runs every loop iteration
#
# Raises StopIteration to stop loop
class Demo:
    def __init__(self):
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.x <= 3:
            val = self.x
            self.x += 1
            return val
        else:
            raise StopIteration


obj = Demo()

it = iter(obj)        # calls __iter__()

print(next(it))       #calls __next__()
print(next(it))
print(next(it))
