from flask import Blueprint, render_template, request, flash, redirect, url_for, json, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from blog.Models.User import User
from blog.Forms.LoginForm import LoginForm
from blog import db
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', static_folder='static')


@auth_bp.route('/login', methods=["GET", "POST"])
def login(err=None):

    form = LoginForm(request.form)
    
    if request.method == "POST":

        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            
            if user and check_password_hash(user.password, password):
                
                remember  = True if ("remember" in request.form) else False
                
                login_user(user, remember=remember)
                
                return redirect(url_for('index.home'))
            else:
                flash('Error: username or password incorrect.')
                return redirect(url_for('auth_bp.login'))

    return render_template('Auth/login_form.html', form=form)



@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.home'))


@auth_bp.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        username = request.form["username"]
        hash_password = generate_password_hash(request.form["password"], method='sha256')
        is_admin = False
    
        #Guardar usuario
        user = User(name=name, username=username, password=hash_password, email=email, is_admin=is_admin)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth_bp.login'))
    return render_template('Auth/signup_form.html')