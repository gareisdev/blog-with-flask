import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, AnonymousUserMixin

#App
app = Flask(__name__)
app.config['SECRET_KEY'] = "YOUR_SECRET_KEY"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" +  os.path.join(os.path.dirname(__file__), "db", "blog.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database
db = SQLAlchemy(app)

# Session Manager
class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = ''

login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'
login_manager.init_app(app)
login_manager.anonymous_user = Anonymous