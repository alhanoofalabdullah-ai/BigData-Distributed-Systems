def detect_anomaly(temperature):

    if temperature > 35:

        return True

    return False

print(detect_anomaly(38))
