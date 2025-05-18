from flask import Flask, render_template
import traceback

try:
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/experience/")
    def experience():
        return render_template("experience.html")

    @app.route("/projects/")
    def projects():
        return render_template("projects.html")

    @app.route("/education/")
    def education():
        return render_template("education.html")

    @app.route("/other/")
    def other():
        return render_template("other.html")

except Exception as e:
    print(e)
    print(traceback.format_exc())

if __name__ == "__main__":
    app.run()
