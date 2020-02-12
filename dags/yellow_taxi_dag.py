import os
import datetime as dt

import requests
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG

args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2020, 2, 11),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=2),
}

FILENAME = os.path.join(os.path.expanduser('~'), 'yellow_tripdata_2018-12.csv')


def download_taxi_data():
    url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2018-12.csv'
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(FILENAME, 'w', encoding='utf-8') as f:
        for chunk in response.iter_lines():
            f.write('{}\n'.format(chunk.decode('utf-8')))


def print_number_of_rows():
    lines = 0
    with open(FILENAME) as f:
        for _ in f:
            lines += 1
    print(f'There are {lines} lines in the file')


with DAG(dag_id='nyc_taxi', default_args=args, schedule_interval=None) as dag:
    create_taxi_file = PythonOperator(
        task_id='download_taxi_data',
        python_callable=download_taxi_data,
        dag=dag
    )

    print_lines = PythonOperator(
        task_id='print_number_of_lines',
        python_callable=print_number_of_rows,
        dag=dag
    )

    create_taxi_file >> print_lines
