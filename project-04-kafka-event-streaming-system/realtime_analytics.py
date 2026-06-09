from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "sales-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

total_sales = 0

for message in consumer:

    total_sales += message.value["amount"]

    print(f"Total Sales: {total_sales}")
