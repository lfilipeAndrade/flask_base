from flask import render_template, redirect, request, url_for
from flask_login import current_user

from apps import db, login_manager
from apps.home import blueprint

@blueprint.route('/index')
def index():
    return render_template( 'home/index.html',user=current_user)