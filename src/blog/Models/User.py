from sqlalchemy import Integer, String, Boolean
from flask_login import UserMixin
from blog import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    username = db.Column(String(50), nullable=False, unique=True)
    password = db.Column(String(50), nullable=False)
    email = db.Column(String(50), nullable=False, unique=True)
    is_admin = db.Column(Boolean)