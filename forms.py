from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField
from wtforms.validators import DataRequired
"""
Forms used throughout the application
"""


class GenreForm(FlaskForm):
    """
    Used to select genre to play music of a particular type
    """
    genres = [(1, "Rock"), (2, "Jazz"), (3, "Metal"), (4, "Alternative & Punk"), (5, "Rock and Roll"), (6, "Blues"),
              (7, "Latin"), (8, "Reggae"), (9, "Pop"), (10, "Soundtrack"), (11, "Bossa Nova"), (12, "Easy Listening"),
              (13, "Heavy Metal"), (14, "R%B"), (15, "Electronica"), (16, "World"), (17, "Hip Hop"), (18, "Sci-Fi"),
              (19, "TV Shows"), (20, "Fantasy"), (21, "Drama"), (22, "Comedy"), (23, "Alternative"), (24, "Classical"),
              (25, "Opera")]

    genre = SelectField('Select Genre', choices=genres, validators=[DataRequired()])
    submit = SubmitField('Submit')


class SongForm(FlaskForm):
    """
    Used to enter a new song into the db
    """
    name = StringField('Name', validators=[DataRequired()])
    album = StringField('Album', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    """
    Used to input search queries
    """
    data = StringField('Name', validators=[DataRequired()])
    parameter = SelectField('Parameter', choices=[(1, "Artist"), (2, "Track"), (3, "Album")],
                            validators=[DataRequired()])
    submit = SubmitField('Submit')