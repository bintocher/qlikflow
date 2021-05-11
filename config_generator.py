
import json, os

def read_config():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '\\config.json', 'r') as f:
        config = json.load(f)
    return config

def save_config():
    """
        Simple config file generator for use with qlikflow module

    """
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
            "root_cert" : 'root.pem', 
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
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '\\config.json', 'w') as f:
        json.dump(config, f)

if __name__ == "__main__":
    # config = read_config()
    save_config()
    config = read_config()
    print (config)
