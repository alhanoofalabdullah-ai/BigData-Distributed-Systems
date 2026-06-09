import pandas as pd

df = pd.read_csv("sample-data/raw-sales.csv")

df.columns = [col.lower() for col in df.columns]

df.to_csv("sample-data/normalized-sales.csv", index=False)

print("Normalization completed")
