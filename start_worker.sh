source env/bin/activate
export FLASK_ENV=development
#export FLASK_ENV=production

python main.py db upgrade && python main.py run_worker