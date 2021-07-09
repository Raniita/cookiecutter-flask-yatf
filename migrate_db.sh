source env/bin/activate
export FLASK_ENV=development

#python main.py db init
#python main.py db migrate --message 'User model finished'
#flask db init
flask db upgrade