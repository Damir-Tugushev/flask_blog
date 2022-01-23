from flask import render_template

from flask_blog import app
from flask_blog.repository.model.user import User


@app.route('/')
def index():
    user: User = User.query.filter_by(name='Damir').first()
    print(user)
    return render_template('base.html', user=user)
