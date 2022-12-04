from app import app
from flask import render_template

@app.route("/home")
def index():
    return render_template("home.html")
    # return render_template("index.html",imgsrc="/api/meme/random")