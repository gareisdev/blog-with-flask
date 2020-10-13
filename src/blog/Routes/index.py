from flask import Blueprint, render_template, request, json, redirect, url_for
from blog.Models.Post import Post
from flask_sqlalchemy import SQLAlchemy
from blog import db
from blog.Forms.PostForm import PostForm
from flask_login import login_required, current_user

index = Blueprint(  'index', 
                    __name__, 
                    template_folder='templates',
                    static_folder='static')


@index.route('/')
def home():
    posts = Post.query.all()

    return render_template('Posts/index.html', user=current_user.username, posts=posts)



@index.route('/post/<string:slug>')
def get_post(slug):
    post = Post.query.filter_by(slug=slug).first()
    return render_template('Posts/post.html', post=post, user=current_user.name)


@index.route('/search')
def search_post():
    title = request.args.get("t")

    posts = Post.query.filter(Post.title.like(f"%{title}%")).all()

    return render_template("Posts/index.html", user=current_user.username, posts=posts)
