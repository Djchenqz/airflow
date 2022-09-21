from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.python import PythonOperator
import json
from datetime import timedelta
#from pytz import timezone
NAMESPACE = "bitools"
IMAGE = "406987170712.dkr.ecr.ap-northeast-1.amazonaws.com/airflow:latest"


def demo(kwargs):
    print('kwargs: ', kwargs)


default_args = {
    'owner': 'airflow',
    #'start_date': datetime(2021,10,29,10, tzinfo=timezone('Asia/Shanghai'))
    'start_date': days_ago(1),
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
        dag_id='dag_test',
        default_args=default_args,
        tags=['test'],
        schedule_interval=None,
        #schedule_interval=None,
        dagrun_timeout=timedelta(minutes=60),
        catchup=False
) as dag:
    """
    demo_task = KubernetesPodOperator(
                task_id='task_test',
                namespace=NAMESPACE,
                image=IMAGE,
                cmds=['python'],
                arguments=[
                    "dags/scripts/executor.py",
                    "demo"
                ],
                name="test",
                get_logs=True,
                is_delete_operator_pod=True,
            )
    """
    demo_task_fargate = KubernetesPodOperator(
                task_id='task_test_fargate',
                namespace=NAMESPACE,
                image=IMAGE,
                cmds=['python'],
                arguments=[
                    "dags/scripts/executor.py",
                    "demo"
                ],
                name="test",
                labels={"infrastructure": "fargate"},
                get_logs=True,
                is_delete_operator_pod=True,
                resources={
                    "request_cpu": "500m",
                    "request_memory": "2048Mi"}
                    #"limit_cpu": "{{ dag_run.conf['cpu'] }}",
                    #"limit_memory": "{{ dag_run.conf['memory'] }}"},
            )
    """
    demo_task = PythonOperator(
                task_id='demo',
                python_callable=demo,
                op_kwargs={'args': 'this is a demo'}
            )
    """
