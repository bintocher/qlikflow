# qlikflow

## Description

This module allows you to create simple Apache Airflow DAG files-constructors for QlikView, Qlik Sense and NPrinting.

## Install

``` bash
pip3 install qlikflow
```

## Create config-file

Open ``config_generator.py`` with your IDE editor, and set settings, save script

Then run script to create ``config.json`` file

Put this ``config.json`` file on your Apache Airflow server in folder with ``DAG``'s

## Use in DAG-files

``` python
from airflow import DAG
from airflow.utils.dates import days_ago
import qlikflow
from datetime import datetime

tasksDict = {
    u'qliksense. Test task': {
        'Soft' : 'qs1',
        'TaskId' : 'c5d80e71-f574-4655-8874-3a6e2aed6218',
        'RandomStartDelay' : 10, 
        },
    u'np100. run nprinting tasks' : {
        'Soft' : 'np100',
        'TaskId' : [
            'taskid1',
            'taskid2',
            'taskid3',
            'taskid4',
        ],
        'Dep' : {
            u'qliksense. Test task',
            }
        }
    }

default_args  = {
    'owner': 'test',
    'depends_on_past': False,
}

dag = DAG(
    dag_id = '_my_test_dag',
    default_args = default_args ,
    start_date = days_ago(1),
    schedule_interval = '@daily',
    description = 'Default test dag',
    tags = ['qliksense', 'testing'],
    catchup = False
)

airflowTasksDict = {}
qlikflow.create_tasks(tasksDict, airflowTasksDict, dag)
```
