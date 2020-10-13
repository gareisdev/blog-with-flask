from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from blog import db
from blog.Models.Post import Post
from blog.Forms.PostForm import PostForm
from slugify import slugify
manage = Blueprint('manage', __name__,
                   template_folder='templates', static_folder='static')


@manage.route("/list")
@login_required
def list_post():
    posts = Post.query.filter_by(author_id=current_user.id)

    return render_template('Posts/manage_post.html', user=current_user.name, posts=posts)


@manage.route('/post/create', methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():

            title = form.title.data
            slug = slugify(title)
            print(slug)
            description = form.description.data
            content = form.content.data
            image = form.image.data

            search_slug = Post.query.filter_by(slug=slug).first()
            if search_slug:
                slug+="-2"

            post = Post(title=title, slug=slug, description=description,
                        content=content, image=image, author_id=current_user.id)

            db.session.add(post)
            db.session.commit()

        return redirect(url_for("index.home"))

    return render_template('Posts/create_post.html', user=current_user.name, form=form)


@manage.route("/edit")
@login_required
def edit_post():
    id = request.args.get('id')
    post = Post.query.filter_by(id=id).first()
    form = PostForm()
    print(form.title.data)
    return render_template('Posts/edit_post.html', post=post, user=current_user.name, form=form)


@manage.route("/delete/<int:id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('manage.list_post'))

@manage.route('/update/<int:id>', methods=["POST"])
@login_required
def update_post(id):
    form = PostForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():

            title = form.title.data
            description = form.description.data
            content = form.content.data
            image = form.image.data


            db.session.query(Post).filter(Post.id == id).update({
                Post.title: title,
                Post.description : description,
                Post.content : content,
                Post.image : image
            })
            
            db.session.commit()

    return redirect(url_for("index.home"))
