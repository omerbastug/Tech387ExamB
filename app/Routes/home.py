from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import current_user
@app.route("/home")
def home():
    if not current_user.is_authenticated:
        flash("Potrebna je prijava")
        return redirect(url_for("login_page"))

    return render_template("home.html")