from typing import Final

from flask_wtf import FlaskForm
from werkzeug import Response
from werkzeug.exceptions import HTTPException


class ApiError(HTTPException):
    def __init__(self, code: int = 403, description: str | None = None,
                 response: Response | None = None) -> None:
        super().__init__(description, response)
        self.code: Final[int] = code


class FormValidationError(ApiError):
    def __init__(self, form: FlaskForm, code: int = 403, description: str | None = None,
                 response: Response | None = None) -> None:
        super().__init__(code, description, response)
        self.errors: dict = form.errors
