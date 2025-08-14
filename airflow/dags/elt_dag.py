import subprocess
from datetime import datetime, timedelta
from pathlib import Path

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

from airflow import DAG

BASE_DIR = Path(__file__).parent.parent.parent.resolve()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
}


def run_elt_script():
    script_path = "/opt/airflow/elt_script/elt_script.py"
    subprocess.run(
        ["python", script_path], capture_output=True, text=True, check=True
    )


dag = DAG(
    "elt_and_dag",
    default_args=default_args,
    description="ELT DAG with dbt",
    start_date=datetime(2025, 8, 13),
    catchup=False,
)

t1 = PythonOperator(
    task_id="run_elt_script",
    python_callable=run_elt_script,
    dag=dag,
)

t2 = DockerOperator(
    task_id="dbt_run",
    image="ghcr.io/dbt-labs/dbt-postgres:1.4.7",
    command=["run", "--profiles-dir", "/root", "--project-dir", "/dbt"],
    auto_remove=True,
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    mounts=[
        Mount(
            source=str(
                "/Users/Ismail/Library/CloudStorage/OneDrive-LAJAVANESS/Projets/Perso/data-engineering/etl-airflow/postgres_transformations"
            ),
            target="/dbt",
            type="bind",
        ),
        Mount(
            source=str("/Users/Ismail/.dbt"),
            target="/root",
            type="bind",
        ),
    ],
    mount_tmp_dir=False,
    dag=dag,
)

t1 >> t2

# t1
