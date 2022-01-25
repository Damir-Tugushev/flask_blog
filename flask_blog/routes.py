from urllib.parse import urljoin, urlparse

from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required

from . import app
from .forms import LoginForm, RegisterForm
from .repository import db
from .repository.model import User, Session


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user: User = User.query.filter_by(login=form.login.data).one_or_none()
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

    return render_template('login.html', title='Log in', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        # noinspection PyArgumentList
        user: User = User(login=form.login.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# noinspection PyShadowingNames
@app.route('/user/<login>')
def user_def(login: str):
    user: User = User.query.filter_by(login=login).first_or_404()
    return render_template('user.html', title=f"Hello, {user.login}", user=user)


# noinspection PyUnusedLocal
@app.errorhandler(404)
def error_404_not_found(error):
    return render_template('404_not_found.html', title='404 Not Found'), 404
