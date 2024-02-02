import random
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id='python_operator',
    start_date=pendulum.datetime(2023, 12, 12, tz='Asia/Seoul'),
    schedule='0 0 * * *',
    catchup=False
) as dag:

    def select_drink():
        drink = ['ice americano', 'cola', 'orange juice', 'cider']
        idx = random.randint(0, len(drink))
        return drink[idx]

    t1 = PythonOperator(
        task_id='t1',
        python_callable=select_drink
    )

    t2 = PythonOperator(
        task_id='t2',
        python_callable=select_drink
    )

    t1 >> t2
