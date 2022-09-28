from datetime import datetime
from flask import Flask, render_template, url_for, flash,redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '33f1ae20b4a0d78c4d3eb6ecdce3fb1a'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20),unique=True, nullable =False)
    email = db.Column(db.String(120),unique=True, nullable =False)
    image_file = db.Column(db.String(20), nullable =False, default= 'default.jpg')
    password = db.Column(db.String(60), nullable =False)

    def __repr__(self):
        return f"User ('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(20),unique=True, nullable =False)
    title = db.Column(db.String(100), nullable =False)
    content = db.Column(db.String(20), nullable =False, default= 'default.jpg')
    date_posted = db.Column(db.DateTime, nullable =False)


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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created succesfully for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template('register.html',title='register',form=form)


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f"Login succesful {form.email.data}!", "success")
            return redirect(url_for('home'))
        else:
            flash(f"Login unsuccessful, check username and password", "danger")
    return render_template('login.html',title='login.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)
