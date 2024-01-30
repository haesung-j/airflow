import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id='dags_bash_operator',  # 화면 표시 이름: 주로 파일명과 일치시킴
    schedule="0 0 * * *",  # cron 스케줄 (분 시 일 월 요일)
    start_date=pendulum.datetime(2024, 3, 1, tz='Asia/Seoul'),  # 시작 날짜
    catchup=False,  # (현재 3월 1일일 때, start_date가 1월 1일부터라면, True인 경우 누락 구간도 돌림(1/1~2/28)
    # dagrun_timeout=datetime.timedelta(minutes=60),  # 이 DAG이 60분이상 돌면 실패
    tags=['tag', 'tag2'],  # UI상 tag 표기
    # params={'example_key': 'example_value'}, # DAG 선언 밑 TASK들을 만들 때 공통적으로 넘길 파라미터
) as dag:
    # TASK 객체 생성
    bash_task1 = BashOperator(
        task_id="bash_task1",
        bash_command="echo this is bash_task1",  # 어떤 쉘 스크립트를 실행할 것인지
    )

    bash_task2 = BashOperator(
        task_id='bash_task2',
        bash_command="echo $HOSTNAME"  # HOSTNAME 환경변수 출력
    )

    # task 수행 순서 정의
    bash_task1 >> bash_task2
