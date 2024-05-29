from flask import Flask, request, render_template, redirect, url_for
from models import Db_start, Db_service
import json

app = Flask(__name__)
# app.config['SECRET_KEY'] = '87dc78b17b20d8d22b7850529c3815622f949339bfbfc33c'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/poll", methods=["GET", "POST"])
def poll():
    if request.method == "GET":
        return render_template("poll.html")

    if request.method == "POST":
        username = request.form["username"]
        age = request.form["age"]
        city = request.form["city"]
        country = request.form["country"]
        print(username)
        Db_service().add_record_to_poll(username, age, city, country)
        return redirect(url_for("results"))

@app.route("/results")
def results():
    data = Db_service().get_last_record_from_poll()
    return render_template("results.html", data=data)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        return redirect(url_for("index"))
    
@app.route("/loaderio-12e71f86ba0e1bc3612073cdb4846861.txt")
def loaderio():
    return "loaderio-12e71f86ba0e1bc3612073cdb4846861"

if __name__ == "__main__":
    Db_start()
    app.run(debug=True)
