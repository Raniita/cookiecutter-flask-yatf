
# YAFT (yes-another-flask-template)
Flask template starter powered with [Cookiecutter](https://github.com/cookiecutter/cookiecutter).

## Description
Light starter of fully opinionated Flask template. Based on previous experience. Be free to open an issue or fork this repo.

## Usage

Install cookiecutter

```bash
    $ pip install cookiecutter
```

on Arch Linux, use:

```bash
    $ sudo pacman -S python-cookiecutter
```

Generate the project using the template

```bash
    $ cookiecutter https://github.com/Raniita/yes-another-flask-template.git
```

Fill the differents vars for the project.

### Optional
* Configure virtual environment (pipenv, venv, ...)
* Install python package requeriments:
```bash
    $ pip install -r requeriments.txt
```
* Setup git
* Add License.md

  
## Features
Powered with this extensions:

- Flask >= 2.0
- Flask CLI commands
- Flask-Minify
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-bcrypt
- Flask-Login
- Flask-Admin
- Flask-WTF
- Flask-RQ2
- Flask-DebugToolBar

Extras:
- Blueprints and [application factory pattern](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/)
- Continous integration with [drone.ci](https://www.drone.io/)
- Access control to views based on roles
- Admin panel (File browser, DB management)
- Admin dashboard
- Deploy based en Docker [docker-compose]

  
## License

[AGPL-3.0](https://choosealicense.com/licenses/agpl/)

  