from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

producer.send(
    "sales-events",
    {
        "transaction_id": 1001,
        "amount": 4500
    }
)

producer.flush()
