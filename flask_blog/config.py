import os
from typing import Final


class Config:
    SECRET_KEY: Final[str] = \
        os.environ.get('SECRET_KEY') or \
        'yn934tqi[c4,i.t]oy34xw=uyvqJizaueXAdxcdcxCDEuyd3yatc47i36'
    SQLALCHEMY_TRACK_MODIFICATIONS: Final[bool] = True
    SQLALCHEMY_DATABASE_URI: Final[str] = \
        os.environ.get('DATABASE_URL') or \
        'postgresql://dr3am_b3ast:password@localhost:5432/flask_blog'
