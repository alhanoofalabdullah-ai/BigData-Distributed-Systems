import csv

file_path = "sample-data/sales-data.csv"

required_columns = ["transaction_id", "region", "product", "amount"]

with open(file_path, "r") as file:

    reader = csv.DictReader(file)

    if reader.fieldnames == required_columns:

        print("Data validation passed")

    else:

        print("Data validation failed")
