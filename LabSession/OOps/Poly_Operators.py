class Number:
    def __init__(self, value):
        self.value = value

    # Addition
    def __add__(self, other):
        return self.value + other.value

    # Subtraction
    def __sub__(self, other):
        return self.value - other.value

    # Multiplication
    def __mul__(self, other):
        return self.value * other.value

    # Equal to
    def __eq__(self, other):
        return self.value == other.value

    # Greater than
    def __gt__(self, other):
        return self.value > other.value

    # Less than
    def __lt__(self, other):
        return self.value < other.value


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)   # add
print(n1 - n2)   # sub
print(n1 * n2)   # mul
print(n1 == n2)  # equal
print(n1 > n2)   # greater
print(n1 < n2)   # smaller
