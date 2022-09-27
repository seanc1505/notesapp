from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Hello to the world</h1>"

@app.route("/about")
def hi_there():
    return "<h1>About</h1>"

if __name__ == "__main__":
    app.run(debug=True)
