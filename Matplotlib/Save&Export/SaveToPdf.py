import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

#plt.show()
#save pict as jpg
plt.savefig("Daily Steps Count.png")

#save as pdf
plt.savefig("bar.pdf",format="pdf")