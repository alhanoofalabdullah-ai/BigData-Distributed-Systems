from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(

    "security-logs",

    bootstrap_servers="localhost:9092",

    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

for event in consumer:

    if event.value["result"] == "failed":

        print("Security Alert Generated")
