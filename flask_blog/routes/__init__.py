from .auth import *
from .base import *


# noinspection PyUnusedLocal
@app.errorhandler(404)
def error_404_not_found(error):
    return render_template('404_not_found.html', title='404 Not Found'), 404
