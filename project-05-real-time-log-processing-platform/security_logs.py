import json
import random
import time

while True:

    log = {

        "event": "authentication",

        "result": random.choice(["success", "failed"]),

        "source_ip": "192.168.1.100"

    }

    print(json.dumps(log))

    time.sleep(2)
