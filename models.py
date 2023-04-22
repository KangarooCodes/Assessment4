"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = 'playlists'
    
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String,nullable=False,unique=True)
    description = db.Column(db.String(50),nullable=True)
    
    
class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'
    
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String,nullable=False,unique=True)
    artist = db.Column(db.String,nullable=False)
    

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlist_songs'
    
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    playlist_id = db.Column(db.Integer,db.ForeignKey('playlists.id'),primary_key=True)
    song_id = db.Column(db.Integer,db.ForeignKey('songs.id'),primary_key=True)
        
    
    rel_song = db.relationship('Song', backref = 'PlaylistSong')
    rel_play = db.relationship('Playlist', backref = 'PlaylistSong')
    



########## DO NOT MODIFY THIS FUNCTION ##########

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
