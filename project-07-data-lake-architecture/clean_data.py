import pandas as pd

df = pd.read_csv("data-lake/raw-zone/sales/sales.csv")

df.dropna(inplace=True)

df.to_csv(
    "data-lake/processed-zone/cleaned-sales/sales.csv",
    index=False
)

print("Data cleaned successfully")
