from app import *
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
    random.shuffle(tracks)
    tracks = tracks[:50]
    names = [row[1] for row in tracks]
    urls = [row[9] for row in tracks]

    conn.close()

    return render_template('home.html', names=names, urls=urls)


@app.route('/genres')
def genre():
    flash("Work in progress!", category='error')
    conn = create_connection()
    tracks = select_track_by_genre(conn, 3)
    random.shuffle(tracks)
    tracks = tracks[:50]
    names = [row[1] for row in tracks]
    urls = [row[9] for row in tracks]
    print(urls)

    conn.close()

    return render_template('home.html', names=names, urls=urls)

