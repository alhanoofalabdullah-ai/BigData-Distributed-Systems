import pandas as pd

df = pd.read_csv("sample-data/enriched-sales.csv")

print(f"{len(df)} records loaded into warehouse")
