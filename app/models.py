from app import db

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """ User account model. """

    #__tablename__ = 'user'

    id = db.Column(
        db.Integer,
        primary_key=True)

    name = db.Column(
        db.String(100), 
        nullable=False, 
        unique=False)

    email = db.Column(
        db.String(40), 
        unique=True,
        nullable=False)

    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False)

    website = db.Column(
        db.String(60),
        index=False,
        unique=False,
        nullable=True)

    role = db.Column(
        db.String(100),
        index=False,
        unique=False,
        nullable=False)

    created_on = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True)

    last_login = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True)

    def set_password(self, password):
        """ Create hashed password """
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """ Check hashed password """
        return check_password_hash(self.password, password)

    def is_admin(self):
        """ Return True if admin """
        if self.role == 'admin':
            return True
        else:
            return False

    def update_last_login(self, time):
        """ Update user last_login datetime """
        self.last_login = time

    def __repr__(self):
        return '<User {}>'.format(self.username)