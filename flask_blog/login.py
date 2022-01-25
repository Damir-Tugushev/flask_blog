from flask_login import LoginManager

from . import app
from .repository.model import User, Session

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(session_id: str) -> User | None:
    session = Session.query.get(session_id)
    return session.user if session else None
