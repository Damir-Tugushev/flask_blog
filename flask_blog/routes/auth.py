from flask import render_template, redirect, url_for
from flask_login import current_user, logout_user, login_required

from .. import app
from ..repository.model import User
from ..forms import LoginForm, RegisterForm


# noinspection PyShadowingNames
@app.route('/login')
def login():
    user: User = current_user
    if user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    return render_template('login.html', title='Log in', user=user, form=form)


# noinspection PyShadowingNames
@app.route('/register')
def register():
    user: User = current_user
    if user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()
    return render_template('register.html', title='Register', user=user, form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
