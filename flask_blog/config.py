import os
from typing import Final


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS: Final[bool] = True
    SQLALCHEMY_DATABASE_URI: Final[str] = \
        os.environ.get('DATABASE_URL') or \
        'postgresql://dr3am_b3ast:password@localhost:5432/flask_blog'
