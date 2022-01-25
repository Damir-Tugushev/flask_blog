from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from ..repository.model import User


class RegisterForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    # noinspection PyMethodMayBeStatic
    def validate_login(self, login: StringField):
        login = login.data
        user: User = User.query.filter_by(login=login).one_or_none()
        if user is not None:
            raise ValidationError(f'User with provided username {login} already exists!')
