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

1. `set FLASK_DEBUG = 1 `
   1. This opens in debug mode

## Running files via python 

```
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

```
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


## Adding Navbar 

