from flask import Blueprint, render_template

bp = Blueprint("index", __name__, template_folder='templates')

@bp.route('/')
def show():
    return render_template('index.html')
