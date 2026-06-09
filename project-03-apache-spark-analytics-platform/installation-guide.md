# Installation Guide

## Navigate to Project

```bash
cd project-03-apache-spark-analytics-platform
```

## Start Spark Cluster

```bash
docker-compose up -d
```

## Open Spark Master UI

```text
http://localhost:8080
```

## Run Spark Job

```bash
spark-submit jobs/sales_analytics.py
```
