from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired


class GenreForm(FlaskForm):
    genre = SelectField('Select Genre', choices=[(1, "One"), (2, "Two"),(3, "Three"), (4, "Four"),
                                                 (5, "Five")], validators=[DataRequired()])
    submit = SubmitField('Submit')
