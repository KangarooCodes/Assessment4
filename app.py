from flask import Flask, redirect, render_template, flash, request
from flask_debugtoolbar import DebugToolbarExtension



from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""
    
    form = PlaylistForm()
    all_playlists = Playlist.query.all()
    descrip = form.description.data
    
    for play in all_playlists:
        print('***********************')
        print(play.name)
        print((all_playlists.index(play)))
        print('***********************')
    
    # raise
    return render_template("playlists.html",
                           all_playlists=all_playlists,descrip=descrip,form=form)
 


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    
    all_playlists = Playlist.query.all()
    playlist = all_playlists[playlist_id-1]
    all_songs = Song.query.all()
    song = all_songs[playlist_id-1]
    all_playlist_songs = PlaylistSong.query.all()
    playlist_song = all_playlist_songs[playlist_id-1]
    
    #raise
    return render_template("playlist.html",
                           playlist=playlist,song=song,playlist_song=playlist_song,
                           all_playlists=all_playlists,all_songs=all_songs,
                           all_playlist_songs=all_playlist_songs)
    

@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    
    form = PlaylistForm()
    
    all_playlists = Playlist.query.all()
    name = form.name.data        
    description = form.description.data
        
    if form.validate_on_submit():
        '''Update playlists table with user inputs of Name and Description'''
        
        new_playlist = Playlist(name=name, description = description)
        
        # Adds new playlist to database 'playlists'
        if len(all_playlists) == 0:
            db.session.add(new_playlist)
            db.session.commit()
            flash(f"Playlist created with name of: '{name}' !")                
            return redirect('/playlists')
        else:       # Below makes sure any playlist name is not added twice
            for play in all_playlists:
                repeat_checker = []
                repeat_checker.append(play.name)
                if play.name not in repeat_checker:
                    db.session.add(new_playlist)
                    db.session.commit()
                    flash(f"Playlist created with name of: '{name}' !")                
                    return redirect('/playlists')
                else:
                    flash(f"Playlist w/ That Name Already Exists!")
                    return render_template("new_playlist.html", form=form)
   
    else:
        # Shows when GET request instead of POST
        # raise
        print("** GET REQUEST **")
        return render_template("new_playlist.html", form=form)
    


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    form = SongForm()
    all_songs = Song.query.all()
    title = form.title.data
    
    #raise
    return render_template("songs.html",
                           all_songs=all_songs,title=title,form=form)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    all_songs = Song.query.all()
    song = all_songs[song_id-1]
    all_playlists = Playlist.query.all()
    playlist = all_playlists[song_id-1]
    all_songs = Song.query.all()
    all_playlist_songs = PlaylistSong.query.all()
    playlist_song = all_playlist_songs[song_id-1]

    # raise
    return render_template("song.html",song=song,playlist=playlist,
                           playlist_song=playlist_song,all_playlists=all_playlists,
                           all_songs=all_songs,all_playlist_songs=all_playlist_songs)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    
    form = SongForm()
    
    all_songs = Song.query.all()
    title = form.title.data        
    artist = form.artist.data
    
    
    if form.validate_on_submit():
        # Updated playlists table with user inputs of Name and Description
        
        new_song = Song(title=title, artist = artist)
        
        # Adds new playlist to database 'playlists'
        if len(all_songs) == 0:
            db.session.add(new_song)
            db.session.commit()          
            flash(f"Song Added with name of: '{title}' !") 
            return redirect('/songs')
        else:       # Below makes sure any song is not added twice
            for song in all_songs:
                repeat_checker = []
                repeat_checker.append(song.title)
                if song.title in repeat_checker:
                    flash(f"Song Already Exists!")                         
                    return render_template("new_song.html", form=form)
                else:    
                    db.session.add(new_song)
                    db.session.commit()          
                    flash(f"Song Added with name of: '{title}' !") 
                    return redirect('/songs')
   
    else:
        # Shows when GET request instead of POST
        # raise
        print("** GET REQUEST **")
        return render_template("new_song.html", form=form)

@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS
    
    form = NewSongForPlaylistForm()
    
    playlist = Playlist.query.get_or_404(playlist_id)
    
    playlist_songs = PlaylistSong.query.all()
    playlist_song_id = PlaylistSong.query[playlist_id-1].song_id
    #raise
    form.song.choices = (db.session.query(Song.id, Song.title)
                      .filter(Song.id != playlist_song_id)
                      .all())  
    #raise
    song = form.song.data
    # Restrict form to songs not already on this playlist
    added_song = Song.query.get(song)
    
    # raise
    if form.validate_on_submit():

        playlist_song = PlaylistSong(song_id=form.song.data, playlist_id=playlist_id)
        
        
        db.session.add(playlist_song)
        db.session.commit()
        return redirect(f"/playlists/{playlist_id}")
    
    return render_template("add_song_to_playlist.html",playlist=playlist,form=form)
