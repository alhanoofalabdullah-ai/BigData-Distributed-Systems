import pandas as pd

customers = pd.read_csv("data-sources/customers.csv")

print("Customer data extracted")

print(customers.head())
