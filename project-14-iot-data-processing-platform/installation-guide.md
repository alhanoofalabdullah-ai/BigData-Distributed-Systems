# Installation Guide

## Navigate to Project

```bash
cd project-14-iot-data-processing-platform
```

## Start Platform

```bash
docker-compose up -d
```

## Run Telemetry Producer

```bash
python producers/telemetry_producer.py
```

## Run Consumer

```bash
python consumers/telemetry_consumer.py
```

## Open Spark UI

```text
http://localhost:8080
```
