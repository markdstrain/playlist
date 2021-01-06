"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__="playlists"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    songs = db.relationship("PlaylistSong", backref='playlist')

    
    @classmethod
    def create_playlist(cls, name, description):
        """Creating a playlist with a name and description of playlist"""
        p = Playlist.query.filter_by(name=name).first()
        if p:
            return False
        else:
            playlist = cls(
                name=name,
                description=description
            )
            db.session.add(playlist)
            return playlist

    

class Song(db.Model):
    """Song."""
    __tablename__= "songs"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True,)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)
    playlists = db.relationship("PlaylistSong", backref='songs')
    
    @classmethod
    def create_song(cls, title, artist):
        """Creating a playlist with a name and description of playlist"""
        song = cls(
            title=title,
            artist=artist
        )
        db.session.add(song)
        return song
    

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song.""" 
   
    __tablename__="playlistsongs"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    playlist_id = db.Column(db.Integer,
                    db.ForeignKey('playlists.id'))
    songs_id = db.Column(db.Integer,
                db.ForeignKey('songs.id'))

    
    
    


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
