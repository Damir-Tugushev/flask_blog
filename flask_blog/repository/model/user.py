from uuid import uuid4

from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash

from .. import db


class User(UserMixin, db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    login = db.Column(db.VARCHAR(50), nullable=False, unique=True)
    password_hash = db.Column(db.VARCHAR(128), nullable=False)
    # role_id =
    description = db.Column(db.VARCHAR(250), nullable=True, default=None)
    email = db.Column(db.VARCHAR(254), nullable=True, unique=True, default=None)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True, default=None)

    def __repr__(self) -> str:
        return f'<User id={self.id} name="{self.login}">'

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def get_id(self) -> str:
        return self.session.id
