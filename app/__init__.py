from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder="static/templates")

@app.route("/")
@app.route("/index")
def index():
        return render_template("index.html")