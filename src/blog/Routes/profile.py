from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from blog.Models.User import User
profile = Blueprint('profile', __name__,
                   template_folder='templates', static_folder='static')

@profile.route('/profile', methods=["GET", "POST"])
@login_required
def profile_info():

    print("Hello")
    user_info = User.query.get(current_user.id)
    print(user_info)
    if(request.method == "POST"):
        print("POST req")
        return render_template('Auth/profile.html', user_info=user_info, user=current_user.name)
    return render_template('Auth/profile.html', user_info=user_info, user=current_user.name)