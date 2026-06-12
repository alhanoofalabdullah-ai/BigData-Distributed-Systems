# Installation Guide

## Navigate to Project

```bash
cd project-17-multi-cluster-data-replication-system
```

## Start Environment

```bash
docker-compose up -d
```

## Run Replication Engine

```bash
python replication/replication-engine.py
```

## Test Failover

```bash
python disaster-recovery/failover-manager.py
```
