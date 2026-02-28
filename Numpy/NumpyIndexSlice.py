# NumPy Indexing is used to access or modify elements in an array.

import numpy as np

a = np.arange(10)
print(a)

b = a[9]
print(b)


scores = ['86', '98', '100', '65', '75']
arr = np.array(scores)
print (arr [2])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print(arr2[0, 1])
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])

# slicing - Slicing is the way to extract a subset of data from a NumPy array
# The syntax for slicing an array is [start:stop:step]

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[1:8:2])


#slice  with starting parameter
a=np.arange(10)
print(a[2:])

#slice with Stop parameter
a= np.arange(10)
print(a[:7])

#using  step parameter
a=np.arange(10)
print(a[::7])

import numpy as np

# slicing of 2D arrays

employees = np.array([
    [1, 25, 50000],
    [2, 30, 60000],
    [3, 28, 55000],
    [4, 35, 65000],
    [5, 40, 70000]
])

print("Information of Employee 2:", employees[1])
print("Ages of employees from index 2 onwards:", employees[2:, 1])

import numpy as np

# slicing in 3D array

arr_3d = np.arange(24).reshape(2, 3, 4)
print("Original 3D array:\n", arr_3d)

subarray = arr_3d[0, :, :2]
print(subarray)


# Negative Slicing

marks = np.array([93, 87, 98, 89, 67, 65, 54, 32, 21])
print("Lowest 5 marks is:", marks[-5:])