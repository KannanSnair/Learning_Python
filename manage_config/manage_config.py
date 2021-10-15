"""Manage Configs """

import json
import logging

from airflow import configuration as conf


def default_init(dag_id):
  logging.info("DAG Id" + dag_id)
  airflow_dag_folder_path = conf.get("core", "dags_folder")
  dag_config_path_format = "{airflow_home_path_param}/dag_config/{dag_id_param}/config.json"
  dag_abs_config_path = dag_config_path_format.format(airflow_home_path_param=str(airflow_dag_folder_path),
                                                      dag_id_param=dag_id)
  logging.info("DAG absolute config path" + dag_abs_config_path)
  dag_config = None
  with open(dag_abs_config_path) as configFile:
    dag_config = json.load(configFile)
  return dag_config