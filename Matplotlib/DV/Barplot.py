import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# x axis data
x = np.array([1, 2, 3, 4])

# y axis data
y = x * 2

plt.bar(x, y)
plt.show()

# line plot using pandas
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [4000, 5500, 7000, 6500, 8000]
}

df = pd.DataFrame(data)

df.plot(x="Day", y="Steps", kind="bar")

plt.title("Daily Steps Count")
plt.xlabel("Day")
plt.ylabel("Steps")

plt.show()