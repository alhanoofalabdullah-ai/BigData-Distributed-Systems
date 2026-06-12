from fraud_rules import detect_fraud

transaction = {

    "amount": 25000

}

if detect_fraud(transaction):

    print("Fraud Alert Generated")
