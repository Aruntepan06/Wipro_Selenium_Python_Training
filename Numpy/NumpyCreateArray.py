import numpy as np

# Changing Shape

# reshape
a = np.arange(1, 7)
print("Original array", a)

# reshape the array
reshaped = a.reshape(2, 3)
print(reshaped)


# flat - returns 1D iterator over the array
arr = np.array([[1, 2], [3, 4]])

for x in arr.flat:
    print(x)


# flatten - Returns a copy of the array collapsed into one dimension
arr = np.array([[1, 2], [3, 4]])
print(arr)

flat_arr = arr.flatten()
print(flat_arr)


# ravel() - Returns a flattened array
arr = np.array([[1, 2], [3, 4]])
print(arr)

at_arr = arr.ravel()
print(at_arr)


# pad() - Returns a padded array with shape increased according to pad_width.
arr = np.array([1, 2, 3])

padded = np.pad(arr, pad_width=3, mode='constant')
print(padded)
