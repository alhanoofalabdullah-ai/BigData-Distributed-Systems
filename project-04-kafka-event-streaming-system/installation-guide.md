# Installation Guide

## Navigate to Project

```bash
cd project-04-kafka-event-streaming-system
```

## Start Kafka

```bash
docker-compose up -d
```

## Create Topics

```bash
docker exec kafka kafka-topics \
--create \
--topic sales-events \
--bootstrap-server localhost:9092
```

## Run Producer

```bash
python producers/sales_producer.py
```

## Run Consumer

```bash
python consumers/sales_consumer.py
```
