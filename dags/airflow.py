import airflow
from airflow import DAG
from datetime import timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.utils.dates import days_ago


default_args={"owner":'airflow', "start_date":datetime(2021,3,29)}

with DAG (dag_id="workflow",default_args=default_args,schedule_interval="daily") as dag:
    insert_records=MySqlOperator(
        task_id="insert_data"
        mysql_conn_id=""
        sql="LOAD DATA INFILE ..\yellow_tripdata_2021-01 (1).csv INTO TABLE data FIELDS TERMINATED "
    )
