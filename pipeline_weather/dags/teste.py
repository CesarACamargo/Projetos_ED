from airflow.sdk import dag, task
from datetime import datetime

@dag(
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["teste"],
)
def teste_dag():

    @task
    def inicio():
        print("Airflow funcionando!")

    inicio()

teste_dag()
