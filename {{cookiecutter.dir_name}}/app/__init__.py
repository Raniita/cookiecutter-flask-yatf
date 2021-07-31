import click
import logging
import os

from datetime import timedelta

from flask import Flask, current_app, session, render_template
from flask.cli import with_appcontext
from flask_minify import minify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_admin import Admin
#from flask_admin.contrib.fileadmin import FileAdmin
from flask_debugtoolbar import DebugToolbarExtension
from flask_rq2 import RQ

from app.admin import CustomAdminIndexView, AdminModelView, MainIndexLink
from app.config import ProductionConfig, DevelopmentConfig, TestingConfig
from werkzeug.security import generate_password_hash, check_password_hash

# Extensions declaration
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
toolbar = DebugToolbarExtension()
rq = RQ(is_async=True)
admin = Admin(name='YAFT',
              index_view=CustomAdminIndexView(),
              template_mode='bootstrap4')

# Application factory init
def create_app():
    app = Flask(__name__)

    # Load app config 
    if app.config['ENV'] == 'production':
        # Create logger
        logger = logging.getLogger('flask.errors')
        logger.setLevel(logging.DEBUG)

        # Create console handler and configure it
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)

        logFormat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        consoleHandler.setFormatter(logging.Formatter(logFormat))

        # Add our custom handler to the logger
        logger.addHandler(consoleHandler)

        # Tell the app to use logger
        app.logger.handlers = logger.handlers
        app.logger.setLevel(logger.level)
        
        # Server side minification
        app.logger.info('Minifying')
        minify(app=app, html=True, js=False, cssless=True)
        
        app.logger.info('Starting with ProductionConfig')
        app.config.from_object(ProductionConfig)
    elif app.config['ENV'] == 'testing':
        app.logger.info("Starting with TestingConfig")
        app.config.from_object(TestingConfig)
    else:
        app.logger.info('Starting with DevelopmentConfig')
        app.config.from_object(DevelopmentConfig)

    # Connect to database
    app.logger.info('Using database connection:' + app.config['SQLALCHEMY_DATABASE_URI'])
    app.logger.info('Using redis connection:' + app.config['RQ_REDIS_URL'])
    app.url_map.strict_slashes = True

    # Gotify push notifications
    if app.config['GOTIFY_URL'] is not None:
        app.logger.info('Using Gotify url: {}'.format(app.config['GOTIFY_URL']))

    #
    # Custom flask cli commands
    #
    app.cli.add_command(run_worker)
    app.cli.add_command(run_scheduler)

    #
    # Set up Flask extensions
    #

    # Init Flask-DebugToolbar
    toolbar.init_app(app)

    # Init Flask-RQ2
    rq.init_app(app)

    # Init Flask-SQLAlchemy
    db.init_app(app)

    # Init Flask-Migrate
    migrate.init_app(app, db)

    # Init Flask-Login
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    login_manager.refresh_view = 'auth.login'
    login_manager.needs_refresh_message = (u"Session timedout, please re-login")
    login_manager.needs_refresh_message_category = "info"

    from app.models import User
    from app import admin

    admin.init_app(app)
    admin.add_view(AdminModelView(User, db.session))
    #admin.add_view(FileAdmin('./path/', '/files/', name="File browser"))
    admin.add_link(MainIndexLink(name='Flask Dashboard'))

    try:
        with app.app_context():
            # Create database models
            #db.create_all()

            # Create admin user on startup
            admin_email = app.config['ADMIN_EMAIL']
            admin_name = app.config['ADMIN_NAME']
            admin_pass = app.config['ADMIN_PASSWORD']

            admin = User.query.filter_by(email=admin_email).first()
            if admin.name is None:
                passw = generate_password_hash(admin_pass, method='sha256')
                new_user = User(email=admin_email,
                                name=admin_name,
                                #password=admin_pass,
                                role='admin')
                new_user.set_password(admin_pass)

                db.session.add(new_user)
                db.session.commit()
                app.logger.info('Added admin user to dabatase')
            else:
                # Checking if password has been changed
                admin_hash = generate_password_hash(admin_pass, method='sha256')

                if not check_password_hash(admin_hash, admin.password):
                    # Updating password on database
                    admin.password = admin_hash
                    
                    db.session.add(admin)
                    db.session.commit()
                    #app.logger.info('Updated admin password')
                
            app.logger.info('Database working')

    except Exception as e:
        app.logger.error('Exception Found' + str(e))
        app.logger.error('Database not found. Please read README.md to create the db.')

    app.logger.info('Done. Flask extensions started.')

    # Adding the views app
    from app.views.home import dashboard_bp
    from app.views.auth import auth_bp
    from app.views.api import api_bp

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)

    # Inject global variables to all templates
    @app.context_processor
    def injectVariables():
        return dict(user=current_user)

    # Set up global HTML handlers
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    # Auto logout session. Modify time in minutes
    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=1440)

    return app

#
# Custom commands (flask cli)
#
@click.command(name='run_worker')
@with_appcontext
def run_worker():
    current_app.logger.info("Start worker")

    # Creates a worker that handle jobs in ``default`` queue.
    default_worker = rq.get_worker()

    current_app.logger.info("Running worker...")

    default_worker.work()


@click.command(name='run_scheduler')
@with_appcontext
def run_scheduler():
    current_app.logger.info("Start jobs scheduler")

    from app.tasks import debug_task

    try:
        #debug_task.cron('* * * * *', 'debug_task', queue='default')
        
        current_app.logger.info("Scheduled debug task.")
    except Exception as ex:
        current_app.logger.error("Error scheduling crons: {}".format(ex))

    scheduler = rq.get_scheduler()
    current_app.logger.info("Running scheduler...")
    scheduler.run()
