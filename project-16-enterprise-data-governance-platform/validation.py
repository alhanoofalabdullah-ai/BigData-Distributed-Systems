import pandas as pd

data = pd.read_csv("sample-data/customer-data.csv")

missing_values = data.isnull().sum()

print(missing_values)
