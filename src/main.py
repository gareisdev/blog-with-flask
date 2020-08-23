from flask import Flask
from core.index import index
from auth.auth import auth_bp

app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run(port=4000, debug=True)
