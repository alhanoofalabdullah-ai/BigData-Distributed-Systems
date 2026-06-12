# Project 12 – Large Scale Data Warehouse

Enterprise Data Warehouse Platform using Star Schema architecture for Business Intelligence, OLAP analytics, and executive reporting.

---

# Overview

This project demonstrates enterprise-level data warehouse architecture.

The platform provides:

- Enterprise Data Warehouse
- Star Schema Modeling
- Fact Tables
- Dimension Tables
- OLAP Analytics
- Executive Reporting
- Business Intelligence
- Enterprise Data Analytics

---

# Business Scenario

Organizations collect data from multiple systems:

- ERP Systems
- CRM Platforms
- Sales Systems
- Finance Systems
- Customer Applications

Operational systems are not optimized for analytics.

A Data Warehouse provides a centralized analytical platform.

---

# Architecture

Operational Systems

↓

ETL Layer

↓

Data Warehouse

↓

Fact Tables

↓

Dimension Tables

↓

OLAP Analytics

↓

Executive Dashboards

---

# Components

## Fact Table

Stores:

- Sales Transactions
- Revenue Metrics
- Quantity Sold
- Business Measures

---

## Customer Dimension

Stores:

- Customer Information
- Customer Segments
- Customer Geography

---

## Product Dimension

Stores:

- Product Details
- Product Categories
- Product Hierarchies

---

## Date Dimension

Stores:

- Day
- Month
- Quarter
- Year

---

## Region Dimension

Stores:

- Country
- Region
- City
- Sales Territory

---

# Star Schema

Fact_Sales

↓

Dim_Customers

↓

Dim_Products

↓

Dim_Date

↓

Dim_Region

---

# Analytics Use Cases

## Revenue Analysis

Analyzes:

- Revenue Trends
- Monthly Revenue
- Annual Revenue
- Revenue by Region

---

## Customer Analysis

Analyzes:

- Customer Growth
- Customer Segments
- Customer Value
- Customer Retention

---

## Product Analysis

Analyzes:

- Top Products
- Product Revenue
- Product Categories
- Product Performance

---

## Regional Analysis

Analyzes:

- Regional Revenue
- Regional Growth
- Market Performance

---

# Monitoring Metrics

- warehouse_size
- query_execution_time
- fact_table_records
- dimension_table_records
- etl_success_rate
- warehouse_growth_rate
- active_queries
- storage_utilization

---

# Technologies Used

- SQL
- PostgreSQL
- Python
- Docker
- Data Warehousing
- OLAP Concepts

---

# Skills Demonstrated

- Data Warehouse Design
- Star Schema Modeling
- Data Modeling
- Business Intelligence
- OLAP Analytics
- SQL Development
- ETL Development
- Enterprise Reporting

---

# Author

Alhanoof Alabdullah
