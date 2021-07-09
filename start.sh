source env/bin/activate
export FLASK_ENV=development
#export ADMIN_PASSWORD=test
#export FLASK_ENV=production

flask db migrate
flask run