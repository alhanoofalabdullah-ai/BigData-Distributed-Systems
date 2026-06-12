import pandas as pd

sales = pd.read_csv("sample-data/sales.csv")

sales.columns = [column.lower() for column in sales.columns]

sales.to_csv("sample-data/transformed-sales.csv", index=False)

print("Transformation completed")
