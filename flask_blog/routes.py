from flask import render_template

from . import app
from .repository.model.user import User


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/user/<login>')
def user_def(login: str):
    user: User = User.query.filter_by(login=login).first_or_404()
    print(user)
    return render_template('user.html', title=f"Hello, {user.login}", user=user)


@app.errorhandler(404)
def error_404_not_found(error):
    return render_template('404_not_found.html', title='404 Not Found'), 404
