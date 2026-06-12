import pandas as pd

df = pd.read_csv(
    "data-lake/raw-zone/sales/sales.csv"
)

duplicates = df.duplicated().sum()

print(f"Duplicate Records: {duplicates}")
