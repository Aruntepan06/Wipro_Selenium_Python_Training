import pandas as pd
import numpy as np

# 1) Create a DataFrame containing missing (None/NaN) values
df = pd.DataFrame({
    "Name": ["Arun", "Bala", "Charvi", "Divya", "Eshan"],
    "Age": [24, None, 29, 22, np.nan],
    "Salary": [60000, 50000, None, 45000, 80000],
    "Department": ["IT", "HR", "IT", "Sales", "HR"],
    "City": ["Bangalore", "Mumbai", "Bangalore", None, "Bangalore"]
})

print("Original DF:\n", df)

# 2) Detect missing values using appropriate function
print("\nMissing values (isna):\n", df.isna())
print("\nMissing values count per column:\n", df.isna().sum())

# 3) Replace missing values with 0
df_filled = df.fillna(0)
print("\nAfter fillna(0):\n", df_filled)

# 4) Drop rows containing missing values
df_dropped = df.dropna()
print("\nAfter dropna():\n", df_dropped)

# 5) Sort the DataFrame by Age in ascending order
df_age_asc = df.sort_values(by="Age", ascending=True)
print("\nSorted by Age (asc):\n", df_age_asc)

# 6) Sort the DataFrame by Salary in descending order
df_salary_desc = df.sort_values(by="Salary", ascending=False)
print("\nSorted by Salary (desc):\n", df_salary_desc)

# 7) Groupby Department and find average Salary per department
avg_salary_dept = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary per Department:\n", avg_salary_dept)

# 8) Find total Salary per department using groupby
total_salary_dept = df.groupby("Department")["Salary"].sum()
print("\nTotal Salary per Department:\n", total_salary_dept)

# 9) Filter employees where Age > 25 AND City = 'Bangalore'
filtered = df[(df["Age"] > 25) & (df["City"] == "Bangalore")]
print("\nAge > 25 AND City == 'Bangalore':\n", filtered)

# 10) Create a new column 'Tax' which is 10% of Salary using apply()
df_with_tax = df.copy()
df_with_tax["Tax"] = df_with_tax["Salary"].apply(lambda x: x * 0.10 if pd.notna(x) else np.nan)
print("\nWith Tax (10% of Salary):\n", df_with_tax)