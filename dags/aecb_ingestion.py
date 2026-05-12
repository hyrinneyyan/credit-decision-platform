from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def pull_aecb_files():
    print("Pulling AECB XML files")


def validate_schema():
    print("Validating XML schema")


def normalize_aecb():
    print("Normalizing AECB records")

with DAG(
    dag_id="aecb_ingestion",
    start_date=datetime(2025, 1, 1),
    schedule="@hourly",
    catchup=False
) as dag:

    ingest = PythonOperator(
        task_id="pull_sftp_xml",
        python_callable=pull_aecb_files
    )

    validate = PythonOperator(
        task_id="validate_xml",
        python_callable=validate_schema
    )

    normalize = PythonOperator(
        task_id="normalize_records",
        python_callable=normalize_aecb
    )

    ingest >> validate >> normalize
