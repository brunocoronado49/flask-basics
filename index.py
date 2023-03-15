from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route("/<name>")
def hello_name(name):
    return f"Hello, {escape(name)}"


if __name__ == "__main__":
    app.run(debug=True)
 