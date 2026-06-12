import shutil

source = "sample-data/customers.csv"

destination = "data-lake/raw-zone/customers/customers.csv"

shutil.copy(source, destination)

print("Customer data ingested")
