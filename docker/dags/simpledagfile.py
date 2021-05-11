"""
   Copyright 2021 Stanislav Chernov

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

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