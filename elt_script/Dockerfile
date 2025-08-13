FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y wget gnupg lsb-release cron procps && \
    echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && \
    apt-get install -y postgresql-client-17 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY elt_script.py .
COPY start.sh /app/start.sh
COPY crontab /etc/cron.d/etl-cron

CMD ["/bin/bash", "/app/start.sh"]
