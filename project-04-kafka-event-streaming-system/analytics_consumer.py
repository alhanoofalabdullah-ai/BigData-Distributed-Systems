from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "analytics-events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

for event in consumer:

    print("Analytics Event:", event.value)
