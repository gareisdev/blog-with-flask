from flask import Blueprint, render_template

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', static_folder='static')

@auth_bp.route('/auth', methods=['GET','POST'])
def login():
    return render_template('login_form.html')
