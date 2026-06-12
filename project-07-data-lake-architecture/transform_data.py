import pandas as pd

df = pd.read_csv(
    "data-lake/processed-zone/cleaned-sales/enriched-sales.csv"
)

summary = df.groupby("region")["amount"].sum()

summary.to_csv(
    "data-lake/curated-zone/analytics/revenue-by-region.csv"
)

print("Transformation completed")
