# Installation Guide

## Navigate to Project

```bash
cd project-11-distributed-search-engine
```

## Start Elasticsearch

```bash
docker-compose up -d
```

## Install Dependencies

```bash
pip install elasticsearch
```

## Create Index

```bash
python indexing/create_index.py
```

## Load Data

```bash
python indexing/bulk_index.py
```

## Run Search

```bash
python search/basic_search.py
```

## Open Kibana

```text
http://localhost:5601
```
