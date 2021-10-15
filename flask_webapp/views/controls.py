from flask import Blueprint, render_template

bp = Blueprint("controls", __name__, template_folder='templates')

@bp.route('/controls')
def show():
    return render_template('controls.html')
