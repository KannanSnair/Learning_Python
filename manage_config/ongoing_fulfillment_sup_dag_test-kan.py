import logging
import re
import datetime

from airflow import DAG
from airflow.contrib.operators.dataflow_operator import DataFlowJavaOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from manage_config import default_init

#Dag Details
dagname = 'ews_de_ongoing_fulfillment_workflow'
dag_id_prefix = os.path.basename(__file__).replace(".pyc", "").replace(".py", "")
dag_config = default_init(dag_id_prefix)
processor_job_name = 'ews-de-nstf-billing-extract-processor'##dataflow name, not sure??

tempLocation = dag_config['tempLocation']
stagingLocation = dag_config['stagingLocation']
project = dag_config['project']
workerZone = dag_config['workerZone']
region = dag_config['region']
usePublicIps = dag_config['usePublicIps']
serviceAccount = dag_config['serviceAccount']
subnetwork = dag_config['subnetwork']
workerMachineType = dag_config['workerMachineType']
numWorkers = dag_config['numWorkers']
numberOfWorkerHarnessThreads = dag_config['numberOfWorkerHarnessThreads']
autoscalingAlgorithm = dag_config['autoscalingAlgorithm']
bigquery_conn_id = dag_config['bigquery_conn_id']

processorBucketName = dag_config['processor']['bucketName']
processorPropertyFileLocation = dag_config['processor']['configFileLocation']
processorLabels = dag_config['processor']['labels']
processorJarLocation = dag_config['processor']['jarLocation']

default_dag_args = {
    'dataflow_default_options': {
        'tempLocation': tempLocation,
        'stagingLocation': stagingLocation,
        'project': project,
        'workerZone': workerZone,
        'region': region,
        'usePublicIps': usePublicIps,
        'serviceAccount': serviceAccount,
        'subnetwork': subnetwork,
        'workerMachineType': workerMachineType,
        'numWorkers': numWorkers,
        'numberOfWorkerHarnessThreads': numberOfWorkerHarnessThreads,
        'autoscalingAlgorithm': autoscalingAlgorithm,

    }
}
ongoing_fulfillment_dataflow_job_args = {
    'startDate': '{{ ti.xcom_pull(task_ids="get_dates_for_df", key="start_date") }}' ,
    'endDate': '{{ ti.xcom_pull(task_ids="get_dates_for_df", key="end_date") }}',
    'bucketName': processorBucketName,
    'propertyFileLocation': processorPropertyFileLocation,
    'labels': processorLabels
}
dag = DAG(
    start_date=datetime.datetime(1970, 1, 1),
    dag_id=dagname,
    catchup=False,
    #schedule_interval=cronExpression,####needed ?
    default_args=default_dag_args)

start_dataflow = DataFlowJavaOperator(
    task_id='ongoing-fulfillment',
    jar=processorJarLocation,
    options=ongoing_fulfillment_dataflow_job_args,
    job_name=processor_job_name,
    gcp_conn_id=bigquery_conn_id,
    dag=dag)


#startdata/enddate -> dataflow->
def read_pubsub(**kwargs):
    kwargs['ti'].xcom_push(key='start_date', value='')
    kwargs['ti'].xcom_push(key='end_date', value='')


start = DummyOperator(
    task_id='start',
    dag=dag
)
get_dates_for_df = PythonOperator(
    date_for_dataflow_input = read_pubsub,
    provide_context=True
)

start \
>> get_dates_for_df \
>> start_dataflow \


