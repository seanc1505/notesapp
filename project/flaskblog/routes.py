from flask import render_template, url_for, flash,redirect, request, abort
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostFrom
from flaskblog.models import User, Post
from flaskblog import app, db , bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image

@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title="About")

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created succesfully for {form.username.data}! Please login now", "success")
        return redirect(url_for('login'))
    return render_template('register.html',title='register',form=form)


@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash(f"Login unsuccessful, check Email and password", "danger")
    return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _ , file_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + file_ext
    picture_path = os.path.join( app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125,125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save( picture_path)
    return picture_fn

@app.route("/account", methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.image_file.data:
            picture_file = save_picture(form.image_file.data)
            current_user.image_file = picture_file
        db.session.commit()
        flash('Your account details have been updated','success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
    return render_template('account.html',title='Account',
     image_file= image_file, form=form)

@app.route('/post/new', methods=['GET','POST'])
@login_required
def new_post():
    form = PostFrom()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post Created!','success')
        return redirect(url_for('home'))
    return render_template('new_post.html',title='New Post',form=form, legend = "New Post")

@app.route("/post/<int:post_id>", methods=['GET','POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html',title=post.title,post=post)


@app.route("/post/<int:post_id>/edit", methods=['GET','POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostFrom()
    return render_template('new_post.html',title="Edit Post" ,form=form, legend = "Update "+  post.title)