from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[Required("Please, insert your username")])
    password = PasswordField("Password", validators=[Required("Please, insert your password")])
    submit = SubmitField("LogIn")