import sys

current_region = None

total_sales = 0

for line in sys.stdin:

    region, amount = line.strip().split("\t")

    amount = float(amount)

    if current_region == region:

        total_sales += amount

    else:

        if current_region:

            print(f"{current_region}\t{total_sales}")

        current_region = region

        total_sales = amount

if current_region:

    print(f"{current_region}\t{total_sales}")
