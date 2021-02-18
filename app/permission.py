from functools import wraps
from flask_login import current_user
from flask_login.config import EXEMPT_METHODS
from flask import current_app, request, redirect, url_for, flash

def restricted_role(role):
    ''' Decorator to deny the endpoint if user is in role list '''

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.method in EXEMPT_METHODS:
                return func(*args, **kwargs)
            elif not current_user.is_authenticated:
                return redirect(url_for('auth.login'))
            elif current_user.role in role:
                flash('Not enough permissions to do that')
                current_app.logger.info('{} try to access a restricted endpoint {}'.format(current_user, request.endpoint))
                return redirect(url_for('dashboard.home'))
            return func(*args, **kwargs)
        return wrapper
    return decorator
    