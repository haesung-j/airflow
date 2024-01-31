from airflow import DAG
import pendulum
from airflow.operators.empty import EmptyOperator  # 아무것도 하지 않는 오퍼레이터

"""
각 Task를 생성한 후, Task간 연결하여 그래프 확인
"""

with DAG(
    dag_id="connet_test",
    schedule=None,
    start_date=pendulum.datetime(2023, 1, 1, tz='Asia/Seoul'),
    catchup=False
) as dag:
    task1 = EmptyOperator(
        task_id='t1'
    )

    task2 = EmptyOperator(
        task_id='t2'
    )

    task3 = EmptyOperator(
        task_id='t3'
    )

    task4 = EmptyOperator(
        task_id='t4'
    )

    task5 = EmptyOperator(
        task_id='t5'
    )

    task6 = EmptyOperator(
        task_id='t6'
    )

    task7 = EmptyOperator(
        task_id='t7'
    )

    task8 = EmptyOperator(
        task_id='t8'
    )

    task1 >> [task2, task3] >> task4
    task5 >> task4
    [task4, task7] >> task6 >> task8