from airflow import models
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

DAG_ID = 'docker_test'

with models.DAG(
    DAG_ID,
    schedule_interval="@once",
    start_date=days_ago(0),
    catchup=False,
    tags=["example", "docker"],
) as dag:
    t1 = BashOperator(task_id='print_date', bash_command='date', dag=dag)
    t2 = BashOperator(task_id='sleep', bash_command='sleep 5', retries=3, dag=dag)
    # [START howto_operator_docker]
    t3 = DockerOperator(
        docker_url='unix://var/run/docker.sock',  # Set your docker URL
        command='/bin/sleep 10',
        image='busybox:latest',
        network_mode='bridge',
        task_id='docker_op_tester',
        dag=dag,
    )
    # [END howto_operator_docker]
    t4 = BashOperator(task_id='print_hello', bash_command='echo "hello world!!!"', dag=dag)
    (
        # TEST BODY
        t1
        >> [t2, t3]
        >> t4
    )
