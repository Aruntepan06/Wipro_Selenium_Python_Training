import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# x axis data
x = np.array([1, 2, 3, 4])

# y axis data
y = x * 2

# Scatter plot using numpy
plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# scatter plot using pandas
data = {
    "Day_Number": [1, 2, 3, 4, 5],
    "Steps": [4000, 5500, 7000, 6500, 8000]
}

df = pd.DataFrame(data)

df.plot(x="Day_Number", y="Steps", kind="scatter")

plt.title("Daily Steps Scatter Plot")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.show()