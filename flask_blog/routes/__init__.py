from .api import *
from .auth import *
from .base import *
from .errors import FormValidationError, ApiError


# noinspection PyUnusedLocal
@app.errorhandler(404)
def error_404_not_found(error):
    return render_template('404_not_found.html', title='404 Not Found',
                           current_user=current_user), 404


@app.errorhandler(ApiError)
def api_error(error: ApiError):
    if isinstance(error, FormValidationError):
        return error
    return jsonify({'message': error.description}), error.code


@app.errorhandler(FormValidationError)
def form_validation_error(error: FormValidationError):
    data = {
        'message': error.description,
        'errors': error.errors,
    }
    return jsonify(data), error.code
