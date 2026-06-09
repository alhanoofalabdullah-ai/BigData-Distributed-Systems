import json
import random
import time

while True:

    log = {

        "event": "user_login",

        "status": random.choice(["success", "failed"]),

        "timestamp": time.time()

    }

    print(json.dumps(log))

    time.sleep(1)
