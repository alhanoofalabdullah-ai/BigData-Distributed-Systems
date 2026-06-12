from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

transaction = {

    "transaction_id": "TX1001",

    "customer_id": "C001",

    "amount": 15000,

    "country": "Unknown"

}

producer.send("transactions", transaction)

producer.flush()

print("Transaction sent")
