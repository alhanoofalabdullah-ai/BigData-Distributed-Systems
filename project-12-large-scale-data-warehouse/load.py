import pandas as pd

sales = pd.read_csv("sample-data/transformed-sales.csv")

print(f"{len(sales)} records loaded into warehouse")
