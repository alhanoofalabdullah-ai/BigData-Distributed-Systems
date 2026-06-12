# Installation Guide

## Navigate to Project

```bash
cd project-13-real-time-fraud-detection-system
```

## Start Kafka

```bash
docker-compose up -d
```

## Run Producer

```bash
python producers/transaction_producer.py
```

## Run Consumer

```bash
python consumers/transaction_consumer.py
```
