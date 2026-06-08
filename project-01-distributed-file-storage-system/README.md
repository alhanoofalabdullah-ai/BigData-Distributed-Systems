# Project 01 – Distributed File Storage System

Enterprise Distributed File Storage System inspired by Google File System (GFS), HDFS, and modern distributed storage architectures.

---

# Overview

This project demonstrates a scalable distributed file storage platform.

The system provides:

- Distributed File Storage
- File Replication
- Fault Tolerance
- High Availability
- Metadata Management
- Storage Monitoring
- Node Health Monitoring
- Distributed Data Management

---

# Business Scenario

Modern enterprises store massive amounts of data.

Challenges include:

- Storage Scalability
- Data Availability
- Node Failures
- Data Redundancy
- Storage Optimization

This project solves these challenges through distributed storage architecture.

---

# Architecture

Client

↓

Storage Gateway

↓

Metadata Server

↓

Storage Nodes

↓

Replicated Storage Blocks

---

# Components

## Metadata Management

Stores:

- File Locations
- Replication Information
- Node Information
- Storage Capacity

---

## Storage Nodes

Responsible for:

- File Storage
- Block Replication
- Health Reporting
- Capacity Monitoring

---

## Replication Engine

Provides:

- Data Redundancy
- High Availability
- Failover Recovery
- Data Protection

---

## Monitoring System

Tracks:

- Node Health
- Storage Utilization
- Replication Status
- System Availability

---

# Dashboard Panels

## Storage Overview

Displays:

- Total Capacity
- Used Capacity
- Available Capacity
- Replication Health

---

## Node Dashboard

Displays:

- Active Nodes
- Failed Nodes
- Storage Usage
- Node Performance

---

## Replication Dashboard

Displays:

- Replication Status
- Replication Failures
- Data Redundancy
- Recovery Events

---

# Monitoring Metrics

- total_storage
- used_storage
- available_storage
- active_nodes
- failed_nodes
- replication_factor
- storage_growth_rate
- node_health_score

---

# Technologies Used

- Python
- Docker
- Linux
- Distributed Storage Concepts
- JSON Metadata Management

---

# Skills Demonstrated

- Distributed Systems
- Storage Architecture
- Data Replication
- High Availability
- Fault Tolerance
- Storage Monitoring
- Data Engineering Fundamentals
- Enterprise Architecture

---

# Author

Alhanoof Alabdullah
