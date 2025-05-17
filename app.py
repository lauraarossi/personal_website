# a barebones, starter app
# run locally from console with:
#   flask --app app run
# or leveraging autodicovery:
#   flask run
# (since it's called app)
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/experience")
def experience():
    return render_template("experience.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/other")
def other():
    return render_template("other.html")
