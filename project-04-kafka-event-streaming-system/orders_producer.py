from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

order = {
    "order_id": 5001,
    "customer": "C001",
    "status": "Created"
}

producer.send("order-events", order)

producer.flush()

print("Order event sent")
