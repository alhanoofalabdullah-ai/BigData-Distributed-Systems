from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "sales-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

count = 0

for message in consumer:

    count += 1

    print(f"Processed Events: {count}")
