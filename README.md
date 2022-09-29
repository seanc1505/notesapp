# notesapp

Starter project for web development

# Tutorial 1

[**Tutorial source**](https://www.youtube.com/watch?v=MwZwr5Tvyxo)

## Getting set up with python virtual env and running basic flask

1. Create vitural env
   1. `python -m venv env`
      1. Creates a venv in env/
2. Create a project folder
   1. `mkdir project`
3. Create a file in folder
4. change enviroment in bottom right to venv version of python
5. import flask
6. set up helloworld
7. set enviroment var FLASK_APP
   1. `set FLASK_APP=<filename>`
   2. `flask run`

## Continous debug

1. `set FLASK_DEBUG = 1`
   1. This opens in debug mode

## Running files via python

```python
   if __name__ == "__main__":
       app.run(debug=True)
```

## @app.route

1. Dictates url for the functions
2. Can point multiple routes to the same page#

Home page at `@app.route("/") @app.route("/home")`

# Tutorial 2

[**Tutorial source**](https://www.youtube.com/watch?v=QnDWIZuWYW0)

## Templates

1. Makes sense to return a template within a function rather than returning a HTML string for cleanlieness
2. Create a templates folder
3. Create a html file for each page
4. import render_templates
   1. ``return render_templates('home.html')``

Flask uses Jinja2 for writing code within templates

Use a code block such as `{%for post in posts%}` and end with ``{%endfor%}``

### for loop using jinja2

**Sample code block for a dict `posts`**

```txt
   {% for post in posts %}
      <h1>{{post.title}}</h1>
      <p>By {{post.author}} on {{post.date_posted}}<p>
      <p> {{post.content}} </p>
   {% endfor %}
```

### if else

```html
{% if title %}
   <title>Flask Blog - {{title}} </title>
{% else %}
   <title>Flask Blog</title>
{% endif %}
```

## Template Inheritance

* Important to maintain as much unique information in 1 place
* import common data from one place
* Uses the `block` key word
  * `{% block content %}{% endblock %}`
* To inherit the template, use ;

```jinja2
{% extends  "layout.html" %}
{% block content %}
```

## Bootstrap

* A popular library to add styles to website

### To add bootstrap

Open starter template from documentation
(can use flask bootstrap)
We need to pull in specific CSS and Javascript into out layout template

To use a container use lines;

``` html
 <div class = "container">
 </div>
```

* We need to add some javascript to import JQuery, Popper.js and Bootstrap.js
  * Goes in body before closing ``</body>`` tag

```html
<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
```

* We need to add meta tags

``` html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
```

* We need to add link to bootstrap CSS style sheet.
  * REL=StyleSheet specifies a persistent or preferred style while

``` html
<!-- Bootstrap CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous" 
```

## Adding Navigation bar and global styles

* Uses alot of HTML code, explained below

### Navbar

* This code snippet is added to `<body></body>`
* The enitre snippet is stored in snippet/navbar.html
* Added a navbar with some boostrap classes
* Is responsive to screen size

### main section for content

* The enitre snippet is stored in snippet/main.html
* This is where we now put content from dictionary of content
* Goes in body tags

### Custom styles that are non bootstrap specific

* CSS files go in a static directory
* To use them in the layout.html file
* Use the url_for function to find the location of the file
  * `<link rel="stylesheet" type = "text/css" href="{{ url_for('static',filename='main.css')}}">`
    * Href says where file is.
    * url for points to static directory and file name of main.css

## Improving formatting of blog posts

* Added the html code from snippets/article.html into layout.html
* Splits posts into individual blocks and gives good formatting

# Tutorial 3 - Forms and user input

[**Tutorial source**](https://www.youtube.com/watch?v=UIJKdCIEXUQ)

## Forms

* Creating forms from scratch is difficult but there are many extensions, most common is **WT-forms**, install with pip install ``flask-wtf``
  * We can write python classes which represent html forms
* Creating 2 forms, login and register

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class RegistrationForm(FlaskForm):
   username = StringField('Username',
                            validators=[DataRequired(),
                                        Length(min=2,max=20)]
                            )
```

* Create a form by creating a class with variables that are generated as a type of field
* Create a html file for each form
* extend layout
* Each entry into form gets a `<div class="form-group">`
  * in this div goes html info
    * ``{{ form.email.label(class="form-control-label") }}``
    * ``{{ form.email(class="form-control form-control-lg") }}``
  * Also Add error information in terms of if statement `{% if form.email.errors %}`
* Add data validation to main file functions

# Tutorial 4 - Database with SQLAlchemy

[**Tutorial source**](https://www.youtube.com/watch?v=cYWiDiIUxQc)

ORM - Object relational mapper

We can use different types of databases with this python methof
We use SQLlite for dev and then move to PostGres

1. `from flask_sqlalchemy import SQLAlchemy`
2. Need to specify URI for database (where database is located)
   * For now using SQLlite database (A file on filesytem)
   * Must be set as a configuration `app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'`
   * Relative path using `///`
3. Create database instance
   * `db = SQLAlchemy(app)`
   * Can represent database structure as classes (models)
4. Creating models in flask_blog.py for now
   * create models via a class `class User(db.Model):`
5. Columns are represented by class vars
    * ``id = db.Column(db.Integer, primary_key = True)``
6. Set a repr method

```
   def __repr__(self): 
      return f"Post('{self.title}')
```

## create database

* open terminal in project dir
* `from flask_blog import db`
* `db.create_all()`
* manually add data
  * `from flask_blog import User`
  * `user_1 = User(User(username='sean',email='s@demo.com',password='password')`
  * `db.session.add(user_2) `
  * `db.session.commit()`

## access data in terminal

* `User.query.all()`
* ` User.query.filter_by(username='sean').all()`
* ` User.query.first()`
* ``db.drop_all`` deletes all files


# Tutorial 5 - Package Strucutre

[**Tutorial source**](https://www.youtube.com/watch?v=44PvX0Yv368)
 
* moving models to models.py
  * We get circular imports
  * create a package for flask_blog (new folder with **__init__**)
    * populate init.py with all imports
* Move all files into it
* Create routes.py and put all route code in there
* Rename flask_blog to run.py

# Tutorial 5 - User Authentication


[**Tutorial source**](https://www.youtube.com/watch?v=CSHx6eCkmv0)

## addding password hashing
* dont want to use plain text password storage
  * need to use a hashing algorithim
    * `pip install flask-bcrypt `
    * Add ``bcrypt = Bcrypt(app)`` to init.py
    * add following lines to the register route


## Create account

```python 
hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
user = User(username = form.username.data, email = form.email.data, password=hashed_password)
db.session.add(user)
db.session.commit()
```

## Verifying unique email and user

Adding the following to the register form

```python
def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:    
            raise ValidationError('This username is taken, please try another')
    
```

## login

* Create a funciton with a decerator
  * reloading a user from user id stored in session
* Adding following to models.py

```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

```

Added check if logged in to return to home page if login is pressed

```python
if current_user.is_authenticated:
   return redirect(url_for('home'))
```

# html learnings

* ``<meta >`` tags contain metadata about the html document.
  * Always go inside head of document.
  * Typically used to specify character set, page description, keywords, author of the document, and viewport settings.
* `<div class=>` defines a division or a section in an HTML document.
  * The `<div>` tag is used as a container for HTML elements - which is then styled with CSS or manipulated with JavaScript.
* `{{}}` dictates a code injection
  * `<link rel="stylesheet" type = "text/css" href="{{ url_for('static',filename='main.css')}}">` Injects the url_for function to find location of main.css
