from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms_html5 import AutoAttrMeta


class PostForm(FlaskForm):
    class Meta(AutoAttrMeta):
        pass

    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    text_content = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Add')
