# normal fucntion
def numbers():
    return [1,2,3,4,]

print(numbers())
# normal functions loads all the values into memory

# generator

def generator():
    print("printing 1")
    yield 1

    print("printing 2")
    yield 2

    print("printing 3")
    yield 3

ret_val = generator()
print(next(ret_val))
print(next(ret_val))
print(next(ret_val))
