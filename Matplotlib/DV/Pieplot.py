import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# x axis data
x = np.array([1, 2, 3, 4])
labels = ["A", "B", "C", "D"]

# Pie chart using numpy
plt.pie(x, labels=labels, autopct="%1.1f%%")
plt.title("Simple Pie Chart")
plt.show()

# pie plot using pandas
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [4000, 5500, 7000, 6500, 8000]
}

df = pd.DataFrame(data)

df.set_index("Day")["Steps"].plot(kind="pie", autopct="%1.1f%%")

plt.title("Daily Steps Distribution")
plt.ylabel("")
plt.show()