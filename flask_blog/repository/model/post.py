from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from .. import db
from .user import User


class Post(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    author_id = db.Column(UUID(as_uuid=True),
                          db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.VARCHAR(100), index=True, nullable=False)
    text_content = db.Column(db.TEXT, nullable=False)
    created_at = db.Column(db.TIMESTAMP, index=True, nullable=False, default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True, default=None)
    # comments_enabled = db.Column(db.BOOLEAN,
    # view_count = db.Column(db.INTEGER,
    author: User = db.relationship('User', backref=db.backref('post', lazy=True))


class DeletedPost(db.Model):
    post_id = db.Column(UUID(as_uuid=True),
                        db.ForeignKey('post.id', ondelete='CASCADE'), primary_key=True)
    soft_deleted_at = db.Column(db.TIMESTAMP, index=True, nullable=False, default=db.func.now())
    post: Post = db.relationship('Post')
