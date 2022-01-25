from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required

from .utils import is_safe_url
from .. import app
from ..forms import LoginForm, RegisterForm
from ..repository import db
from ..repository.model import User, Session


# noinspection PyShadowingNames
@app.route('/login', methods=['GET', 'POST'])
def login():
    user: User = current_user
    if user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).one_or_none()
        if user is None:
            flash("User with provided login name doesn't exist!")
            return redirect(url_for('login'))
        if not user.check_password(form.password.data):
            flash('Invalid password for the user with provided login name!')
            return redirect(url_for('login'))

        session: Session = Session.query.with_parent(user).one_or_none()
        if session is None:
            session = Session(user=user)
            db.session.add(session)
            db.session.commit()
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or not is_safe_url(next_page):
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Log in', user=user, form=form)


# noinspection PyShadowingNames
@app.route('/register', methods=['GET', 'POST'])
def register():
    user: User = current_user
    if user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        # noinspection PyArgumentList
        user = User(login=form.login.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', user=user, form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
