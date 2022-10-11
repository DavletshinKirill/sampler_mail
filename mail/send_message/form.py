from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField
from wtforms.validators import DataRequired


class EmailForm(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired()])
    submit = SubmitField("Send")
