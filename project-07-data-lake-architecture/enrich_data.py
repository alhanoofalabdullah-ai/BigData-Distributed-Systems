import pandas as pd

df = pd.read_csv(
    "data-lake/processed-zone/cleaned-sales/sales.csv"
)

df["processing_date"] = pd.Timestamp.now()

df.to_csv(
    "data-lake/processed-zone/cleaned-sales/enriched-sales.csv",
    index=False
)

print("Data enrichment completed")
