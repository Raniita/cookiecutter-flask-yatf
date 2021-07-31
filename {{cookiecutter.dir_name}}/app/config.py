import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', '{{cookiecutter.secret_key}}')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RQ_QUEUES = ["default"]
    RQ_SCHEDULER_INTERVAL = 60 

    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', '{{cookiecutter.admin_email}}')
    ADMIN_NAME = os.environ.get('ADMIN_NAME', '{{cookiecutter.admin_username}}')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', '{{cookiecutter.admin_password}}')

    FLASK_ADMIN_SWATCH = 'lumen'

    # Must be: https://gotify.example.com/ or https://gotify.example.com
    GOTIFY_URL = os.environ.get('GOTIFY_URL')
    if GOTIFY_URL is not None:
        # Obtained on gotify webapp. Apps -> Create aplication -> Token
        GOTIFY_TOKEN = os.environ.get('GOTIFY_TOKEN')

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    DB_USER = os.environ.get('MYSQL_USER', 'root')
    DB_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'root')
    DB_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    DB_DATABASE = os.environ.get('MYSQL_DATABASE', 'db')

    SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DATABASE

    REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
    REDIS_PORT = os.environ.get('REDIS_HOST_PORT', '6379')
    RQ_REDIS_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'

class DevelopmentConfig(Config):
    DEBUG = True

    ## SQLAlchemy folder
    if not os.path.exists(os.path.join(basedir, 'db')):
        os.makedirs(os.path.join(basedir, 'db'))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db', 'app.sqlite')

    RQ_REDIS_URL = 'redis://localhost:6379'

    DEBUG_TB_INTERCEPT_REDIRECTS = False

class TestingConfig(Config):
    DEBUG = True

    ## SQLAlchemy folder
    if not os.path.exists(os.path.join(basedir, 'db')):
        os.makedirs(os.path.join(basedir, 'db'))

    # Bcrypt algorithm hashing rounds (reduced for testing purposes only!)
    BCRYPT_LOG_ROUNDS = 4

    # Enable the TESTING flag to disable the error catching during request handling
    # so that you get better error reports when performing test requests against the application.
    TESTING = True
    
    # Disable CSRF tokens in the Forms (only valid for testing purposes!)
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db', 'app_testing.sqlite')

    RQ_REDIS_URL = 'redis://localhost:6379'

    DEBUG_TB_INTERCEPT_REDIRECTS = False
