# Pandas - high perfomance data manipulation and data analysis tool
# 2008 Mckinnley
# data frame object
# list , csv , josn , pdf

# series - A one-dimensional labeled homogeneous array, sizeimmutable.
# DataFrames    2  A two-dimensional labeled, size-mutable tabular structure with potentially heterogeneously typed columns.


import pandas as pd
# creation of series Out of lists
data = ['Steve', '35', 'Male', '3.5']
series = pd.Series(data, index=['Name', 'Age', 'Gender', 'Rating'])
print(series)

# create series using custom index
data = [100, 200, 300]
s = pd.Series(data, index=['a', 'b', 'c'])
print(s)

# create series from dictionary
import pandas as pd

data = {'a': 1, 'b': 2, 'c': 3}
s = pd.Series(data)
print(s)

# create series from Numpy array
import numpy as np

arr = np.array([5, 10, 15])
s = pd.Series(arr)
print(s)