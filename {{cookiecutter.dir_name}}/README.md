# {{cookiecutter.project_name}}

## Extensions used
* Flask
* Flask-Login
* Flask-Manager
* Flask-WTF
* Flask-SQLAlchemy
* Flask-Admin (Endpoint: `/admin` only for role = `admin`)

## How to start the app
`flask run`

Task to migrate/update/rebuild database
* Init the migration: `flask db init`
* Create the migrate script: `flask db migrate --message 'Initial database migration`
* Apply the migration (update the model): `flask db upgrade`

## How to start a worker for the tasks
`flask run_worker`

## How to start a scheduler for the tasks (crons jobs)
`flask run_scheduler`

## Environments Vars

* FLASK_ENV: _Default: production_
* SECRET_KEY: _Default: flask-template_
* ADMIN_EMAIL: _Default: example@mail.es_
* ADMIN_NAME: _Default: rani_
* ADMIN_PASSWORD: _Default: 654321_
* MYSQL_USER: _Default: root_
* MYSQL_PASSWORD: _Default: root_
* MYSQL_HOST: _Default: localhost_
* MYSQL_DATABASE: _Default: db_
* REDIS_HOST: _Default: redis_
* REDIS_PORT: _Default: 6379_

### Setting FLASK_ENV
If __FLASK_ENV__ is different to _production_, the DevelopmentConfig is loaded. Thats means thats the app its using __SQLITE__ for the database, otherwise will be using __MYSQL__
