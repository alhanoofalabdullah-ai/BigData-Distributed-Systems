from kafka import KafkaProducer
import json

producer = KafkaProducer(

    bootstrap_servers="localhost:9092",

    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

log_event = {

    "event": "user_login",

    "status": "success"

}

producer.send("application-logs", log_event)

producer.flush()

print("Log sent")
