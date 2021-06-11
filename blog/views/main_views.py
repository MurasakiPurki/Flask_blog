from re import template
from flask import Blueprint, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/signin')
def signin():
    return render_template('signin.html')

@bp.route('/signup')
def signup():
    return render_template('signup.html')
