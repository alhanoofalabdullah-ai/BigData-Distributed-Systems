import pandas as pd

df = pd.read_csv("sample-data/raw-sales.csv")

df.dropna(inplace=True)

df.to_csv("sample-data/clean-sales.csv", index=False)

print("Data cleaned successfully")
