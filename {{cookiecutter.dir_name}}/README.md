
# {{cookiecutter.project_name}}

A brief description of what this project does and who it's for

Powered with [cookiecutter-flask-yatf](https://github.com/Raniita/cookiecutter-flask-yatf)

## Features
Powered with this extensions:

- Flask >= 2.0
- Flask CLI commands
- Flask-Minify
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-bcrypt
- Flask-Login
- Flask-Admin (endpoint: `/admin` only for `role = admin`)
- Flask-WTF
- Flask-RQ2
- Flask-DebugToolBar
## Run website

```bash
$ flask run
```

## Run worker
```bash
$ flask run_worker
```

## Run scheduler
```bash
$ flask run_scheduler
```

## Migrate database
Usefull locally
```bash
$ flask db init
$ flask db migrate
$ flask db upgrade
```
## Environment Variables

`FLASK_ENV` [*default: production*]

`SECRET_KEY` [*default: flask-template*]

`ADMIN_EMAIL` [*default: example@mail.es*]

`ADMIN_NAME` [*default: rani*]

`ADMIN_PASSWORD` [*default: 654321*]
    
`MYSQL_USER` [*default: root*]

`MYSQL_PASSWORD` [*default: root*]

`MYSQL_HOST` [*default: localhost*]

`MYSQL_DATABASE` [*default: db*]

`REDIS_HOST` [*default: redis*]

`REDIS_PORT` [*default: 6379*]

`GOTIFY_URL` [*default: none*]

`GOTIFY_TOKEN` [*default: none*]

  ## Setting FLASK_ENV

If **FLASK_ENV** is different to *production*, the DevelopmentConfig is loaded. Thats means thats the app its using **SQLITE** for the database, otherwise will be using **MYSQL**