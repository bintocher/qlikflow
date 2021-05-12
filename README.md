[![GitHub stars](https://img.shields.io/github/stars/bintocher/qlikflow.svg)](https://github.com/bintocher/qlikflow/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/bintocher/qlikflow.svg)](https://github.com/bintocher/qlikflow/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/bintocher/qlikflow.svg)](https://github.com/bintocher/qlikflow/graphs/contributors)
[![GitHub license](https://img.shields.io/github/license/bintocher/qlikflow.svg)](https://github.com/bintocher/qlikflow/blob/master/LICENSE)
[![Pipy Installs](https://img.shields.io/pypi/dm/qlikflow)](https://img.shields.io/pypi/dm/qlikflow)

# qlikflow

This module allows you to create simple Apache Airflow DAG files-constructors for QlikView, Qlik Sense and NPrinting.

## Information files

- Changelog : https://github.com/bintocher/qlikflow/blob/main/CHANGELOG.md

- Manual(en) : https://github.com/bintocher/qlikflow/blob/main/doc/readme.md

- This readme : https://github.com/bintocher/qlikflow/blob/main/README.md

## Install

``` bash
pip3 install qlikflow
```

## Upgrade

``` bash
pip3 install qlikflow -U
```

## Create config-file

Open ``config_generator.py`` with your IDE editor, and set settings, save script

Then run script to create ``config.json`` file

Put this ``config.json`` file on your Apache Airflow server in folder: ``AIRFLOW_HOME/config/``

## Use in DAG-files

``` python

from airflow import DAG
from airflow.utils.dates import days_ago
from qlikflow import qlikflow
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

This code convert into DAG like this:
![image](https://user-images.githubusercontent.com/8188055/117771014-020b1600-b279-11eb-9565-de198a12c9e2.png)
