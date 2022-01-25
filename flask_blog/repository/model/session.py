from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from flask_blog.repository import db
from flask_blog.repository.model.user import User


class Session(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), unique=True, nullable=False)
    user: User = db.relationship('User', backref=db.backref('session', lazy=True, uselist=False))
