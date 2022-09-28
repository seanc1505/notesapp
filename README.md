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

# html learnings

* ``<meta >`` tags contain metadata about the html document.
  * Always go inside head of document.
  * Typically used to specify character set, page description, keywords, author of the document, and viewport settings.
* `<div class=>` defines a division or a section in an HTML document.
  * The `<div>` tag is used as a container for HTML elements - which is then styled with CSS or manipulated with JavaScript.
* `{{}}` dictates a code injection
  * `<link rel="stylesheet" type = "text/css" href="{{ url_for('static',filename='main.css')}}">` Injects the url_for function to find location of main.css
    