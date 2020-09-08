from flask import Blueprint, render_template, request, json
from .models.Post import Post
from flask_sqlalchemy import SQLAlchemy


index = Blueprint(  'index', 
                    __name__, 
                    template_folder='templates',
                    static_folder='static')



@index.route('/')
def home():
    user=None

    posts = Post.query.all()

    if request.cookies.get('user'):
        user = request.cookies.get('user')
        loged = True
        print(user)
    else:
        loged = False
    return render_template('index.html', user=user, log=loged, posts=posts)

@index.route('/post/<int:id>')
def post_id(id):
    post = Post.query.filter_by(id=id).first()
    return render_template('post.html', post=post)