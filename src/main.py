from flask import Flask
from flask_login import current_user
from blog.Routes.index import index
from blog.Routes.auth import auth_bp
from blog.Routes.manage import manage
from blog.Routes.profile import profile
from blog import app, db, login_manager
from blog.Models.User import User

# Blueprints
app.register_blueprint(index)   # Post
app.register_blueprint(auth_bp) # Login and Signup
app.register_blueprint(manage)
app.register_blueprint(profile)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == '__main__':
    db.create_all()
    app.run(port=4000, debug=True)