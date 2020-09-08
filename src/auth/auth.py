from flask import Blueprint, render_template, request, flash, redirect, url_for, json, make_response

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', static_folder='static')

@auth_bp.route('/login')
def login(err=None):
    if err:
        flash(err)
    return render_template('login_form.html')

@auth_bp.route('/login_validate', methods=['POST'])
def login_post():
    print("aca estoy")
    if request.method == 'POST':
        if request.form.get('email') and request.form.get('passw'):
            if request.form.get('email') == 'my_user@gmail.com' and request.form.get('passw') == "1234":
                print("LOGIN SUCCESFULLY")
                res = make_response(redirect(url_for('index.home')))
                res.set_cookie("user", "badbyte")
                return res
            else:
                print("Error")
    return redirect('/login')

@auth_bp.route('/logout')
def logout():
    res = make_response(redirect(url_for('index.home')))
    res.set_cookie('user', '', expires=0)
    return res