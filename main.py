from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from rq import Connection, Worker
import redis

from app import create_app, db

app = create_app()

# Setup Manager and Migrate
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def run_worker():
    redis_url = app.config["REDIS_URL"]
    redis_connection = redis.from_url(redis_url)
    with Connection(redis_connection):
        worker = Worker(app.config["QUEUES"])
        worker.work()


if __name__ == "__main__":
    manager.run()