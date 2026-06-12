import pandas as pd

data = pd.read_csv("data/raw/customers.csv")

data["customer_value"] = data["total_spend"] / data["orders"]

data.to_csv(
    "data/features/customer_features.csv",
    index=False
)

print("Features generated successfully")
