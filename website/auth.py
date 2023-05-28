from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            return 'Logged in successfully!', 200
        else:
            return 'Incorrect password, try again.', 400
    else:
        return 'Email does not exist.', 400


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return "Logout successfully! ", 200


@auth.route('/sign-up', methods=['POST'])
def sign_up():
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    is_admin = request.form.get('is_admin') == "True"


    user = User.query.filter_by(email=email).first()
    if user:
        return 'Email already exists.', 400
    elif len(email) < 4:
        return 'Email must be greater than 3 characters.', 400
    elif len(first_name) < 2:
        return 'First name must be greater than 1 character.', 400
    elif password1 != password2:
        return 'Passwords don\'t match.', 400
    elif len(password1) < 7:
        return 'Password must be at least 7 characters.', 400
    else:
        new_user = User(email=email, first_name=first_name, password=generate_password_hash(
            password1, method='sha256'), is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        return f'Account created!{is_admin}', 200
