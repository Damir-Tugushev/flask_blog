from flask import Flask

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

from . import routes, repository, login  # noqa E402


@app.shell_context_processor
def shell_context():
    from .repository import db
    from .repository.model import User, Session, Post, DeletedPost

    return {'db': db, 'User': User, 'Session': Session,
            'Post': Post, 'DeletedPost': DeletedPost, }
