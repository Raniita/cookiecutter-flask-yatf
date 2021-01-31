source env/bin/activate
export FLASK_ENV=development

python main.py db init
python main.py db migrate --message 'User model finished'
python main.py db upgrade