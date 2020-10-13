from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[Required("Please, insert your username")])
    name = StringField("Name", validators=[Required("Please, insert your name")])
    email = StringField("Email", validators=[Required("Please, insert your email")])
    password = PasswordField("Password", validators=[Required("Please, insert your password")])
    submit = SubmitField("SignUp")