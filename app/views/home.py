from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
from flask_login import login_required, logout_user, current_user

from app import tasks

dashboard_bp = Blueprint('dashboard', __name__)

#
# Home page
#
@dashboard_bp.route('/')
@login_required
def home():
    return render_template('dashboard/home.html', user=current_user)