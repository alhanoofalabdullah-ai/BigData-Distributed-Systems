# Installation Guide

## Navigate to Project

```bash
cd project-05-real-time-log-processing-platform
```

## Start Platform

```bash
docker-compose up -d
```

## Create Topics

```bash
docker exec kafka kafka-topics \
--create \
--topic application-logs \
--bootstrap-server localhost:9092
```

## Run Producer

```bash
python producers/kafka_log_producer.py
```

## Run Consumer

```bash
python consumers/log_consumer.py
```

## Open Elasticsearch

```text
http://localhost:9200
```
