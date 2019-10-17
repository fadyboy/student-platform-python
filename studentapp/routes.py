from studentapp import app
from flask import render_template, flash, redirect, url_for
from studentapp.forms import LoginForm
from flask_login import login_user, current_user, logout_user
from studentapp.models import Admin


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        admin_user = Admin.query.filter_by(username=form.username.data).first()
        if admin_user is None or not admin_user.check_password(form.password.data):
            flash(f"Invalid username or password")
            return redirect(url_for("login"))
        login_user(admin_user)
        return redirect(url_for("index"))

    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
