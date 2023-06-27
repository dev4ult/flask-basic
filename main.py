from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", first_name="nibras", last_name="alyassar")


@app.route("/<name>")
def dashboard(name):
    return f"Hello {name}"


@app.route("/main")
def main():
    return redirect(url_for("dashboard", name="nibras"))


if __name__ == "__main__":
    app.run()
