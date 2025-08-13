FROM apache/airflow:2.8.1

RUN pip install apache-airflow-providers-docker

USER root
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*
USER airflow