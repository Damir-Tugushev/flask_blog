from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_blog import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)
