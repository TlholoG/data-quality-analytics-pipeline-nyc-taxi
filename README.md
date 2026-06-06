# Data Quality & Analytics Pipeline (NYC Taxi Dataset)

## 📌 Overview

This project implements an end-to-end data engineering pipeline for processing and analysing NYC Taxi trip data. The pipeline ingests raw data, loads it into a cloud data warehouse, transforms it into analytics-ready models, and applies data quality checks to ensure reliability.

The goal of this project is to demonstrate practical data engineering skills including ingestion, transformation, and validation using modern data stack tools.

---

## 🏗️ Architecture

**Pipeline Flow:**

1. Data Ingestion (Python)
2. Data Storage (Google BigQuery)
3. Transformation Layer (dbt)
4. Data Quality Checks (dbt tests)
5. Analytics & Visualization (Google Data Studio)

---

## ⚙️ Tech Stack

* **Python** – Data ingestion and preprocessing
* **Google BigQuery** – Cloud data warehouse
* **dbt (Data Build Tool)** – Data transformation and modeling
* **SQL** – Data transformation logic
* **Google Data Studio** – Dashboarding and reporting

---

## 📊 Data Pipeline Details

### 1. Data Ingestion

* Extracted NYC Taxi dataset
* Automated loading into BigQuery
* Structured raw data into staging tables

### 2. Data Transformation (dbt)

* Built modular models:

  * Staging layer
  * Core fact and dimension tables
* Applied transformations for analytics use cases

### 3. Data Quality

* Implemented dbt tests:

  * Not null constraints
  * Unique key validation
  * Referential integrity checks

---

## 📈 Analytics Use Cases

* Trip volume trends over time
* Revenue analysis
* Pickup and drop-off location insights
* Peak demand patterns

---

## 🚧 Work in Progress

* Orchestration using Apache Airflow (planned)
* Advanced data quality monitoring
* Dashboard development in Google Data Studio

---

## 📁 Project Structure

```bash
├── ingestion/        # Python scripts for data ingestion
├── models/           # dbt models (staging, core)
├── tests/            # dbt tests
├── dashboards/       # (Planned) reporting layer
├── README.md
```

---

## 🚀 Key Learnings

* Building scalable data pipelines using cloud-native tools
* Applying modular data modeling with dbt
* Ensuring data reliability through testing
* Designing analytics-ready datasets

---

## 📬 Future Improvements

* Implement Airflow for pipeline orchestration
* Add incremental models for scalability
* Introduce monitoring and alerting
* Optimize cost and performance in BigQuery

---
