from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Definir la función que será ejecutada por la tarea
def tarea_1():
    print("Esta es la Tarea 1")

def tarea_2():
    print("Esta es la Tarea 2")

# Definir el DAG
dag = DAG(
    'mi_dag_dumi',  # Nombre del DAG
    description='Un ejemplo simple de DAG en Airflow',  # Descripción
    schedule_interval=None,  # No programado, solo se ejecuta cuando se dispara manualmente
    start_date=datetime(2025, 4, 14),  # Fecha de inicio
    catchup=False,  # No hacer retroceso para fechas anteriores
)

# Definir las tareas
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

# Establecer dependencias: tarea1 debe ejecutarse antes que tarea2
tarea1 >> tarea2
