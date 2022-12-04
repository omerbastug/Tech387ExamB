from app import app
from app.Models.User import User
from flask import render_template ,request, redirect, flash, url_for
from flask_login import login_user

@app.route("/login" , methods=['get'])
def login_page():
    return render_template("login.html")

@app.route("/login" , methods=['post'])
def login_redirect():
    body = request.form
    print(body)
    try:
        user = User.query.filter_by(email=body.get("email")).first()
        if not user:
            # log 
            flash("Pogresan e-mail ili password", category="incorrectPassword")
            return redirect(url_for('login_page'))

        if not user.truePassword(body.get('password')):
            # log
            flash("Pogresan e-mail ili password", category="danger")
            return redirect(url_for('login_page'))

    except BaseException as err:
        print(err)
        flash("Interni server error.", category='danger')
        return redirect(url_for('login_page'))

    login_user(user)
    flash("login successful", category='success')
    return redirect(url_for('home'))