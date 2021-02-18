source env/bin/activate
export FLASK_ENV=development
#export ADMIN_PASSWORD=test
#export FLASK_ENV=production

python main.py db upgrade && python main.py run