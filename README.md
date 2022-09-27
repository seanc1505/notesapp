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
