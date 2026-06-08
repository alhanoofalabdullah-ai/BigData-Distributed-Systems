# Project 02 – Hadoop Data Processing Pipeline

Enterprise Hadoop Data Processing Pipeline using HDFS, MapReduce, YARN, and batch data processing concepts.

---

# Overview

This project demonstrates a distributed data processing pipeline using Hadoop.

The system provides:

- HDFS Distributed Storage
- Batch Data Processing
- MapReduce Jobs
- Data Ingestion
- Data Validation
- Data Transformation
- Large-Scale Analytics
- Pipeline Monitoring

---

# Business Scenario

Enterprises process large volumes of historical data from multiple business systems.

Examples include:

- Sales Data
- Customer Data
- Transaction Records
- Application Logs
- Operational Data

This project demonstrates how Hadoop can process large datasets in a distributed environment.

---

# Architecture

Data Sources

↓

Data Ingestion

↓

HDFS

↓

MapReduce

↓

YARN

↓

Processed Output

↓

Analytics Reports

---

# Components

## HDFS

Responsible for:

- Distributed Storage
- Large File Management
- Data Replication
- Fault Tolerance

---

## MapReduce

Responsible for:

- Batch Processing
- Data Aggregation
- Distributed Computation
- Large Dataset Analysis

---

## YARN

Responsible for:

- Resource Management
- Job Scheduling
- Cluster Resource Allocation

---

## Data Pipeline

Responsible for:

- Data Ingestion
- Data Validation
- Data Transformation
- Output Generation

---

# Processing Workflow

1. Load raw data into HDFS

2. Validate data quality

3. Execute MapReduce job

4. Aggregate results

5. Store processed output

6. Generate processing report

---

# Example Use Case

Sales transaction data is uploaded into HDFS.

MapReduce processes the data and calculates:

- Total Sales by Region
- Total Sales by Product
- Number of Transactions
- Revenue Summary

---

# Monitoring Metrics

- hdfs_storage_used
- hdfs_storage_available
- active_datanodes
- failed_datanodes
- running_yarn_jobs
- completed_mapreduce_jobs
- failed_mapreduce_jobs
- processing_duration

---

# Technologies Used

- Apache Hadoop
- HDFS
- MapReduce
- YARN
- Python
- Docker
- Linux

---

# Skills Demonstrated

- Big Data Processing
- Hadoop Architecture
- Distributed Storage
- Batch Processing
- Data Engineering
- MapReduce Development
- Pipeline Monitoring
- Enterprise Data Analytics

---

# Author

Alhanoof Alabdullah
