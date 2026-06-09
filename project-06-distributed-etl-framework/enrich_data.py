import pandas as pd

sales = pd.read_csv("sample-data/normalized-sales.csv")

sales["processing_date"] = pd.Timestamp.now()

sales.to_csv("sample-data/enriched-sales.csv", index=False)

print("Data enrichment completed")
