from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def tarea_1():
    print("Esta es la Tarea 1")

def tarea_2():
    print("Esta es la Tarea 2")
# Definición del DAG con control de acceso a nivel de DAG
dag = DAG(
    'dag_prueba5',
    description='Un ejemplo simple de DAG en Airflow',
    schedule_interval=None,
    tags=["rol3","Fareco","Roles"],
    start_date=datetime(2025, 4, 14),
    catchup=False,
    access_control={
        "Grupo5": {
            "can_read",
            "can_edit"
        }
        },
)

tarea1 = PythonOperator(
    task_id='tarea_1',
    python_callable=tarea_1,
    dag=dag,
)

tarea2 = PythonOperator(
    task_id='tarea_2',
    python_callable=tarea_2,
    dag=dag,
)

tarea1 >> tarea2
