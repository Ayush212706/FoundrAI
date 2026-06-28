from flask import Blueprint, render_template, request, redirect, url_for

from flask_login import login_user, logout_user

from src.models.database import db
from src.models.user import User
from src.services.auth_service import hash_password, verify_password

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        user = User(

            username=request.form["username"],

            email=request.form["email"],

            password=hash_password(request.form["password"]),

            startup_name=request.form["startup_name"],

            industry=request.form["industry"]

        )

        db.session.add(user)

        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        user = User.query.filter_by(

            email=request.form["email"]

        ).first()

        if user and verify_password(

            request.form["password"],

            user.password

        ):

            login_user(user)

            return redirect(url_for("main.home"))

    return render_template("login.html")


@auth.route("/logout")
def logout():

    logout_user()

    return redirect(url_for("main.home"))