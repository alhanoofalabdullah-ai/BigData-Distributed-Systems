# Installation Guide

## Navigate to Project

```bash
cd project-12-large-scale-data-warehouse
```

## Start PostgreSQL

```bash
docker-compose up -d
```

## Execute Schema

```bash
psql -U admin -d enterprise_dw -f warehouse/fact-sales.sql
```

## Run ETL

```bash
python etl/warehouse_etl.py
```

## Execute Analytics

```bash
psql -U admin -d enterprise_dw -f analytics/revenue_analysis.sql
```
