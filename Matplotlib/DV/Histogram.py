import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# x axis data
x = np.array([1, 2, 3, 4])

# Histogram using numpy
plt.hist(x, bins=4)
plt.title("Simple Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# histogram using pandas
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [4000, 5500, 7000, 6500, 8000]
}

df = pd.DataFrame(data)

df["Steps"].plot(kind="hist", bins=5)

plt.title("Daily Steps Distribution")
plt.xlabel("Steps")
plt.ylabel("Frequency")
plt.show()