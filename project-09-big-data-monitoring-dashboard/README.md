# Project 09 – Big Data Monitoring Dashboard

Enterprise Big Data Monitoring Dashboard using Prometheus and Grafana for monitoring Hadoop, Spark, Kafka, and Cassandra environments.

---

# Overview

This project demonstrates centralized monitoring for Big Data platforms.

The platform provides:

- Hadoop Monitoring
- Spark Monitoring
- Kafka Monitoring
- Cassandra Monitoring
- Cluster Health Monitoring
- Resource Utilization Tracking
- Capacity Planning
- Executive Reporting

---

# Business Scenario

Enterprise Big Data environments contain multiple platforms:

- Hadoop Clusters
- Spark Processing Engines
- Kafka Streaming Platforms
- Cassandra Databases

Without centralized monitoring:

- Failures remain undetected
- Resource waste increases
- Performance issues impact analytics
- Troubleshooting becomes difficult

This project provides a single monitoring platform.

---

# Architecture

Hadoop Cluster

↓

Spark Cluster

↓

Kafka Platform

↓

Cassandra Cluster

↓

Prometheus

↓

Grafana

↓

Operations Team

---

# Components

## Hadoop Monitoring

Monitors:

- NameNode Health
- DataNode Health
- HDFS Capacity
- Running Jobs

---

## Spark Monitoring

Monitors:

- Active Applications
- Executors
- Running Jobs
- Resource Usage

---

## Kafka Monitoring

Monitors:

- Topics
- Partitions
- Consumer Lag
- Broker Health

---

## Cassandra Monitoring

Monitors:

- Node Status
- Read Latency
- Write Latency
- Replication Health

---

## Executive Dashboard

Monitors:

- Overall Platform Health
- Active Clusters
- Resource Utilization
- Critical Alerts

---

# Dashboard Panels

## Hadoop Dashboard

Displays:

- HDFS Utilization
- Active DataNodes
- Running Jobs
- Cluster Status

---

## Spark Dashboard

Displays:

- Spark Applications
- Executor Usage
- Job Performance
- Resource Consumption

---

## Kafka Dashboard

Displays:

- Topics
- Messages Per Second
- Consumer Lag
- Broker Status

---

## Cassandra Dashboard

Displays:

- Cluster Health
- Read Latency
- Write Latency
- Replication Status

---

## Executive Dashboard

Displays:

- Cluster Health Score
- Active Alerts
- Resource Consumption
- Business Impact Indicators

---

# Monitoring Metrics

- cluster_health_score
- hdfs_utilization
- active_spark_jobs
- kafka_consumer_lag
- cassandra_read_latency
- cassandra_write_latency
- cpu_utilization
- memory_utilization
- storage_utilization

---

# Alert Rules

## Cluster Down

Severity:

Critical

---

## Storage Capacity High

Severity:

Warning

---

## Kafka Consumer Lag

Severity:

Warning

---

## Cassandra Node Failure

Severity:

Critical

---

## Spark Job Failure

Severity:

Critical

---

# Technologies Used

- Prometheus
- Grafana
- Hadoop
- Spark
- Kafka
- Cassandra
- Docker
- Linux

---

# Skills Demonstrated

- Big Data Monitoring
- Grafana Dashboards
- Prometheus Administration
- Cluster Monitoring
- Performance Analysis
- Capacity Planning
- Enterprise Monitoring
- Platform Operations

---

# Author

Alhanoof Alabdullah
