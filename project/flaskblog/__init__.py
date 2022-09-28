from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '33f1ae20b4a0d78c4d3eb6ecdce3fb1a'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog import routes