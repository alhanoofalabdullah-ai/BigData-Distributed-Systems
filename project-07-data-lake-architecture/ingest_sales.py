import shutil

source = "sample-data/sales.csv"

destination = "data-lake/raw-zone/sales/sales.csv"

shutil.copy(source, destination)

print("Sales data ingested")
