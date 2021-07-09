from flask import current_app as app

from app import rq

# Every function in this file can be run directly from the API

def hello_task():
    print('hello redis')

    return "Result task executed by worker."


@rq.job(result_ttl=-1)
def debug_task():
    with app.app_context():
        app.logger.info(
            "Useless debug task intended to signal that stuff is working successfully executed. ")
    return "OK"
