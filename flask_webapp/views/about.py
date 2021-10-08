from flask import Blueprint, render_template

bp = Blueprint("about", __name__, template_folder='templates')

@bp.route('/about')
def show():
    return render_template('about.html')
