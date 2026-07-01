from flask import Blueprint, render_template, redirect, url_for

from forms import RegistrationForm, LoginForm
from models import db
from models.user import User

from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(
        email=form.email.data
        ).first()

        if existing_user:
            return "This email is already registered."

        hashed_password = generate_password_hash(
            form.password.data
        )

        user = User(
            full_name=form.full_name.data,
            email=form.email.data,
            password_hash=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template(
        "register.html",
        form=form
    )

@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and check_password_hash(
            user.password_hash,
            form.password.data
        ):

            login_user(user)

            return redirect(url_for("home"))

        return "Invalid email or password."

    return render_template(
        "login.html",
        form=form
    )

@auth.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("home"))