from flask import render_template, url_for, flash,redirect, request, abort
from sqlalchemy import desc
from flaskblog.forms import (RegistrationForm, LoginForm, UpdateAccountForm, PostFrom,
                             ResetPasswordForm, RequestPasswordReset)
from flaskblog.models import User, Post
from flaskblog import app, db , bcrypt, mail
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image
from flask_mail import Message

@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate( page= page, per_page=5)
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
    if form.validate_on_submit():
        post.title =form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post Updated!','success')
        return redirect(url_for('post',post_id = post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template('new_post.html',title="Edit Post" ,form=form, legend = "Update Post: "+  post.title)

@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted', 'success')
    return redirect(url_for('home'))

@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate( page= page, per_page=5)
    return render_template('user_posts.html',posts=posts,user=user)

def send_reset_email(user): 
    token = user.get_reset_token()
    msg = Message('Password reset request',
     sender='noreply+seancahill15@gmail.com',
     recipients=[user.email])
    msg.body= f'''To reset password, visit following link:
{url_for('reset_token',token=token,_external=True)}

Please ignore this email if you did not make this request
    '''
    mail.send(msg)

@app.route('/reset_password', methods=['GET','POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestPasswordReset()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() 
        send_reset_email(user)   
        flash('An email has been sent with instructions to reset your password','info')
        return redirect(url_for('login'))
    return render_template('reset_request.html',title='Reset Password',form=form)


@app.route('/reset_password/<token>', methods=['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid/expired token','warning')
        return redirect(url_for('reset_request'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f"Password for {form.username.data} succesfully changed! Please login now", "success")
        return redirect(url_for('login'))
    return render_template('reset_password.html',title='Reset Password',form=form)
