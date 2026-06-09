import csv

input_file = "sample-data/sales-data.csv"

output_file = "sample-data/transformed-sales-data.csv"

with open(input_file, "r") as source, open(output_file, "w", newline="") as target:

    reader = csv.DictReader(source)

    fieldnames = ["region", "product", "amount"]

    writer = csv.DictWriter(target, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:

        writer.writerow({

            "region": row["region"],

            "product": row["product"],

            "amount": row["amount"]
        })

print("Data transformation completed")
