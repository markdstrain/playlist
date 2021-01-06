"""Forms for playlist app."""

from wtforms import SelectField, StringField,TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Optional

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name", validators=[ InputRequired(), Length(min=1, max=50)])
    description = TextAreaField("Playlist Description", validators=[ Optional(), Length(min=0, max=1000, message="Playlist Description can't be longer than a 1000 characters.")])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title", validators=[ InputRequired(), Length(min=1, max=100, message="Song Title must be at least 1 character long and no longer than 100")])
    artist = StringField("Artist", validators=[ InputRequired(), Length(min=1, max=100, message="Artist name must ber at least 1 character long and no longer than 100")])
# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
