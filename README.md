# yes-another-flask-template

## Extensions used
* Flask
* Flask-Login
* Flask-Manager
* Flask-WTF
* Flask-SQLAlchemy
* Flask-Admin (Endpoint: `/admin` only for role = `admin`)

## How to start the app
`python main.py run`

Task to migrate/update/rebuild database
* Init the migration: `python main.py db init`
* Create the migrate script: `python main.py db migrate --message 'Initial database migration`
* Apply the migration (update the model): `python main.py db upgrade`

## How to start a worker for the Tasks
`python main.py run_worker`

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