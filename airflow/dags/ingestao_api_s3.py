from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import boto3
import json

def salvar_dados_no_s3():
    url = "https://jsonplaceholder.typicode.com/posts"
    resposta = requests.get(url)
    dados = resposta.json()

    s3 = boto3.client('s3')
    bucket = "projeto-ingestao-airflow-250309"  # ajuste se seu bucket tiver outro nome
    hoje = datetime.now()
    path = f"raw/jsonplaceholder/ano={hoje.year}/mes={hoje.month:02}/dia={hoje.day:02}/posts.json"

    s3.put_object(Bucket=bucket, Key=path, Body=json.dumps(dados))

with DAG(
    dag_id="ingestao_api_s3",
    start_date=datetime(2025, 5, 19),
    schedule_interval=None,  # manual
    catchup=False,
    tags=["projeto-ingestao", "api", "s3"],
) as dag:

    tarefa_ingestao = PythonOperator(
        task_id="salvar_json_api_no_s3",
        python_callable=salvar_dados_no_s3,
    )
