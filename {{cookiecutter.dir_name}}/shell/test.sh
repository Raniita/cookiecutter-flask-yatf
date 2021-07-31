source env/bin/activate
export FLASK_ENV=testing

#python -m pytest tests --setup-show --flake8 -W ignore::DeprecationWarning
#python -m pytest tests --flake8 -W ignore::DeprecationWarning
pytest --flake8 -W ignore::DeprecationWarning