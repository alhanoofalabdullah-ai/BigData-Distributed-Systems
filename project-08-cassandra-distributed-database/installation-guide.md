# Installation Guide

## Navigate to Project

```bash
cd project-08-cassandra-distributed-database
```

## Start Cassandra Cluster

```bash
docker-compose up -d
```

## Create Keyspace

```bash
cqlsh -f cassandra/keyspace.cql
```

## Create Tables

```bash
cqlsh -f schemas/customers_table.cql

cqlsh -f schemas/orders_table.cql

cqlsh -f schemas/products_table.cql
```

## Run Python Scripts

```bash
pip install cassandra-driver

python scripts/insert_customers.py
```
