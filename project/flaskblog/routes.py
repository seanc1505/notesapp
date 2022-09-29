from flask import render_template, url_for, flash,redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app, db , bcrypt
from flask_login import login_user, current_user

posts = [
        {
        'author':'Sean Cahill',
        'title':'blog 1',
        'content':'First post content',
        'date_posted':'April 20, 2018'
        },
        {
        'author':'Kevin Cahill',
        'title':'blog 2',
        'content':'Second post content',
        'date_posted':'April 25, 2018'
        }
    ]

@app.route("/")
@app.route("/home")
def home():
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
            return redirect(url_for('home'))
        else:
            flash(f"Login unsuccessful, check Email and password", "danger")
    return render_template('login.html',title='login.html',form=form)
