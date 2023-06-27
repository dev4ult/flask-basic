from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/auth", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "nibras" and password == "nibras123":
            return redirect(url_for("main"))
        else:
            return render_template(
                "login.html", error_msg="Username atau password salah"
            )
    else:
        return render_template("login.html")


@app.route("/<unknown_url>")
def not_found404(unknown_url):
    return render_template("not_found404.html", page=unknown_url)


@app.route("/main")
def main():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
