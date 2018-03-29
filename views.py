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
    search_form = SearchForm()

    conn = create_connection()
    tracks = select_all_tracks(conn)
    # random.shuffle(tracks)
    tracks = tracks[:50]
    names = [row[1] for row in tracks]
    urls = [row[9] for row in tracks]

    conn.close()

    return render_template('home.html', names=names, urls=urls, search_form=search_form)


@app.route('/genres')
def genre():
    search_form = SearchForm()
    form = GenreForm()

    return render_template('genres.html', title='Select Genre', form=form, search_form=search_form)


@app.route('/genre_play', methods=['GET', 'POST'])
def genre_play():
    search_form = SearchForm()
    conn = create_connection()
    tracks = select_track_by_genre(conn, request.form['genre'])
    # random.shuffle(tracks)
    tracks = tracks[:50]
    names = [row[1] for row in tracks]
    urls = [row[9] for row in tracks]

    conn.close()

    return render_template('genre_play.html', names=names, urls=urls, search_form=search_form)


@app.route('/new_song')
def new_song():
    search_form = SearchForm()
    form = SongForm()
    return render_template('new_song.html', title='Add New Song', form=form, search_form=search_form)


@app.route('/song', methods=['GET', 'POST'])
def song_play():
    search_form = SearchForm()
    name = request.form['name']
    album = request.form['album']
    artist = request.form['artist']

    conn = create_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Artist WHERE Name='{artist}'".
                format(artist=artist))
    rows = cur.fetchall()

    if len(rows) is 0:
        cur.execute("INSERT INTO Artist (Name) VALUES ('{artist}')".
                    format(artist=artist))
        conn.commit()

        cur.execute("SELECT * FROM Artist WHERE Name='{artist}'".
                    format(artist=artist))
        rows = cur.fetchall()

    artist_id = rows[0][0]

    cur.execute("SELECT * FROM Album WHERE Title='{album}'".
                format(album=album))
    rows = cur.fetchall()

    if len(rows) is 0:
        cur.execute("INSERT INTO Album (Title, ArtistId) VALUES ('{album}', '{_id}' )".
                    format(_id=artist_id, album=album))
        conn.commit()

        cur.execute("SELECT * FROM Album WHERE Title='{album}'".
                    format(album=album))
        rows = cur.fetchall()

    album_id = rows[0][0]

    url = get_url.youtube_search((name + artist))
    print(url)
    print(album_id)
    print(name)

    cur.execute("INSERT INTO Track (Name, AlbumId, url, MediaTypeId, Milliseconds, UnitPrice) VALUES ('{name}', '{_id}', '{url}', '{MediaTypeId}', '{Milliseconds}', '{UnitPrice}' )".
                format(_id=album_id, name=name, url=url, MediaTypeId=1, Milliseconds=0, UnitPrice=0.99))
    conn.commit()

    cur.execute("SELECT * FROM Track WHERE url='{url}'".
                format(url=url))

    rows = cur.fetchall()[0]

    return render_template('song_play.html', name=name, url=url, search_form=search_form)


@app.route('/search', methods=['GET', 'POST'])
def search():
    search_form = SearchForm()
    conn = create_connection()
    cur = conn.cursor()

    parameter = request.form['parameter']
    data = request.form['data']
    print((parameter, data))
    tracks = []
    if parameter is '1':
        cur.execute("SELECT * FROM Artist WHERE Name='{artist}'".
                    format(artist=data))
        rows = cur.fetchall()

        if len(rows) is 0:
            flash("Not Found", category='error')
            return redirect(url_for("home"))
        else:
            artist_id = rows[0][0]
            cur.execute("SELECT * FROM Album WHERE ArtistId='{_id}'".
                        format(_id=artist_id))
            rows = cur.fetchall()
            album_id = [row[0] for row in rows]
            print(album_id)

        for _id in album_id:
            cur.execute("SELECT * FROM Track WHERE AlbumId='{_id}'".format(_id = _id))
            tracks.append(cur.fetchall())
        tracks = tracks[0]

    if parameter is '2':
        cur.execute("SELECT * FROM Track WHERE Name='{name}'".format(name=data))
        tracks = cur.fetchall()
        if len(tracks) is 0:
            flash("Not Found", category='error')
            return redirect(url_for("home"))

    if parameter is '3':
        cur.execute("SELECT * FROM Album WHERE Title='{title}'".
                    format(title=data))
        rows = cur.fetchall()
        if len(rows) is 0:
            flash("Not Found", category='error')
            return redirect(url_for("home"))
        album_id = [row[0] for row in rows]
        print(album_id)

    for _id in album_id:
        cur.execute("SELECT * FROM Track WHERE AlbumId='{_id}'".format(_id=_id))
        tracks.append(cur.fetchall())
    tracks = tracks[0]


    print(tracks[0])
    names = [row[1] for row in tracks]
    urls = [row[9] for row in tracks]

    conn.close()

    return render_template('genre_play.html', names=names, urls=urls, search_form=search_form)
