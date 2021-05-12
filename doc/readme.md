# Documentation

In progress...


## How to configure tasksDict = {} in DAG files

``` python
tasksDict = {
    # Name of Task
    u'NP. Monitoring': {
        # -----
        # Pool for this task, if not set - will be used default from config.json
        'Pool' : 'default_pool', 
        # -----
        # Soft name, 2 left char will select python_operator function for run task
        # Required and possible values: np , qs , qv, sleep
        # After the name - any characters, it is important that the names written here match the names in config.json
        'Soft' : 'np1',
        # 'Soft' : 'qs-dev',
        # 'Soft' : 'qstesting',
        # -----
        # GUID(s) of task to run
        # in qs - you can see it in taks page, in np - we use "App GUIDs", in qv - look at dictribution folder or qlikview in xml's
        'TaskId' : 'bc58a89f-4401-4769-abbd-f515e13d386e', 
        # you can use lists to create tasks with the same parameters.
        # very convenient to use for NPrinting tasks
        # 'TaskId' : [
        #    'task1_guid',
        #    'task2_guid',
        #    'task3_guid',
        #    'task4_guid',
        #    'task5_guid',
        #     ],
        # -----
        # start time: hour, minute - without leading zeros
        # this option will create a previous task with the specified time for this task
        # you should not create too many tasks with such parameter, because this consumes slots in pools in airflow
        'StartTime' : [5,27] , 
        # -----
        # hang on to other tasks that precede them until they are executed - this task will not start running
        'Dep' : [
             u'qs-dev.task1',
             u'ds-test.task2',
        ] ,
        # -----
        # used only for NPrinting
        # if the task completion status is warning, then do fail this task, otherwise-complete
        'WarningIsFail' : True,
        # -----
        # send email's on task fails
        # must be congired smtp settings in airflow.cfg file
        'OnFail' : { 'mail' : 'schernov1@gmail.com'}, # mail address to send msg
        # -----
        # for telegram, 
        # if task is done without errors , you will receive a message
        # you can send messages to yourself or to groups or channels
        # the chat ID can be obtained from the bot @ShowJsonBot
        # if you add him to the group, he will write full information about it, including the Chat ID - which we need
        # if you forward a message to the bot, it will show information about this message and the ID of its sender
        'OnSuccess' : { 'telegram' : '585108837'},
        # -----
        # the number of attempts to perform the task in case of errors
        'Retries_count' : 10, 
        # -----
        # the interval for restarting the task in case of an execution error, in seconds
        'Retries_delay' : 30, 
        # -----
        # the restart interval will increase exponentially automatically on each subsequent attempt to start
        'Retries_ExponentialDelay' : True, # or False
        # -----
        # arbitrary delay time up to the specified seconds, before starting the task execution
        'RandomStartDelay' : 10, # random interval 0.0001 < 10 seconds
        #'RandomStartDelay' : 100, # random interval 0.0001 < 100 seconds
        # -----
    }, 
}
```

``` python
tasksDict = {
    # Name of Task 
    u'Virtual sleep' : { 
        # we will create sleep timer
        'Soft' : 'sleep', 
        # name to display on the charts in Airflow
        'TaskId' : u'это будет названием таска',
        # waiting time, in seconds
        'Seconds' : 10 , 
        # hang on to other tasks that precede them until they are executed - this task will not start running
        'Dep' : [
            u'QS1. Test hidden',
        ],
    },
}
```

## Config generator

``` python
config = {
        # If you plan to use 'sleep' tasks, then you need to describe the sleep parameter with the default pool
        "sleep" : {
            # the name of default pool, they are created at http://yourariflow.server.com:8080/pool/list/
            "default_pool": "sensors",
        },
        # The first two letters define soft, which in turn starts the task function.
        # These names should be specified in the dictionary with the list of tasks
        # You can specify parameters for any number of your QV/QS/NP servers
        # One name - one server, possible names, for example: 
        # for NPrinting : np100, npmyserver1, np1, np5, npmyotherName...
        # for Qlik Sense : qs1, qs22, qsense, qsense5 ...
        # for QlikView : qvmyserver.domain.com , qv1, qv2 ...
        "np100": { #nprinting server
            # Full FQDN server name with http[s] prefix
            "server": "https://server15.domain.com",
            # Your domain and account names
            "credential": "domain\\username",
            # Domain user password
            "password": "password",
            # the name of default pool, they are created at http://yourariflow.server.com:8080/pool/list/
            "default_pool": "np1_default_pool"
        }, 
        "qv1asd": { # qlikview server
            # Full FQDN server name with http[s] prefix
            "server" : "http://server3.domain.com",
            # QlikView Management Service API port
            "port" : "4799",
            # QlikView Management Service API url path
            "extraurl" : "/QMS/Service",
            # username without domain!
            "username" : "username",
            # user password
            "password" : "password",
            # the name of default pool, they are created at http://yourariflow.server.com:8080/pool/list/
            "default_pool" : "qv1_default_pool",
        },
        "qs1": { # qlik sense server
            "server" : "https://server2.domain.com",
            # your domain and username
            "username" : "domain\\username",
            # user password
            "password" : "password",
            # the name of default pool, they are created at http://yourariflow.server.com:8080/pool/list/
            "default_pool" : "qs1_default_pool", 
            # Qlik Sense exported certificates path's
            # You can get it from https://qliksense.server.name/qmc/certificates
            # Export in PEM-format and then put it to airflow server
            # put it in AIRFLOW_HOME/cert folder
            "certificate" : ('client.pem', 'client_key.pem'), 
            # "root_cert" : 'root.pem', 
        },
        # Telegram parameter used for send messages to telegram channels
        # Create a new bot from https://t.me/botfather
        # And enter token here
        # Chat id's you can get from @userinfobot (https://github.com/nadam/userinfobot)
        # and use it in tasks dicts
        "telegram" : {
            "token" : "", # put here telegram bot api token
        },
    }
```
