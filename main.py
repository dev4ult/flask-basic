from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<name>")
def dashboard(name):
    return f"Hello {name}"


@app.route("/main")
def main():
    return redirect(url_for("dashboard", name="asdasd"))


if __name__ == "__main__":
    app.run(debug=True)
