'''
=================================================
Milestone 3

Nama  : Azhar Muhammad
Batch : RMT - 042

Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch. Adapun dataset yang dipakai adalah dataset mengenai penjualan mobil di Indonesia selama tahun 2020.
=================================================
'''

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from sqlalchemy import create_engine
from elasticsearch import Elasticsearch, helpers
import os

# --- Fungsi: Fetch dari PostgreSQL ---
def fetch_postgres():
    engine = create_engine("postgresql://airflow:airflow@postgres:5432/airflow")
    query = "SELECT * FROM table_m3"
    df = pd.read_sql(query, con=engine)

    os.makedirs("data", exist_ok=True)  # Membuat folder jika belum ada
    df.to_csv("/opt/airflow/data/raw_data.csv", index=False)

# --- Fungsi: Data Cleaning dan simpan ke CSV ---
def clean_data():
    df = pd.read_csv("/opt/airflow/data/raw_data.csv")

    # hapus duplikat data
    df = df.drop_duplicates()
    
    # mengubah nama kolom menjadi lowercase
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    # hapus missing value
    df = df.dropna()
    
    # simpan hasil cleaning data
    df.to_csv("/opt/airflow/data/clean_data.csv", index=False)


# --- Fungsi: Post ke Elasticsearch ---
def post_to_elasticsearch():
    es = Elasticsearch("http://elasticsearch:9200")

    df = pd.read_csv("/opt/airflow/data/clean_data.csv")

    actions = [
        {
            "_index": "table_m3_index",
            "_source": row.to_dict()
        }
        for _, row in df.iterrows()
    ]
    
    helpers.bulk(es, actions)

# --- DAG Definition ---
default_args = {
    'owner': 'azhar_muhammad',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'P2M3_azhar_muhammad_DAG',
    default_args=default_args,
    # schedule_interval='10 9-9/10 * * 6',
    # catchup=True, --> syntax untuk penjadwalan.
    schedule_interval=None,
    catchup=False,
    description='Milestone 3 DAG by Azhar Muhammad',
)

fetch_task = PythonOperator(
    task_id='fetch_from_postgresql',
    python_callable=fetch_postgres,
    dag=dag
)

clean_task = PythonOperator(
    task_id='data_cleaning',
    python_callable=clean_data,
    dag=dag
)

post_task = PythonOperator(
    task_id='post_to_elasticsearch',
    python_callable=post_to_elasticsearch,
    dag=dag
)

fetch_task >> clean_task >> post_task
