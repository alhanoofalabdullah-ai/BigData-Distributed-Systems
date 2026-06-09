# Installation Guide

## Navigate to Project

```bash
cd project-02-hadoop-data-processing-pipeline
```

## Start Hadoop Cluster

```bash
docker-compose up -d
```

## Access Hadoop UI

```text
HDFS NameNode:
http://localhost:9870

YARN ResourceManager:
http://localhost:8088
```

## Run Data Ingestion

```bash
python data-pipeline/ingestion.py
```

## Run Validation

```bash
python data-pipeline/validation.py
```
