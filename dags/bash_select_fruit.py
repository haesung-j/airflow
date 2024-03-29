from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="bash_select_fruit",
    schedule="10 0 * * 0,6",  # 주말 0시 10분마다
    start_date=pendulum.datetime(2024,1,1, tz='Asia/Seoul'),
    catchup=False
) as dag:

    t1_orange = BashOperator(
        task_id="t1_orange",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE"
    )

    t2_banana = BashOperator(
        task_id="t2_banana",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh BANANA"
    )

    t1_orange >> t2_banana
