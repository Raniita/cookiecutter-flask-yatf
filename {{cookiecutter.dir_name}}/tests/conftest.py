from datetime import datetime
import pytest

from app.models import User
from app import create_app, db


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope="module")
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User(name = 'test-admin',
                 email = 'admin@flask.com',
                 created_on = datetime.now(),
                 role = 'admin'
    )
            
    user1.set_password('admin_password')
    user1.update_last_login(datetime.now())
    db.session.add(user1)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='module')
def new_user():
    user = User(name='test-user', email='test@flask.com', role='user')
    user.set_password('test-password')
    return user