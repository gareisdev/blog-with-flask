from flask import Flask
from core.index import index
from auth.auth import auth_bp
from flask_sqlalchemy import SQLAlchemy
from core.models.Post import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "holamundo"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/blog.db'


app.register_blueprint(index)
app.register_blueprint(auth_bp)

db.init_app(app) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)

