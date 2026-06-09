from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

event = {
    "transaction_id": 1001,
    "amount": 4500,
    "region": "Riyadh"
}

producer.send("sales-events", event)

producer.flush()

print("Sales event sent")
