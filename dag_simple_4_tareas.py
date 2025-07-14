from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator

# Definición del DAG
dag = DAG(
    dag_id='dag_simple_4_tareas',
    start_date=datetime(2025, 7, 14),
    schedule_interval='@daily',
    catchup=False,
)

# Tareas
tarea_1 = DummyOperator(task_id='tarea_1', dag=dag)
tarea_2 = DummyOperator(task_id='tarea_2', dag=dag)
tarea_3 = DummyOperator(task_id='tarea_3', dag=dag)
tarea_4 = DummyOperator(task_id='tarea_4', dag=dag)

# Dependencias
# t1 >> [t2, t3] permite que t2 y t3 se ejecuten en paralelo tras t1
# luego ambas convergen en t4
tarea_1 >> [tarea_2, tarea_3] >> tarea_4
