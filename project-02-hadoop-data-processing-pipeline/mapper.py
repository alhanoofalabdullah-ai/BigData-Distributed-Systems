import sys

for line in sys.stdin:

    line = line.strip()

    if line.startswith("transaction_id"):
        continue

    fields = line.split(",")

    if len(fields) == 4:

        region = fields[1]

        amount = fields[3]

        print(f"{region}\t{amount}")
