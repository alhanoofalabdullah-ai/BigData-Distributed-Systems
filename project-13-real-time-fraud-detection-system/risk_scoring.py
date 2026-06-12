def calculate_risk(transaction):

    risk_score = 0

    if transaction["amount"] > 10000:

        risk_score += 50

    if transaction["country"] == "Unknown":

        risk_score += 40

    return risk_score


sample_transaction = {

    "amount": 15000,

    "country": "Unknown"

}

print("Risk Score:", calculate_risk(sample_transaction))
