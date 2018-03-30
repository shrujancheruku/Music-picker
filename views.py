from app import *
from forms import GenreForm, SongForm, SearchForm
from flask import request, redirect, render_template, url_for, flash, make_response
import random
from utils import get_url

"""
Views for the Flask app. Contains the routes for the page routing
"""


@app.route('/')
def home():
    """
    Homepage. Shows 100 random songs from the db.
    """
    search_form = SearchForm()

    conn = create_connection()
    tracks = select_all_tracks(conn)

    # randomize order of tracks
    random.shuffle(tracks)

    tracks = tracks[:100]
    names = [row[1] for row in tracks]
    urls = [row[9] for row in tracks]

    # close db connection
    conn.close()

    return render_template('home.html', names=names, urls=urls, search_form=search_form)


@app.route('/genres')
def genre():
    """
    Creates form to select preferred genre
    """
    search_form = SearchForm()
    form = GenreForm()

    return render_template('genres.html', title='Select Genre', form=form, search_form=search_form)


@app.route('/genre_play', methods=['GET', 'POST'])
def genre_play():
    """
     Genre selection form posts to this route, where we select tracks from that genre and play.
    """
    search_form = SearchForm()
    conn = create_connection()

    tracks = select_track_by_genre(conn, request.form['genre'])

    # randomize order of tracks
    random.shuffle(tracks)

    tracks = tracks[:100]
    names = [row[1] for row in tracks]
    urls = [row[9] for row in tracks]

    # close db connection
    conn.close()

    return render_template('genre_play.html', names=names, urls=urls, search_form=search_form)


@app.route('/new_song')
def new_song():
    """
    Creates form for input of new song details
    """
    search_form = SearchForm()
    form = SongForm()
    return render_template('new_song.html', title='Add New Song', form=form, search_form=search_form)


@app.route('/song', methods=['GET', 'POST'])
def song_play():
    """
    Inserts data entered in the song-creation form, and then plays the new song
    """
    search_form = SearchForm()
    name = request.form['name']
    album = request.form['album']
    artist = request.form['artist']

    conn = create_connection()
    cur = conn.cursor()

    # search for the artist
    cur.execute("SELECT * FROM Artist WHERE Name='{artist}'".
                format(artist=artist))
    rows = cur.fetchall()

    # if artist isn't in the db, add it and save the id
    if len(rows) is 0:
        cur.execute("INSERT INTO Artist (Name) VALUES ('{artist}')".
                    format(artist=artist))
        cur.execute("SELECT * FROM Artist WHERE Name='{artist}'".
                    format(artist=artist))
        rows = cur.fetchall()

    artist_id = rows[0][0]

    # see if album exists
    cur.execute("SELECT * FROM Album WHERE Title='{album}'".
                format(album=album))
    rows = cur.fetchall()

    # if album doesn't exist, add it and save the id
    if len(rows) is 0:
        cur.execute("INSERT INTO Album (Title, ArtistId) VALUES ('{album}', '{_id}' )".
                    format(_id=artist_id, album=album))
        cur.execute("SELECT * FROM Album WHERE Title='{album}'".
                    format(album=album))
        rows = cur.fetchall()

    album_id = rows[0][0]

    # query the YouTube API for the first search result for Artist Name + Track Name
    url = get_url.youtube_search((name + artist))

    # insert new song
    cur.execute("INSERT INTO Track (Name, AlbumId, url, MediaTypeId, Milliseconds, UnitPrice) VALUES ('{name}', '{_id}', '{url}', '{MediaTypeId}', '{Milliseconds}', '{UnitPrice}' )".
                format(_id=album_id, name=name, url=url, MediaTypeId=1, Milliseconds=0, UnitPrice=0.99))

    cur.execute("SELECT * FROM Track WHERE url='{url}'".
                format(url=url))

    # close db connection
    conn.commit()
    conn.close()

    return render_template('song_play.html', name=name, url=url, search_form=search_form)


@app.route('/search', methods=['GET', 'POST'])
def search():
    """
    Queries the db based on search type, and then plays resultant playlist
    """
    search_form = SearchForm()

    conn = create_connection()
    cur = conn.cursor()

    parameter = request.form['parameter']
    data = request.form['data']

    tracks = []

    # if searching Artist Name
    if parameter is '1':
        cur.execute("SELECT * FROM Artist WHERE Name='{artist}'".
                    format(artist=data))
        rows = cur.fetchall()

        # if there are no results
        if len(rows) is 0:
            flash("Not Found", category='error')
            return redirect(url_for("home"))
        else:
            # search for artist's albums
            artist_id = rows[0][0]
            cur.execute("SELECT * FROM Album WHERE ArtistId='{_id}'".
                        format(_id=artist_id))
            rows = cur.fetchall()
            album_id = [row[0] for row in rows]

        # get all tracks by artist
        for _id in album_id:
            cur.execute("SELECT * FROM Track WHERE AlbumId='{_id}'".format(_id = _id))
            tracks += (cur.fetchall())

    # if searching Track Name
    if parameter is '2':
        cur.execute("SELECT * FROM Track WHERE Name='{name}'".format(name=data))
        tracks = cur.fetchall()

        # if there are no results
        if len(tracks) is 0:
            flash("Not Found", category='error')
            return redirect(url_for("home"))

    # if searching Album Title
    if parameter is '3':
        cur.execute("SELECT * FROM Album WHERE Title='{title}'".
                    format(title=data))
        rows = cur.fetchall()

        # if there are no results
        if len(rows) is 0:
            flash("Not Found", category='error')
            return redirect(url_for("home"))

        album_id = [row[0] for row in rows]

        # get all tracks from album
        for _id in album_id:
            cur.execute("SELECT * FROM Track WHERE AlbumId='{_id}'".format(_id=_id))
            tracks += (cur.fetchall())

    # randomize track order
    random.shuffle(tracks)

    names = [row[1] for row in tracks]
    urls = [row[9] for row in tracks]

    # close db connection
    conn.close()

    return render_template('genre_play.html', names=names, urls=urls, search_form=search_form)
