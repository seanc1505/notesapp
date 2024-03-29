# notesapp

Starter project for web development

## Tutorial 1

[**Tutorial source**](https://www.youtube.com/watch?v=MwZwr5Tvyxo)

### Getting set up with python virtual env and running basic flask

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

### Continous debug

1. `set FLASK_DEBUG = 1`
   1. This opens in debug mode

### Running files via python

```python
   if __name__ == "__main__":
       app.run(debug=True)
```

### @app.route

1. Dictates url for the functions
2. Can point multiple routes to the same page#

Home page at `@app.route("/") @app.route("/home")`

## Tutorial 2

[**Tutorial source**](https://www.youtube.com/watch?v=QnDWIZuWYW0)

### Templates

1. Makes sense to return a template within a function rather than returning a HTML string for cleanlieness
2. Create a templates folder
3. Create a html file for each page
4. import render_templates
   1. ``return render_templates('home.html')``

Flask uses Jinja2 for writing code within templates

Use a code block such as `{%for post in posts%}` and end with ``{%endfor%}``

#### for loop using jinja2

**Sample code block for a dict `posts`**

```txt
   {% for post in posts %}
      <h1>{{post.title}}</h1>
      <p>By {{post.author}} on {{post.date_posted}}<p>
      <p> {{post.content}} </p>
   {% endfor %}
```

#### if else

```html
{% if title %}
   <title>Flask Blog - {{title}} </title>
{% else %}
   <title>Flask Blog</title>
{% endif %}
```

### Template Inheritance

* Important to maintain as much unique information in 1 place
* import common data from one place
* Uses the `block` key word
  * `{% block content %}{% endblock %}`
* To inherit the template, use ;

```jinja2
{% extends  "layout.html" %}
{% block content %}
```

### Bootstrap

* A popular library to add styles to website

#### To add bootstrap

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

### Adding Navigation bar and global styles

* Uses alot of HTML code, explained below

#### Navbar

* This code snippet is added to `<body></body>`
* The enitre snippet is stored in snippet/navbar.html
* Added a navbar with some boostrap classes
* Is responsive to screen size

#### main section for content

* The enitre snippet is stored in snippet/main.html
* This is where we now put content from dictionary of content
* Goes in body tags

#### Custom styles that are non bootstrap specific

* CSS files go in a static directory
* To use them in the layout.html file
* Use the url_for function to find the location of the file
  * `<link rel="stylesheet" type = "text/css" href="{{ url_for('static',filename='main.css')}}">`
    * Href says where file is.
    * url for points to static directory and file name of main.css

### Improving formatting of blog posts

* Added the html code from snippets/article.html into layout.html
* Splits posts into individual blocks and gives good formatting

## Tutorial 3 - Forms and user input

[**Tutorial source**](https://www.youtube.com/watch?v=UIJKdCIEXUQ)

### Forms

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

## Tutorial 4 - Database with SQLAlchemy

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

```python
   def __repr__(self): 
      return f"Post('{self.title}')
```

### create database

* open terminal in project dir
* `from flask_blog import db`
* `db.create_all()`
* manually add data
  * `from flask_blog import User`
  * `user_1 = User(User(username='sean',email='s@demo.com',password='password')`
  * `db.session.add(user_2)`
  * `db.session.commit()`

### access data in terminal

* `User.query.all()`
* `User.query.filter_by(username='sean').all()`
* `User.query.first()`
* ``db.drop_all`` deletes all files

## Tutorial 5 - Package Strucutre

[**Tutorial source**](https://www.youtube.com/watch?v=44PvX0Yv368)

* moving models to models.py
  * We get circular imports
  * create a package for flask_blog (new folder with **\_\_init\_\_**)
    * populate init.py with all imports
* Move all files into it
* Create routes.py and put all route code in there
* Rename flask_blog to run.py

## Tutorial 6 - User Authentication

[**Tutorial source**](https://www.youtube.com/watch?v=CSHx6eCkmv0)

### addding password hashing

* dont want to use plain text password storage
  * need to use a hashing algorithim
    * `pip install flask-bcrypt`
    * Add ``bcrypt = Bcrypt(app)`` to init.py
    * add following lines to the register route

### Create account

```python
hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
user = User(username = form.username.data, email = form.email.data, password=hashed_password)
db.session.add(user)
db.session.commit()
```

### Verifying unique email and user

Adding the following to the register form

```python
def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:    
            raise ValidationError('This username is taken, please try another')
    
```

### login

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

### Logout

Add the following section to a logout route

```python
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
```

## Tutorial 7 - User Account and Profile Picture

[**Tutorial source**](https://www.youtube.com/watch?v=CSHx6eCkmv0)

### Displaying profile details on Account page

1. added profile photo, create folder in static
2. Add html for displaying
3. Pull profile pic from static folder in routes.py

### Editing account details

1. Created update form in forms.py
2. Added form html to accounts.html
3. Added database change to routes.py
4. Added aditional form block to change picture
5. Added html code to display form
6. Added code to routes to save image details in database

## Tutorial 8 - Create, Update, and Delete Posts

[**Tutorial source**](https://www.youtube.com/watch?v=u0oDDZrDz9U)

### Creating a new post

1. Create a new post.html
   1. populate with form to add title content and post
2. Create a form to add content title and post
3. Create a route for new post
   1. Create a new post object and pass in the data from a post form
   2. Add post to database
4. Add route to navbar
5. Update home route to look for posts via query rather than from fake data

``Post.query.get_or_404`` returns the content or 404

### Editing a post

1. Add a route that takes you to edit post id
2. only allow edit if user is author `if post.author != current_user: abort(403)`
3. Use the create post form to pull in title and content changes and commit those

### Deleteing a post

1. Added a modal to the post.html which is a pop up for deletion confirmation
   1. Taken from bootstrap example
2. Added a route for delete once confirmed, it deletes the content
   1. Only allows POST methods not gets.
   2. Only allows authors of post to post

## Tutorial 9 Adding pagination

[**Tutorial source**](https://www.youtube.com/watch?v=PSWf2TjTGNY)

### Adding pagination

1. `posts = Post.query.paginate(per_page=5,page=2)`
2. `posts.total` = total num pages
3. Adding to routes in code snippet below
4. Change to home.html to look at posts.items
5. Added buttons to flick through pages

```python
page = request.args.get('page',1,type=int)
posts = Post.query.order_by(Post.date_posted.desc()).paginate( page= page, per_page=5)
```

### Added user posts

1. Basically same as home page but looks at user posts instead
2. Added below to routes

```python
   page = request.args.get('page',1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate( page= page, per_page=5)
```

## Tutorial 10 - Email password and reset

[**Tutorial source**](https://www.youtube.com/watch?v=vutyTx7IaAI)

### Time sensitive token

`from itsdangerous import TimedJSONWebSignatureSerializer as Serializer`

## Tutorial 11 - Blueprints and Configuration

[**Tutorial source**](https://www.youtube.com/watch?v=Wfx4YBzg16s)

### Breaking up into blueprints

1. Creating a package for each type of route and object.
2. Create a init.py in each package
   1. Each package takes a routes.py and forms.py
3. Create a blueprint for each object type (main, users, posts)
4. Update all templates so that url_fors to point to `'users.route'` rahter than `'route'`
5. Update main init.py to be able to create multiple instances of website, call a function
6. Move routes and forms from main file into their respective packages
   1. update app.route to respective .route eg. main/users etc.
7. Add config file to hold key variables
8. import blueprints into main init.py
9. Update all files with correct import packages

## Tutorial 12 - Error Handling

[**Tutorial source**](https://www.youtube.com/watch?v=uVNfQDohYNI)

1. New blueprint, errors
   1. create new package
2. Add errors accoring to the code setion below
3. Add relevant HTML files and include these in the handlers file
4. add the error blueprint to the create app function

```python
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'),404
```

## Tutorial 13 - Deploying to server

[**Tutorial source**](https://www.youtube.com/watch?v=goToXTC96Co)

1. We will be using Linode to deploy
   1. Gives flexibility but costs
2. Create Linode account
3. create nanode server
4. save password
5. ssh to server `ssh root@ip`
6. `apt update && apt upgrade`
7. `hostnamectl set-hostname flask-server`
8. `nano /etc/hosts`
   1. add ip and host name to hosts
9. Add personal user  `adduser <USERNAME>`
   1. Password is required
   2. Name etc is optional
10. Add personal user to sudo group `adduser <USERNAME> sudo`
11. `exit` quits the ssh connection
12. login with user this time
13. create .ssh folder
    1. In home terminal create ssh key using `ssh-keygen - b 4096`
    2. `scp ~/.ssh/id_rsa.pub seanc@<ip>:~/.ssh/authorized_keys`
    3. `sudo chmod 700 ~/.ssh/` 700 is read write and execute for user
    4. `sudo chmod 600 ~/.ssh/*`
14. we can now ssh without password
15. to dissalow root logins over ssh
    1. `sudo nano /etc/ssh/sshd_config`
    2. We change PermitRootLogin to no
    3. we change password auth to no
    4. ``sudo systemctl restart sshd`` 
16. Set up a firewall
    1. `sudo apt install ufw`
    2. `sudo ufw default deny incoming`
    3. `sudo ufw default allow outgoing`
    4. `sudo ufw allow ssh`
    5. `sudo ufw allow 5000`
    6. `sudo ufw enable`
    7. `sudo ufw status`
17. Create a requirements file for package
    * ``pip freeze > requirements.txt``
18. Move files to server
    * `scp -r requirements.txt seanc@<ip>:~/`
19. install python3 and venv
    1. Create venv `python3 -m venv project/venv`
    2. Enable venv `source venv/bin/activate`
20. install packages from requirements.txt
    1. `pip install -r requirements.txt`
21. Test server on dev
    1. Get env vars and move to config.json
    2. `sudo nano /etc/config.json`
    3. Create a json of key value pairs
    4. Edit config.py to look for json file `with open(file name) json.load`
    5. replace os.get with `config.get`
22. in command line set `export FLASK_APP=run.py`
23. `flask run --host=0.0.0.0` -  we run a local dev server on the linode
24. install nginx with apt
    1. Remove nginx default config `sudo rm /etc/nginx/sites-enabled/default`
    2. Add config for flaskblog `sudo nano /etc/nginx/sites-enabled/flaskblog`
       1. Add relevant code
       2. try to run and see we dont have gunicorn running
       3. `sudo nano ufw allow http/tcp` &`sudo ufw delete allow 5000` &`sudo ufw enable` 
       4. `sudo systemctl restart nginx` - restart nginx server
25. install gunicorn with pip
    1. `gunicorn -w 3 run:app` main site should run now but we cant use server at all
26. `sudo apt install supervisor` install supervisor runs gunicorn in background
27. `sudo nano /etc/supervisor/conf.d/flaskblog.conf` add snippet to configure file for flask blog package
28. Create log files mentioned in flaskblog .conf
    1. `sudo touch /var/log/flaskblog/flaskblog.err.log` &
`sudo touch /var/log/flaskblog/flaskblog.out.log`
29. `sudo supervisorctl reload`
30. Shouls now be working
31. `sudo nano /etc/nginx/nginx.conf`
     1. Edit the size of upload to 5M
32. `sudo systemctl restart nginx`

## html learnings

* ``<meta >`` tags contain metadata about the html document.
  * Always go inside head of document.
  * Typically used to specify character set, page description, keywords, author of the document, and viewport settings.
* `<div class=>` defines a division or a section in an HTML document.
  * The `<div>` tag is used as a container for HTML elements - which is then styled with CSS or manipulated with JavaScript.
* `{{}}` dictates a code injection
  * `<link rel="stylesheet" type = "text/css" href="{{ url_for('static',filename='main.css')}}">` Injects the url_for function to find location of main.css
