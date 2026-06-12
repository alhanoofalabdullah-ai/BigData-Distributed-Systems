def detect_fraud(transaction):

    if transaction["amount"] > 10000:

        return True

    return False


transaction = {

    "amount": 15000

}

print("Fraud:", detect_fraud(transaction))
