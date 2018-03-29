from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField
from wtforms.validators import DataRequired


class GenreForm(FlaskForm):
    genre = SelectField('Select Genre', choices=[(1, "One"), (2, "Two"),(3, "Three"), (4, "Four"),
                                                 (5, "Five")], validators=[DataRequired()])
    submit = SubmitField('Submit')


class SongForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    album = StringField('Album', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    data = StringField('Name', validators=[DataRequired()])
    parameter = SelectField('Parameter', choices=[(1, "Artist"), (2, "Track"), (3, "Album")], validators=[DataRequired()])
    submit = SubmitField('Submit')