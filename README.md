# ETL Pipeline with Airflow, Docker & dbt

This project is an ELT pipeline using Apache Airflow for orchestration. It extracts data from a PostgreSQL source, loads it into a destination database via a Python script, and applies transformations using dbt.

## Stack

- PostgreSQL (source + destination)
- Python ETL script (run as an Airflow task)
- dbt (for transformations)
- Apache Airflow (for orchestration & scheduling)
- Docker Compose (for containerized setup)

## How It Works

1. elt_script.py runs as the first Airflow task. It extracts data from source_postgres and inserts it into destination_postgres.
2. Once the ELT script completes, a second task runs dbt models defined in postgres_transformations/.
3. Airflow ensures transformations only start after data is loaded.

## Setup

```bash
docker compose up --build
```

## ✨ Author  
Ismail El Hatimi (📍 Data Scientist & Engineer)  

🔗 [LinkedIn](https://www.linkedin.com/in/isma%C3%AFl-e-59b45737/)
