from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 8),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'tags': ['sample'],
}
dag = DAG('hellooo', default_args=default_args, schedule_interval=timedelta(days=1))
t1 = BashOperator(
    task_id='say_hello',
    bash_command='echo "Hello Neal this is Airflow!"',
    dag=dag,
)
