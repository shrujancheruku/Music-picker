from app import *
from forms import GenreForm
from flask import request, redirect, render_template, url_for, flash, make_response
import random

"""
Views for the Flask app. Contains the routes for the page routing
"""


@app.route('/')
def home():
    flash("Work in progress!", category='error')
    conn = create_connection()
    tracks = select_all_tracks(conn)
    # random.shuffle(tracks)
    tracks = tracks[:50]
    names = [row[1] for row in tracks]
    urls = [row[9] for row in tracks]

    conn.close()

    return render_template('home.html', names=names, urls=urls)


@app.route('/genres')
def genre():
    flash("Work in progress!", category='error')

    form = GenreForm()

    return render_template('genres.html', title='Select Genre', form=form)


@app.route('/genre_play', methods=['GET', 'POST'])
def genre_play():

        print("Post")
        print(request.form['genre'])

        conn = create_connection()
        tracks = select_track_by_genre(conn, request.form['genre'])
        # random.shuffle(tracks)
        tracks = tracks[:50]
        names = [row[1] for row in tracks]
        urls = [row[9] for row in tracks]

        conn.close()

        return render_template('genre_play.html', names=names, urls=urls)