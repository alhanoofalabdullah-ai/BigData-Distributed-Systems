import pandas as pd

df = pd.read_csv("sample-data/raw-sales.csv")

duplicates = df.duplicated().sum()

print(f"Duplicate records: {duplicates}")

if duplicates == 0:

    print("Validation Passed")

else:

    print("Validation Failed")
