from flask import current_app as app

# Every function in this file can be run directly from the API

def hello_task():
    print('hello redis')

    return "Result task executed by worker."