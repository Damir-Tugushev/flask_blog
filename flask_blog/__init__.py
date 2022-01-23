from flask import Flask

from flask_blog.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from flask_blog import routes  # noqa E402
