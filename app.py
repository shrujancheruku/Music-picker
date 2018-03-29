from flask import Flask
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
app.config['SECRET_KEY'] = "so_secret_wow"

DATABASE = 'media.sqlite'


def create_connection():
    """
    Create a database connection to the SQLite database
    specified by the db_file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(DATABASE)
        return conn

    except Error as e:
        print(e)

    return None


def select_all_tracks(conn):
    """
    Query all rows in the Track table
    :param conn: the Connection object
    :return: list of all Track objects
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Track")

    rows = cur.fetchall()
    return rows


def select_track_by_genre(conn, genre):
    """
    Query tracks by genre
    :param conn: the Connection object
    :param genre:
    :return:l ist of all Track objects of that genre
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Track WHERE GenreId=?", (genre,))

    rows = cur.fetchall()

    return rows


def select_genres(conn):
    """
    Query genres
    :param conn: the Connection object
    :return: list of all Genre objects
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Genre", (genre,))

    rows = cur.fetchall()

    return rows


if __name__ == '__main__':
    app.run()


import views
