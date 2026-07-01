from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from src.models.database import db
from src.models.user import User


auth = Blueprint("auth", __name__)


# -----------------------------
# Register
# -----------------------------
@auth.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        startup_name = request.form.get("startup_name", "").strip()
        industry = request.form.get("industry", "").strip()

        if not username or not email or not password:

            flash("Please fill all required fields.", "danger")
            return render_template("register.html")

        existing_user = User.query.filter_by(
            username=username
        ).first()

        if existing_user:

            flash("Username already exists.", "warning")
            return render_template("register.html")

        existing_email = User.query.filter_by(
            email=email
        ).first()

        if existing_email:

            flash("Email already registered.", "warning")
            return render_template("register.html")

        hashed_password = generate_password_hash(password)

        user = User(
            username=username,
            email=email,
            password=hashed_password,
            startup_name=startup_name,
            industry=industry
        )

        db.session.add(user)
        db.session.commit()

        flash(
            "Registration successful. Please login.",
            "success"
        )

        return redirect(url_for("auth.login"))

    return render_template("register.html")


# -----------------------------
# Login
# -----------------------------
@auth.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        remember = request.form.get("remember") == "on"

        user = User.query.filter_by(email=email).first()

        if user is None:

            flash("Account not found.", "danger")
            return render_template("login.html")

        if not check_password_hash(
            user.password,
            password
        ):

            flash("Invalid password.", "danger")
            return render_template("login.html")

        login_user(
            user,
            remember=remember
        )

        flash(
            f"Welcome back, {user.username}!",
            "success"
        )

        return redirect(url_for("main.dashboard"))

    return render_template("login.html")


# -----------------------------
# Logout
# -----------------------------
@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Logged out successfully.",
        "info"
    )

    return redirect(url_for("auth.login"))