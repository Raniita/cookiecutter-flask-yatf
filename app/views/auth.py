from flask import Blueprint, render_template, request, redirect, flash, session, url_for, current_app
from flask_login import login_required, logout_user, current_user, login_user

from app.forms import LoginForm, SignupForm
from app.models import User
from app import db, login_manager

auth_bp = Blueprint('auth', __name__)

#
# Login Page
#
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registed users.

    GET -> request serve Log-in page.
    POST -> requests validate and redirect user to dashboard
    """

    # Bypass if user is logged in:
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.home'))

    form = LoginForm()
    # Validate Form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard.home'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/login.html',form=form)


#
# Sign Up Page
#
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page

    GET -> requests serve sign-up page
    POST -> requests validate form & user creation
    """

    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name = form.name.data,
                email = form.email.data,
                website = form.website.data,
                role = 'user'
            )
            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('dashboard.home'))

        error = 'A user already exists with that email address.'
        flash(error)
        current_app.logger.error(error)
    
    # Check if user already login
    if current_user.is_authenticated:
        error = 'User already logged in. Sign out first.'
        flash(error)
        current_app.logger.error(error)
        return redirect(url_for('dashboard.home'))
    else:
        return render_template('auth/signup.html',form=form)

#
# Logout page
#
@auth_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""

    if user_id is not None:
        return User.query.get(user_id)
    return None@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""

    flash('You must be logged in to view that page.')
    return redirect(url_for('auth.login'))