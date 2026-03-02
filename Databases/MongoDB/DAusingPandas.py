import pandas as pd
from CURD import collection

data = list(collection.find())
df = pd.DataFrame(data)

print(df)

print(df["marks"].mean())

print(df[df["marks"] == df["marks"].max()])

print(df.groupby("subject")["marks"].mean())