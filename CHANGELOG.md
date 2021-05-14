# Changelog

## verison 1.0.12

### Change

- currently, config.json file is read when the task is started, previously, it was read when the dag was started

### Fix

- airflow task was completed without waiting for the task to be completed in qlik sense server

## verison 1.0.11

- some fixes, disable debug msg's

## verison 1.0.10

testing version

### Fix

- remove unused modules

## verison 1.0.9

### Add

- update documentations files; for config.json, dag creation dict{} and folders in docker folder

## verison 1.0.8

### Fix

- fix error `File "/home/airflow/.local/lib/python3.6/site-packages/qlikflow/qlikflow.py", line 459, in create_aftask`

### Add

- add `dockerfile` and update `docker-compose.yaml`

## verison 1.0.7

### Add

- add dependency apache-airflow[telegram]

- in `readme.md` add shields for git repository and pipy installs

### Change

- remove "root" param in certs for qlik sense servers

### Fix

- fix path for qlik sense certificates


## verison 1.0.6

- fix config.json location to AIRFLOW_HOME/config/

- fix cert's location to AIRFLOW_HOME/cert/

## verison 1.0.5

- lowered version for required dependencies

- exclude airflow dep's from install

## verison 1.0.4

- update config.json folder from AIRFLOW_HOME env

## verison 1.0.3

- update documentation info in pip package

## verison 1.0.2

- add package dependencies

## verison 1.0.1

- remove unused files

## version 1.0.0

- initial commit

- work with Qlik Sense, QlikView and NPrinting tasks