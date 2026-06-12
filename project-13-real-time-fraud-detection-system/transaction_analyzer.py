import json

with open("sample-data/transactions.json") as file:

    transactions = json.load(file)

for transaction in transactions:

    if transaction["amount"] > 10000:

        print("Suspicious Transaction:", transaction)
