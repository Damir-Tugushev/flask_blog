from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from flask_blog.repository import db


class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    login = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.CHAR(60), nullable=False)
    # role_id =
    description = db.Column(db.VARCHAR(250), nullable=True, default=None)
    email = db.Column(db.VARCHAR(254), nullable=True, unique=True, default=None)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True, default=None)

    def __repr__(self) -> str:
        return f'<User id={self.id} name="{self.login}">'
