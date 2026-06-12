import pandas as pd

data = pd.read_csv("sample-data/customer-data.csv")

print(data.describe())
