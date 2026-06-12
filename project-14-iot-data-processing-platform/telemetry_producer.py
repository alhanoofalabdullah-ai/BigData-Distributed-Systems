from kafka import KafkaProducer
import json
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

event = {

    "device_id": "DEV001",

    "temperature": random.randint(20,40),

    "humidity": random.randint(40,90)

}

producer.send("telemetry-events", event)

producer.flush()

print("Telemetry Event Sent")
