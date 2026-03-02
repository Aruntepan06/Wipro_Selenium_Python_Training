import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

user = "root"
password = "Root@123"
host = "localhost"
db = "school"

engine = create_engine(
    f"mysql+mysqlconnector://{user}:{quote_plus(password)}@{host}/{db}"
)

df = pd.read_sql("SELECT * FROM students", engine)

print(df)

# average marks
print(df["marks"].mean())

# highest score
print(df[df["marks"] == df["marks"].max()])

# group by Subject
print(df.groupby("subject")["marks"].mean())