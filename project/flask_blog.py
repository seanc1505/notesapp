from flask import Flask, render_template

app = Flask(__name__)

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
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def hi_there():
    return render_template('about.html',title="About")

if __name__ == "__main__":
    app.run(debug=True)
