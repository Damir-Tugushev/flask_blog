from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length
from wtforms_html5 import AutoAttrMeta

from ..repository.model import User


class RegisterForm(FlaskForm):
    class Meta(AutoAttrMeta):
        pass

    login = StringField('Login', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    repeat_password = PasswordField('Repeat password', validators=[
        DataRequired(), Length(min=8, max=20), EqualTo('password')
    ])
    submit = SubmitField('Submit')

    # noinspection PyMethodMayBeStatic
    def validate_login(self, login: StringField):
        user: User | None = User.query.filter_by(login=login.data).one_or_none()
        if user is not None:
            raise ValidationError('User with provided login already exists')
